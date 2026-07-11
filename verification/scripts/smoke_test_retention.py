#!/usr/bin/env python3
"""Synthetic end-to-end smoke test for the common-AGL retention analysis."""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd
import polars as pl
import xarray as xr

SCRIPTS = Path(__file__).resolve().parent
META = SCRIPTS.parent / "data" / "stations_2013_selection.csv"
G = 9.81
NT, NZ, NY, NX = 5, 22, 30, 30


def fake_wrfout(
    path: Path,
    stability_k: float,
    transport_wind_ms: float,
    pblh_m: float,
    t2_c: float,
) -> None:
    times = pd.date_range("2013-02-02T14:00:00", periods=NT, freq="1h")
    stamps = np.array([list(item.strftime("%Y-%m-%d_%H:%M:%S")) for item in times], dtype="S1")
    lat = np.linspace(39.7, 40.6, NY)
    lon = np.linspace(-110.5, -109.2, NX)
    xlon, xlat = np.meshgrid(lon, lat)
    hgt = 1450.0 + 500.0 * (xlat - xlat.min()) / (xlat.max() - xlat.min())
    z_stag_agl = np.linspace(0.0, 1100.0, NZ + 1)
    z_mass_agl = 0.5 * (z_stag_agl[:-1] + z_stag_agl[1:])
    theta = 285.0 + stability_k * (z_mass_agl - 50.0) / 450.0

    phb = (hgt[None, :, :] + z_stag_agl[:, None, None]) * G
    phb = np.broadcast_to(phb, (NT, NZ + 1, NY, NX)).copy()
    t = np.broadcast_to((theta - 300.0)[:, None, None], (NT, NZ, NY, NX)).copy()
    u = np.full((NT, NZ, NY, NX + 1), transport_wind_ms)
    v = np.zeros((NT, NZ, NY + 1, NX))
    surface = (NT, NY, NX)
    ds = xr.Dataset(
        {
            "Times": (("Time", "DateStrLen"), stamps),
            "XLAT": (("Time", "south_north", "west_east"), np.broadcast_to(xlat, surface)),
            "XLONG": (("Time", "south_north", "west_east"), np.broadcast_to(xlon, surface)),
            "HGT": (("Time", "south_north", "west_east"), np.broadcast_to(hgt, surface)),
            "T": (("Time", "bottom_top", "south_north", "west_east"), t),
            "PH": (("Time", "bottom_top_stag", "south_north", "west_east"), np.zeros_like(phb)),
            "PHB": (("Time", "bottom_top_stag", "south_north", "west_east"), phb),
            "U": (("Time", "bottom_top", "south_north", "west_east_stag"), u),
            "V": (("Time", "bottom_top", "south_north_stag", "west_east"), v),
            "COSALPHA": (("Time", "south_north", "west_east"), np.ones(surface)),
            "SINALPHA": (("Time", "south_north", "west_east"), np.zeros(surface)),
            "PBLH": (("Time", "south_north", "west_east"), np.full(surface, pblh_m)),
            "T2": (("Time", "south_north", "west_east"), np.full(surface, t2_c + 273.15)),
            "U10": (("Time", "south_north", "west_east"), np.full(surface, transport_wind_ms)),
            "V10": (("Time", "south_north", "west_east"), np.zeros(surface)),
            "PSFC": (("Time", "south_north", "west_east"), np.full(surface, 85000.0)),
        }
    )
    ds.to_netcdf(path)


def fake_obs(path: Path) -> None:
    meta = pd.read_csv(META)
    meta = meta[meta["in_case_window"].astype(bool)]
    rows = []
    for station in meta.itertuples():
        for when in pd.date_range("2013-02-02T14:00:00", periods=NT, freq="1h"):
            rows.append(
                {
                    "stid": station.stid,
                    "valid_time": when,
                    "temp_2m": -5.0,
                    "wind_speed_10m": 1.0,
                    "pressure_surface": 85000.0,
                    "elevation": station.elev_m / 0.3048,
                }
            )
    pl.DataFrame(rows).write_parquet(path)


def main() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="wrf_retention_smoke_"))
    configs = {
        "gfs2": (3.0, 3.0, 300.0, -2.0),
        "gfs1": (3.2, 3.1, 301.0, -1.9),
        "nam2": (8.0, 1.0, 100.0, -5.0),
        "nam1": (8.1, 1.05, 102.0, -4.9),
    }
    run_args = []
    for label, values in configs.items():
        directory = tmp / label
        directory.mkdir()
        fake_wrfout(directory / "wrfout_d02_2013-02-02_12:00:00", *values)
        run_args.extend(["--run", f"{label}={directory}"])
    obs = tmp / "obs.parquet"
    fake_obs(obs)
    out = tmp / "out"
    cmd = [
        sys.executable,
        str(SCRIPTS / "analyze_wrf_retention.py"),
        *run_args,
        "--display",
        "gfs2=GFS two-way",
        "--display",
        "gfs1=GFS one-way",
        "--display",
        "nam2=NAM two-way",
        "--display",
        "nam1=NAM one-way",
        "--pair",
        "gfs2,nam2",
        "--pair",
        "gfs1,nam1",
        "--pair",
        "gfs1,gfs2",
        "--pair",
        "nam1,nam2",
        "--interaction",
        "gfs1,gfs2,nam1,nam2",
        "--obs",
        str(obs),
        "--stations",
        str(META),
        "--out-dir",
        str(out),
        "--bootstrap-resamples",
        "500",
    ]
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

    rows = pd.read_csv(out / "retention_station_timeseries.csv")
    assert len(rows) == 4 * 11 * 5, len(rows)
    summary = pd.read_csv(out / "retention_pair_summary.csv")

    def estimate(pair: str, metric: str) -> float:
        row = summary[(summary["pair"] == pair) & (summary["metric"] == metric)]
        assert len(row) == 1, (pair, metric, row)
        return float(row.iloc[0]["mean_hourly_spatial_median"])

    assert abs(estimate("gfs2_minus_nam2", "stability_k") + 5.0) < 1.0e-6
    assert abs(estimate("gfs2_minus_nam2", "transport_wind_ms") - 2.0) < 1.0e-6
    assert abs(estimate("nam1_minus_nam2", "stability_k") - 0.1) < 1.0e-6
    interaction = pd.read_csv(out / "retention_interaction_summary.csv")
    row = interaction[
        (interaction["interaction"] == "gfs1_minus_gfs2__minus__nam1_minus_nam2")
        & (interaction["metric"] == "stability_k")
    ]
    assert len(row) == 1 and abs(float(row.iloc[0]["mean_hourly_spatial_median"]) - 0.1) < 1.0e-6
    surface = pd.read_csv(out / "surface_skill_pair_summary.csv")
    t2 = surface[(surface["pair"] == "gfs2_minus_nam2") & (surface["metric"] == "t2_bias_c")]
    assert len(t2) == 1 and abs(float(t2.iloc[0]["mean_hourly_spatial_median"]) - 3.0) < 1.0e-6
    for name in (
        "wrf_retention_ventilation_d02_14to18.png",
        "wrf_retention_ventilation_d02_14to18.pdf",
        "retention_analysis_metadata.json",
    ):
        artifact = out / name
        assert artifact.exists() and artifact.stat().st_size > 1000, artifact
    print(f"OK: common-AGL metrics, paired block summaries, surface skill, and figure -> {tmp}")


if __name__ == "__main__":
    main()
