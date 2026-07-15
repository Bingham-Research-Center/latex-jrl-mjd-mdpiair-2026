#!/usr/bin/env python3
"""WRF-vs-obs overlay figures for the Feb 1-2 2013 cold-air-pool episode.

Companion to plot_obs_feb0102.py (whose styling/helpers it reuses): same conventions,
now with N WRF runs (the gfs_2way / nam_2way / nam_1way touchstones) overlaid on the
observed episode. Two figures:

1. wrf_temp_timeseries_feb0102 -- 2 m temperature at the 4 floor->bench stations
   (one panel each): obs in black, one line per run, min-max across runs shaded.
   The range across supplied runs is descriptive; its interpretation depends on
   the members included.
2. wrf_inversion_index_feb0102 -- bench-minus-floor delta-theta (USU03 - USU07).
   This two-site contrast is a spatial structural index, not a colocated
   inversion profile or a physical cold-pool classification threshold.

Inputs are the per-station files from reduce_wrf_to_stations.py (WRF units: temp K,
pressure Pa; converted here). Obs stays local. Candidate figures go to
verification/figures/candidates unless an explicit output directory is supplied.
When ``--data-out-dir`` is supplied, the exact bench-minus-floor values used by the
plot and a grouped summary are written there as CSV files.

Run:
    PYTHONPATH=~/brc-tools python verification/scripts/plot_wrf_vs_obs_feb0102.py \\
        --wrf wrf_gfs_2way_per_station.csv wrf_nam_2way_per_station.csv ...
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import polars as pl

from plot_obs_feb0102 import (
    DEFAULT_OBS, DEFAULT_OUT, KAPPA, TS_STATIONS, UTC_TO_MST,
    elev_color, load, panel_letter, save, shade_nights, style_axes,
)
from verify_runs_feb0102 import _read, run_label

# Okabe-Ito, CVD-safe; obs stays black.
RUN_COLORS = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00"]
BENCH, FLOOR = "USU03", "USU07"  # Mountain Home (2228 m) minus Pariette Draw (1465 m)


def load_runs(paths: list[Path]) -> pl.DataFrame:
    """Per-station WRF files -> one hourly-MST frame with run, theta, temp in C."""
    frames = []
    for p in paths:
        df = _read(p)
        frames.append(df.with_columns(pl.lit(run_label(df, p)).alias("run")))
    return (
        pl.concat(frames, how="diagonal")
        .with_columns(
            pl.col("valid_time").dt.offset_by(f"{UTC_TO_MST}h").dt.truncate("1h").alias("hour_mst"),
            (pl.col("temp_2m") - 273.15).alias("temp_c"),
            ((pl.col("temp_2m")) * (1000.0 / (pl.col("pressure_surface") / 100.0)) ** KAPPA)
            .alias("theta"),
        )
        .sort("run", "waypoint", "hour_mst")
    )


def x_axis_time(ax, t_min, t_max) -> None:
    if t_max - t_min <= timedelta(days=1):
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    else:
        ax.xaxis.set_major_locator(mdates.DayLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
        ax.xaxis.set_minor_locator(mdates.HourLocator(byhour=[12]))
        ax.tick_params(axis="x", which="major", length=7)


def fig_temp_timeseries(wrf: pl.DataFrame, hourly: pl.DataFrame, names: dict,
                        runs: list[str], out_dir: Path, out_suffix: str = "") -> None:
    fig, axes = plt.subplots(2, 2, figsize=(9.5, 6.2), sharex=True, sharey=True)
    t_min = min(hourly["hour_mst"].min(), wrf["hour_mst"].min())
    t_max = max(hourly["hour_mst"].max(), wrf["hour_mst"].max())
    for ax, st, letter in zip(axes.flat, TS_STATIONS, "abcd"):
        shade_nights(ax, t_min, t_max)
        w = wrf.filter(pl.col("waypoint") == st)
        band = (w.group_by("hour_mst")
                 .agg(pl.col("temp_c").min().alias("lo"), pl.col("temp_c").max().alias("hi"))
                 .sort("hour_mst"))
        if band.height and len(runs) > 1:
            ax.fill_between(band["hour_mst"], band["lo"], band["hi"],
                            color="0.55", alpha=0.25, lw=0, zorder=1,
                            label="run spread (min-max)")
        for run, color in zip(runs, RUN_COLORS):
            d = w.filter(pl.col("run") == run)
            ax.plot(d["hour_mst"], d["temp_c"], color=color, lw=1.1, zorder=2, label=run)
        o = hourly.filter((pl.col("stid") == st) & pl.col("temp_2m").is_not_null())
        ax.plot(o["hour_mst"], o["temp_2m"], color="black", lw=1.5, zorder=3, label="obs")
        ax.axhline(0.0, color="0.7", lw=0.8, zorder=1)
        ev = names[st]["elev_m"]
        panel_letter(ax, letter, f"{names[st]['name']} ({ev:.0f} m)")
        ax.set_xlim(t_min, t_max)
        x_axis_time(ax, t_min, t_max)
        style_axes(ax)
    for ax in axes[:, 0]:
        ax.set_ylabel("2 m temperature (°C)")
    for ax in axes[1, :]:
        ax.set_xlabel("Local time (MST); shaded = night")
    axes.flat[0].legend(loc="lower right", ncols=1)
    fig.tight_layout()
    save(fig, f"wrf_temp_timeseries_feb0102{out_suffix}", out_dir)


def _dtheta(df: pl.DataFrame, key: str, group: list[str]) -> pl.DataFrame:
    both = (
        df.filter(pl.col(key).is_in([BENCH, FLOOR]) & pl.col("theta").is_finite())
        .pivot(on=key, index=group, values="theta")
    )
    if BENCH not in both.columns or FLOOR not in both.columns:
        return pl.DataFrame()
    return (
        both.drop_nulls([BENCH, FLOOR])
        .select(
            *group,
            pl.col(BENCH).alias("bench_theta_k"),
            pl.col(FLOOR).alias("floor_theta_k"),
        )
        .with_columns(
            (pl.col("bench_theta_k") - pl.col("floor_theta_k")).alias("dtheta_k")
        )
        .sort(group)
    )


def dtheta_table(wrf: pl.DataFrame, hourly: pl.DataFrame) -> pl.DataFrame:
    """Return the exact observation and model series used in the bulk-theta plot."""
    obs = _dtheta(hourly, "stid", ["hour_mst"]).with_columns(
        pl.lit("observation").alias("source_type"),
        pl.lit("observations").alias("series_id"),
        pl.lit("Observations").alias("display_label"),
    )
    model = (
        _dtheta(wrf, "waypoint", ["run_id", "run", "hour_mst"])
        .rename({"run_id": "series_id", "run": "display_label"})
        .with_columns(pl.lit("model").alias("source_type"))
    )
    return (
        pl.concat([obs, model], how="diagonal")
        .with_columns(
            pl.col("hour_mst").dt.offset_by(f"{-UTC_TO_MST}h").alias("valid_time_utc"),
            pl.lit(BENCH).alias("bench_station"),
            pl.lit(FLOOR).alias("floor_station"),
        )
        .select(
            "valid_time_utc",
            "hour_mst",
            "source_type",
            "series_id",
            "display_label",
            "bench_station",
            "floor_station",
            "bench_theta_k",
            "floor_theta_k",
            "dtheta_k",
        )
        .sort("valid_time_utc", "source_type", "series_id")
    )


def write_dtheta_tables(table: pl.DataFrame, out_dir: Path, out_suffix: str = "") -> None:
    """Write auditable point values and their descriptive min/max summary."""
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"bulk_theta_contrast_feb0102{out_suffix}"
    data_path = out_dir / f"{stem}.csv"
    summary_path = out_dir / f"{stem}_summary.csv"
    table.write_csv(data_path)
    (
        table.group_by(
            "source_type",
            "series_id",
            "display_label",
            "bench_station",
            "floor_station",
        )
        .agg(
            pl.col("valid_time_utc").min().alias("first_valid_time_utc"),
            pl.col("valid_time_utc").max().alias("last_valid_time_utc"),
            pl.col("dtheta_k").count().alias("n_hours"),
            pl.col("dtheta_k").min().alias("minimum_dtheta_k"),
            pl.col("dtheta_k").max().alias("maximum_dtheta_k"),
            pl.col("dtheta_k").mean().alias("mean_dtheta_k"),
        )
        .sort("source_type", "series_id")
        .write_csv(summary_path)
    )
    print(f"wrote {data_path} + {summary_path}")


def fig_inversion_index(table: pl.DataFrame, runs: list[str],
                        out_dir: Path, out_suffix: str = "") -> None:
    obs_d = table.filter(pl.col("source_type") == "observation")
    fig, ax = plt.subplots(figsize=(9, 3.8))
    t_min, t_max = obs_d["hour_mst"].min(), obs_d["hour_mst"].max()
    shade_nights(ax, t_min, t_max)
    for run, color in zip(runs, RUN_COLORS):
        d = table.filter(
            (pl.col("source_type") == "model") & (pl.col("display_label") == run)
        )
        if d.height:
            ax.plot(d["hour_mst"], d["dtheta_k"], color=color, lw=1.1, zorder=2, label=run)
    ax.plot(obs_d["hour_mst"], obs_d["dtheta_k"], color="black", lw=1.5, zorder=3,
            label="obs")
    ax.set_ylabel("Δθ bench − floor (K)")
    ax.set_xlabel("Local time (MST); shaded = night")
    ax.set_xlim(t_min, t_max)
    x_axis_time(ax, t_min, t_max)
    ax.legend(loc="upper left")
    style_axes(ax)
    fig.tight_layout()
    save(fig, f"wrf_inversion_index_feb0102{out_suffix}", out_dir)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--wrf", nargs="+", required=True, type=Path,
                    help="per-station csv/parquet files from reduce_wrf_to_stations.py, one per run")
    ap.add_argument("--labels", nargs="*", default=None,
                    help="optional display labels in the same order as --wrf inputs")
    ap.add_argument("--obs", type=Path, default=DEFAULT_OBS)
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT,
                    help="candidate-figure output directory")
    ap.add_argument("--data-out-dir", type=Path, default=None,
                    help="optional directory for exact bulk-theta point and summary CSVs")
    ap.add_argument("--min-time", default=None,
                    help="first UTC valid time to retain, e.g. 2013-02-02T14:00")
    ap.add_argument("--max-time", default=None,
                    help="last UTC valid time to retain, e.g. 2013-02-02T18:00")
    ap.add_argument("--out-suffix", default="",
                    help="suffix appended to both output stems, e.g. _gfs_vs_nam")
    args = ap.parse_args()

    hourly, names = load(args.obs)
    wrf = load_runs(args.wrf)
    for value, op in ((args.min_time, "min"), (args.max_time, "max")):
        if value is None:
            continue
        utc = datetime.fromisoformat(value)
        mst = utc + timedelta(hours=UTC_TO_MST)
        if op == "min":
            wrf = wrf.filter(pl.col("valid_time") >= utc)
            hourly = hourly.filter(pl.col("hour_mst") >= mst)
        else:
            wrf = wrf.filter(pl.col("valid_time") <= utc)
            hourly = hourly.filter(pl.col("hour_mst") <= mst)
    if wrf.is_empty() or hourly.is_empty():
        raise SystemExit("selected valid-time window leaves no WRF or observation rows")
    wrf = wrf.with_columns(pl.col("run").alias("run_id"))
    runs = wrf["run"].unique(maintain_order=True).to_list()
    if args.labels is not None:
        if len(args.labels) != len(runs):
            raise SystemExit(f"--labels needs {len(runs)} values, got {len(args.labels)}")
        label_map = dict(zip(runs, args.labels))
        wrf = wrf.with_columns(pl.col("run").replace_strict(label_map))
        runs = args.labels
    print(f"runs: {runs}; WRF stations: {sorted(wrf['waypoint'].unique().to_list())}")

    dtheta = dtheta_table(wrf, hourly)
    if args.data_out_dir is not None:
        write_dtheta_tables(dtheta, args.data_out_dir, args.out_suffix)
    fig_temp_timeseries(wrf, hourly, names, runs, args.out_dir, args.out_suffix)
    fig_inversion_index(dtheta, runs, args.out_dir, args.out_suffix)


if __name__ == "__main__":
    main()
