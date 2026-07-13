#!/usr/bin/env python3
"""Synthetic end-to-end smoke test for the ANA-16 heat-deficit analysis."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd
import xarray as xr


G = 9.80665
NTIMES = 6
NZ, NY, NX = 18, 32, 36
SCRIPTS = Path(__file__).resolve().parent


def fake_wrfout(path: Path, valid: pd.Timestamp, stability_per_m: float) -> None:
    lat = np.linspace(39.70, 40.65, NY)
    lon = np.linspace(-110.55, -109.15, NX)
    xlon, xlat = np.meshgrid(lon, lat)
    distance = ((xlat - 40.15) / 0.52) ** 2 + ((xlon + 109.72) / 0.75) ** 2
    hgt = 1450.0 + 1500.0 * distance
    z_agl_stag = np.linspace(0.0, 1500.0, NZ + 1)
    z_agl_mass = 0.5 * (z_agl_stag[:-1] + z_agl_stag[1:])
    z_stag = hgt[None, :, :] + z_agl_stag[:, None, None]
    theta = 286.0 + stability_per_m * z_agl_mass[:, None, None]
    theta = np.broadcast_to(theta, (NZ, NY, NX)).copy()
    pressure = 85000.0 * np.exp(-z_agl_mass[:, None, None] / 8000.0)
    pressure = np.broadcast_to(pressure, (NZ, NY, NX)).copy()
    stamp = np.array([valid.strftime("%Y-%m-%d_%H:%M:%S")], dtype="S19")
    surface_shape = (1, NY, NX)
    ds = xr.Dataset(
        {
            "Times": (("Time",), stamp),
            "XLAT": (("Time", "south_north", "west_east"), np.broadcast_to(xlat, surface_shape)),
            "XLONG": (("Time", "south_north", "west_east"), np.broadcast_to(xlon, surface_shape)),
            "HGT": (("Time", "south_north", "west_east"), np.broadcast_to(hgt, surface_shape)),
            "MAPFAC_M": (("Time", "south_north", "west_east"), np.ones(surface_shape)),
            "T": (("Time", "bottom_top", "south_north", "west_east"), (theta - 300.0)[None]),
            "P": (("Time", "bottom_top", "south_north", "west_east"), np.zeros((1, NZ, NY, NX))),
            "PB": (("Time", "bottom_top", "south_north", "west_east"), pressure[None]),
            "PH": (("Time", "bottom_top_stag", "south_north", "west_east"), np.zeros((1, NZ + 1, NY, NX))),
            "PHB": (("Time", "bottom_top_stag", "south_north", "west_east"), (z_stag * G)[None]),
        },
        attrs={"DX": 1000.0, "DY": 1000.0, "SIMULATION_START_DATE": "2013-02-02_12:00:00"},
    )
    ds.to_netcdf(path)


def main() -> None:
    brc_tools = Path(os.environ.get("BRC_TOOLS", Path(__file__).resolve().parents[3] / "brc-tools"))
    repo = Path(__file__).resolve().parents[2]
    tmp = Path(tempfile.mkdtemp(prefix="heat_deficit_smoke_"))
    mpl = Path(os.environ.get("MPLCONFIGDIR", tmp / "mpl"))
    cache = Path(os.environ.get("XDG_CACHE_HOME", tmp / "cache"))
    mpl.mkdir(parents=True, exist_ok=True)
    cache.mkdir(parents=True, exist_ok=True)
    configs = {
        "gfs2": (0.0080, -0.00055),
        "nam2": (0.0105, -0.00010),
        "gfs1": (0.0076, -0.00050),
        "nam1": (0.0100, -0.00008),
    }
    run_args: list[str] = []
    for run, (initial, trend) in configs.items():
        run_dir = tmp / run
        run_dir.mkdir()
        for lead, valid in enumerate(pd.date_range("2013-02-02T13:00:00", periods=NTIMES, freq="1h")):
            fake_wrfout(
                run_dir / f"wrfout_d02_{valid:%Y-%m-%d_%H:%M:%S}",
                valid,
                initial + trend * lead,
            )
        run_args.extend(["--run", f"{run}={run_dir}"])
    out = tmp / "out"
    cmd = [
        sys.executable,
        str(SCRIPTS / "analyze_heat_deficit.py"),
        *run_args,
        "--display", "gfs2=GFS two-way",
        "--display", "gfs1=GFS one-way",
        "--display", "nam2=NAM two-way",
        "--display", "nam1=NAM one-way",
        "--pair", "gfs2,nam2",
        "--pair", "gfs1,nam1",
        "--mask-run", "nam1",
        "--stations", str(repo / "verification/data/stations_2013_selection.csv"),
        "--figure-config", str(repo / "verification/config/figures/pelican2013.toml"),
        "--brc-tools-dir", str(brc_tools),
        "--out-dir", str(out),
        "--no-hash-inputs",
    ]
    print(f"$ {' '.join(cmd)}")
    env = os.environ.copy()
    env["MPLCONFIGDIR"] = str(mpl)
    env["XDG_CACHE_HOME"] = str(cache)
    subprocess.run(cmd, check=True, env=env)
    trajectory = pd.read_csv(out / "heat_deficit_trajectory.csv")
    assert len(trajectory) == 4 * 7 * 6, len(trajectory)
    pair_summary = pd.read_csv(out / "heat_deficit_pair_summary.csv")
    assert len(pair_summary) == 2 * 7, len(pair_summary)
    sensitivity = pd.read_csv(out / "heat_deficit_sensitivity.csv")
    overall = sensitivity[sensitivity["scope"] == "both_feedback_modes"]
    assert len(overall) == 1
    assert bool(overall.iloc[0]["weaker_state_pass"])
    assert bool(overall.iloc[0]["maintenance_pass"])
    metadata = json.loads((out / "heat-deficit-analysis.json").read_text())
    assert metadata["decision"]["weaker_state_pass"] is True
    assert metadata["decision"]["maintenance_pass"] is True
    for name in (
        "wrf_heat_deficit_d02_13to18.png",
        "wrf_heat_deficit_d02_13to18.pdf",
        "heat-deficit-analysis.json",
    ):
        artifact = out / name
        assert artifact.exists() and artifact.stat().st_size > 1000, artifact
    print(f"OK: masks, grid checks, metrics, pair tests, sensitivity tests, and figure -> {tmp}")


if __name__ == "__main__":
    main()
