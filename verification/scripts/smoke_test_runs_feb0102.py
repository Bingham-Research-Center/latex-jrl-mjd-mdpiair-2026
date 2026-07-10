#!/usr/bin/env python3
"""End-to-end smoke test for the multi-run pipeline, no WRF data needed.

Builds a synthetic observation file and two synthetic "runs" in exactly the format
reduce_wrf_to_stations.py writes (WRF units: temp K, pressure Pa; run/waypoint/
valid_time keys), then drives verify_runs_feb0102 and plot_wrf_vs_obs_feb0102 on them
and checks the outputs. So when the real
touchstone CSVs arrive from CHPC, the same two commands are known-good.

Run:
    PYTHONPATH=~/brc-tools python verification/scripts/smoke_test_runs_feb0102.py
Everything is written to a temp dir; nothing in the repo is touched.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import polars as pl

SCRIPTS = Path(__file__).resolve().parent
META_CSV = SCRIPTS.parent / "data" / "stations_2013_selection.csv"


def synth_obs(meta_path: Path) -> pl.DataFrame:
    """Create deterministic, physically plausible station observations in memory."""
    meta = pl.read_csv(meta_path)
    rows = []
    start = datetime(2013, 2, 1, 0)
    for station in meta.iter_rows(named=True):
        elev_m = float(station["elev_m"])
        pressure = 101325.0 * np.exp(-elev_m / 8400.0)
        for hour in range(73):
            valid_time = start + timedelta(hours=hour)
            phase = 2.0 * np.pi * ((valid_time.hour - 21) % 24) / 24.0
            rows.append({
                "stid": station["stid"],
                "valid_time": valid_time,
                "temp_2m": -9.0 - 0.002 * (elev_m - 1465.0) + 3.0 * np.sin(phase),
                "pressure_surface": pressure,
                "wind_speed_10m": 1.5 + 0.3 * np.cos(phase),
                "wind_dir_10m": 180.0,
                "elevation": elev_m / 0.3048,
            })
    return pl.DataFrame(rows)


def synth_run(obs: pl.DataFrame, label: str, temp_bias_k: float, seed: int) -> pl.DataFrame:
    rng = np.random.default_rng(seed)
    hourly = (
        obs.with_columns(pl.col("valid_time").dt.truncate("1h"))
        .group_by("stid", "valid_time")
        .agg(pl.col("temp_2m").mean(), pl.col("pressure_surface").mean(),
             pl.col("wind_speed_10m").mean(), pl.col("wind_dir_10m").mean())
        .drop_nulls("temp_2m")
        .sort("stid", "valid_time")
    )
    n = hourly.height
    return hourly.select(
        pl.lit(label).alias("run"),
        pl.col("stid").alias("waypoint"),
        "valid_time",
        # obs are C / Pa; the reduce script writes K / Pa
        (pl.col("temp_2m") + 273.15 + temp_bias_k
         + pl.Series(rng.normal(0, 0.5, n))).alias("temp_2m"),
        (pl.col("wind_speed_10m").fill_null(2.0) + 0.5).alias("wind_speed_10m"),
        pl.col("wind_dir_10m").fill_null(180.0),
        pl.col("pressure_surface").fill_null(84000.0).alias("pressure_surface"),
    )


def main() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="wrf_smoke_"))
    obs_path = tmp / "obs_feb0102.parquet"
    obs = synth_obs(META_CSV)
    obs.write_parquet(obs_path)
    figures = tmp / "figures"
    runs = {"fake_warm": +3.0, "fake_cool": -1.0}
    paths = []
    for (label, bias), seed in zip(runs.items(), (1, 2)):
        p = tmp / f"wrf_{label}_per_station.csv"
        synth_run(obs, label, bias, seed).write_csv(p)
        paths.append(str(p))
    print(f"fixtures -> {tmp}")

    env_cmd = [sys.executable]
    for script, extra in (
        ("verify_runs_feb0102.py", ["--obs", str(obs_path), "--out-dir", str(tmp)]),
        ("plot_wrf_vs_obs_feb0102.py",
         ["--obs", str(obs_path), "--out-dir", str(figures)]),
    ):
        cmd = env_cmd + [str(SCRIPTS / script), "--wrf", *paths, *extra]
        print(f"\n$ {' '.join(cmd)}")
        subprocess.run(cmd, check=True)

    scores = pl.read_csv(tmp / "wrf_runs_scores_feb0102.csv")
    t = scores.filter(pl.col("variable") == "temp_2m")
    warm = t.filter(pl.col("run") == "fake_warm")["bias"].mean()
    cool = t.filter(pl.col("run") == "fake_cool")["bias"].mean()
    assert 2.5 < warm < 3.5, f"fake_warm temp bias {warm:.2f}, expected ~+3"
    assert -1.5 < cool < -0.5, f"fake_cool temp bias {cool:.2f}, expected ~-1"
    assert (tmp / "wrf_runs_spread_feb0102.csv").exists()
    for stem in ("wrf_temp_timeseries_feb0102", "wrf_inversion_index_feb0102"):
        assert (figures / f"{stem}.png").exists(), f"missing figure {stem}.png"
    print(f"\nOK: biases recovered (warm {warm:+.2f} K, cool {cool:+.2f} K), "
          "spread table + 2 figures written")
    print(f"NOTE: all synthetic-fixture outputs remain isolated under {tmp}")


if __name__ == "__main__":
    main()
