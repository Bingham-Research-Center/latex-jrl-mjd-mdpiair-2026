#!/usr/bin/env python3
"""Common-AGL cold-pool retention and lower-layer wind diagnostics for matched WRF runs.

The manuscript's short-window comparison needs a vertical diagnostic that is not tied
to native model-level numbers or to scheme-dependent PBL height alone.  For every
reporting station on a shared WRF domain, this script therefore interpolates each run
to common height-above-ground coordinates and computes:

* ``stability_k``: theta(500 m AGL) minus theta(50 m AGL);
* ``transport_wind_ms``: legacy column name for the magnitude of the height-weighted
  mean earth-relative wind vector from 50 to 500 m AGL;
* ``layer_mean_speed_ms``: height-weighted mean horizontal wind speed over that layer;
* ``alignment_ratio``: vector-mean magnitude divided by scalar-mean speed, used only
  to quantify loss from vertical directional cancellation;
* ``pblh_m``: WRF PBLH, retained as a scheme-dependent companion diagnostic; and
* conventional T2, 10 m wind, and surface-pressure values at the same columns.

Run-pair differences are first paired by station and valid time.  Spatial dependence
is preserved by reducing the fixed station field to one median per hour.  A descriptive
two-hour circular moving-block interval is then formed across the five hourly medians.
An optional four-run interaction applies the same pairing to (A-B)-(C-D) before
the hourly spatial median is calculated.
It is deliberately called a sensitivity interval, not a confidence interval: five
hours cannot establish multi-day persistence or a population sampling distribution.

Heavy real-WRF execution belongs on a CHPC compute node.  The maintained Slurm wrapper
is ``verification/slurm/run_retention_analysis.slurm``.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import glob
import hashlib
import json
import math
from pathlib import Path
import platform
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import polars as pl
import xarray as xr

from plot_obs_feb0102 import FULL_W, panel_letter, style_axes
from reduce_wrf_to_stations import DEFAULT_STATIONS_CSV, _decode_time, nearest_cell

G = 9.81
THETA_BASE = 300.0
DEFAULT_START = "2013-02-02T14:00:00"
DEFAULT_END = "2013-02-02T18:00:00"
DEFAULT_SEED = 20130202
# Okabe-Ito, matching the existing WRF-versus-observation figures without
# importing their brc_tools-dependent scoring module.
RUN_COLORS = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00"]
RUN_STYLES = {
    "gfs2": ("#0072B2", "-"),
    "gfs1": ("#56B4E9", "--"),
    "nam2": ("#D55E00", "-"),
    "nam1": ("#E69F00", "--"),
}

PROFILE_METRICS = {
    "stability_k": ("50–500 m AGL\nθ endpoint difference (K)", "K"),
    "transport_wind_ms": (
        "50–500 m AGL\nlayer-mean wind-vector\nmagnitude (m s$^{-1}$)", "m s-1"
    ),
    "layer_mean_speed_ms": ("50–500 m layer-mean scalar speed (m s$^{-1}$)", "m s-1"),
    "alignment_ratio": ("50–500 m vector/scalar alignment ratio", "1"),
    "pblh_m": ("PBL height (m)", "m"),
}

# PBL height remains in the committed tables but is omitted from the manuscript
# figure because it is scheme dependent and did not reproduce the common-layer
# response.  The two load-bearing geometric diagnostics form the compact figure.
FIGURE_METRICS = {key: PROFILE_METRICS[key] for key in ("stability_k", "transport_wind_ms")}

SURFACE_SKILL_METRICS = {
    "t2_bias_c": "degC",
    "t2_abs_error_c": "degC",
    "wind10_bias_ms": "m s-1",
    "wind10_abs_error_ms": "m s-1",
    "psfc_bias_pa": "Pa",
    "psfc_abs_error_pa": "Pa",
}


def parse_key_value(spec: str, kind: str) -> tuple[str, str]:
    if "=" not in spec:
        raise argparse.ArgumentTypeError(f"{kind} must be KEY=VALUE, got {spec!r}")
    key, value = spec.split("=", 1)
    key, value = key.strip(), value.strip()
    if not key or not value:
        raise argparse.ArgumentTypeError(f"{kind} must be KEY=VALUE, got {spec!r}")
    return key, value


def parse_pair(spec: str) -> tuple[str, str]:
    bits = [item.strip() for item in spec.split(",")]
    if len(bits) != 2 or not all(bits):
        raise argparse.ArgumentTypeError(f"pair must be A,B, got {spec!r}")
    if bits[0] == bits[1]:
        raise argparse.ArgumentTypeError("pair members must differ")
    return bits[0], bits[1]


def parse_interaction(spec: str) -> tuple[str, str, str, str]:
    bits = [item.strip() for item in spec.split(",")]
    if len(bits) != 4 or not all(bits):
        raise argparse.ArgumentTypeError(f"interaction must be A,B,C,D, got {spec!r}")
    if len(set(bits)) != 4:
        raise argparse.ArgumentTypeError("interaction members must be four distinct runs")
    return bits[0], bits[1], bits[2], bits[3]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def mass_height_agl(ds: xr.Dataset, it: int, j: int, i: int, hgt: float) -> np.ndarray:
    ph = np.asarray(ds["PH"].isel(Time=it, south_north=j, west_east=i), dtype=float)
    phb = np.asarray(ds["PHB"].isel(Time=it, south_north=j, west_east=i), dtype=float)
    z_stag = (ph + phb) / G
    return 0.5 * (z_stag[:-1] + z_stag[1:]) - hgt


def earth_relative_profile(ds: xr.Dataset, it: int, j: int, i: int) -> tuple[np.ndarray, np.ndarray]:
    u = np.asarray(
        ds["U"]
        .isel(Time=it, south_north=j, west_east_stag=slice(i, i + 2))
        .mean("west_east_stag"),
        dtype=float,
    )
    v = np.asarray(
        ds["V"]
        .isel(Time=it, south_north_stag=slice(j, j + 2), west_east=i)
        .mean("south_north_stag"),
        dtype=float,
    )
    cosa = float(ds["COSALPHA"].isel(Time=it, south_north=j, west_east=i))
    sina = float(ds["SINALPHA"].isel(Time=it, south_north=j, west_east=i))
    return u * cosa - v * sina, v * cosa + u * sina


def interp_profile(agl: np.ndarray, values: np.ndarray, levels: np.ndarray) -> np.ndarray:
    order = np.argsort(agl)
    z = np.asarray(agl[order], dtype=float)
    field = np.asarray(values[order], dtype=float)
    finite = np.isfinite(z) & np.isfinite(field)
    z, field = z[finite], field[finite]
    if len(z) < 2 or levels[0] < z[0] or levels[-1] > z[-1]:
        raise ValueError(
            f"profile does not span requested {levels[0]:g}-{levels[-1]:g} m AGL; "
            f"available={z[0] if len(z) else np.nan:g}-{z[-1] if len(z) else np.nan:g}"
        )
    return np.interp(levels, z, field)


def layer_mean(values: np.ndarray, levels: np.ndarray) -> float:
    # NumPy 2.4 removed np.trapz; avoid evaluating that fallback eagerly.
    integrate = getattr(np, "trapezoid", None)
    if integrate is None:  # pragma: no cover - compatibility with older NumPy
        integrate = np.trapz
    return float(integrate(values, x=levels) / (levels[-1] - levels[0]))


def _surface_value(ds: xr.Dataset, name: str, it: int, j: int, i: int) -> float:
    return float(ds[name].isel(Time=it, south_north=j, west_east=i))


def extract_column(
    ds: xr.Dataset,
    it: int,
    j: int,
    i: int,
    levels: np.ndarray,
) -> dict[str, float]:
    hgt = _surface_value(ds, "HGT", it, j, i)
    agl = mass_height_agl(ds, it, j, i, hgt)
    theta = np.asarray(ds["T"].isel(Time=it, south_north=j, west_east=i), dtype=float) + THETA_BASE
    u, v = earth_relative_profile(ds, it, j, i)
    theta_i = interp_profile(agl, theta, levels)
    u_i = interp_profile(agl, u, levels)
    v_i = interp_profile(agl, v, levels)
    layer_u = layer_mean(u_i, levels)
    layer_v = layer_mean(v_i, levels)
    layer_mean_speed = layer_mean(np.hypot(u_i, v_i), levels)
    vector_magnitude = float(np.hypot(layer_u, layer_v))

    u10_grid = _surface_value(ds, "U10", it, j, i)
    v10_grid = _surface_value(ds, "V10", it, j, i)
    cosa = _surface_value(ds, "COSALPHA", it, j, i)
    sina = _surface_value(ds, "SINALPHA", it, j, i)
    u10 = u10_grid * cosa - v10_grid * sina
    v10 = v10_grid * cosa + u10_grid * sina

    return {
        "model_terrain_m": hgt,
        "theta_bottom_k": float(theta_i[0]),
        "theta_top_k": float(theta_i[-1]),
        "stability_k": float(theta_i[-1] - theta_i[0]),
        "layer_u_ms": layer_u,
        "layer_v_ms": layer_v,
        "transport_wind_ms": vector_magnitude,
        "layer_mean_speed_ms": layer_mean_speed,
        "alignment_ratio": vector_magnitude / layer_mean_speed if layer_mean_speed else np.nan,
        "pblh_m": _surface_value(ds, "PBLH", it, j, i),
        "t2_c": _surface_value(ds, "T2", it, j, i) - 273.15,
        "u10_ms": u10,
        "v10_ms": v10,
        "wind10_ms": float(np.hypot(u10, v10)),
        "psfc_pa": _surface_value(ds, "PSFC", it, j, i),
    }


def load_station_meta(path: Path) -> pd.DataFrame:
    meta = pd.read_csv(path)
    if "in_case_window" in meta:
        meta = meta[meta["in_case_window"].astype(bool)]
    required = {"stid", "latitude", "longitude", "elev_m"}
    missing = required - set(meta.columns)
    if missing:
        raise SystemExit(f"station metadata missing columns: {sorted(missing)}")
    return meta.sort_values("stid").reset_index(drop=True)


def run_files(run_dir: Path, pattern: str) -> list[Path]:
    files = sorted(Path(item) for item in glob.glob(str(run_dir / pattern)) if not item.endswith(".nc"))
    if not files:
        raise SystemExit(f"no WRF files matched {run_dir / pattern}")
    return files


def extract_run(
    label: str,
    run_dir: Path,
    pattern: str,
    meta: pd.DataFrame,
    start: pd.Timestamp,
    end: pd.Timestamp,
    levels: np.ndarray,
) -> tuple[pd.DataFrame, dict[str, object], tuple[np.ndarray, np.ndarray]]:
    files = run_files(run_dir, pattern)
    with xr.open_dataset(files[0], decode_times=False) as ds0:
        xlat = np.asarray(ds0["XLAT"].isel(Time=0), dtype=float)
        xlon = np.asarray(ds0["XLONG"].isel(Time=0), dtype=float)
    cells = {
        row.stid: nearest_cell(xlat, xlon, float(row.latitude), float(row.longitude))
        for row in meta.itertuples()
    }

    rows: list[dict[str, object]] = []
    used_files: list[dict[str, object]] = []
    for path in files:
        used = False
        with xr.open_dataset(path, decode_times=False) as ds:
            valid = pd.to_datetime(
                [_decode_time(item) for item in ds["Times"].values],
                format="%Y-%m-%d_%H:%M:%S",
            )
            for it, when in enumerate(valid):
                if when < start or when > end:
                    continue
                used = True
                for station in meta.itertuples():
                    j, i = cells[station.stid]
                    values = extract_column(ds, it, j, i, levels)
                    rows.append(
                        {
                            "run": label,
                            "station": station.stid,
                            "valid_time": when,
                            "station_latitude": float(station.latitude),
                            "station_longitude": float(station.longitude),
                            "station_elevation_m": float(station.elev_m),
                            "grid_j": j,
                            "grid_i": i,
                            "grid_latitude": float(xlat[j, i]),
                            "grid_longitude": float(xlon[j, i]),
                            **values,
                        }
                    )
        if used:
            stat = path.stat()
            used_files.append(
                {
                    "name": path.name,
                    "size_bytes": stat.st_size,
                    "mtime_utc": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                }
            )
    frame = pd.DataFrame(rows).sort_values(["run", "station", "valid_time"]).reset_index(drop=True)
    if frame.empty:
        raise SystemExit(f"{label}: selected window {start}..{end} produced no rows")
    provenance = {"run_dir": str(run_dir), "files": used_files, "station_cells": cells}
    return frame, provenance, (xlat, xlon)


def validate_coverage(frame: pd.DataFrame, runs: list[str], stations: list[str], expected: pd.DatetimeIndex) -> None:
    expected_set = set(expected)
    for run in runs:
        part = frame[frame["run"] == run]
        got_times = set(pd.to_datetime(part["valid_time"]).unique())
        if got_times != expected_set:
            missing = sorted(expected_set - got_times)
            extra = sorted(got_times - expected_set)
            raise SystemExit(f"{run}: time mismatch; missing={missing}, extra={extra}")
        counts = part.groupby("station")["valid_time"].nunique()
        bad = {station: int(counts.get(station, 0)) for station in stations if counts.get(station, 0) != len(expected)}
        if bad:
            raise SystemExit(f"{run}: incomplete station coverage: {bad}")


def hourly_summary(frame: pd.DataFrame, metrics: list[str]) -> pd.DataFrame:
    long = frame.melt(
        id_vars=["run", "station", "valid_time"],
        value_vars=metrics,
        var_name="metric",
        value_name="value",
    ).dropna(subset=["value"])
    return (
        long.groupby(["run", "valid_time", "metric"], as_index=False)
        .agg(
            n_stations=("station", "nunique"),
            mean=("value", "mean"),
            median=("value", "median"),
            q25=("value", lambda x: x.quantile(0.25)),
            q75=("value", lambda x: x.quantile(0.75)),
            minimum=("value", "min"),
            maximum=("value", "max"),
        )
        .sort_values(["metric", "run", "valid_time"])
        .reset_index(drop=True)
    )


def circular_block_interval(
    values: np.ndarray,
    block_length: int,
    n_resamples: int,
    seed: int,
) -> tuple[float, float]:
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    if len(values) < 2:
        return np.nan, np.nan
    block_length = min(max(int(block_length), 1), len(values))
    n_blocks = math.ceil(len(values) / block_length)
    rng = np.random.default_rng(seed)
    starts = rng.integers(0, len(values), size=(n_resamples, n_blocks))
    offsets = np.arange(block_length)
    indices = (starts[:, :, None] + offsets[None, None, :]) % len(values)
    indices = indices.reshape(n_resamples, -1)[:, : len(values)]
    estimates = values[indices].mean(axis=1)
    return tuple(float(item) for item in np.quantile(estimates, [0.025, 0.975]))


def summarize_hourly_values(
    hourly: pd.DataFrame,
    group_columns: list[str],
    block_length: int,
    n_resamples: int,
    seed: int,
) -> pd.DataFrame:
    rows = []
    for keys, group in hourly.groupby(group_columns, sort=False):
        if not isinstance(keys, tuple):
            keys = (keys,)
        values = group.sort_values("valid_time")["median"].to_numpy(dtype=float)
        lo, hi = circular_block_interval(values, block_length, n_resamples, seed)
        loo = np.array([np.delete(values, i).mean() for i in range(len(values))]) if len(values) > 1 else values
        row = dict(zip(group_columns, keys))
        row.update(
            {
                "n_hours": len(values),
                "n_stations_min": int(group["n_stations"].min()),
                "mean_hourly_spatial_median": float(values.mean()),
                "median_hourly_spatial_median": float(np.median(values)),
                "hourly_minimum": float(values.min()),
                "hourly_maximum": float(values.max()),
                "positive_hours": int((values > 0).sum()),
                "negative_hours": int((values < 0).sum()),
                "block_length_hours": block_length,
                "block_sensitivity_p025": lo,
                "block_sensitivity_p975": hi,
                "leave_one_hour_mean_min": float(loo.min()),
                "leave_one_hour_mean_max": float(loo.max()),
            }
        )
        rows.append(row)
    return pd.DataFrame(rows)


def paired_hourly(frame: pd.DataFrame, pairs: list[tuple[str, str]], metrics: list[str]) -> pd.DataFrame:
    rows = []
    for a, b in pairs:
        aa = frame[frame["run"] == a].set_index(["station", "valid_time"])
        bb = frame[frame["run"] == b].set_index(["station", "valid_time"])
        common = aa.index.intersection(bb.index)
        if common.empty:
            raise SystemExit(f"pair {a},{b} has no common station/times")
        for metric in metrics:
            diff = (aa.loc[common, metric] - bb.loc[common, metric]).rename("value").reset_index()
            for when, group in diff.groupby("valid_time"):
                values = group["value"].dropna()
                rows.append(
                    {
                        "pair": f"{a}_minus_{b}",
                        "run_a": a,
                        "run_b": b,
                        "valid_time": when,
                        "metric": metric,
                        "n_stations": values.size,
                        "mean": values.mean(),
                        "median": values.median(),
                        "q25": values.quantile(0.25),
                        "q75": values.quantile(0.75),
                        "minimum": values.min(),
                        "maximum": values.max(),
                    }
                )
    return pd.DataFrame(rows).sort_values(["pair", "metric", "valid_time"]).reset_index(drop=True)


def interaction_hourly(
    frame: pd.DataFrame,
    interactions: list[tuple[str, str, str, str]],
    metrics: list[str],
) -> pd.DataFrame:
    columns = [
        "interaction",
        "run_a",
        "run_b",
        "run_c",
        "run_d",
        "valid_time",
        "metric",
        "n_stations",
        "mean",
        "median",
        "q25",
        "q75",
        "minimum",
        "maximum",
    ]
    if not interactions:
        return pd.DataFrame(columns=columns)
    rows = []
    for a, b, c, d in interactions:
        indexed = {
            run: frame[frame["run"] == run].set_index(["station", "valid_time"])
            for run in (a, b, c, d)
        }
        common = indexed[a].index
        for run in (b, c, d):
            common = common.intersection(indexed[run].index)
        if common.empty:
            raise SystemExit(f"interaction {a},{b},{c},{d} has no common station/times")
        name = f"{a}_minus_{b}__minus__{c}_minus_{d}"
        for metric in metrics:
            diff = (
                indexed[a].loc[common, metric]
                - indexed[b].loc[common, metric]
                - indexed[c].loc[common, metric]
                + indexed[d].loc[common, metric]
            ).rename("value").reset_index()
            for when, group in diff.groupby("valid_time"):
                values = group["value"].dropna()
                rows.append(
                    {
                        "interaction": name,
                        "run_a": a,
                        "run_b": b,
                        "run_c": c,
                        "run_d": d,
                        "valid_time": when,
                        "metric": metric,
                        "n_stations": values.size,
                        "mean": values.mean(),
                        "median": values.median(),
                        "q25": values.quantile(0.25),
                        "q75": values.quantile(0.75),
                        "minimum": values.min(),
                        "maximum": values.max(),
                    }
                )
    return (
        pd.DataFrame(rows)
        .sort_values(["interaction", "metric", "valid_time"])
        .reset_index(drop=True)
    )


def load_obs(path: Path, start: pd.Timestamp, end: pd.Timestamp) -> pd.DataFrame:
    if path.suffix == ".csv":
        obs = pd.read_csv(path)
    else:
        # The maintained CHPC environment has Polars' native Parquet reader but
        # intentionally does not carry pandas' optional PyArrow/fastparquet layer.
        obs = pd.DataFrame(pl.read_parquet(path).to_dicts())
    required = {"stid", "valid_time", "temp_2m", "wind_speed_10m", "pressure_surface"}
    missing = required - set(obs.columns)
    if missing:
        raise SystemExit(f"observation cache missing columns: {sorted(missing)}")
    obs = obs.copy()
    obs["valid_time"] = pd.to_datetime(obs["valid_time"], utc=True).dt.tz_convert(None).dt.floor("h")
    obs = obs[(obs["valid_time"] >= start) & (obs["valid_time"] <= end)]
    return (
        obs.groupby(["stid", "valid_time"], as_index=False)
        .agg(
            obs_t2_c=("temp_2m", "mean"),
            obs_wind10_ms=("wind_speed_10m", "mean"),
            obs_psfc_pa=("pressure_surface", "mean"),
        )
        .rename(columns={"stid": "station"})
    )


def surface_skill(frame: pd.DataFrame, obs: pd.DataFrame) -> pd.DataFrame:
    joined = frame.merge(obs, on=["station", "valid_time"], how="left", validate="many_to_one")
    joined["t2_bias_c"] = joined["t2_c"] - joined["obs_t2_c"]
    joined["t2_abs_error_c"] = joined["t2_bias_c"].abs()
    joined["wind10_bias_ms"] = joined["wind10_ms"] - joined["obs_wind10_ms"]
    joined["wind10_abs_error_ms"] = joined["wind10_bias_ms"].abs()
    joined["psfc_bias_pa"] = joined["psfc_pa"] - joined["obs_psfc_pa"]
    joined["psfc_abs_error_pa"] = joined["psfc_bias_pa"].abs()
    return joined


def plot_retention(
    hourly: pd.DataFrame,
    run_order: list[str],
    display: dict[str, str],
    out_dir: Path,
    bottom: float,
    top: float,
) -> None:
    fig, axes = plt.subplots(2, 1, figsize=(FULL_W, 4.3), sharex=True, layout="constrained")
    for ax, (metric, (ylabel, _units)), letter in zip(axes, FIGURE_METRICS.items(), "ab"):
        for index, run in enumerate(run_order):
            part = hourly[(hourly["run"] == run) & (hourly["metric"] == metric)].sort_values("valid_time")
            color, linestyle = RUN_STYLES.get(
                run, (RUN_COLORS[index % len(RUN_COLORS)], "-")
            )
            ax.fill_between(
                part["valid_time"], part["q25"], part["q75"], color=color, alpha=0.16, linewidth=0
            )
            ax.plot(
                part["valid_time"],
                part["median"],
                marker="o",
                markersize=3.2,
                linewidth=1.25,
                color=color,
                linestyle=linestyle,
                label=display.get(run, run),
            )
        panel_letter(ax, letter)
        ax.set_ylabel(ylabel.replace("50–500", f"{bottom:g}–{top:g}"))
        style_axes(ax)
    legend_columns = 2 if len(run_order) == 4 else min(3, len(run_order))
    axes[0].legend(loc="best", ncols=legend_columns)
    axes[-1].set_xlabel("Valid time (UTC); lines = station median, shading = station IQR")
    axes[-1].xaxis.set_major_locator(mdates.HourLocator(interval=1))
    axes[-1].xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    out = out_dir / "wrf_retention_ventilation_d02_14to18"
    fig.savefig(out.with_suffix(".png"), dpi=600, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run", action="append", default=[], metavar="KEY=DIR")
    ap.add_argument("--display", action="append", default=[], metavar="KEY=LABEL")
    ap.add_argument(
        "--plot-hourly-summary",
        type=Path,
        help="plot a committed retention_hourly_summary.csv without reopening WRF output",
    )
    ap.add_argument(
        "--run-order",
        nargs="+",
        default=["gfs2", "gfs1", "nam2", "nam1"],
        help="display order for --plot-hourly-summary",
    )
    ap.add_argument("--pair", action="append", default=[], type=parse_pair, metavar="A,B")
    ap.add_argument(
        "--interaction",
        action="append",
        default=[],
        type=parse_interaction,
        metavar="A,B,C,D",
        help="paired difference-in-differences: (A-B)-(C-D)",
    )
    ap.add_argument("--glob", default="wrfout_d02_2013-02-02_*")
    ap.add_argument("--stations", type=Path, default=DEFAULT_STATIONS_CSV)
    ap.add_argument("--obs", type=Path, default=None)
    ap.add_argument("--start", default=DEFAULT_START)
    ap.add_argument("--end", default=DEFAULT_END)
    ap.add_argument("--agl-bottom", type=float, default=50.0)
    ap.add_argument("--agl-top", type=float, default=500.0)
    ap.add_argument("--agl-step", type=float, default=25.0)
    ap.add_argument("--block-length", type=int, default=2)
    ap.add_argument("--bootstrap-resamples", type=int, default=20_000)
    ap.add_argument("--seed", type=int, default=DEFAULT_SEED)
    ap.add_argument("--out-dir", type=Path, required=True)
    args = ap.parse_args()

    display = dict(parse_key_value(item, "display") for item in args.display)
    if args.plot_hourly_summary is not None:
        hourly = pd.read_csv(args.plot_hourly_summary, parse_dates=["valid_time"])
        available = set(hourly["run"].unique())
        missing = set(args.run_order) - available
        if missing:
            raise SystemExit(f"--run-order missing from hourly summary: {sorted(missing)}")
        args.out_dir.mkdir(parents=True, exist_ok=True)
        plot_retention(
            hourly,
            args.run_order,
            display,
            args.out_dir,
            args.agl_bottom,
            args.agl_top,
        )
        return

    if not args.run:
        ap.error("provide at least one --run, or use --plot-hourly-summary")

    run_items = [parse_key_value(item, "run") for item in args.run]
    runs = dict(run_items)
    if len(runs) != len(run_items):
        raise SystemExit("duplicate --run key")
    unknown = (
        set(display)
        | {member for pair in args.pair for member in pair}
        | {member for interaction in args.interaction for member in interaction}
    ) - set(runs)
    if unknown:
        raise SystemExit(f"display/pair/interaction refers to unknown runs: {sorted(unknown)}")
    if args.agl_bottom < 0 or args.agl_top <= args.agl_bottom or args.agl_step <= 0:
        raise SystemExit("require 0 <= --agl-bottom < --agl-top and --agl-step > 0")
    if args.bootstrap_resamples < 100:
        raise SystemExit("--bootstrap-resamples must be at least 100")

    start, end = pd.Timestamp(args.start), pd.Timestamp(args.end)
    if end <= start:
        raise SystemExit("--end must follow --start")
    expected = pd.date_range(start, end, freq="1h")
    levels = np.arange(args.agl_bottom, args.agl_top + 0.5 * args.agl_step, args.agl_step)
    if not np.isclose(levels[-1], args.agl_top):
        levels = np.append(levels[levels < args.agl_top], args.agl_top)
    meta = load_station_meta(args.stations)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    frames = []
    provenance: dict[str, object] = {}
    reference_grid = None
    for label, directory in run_items:
        frame, run_prov, grid = extract_run(
            label, Path(directory), args.glob, meta, start, end, levels
        )
        if reference_grid is None:
            reference_grid = grid
        else:
            if grid[0].shape != reference_grid[0].shape:
                raise SystemExit(f"{label}: grid shape differs from the first run")
            lat_delta = float(np.nanmax(np.abs(grid[0] - reference_grid[0])))
            lon_delta = float(np.nanmax(np.abs(grid[1] - reference_grid[1])))
            if max(lat_delta, lon_delta) > 1.0e-5:
                raise SystemExit(f"{label}: grid differs; max lat/lon delta={lat_delta:g}/{lon_delta:g}")
            run_prov["max_grid_delta_degrees"] = max(lat_delta, lon_delta)
        frames.append(frame)
        provenance[label] = run_prov
        print(f"{label}: {len(frame)} station-hours from {directory}")

    station_frame = pd.concat(frames, ignore_index=True)
    validate_coverage(station_frame, list(runs), meta["stid"].tolist(), expected)
    profile_metrics = list(PROFILE_METRICS)
    hourly = hourly_summary(station_frame, profile_metrics)
    pair_hourly = paired_hourly(station_frame, args.pair, profile_metrics)
    pair_summary = summarize_hourly_values(
        pair_hourly,
        ["pair", "run_a", "run_b", "metric"],
        args.block_length,
        args.bootstrap_resamples,
        args.seed,
    )
    interaction_frame = interaction_hourly(station_frame, args.interaction, profile_metrics)
    interaction_summary = summarize_hourly_values(
        interaction_frame,
        ["interaction", "run_a", "run_b", "run_c", "run_d", "metric"],
        args.block_length,
        args.bootstrap_resamples,
        args.seed,
    )

    station_frame.to_csv(args.out_dir / "retention_station_timeseries.csv", index=False)
    hourly.to_csv(args.out_dir / "retention_hourly_summary.csv", index=False)
    pair_hourly.to_csv(args.out_dir / "retention_pair_hourly.csv", index=False)
    pair_summary.to_csv(args.out_dir / "retention_pair_summary.csv", index=False)
    interaction_frame.to_csv(args.out_dir / "retention_interaction_hourly.csv", index=False)
    interaction_summary.to_csv(args.out_dir / "retention_interaction_summary.csv", index=False)
    plot_retention(hourly, list(runs), display, args.out_dir, args.agl_bottom, args.agl_top)

    if args.obs is not None:
        obs = load_obs(args.obs, start, end)
        skill = surface_skill(station_frame, obs)
        skill_metrics = list(SURFACE_SKILL_METRICS)
        skill_hourly = hourly_summary(skill, skill_metrics)
        skill_summary = summarize_hourly_values(
            skill_hourly,
            ["run", "metric"],
            args.block_length,
            args.bootstrap_resamples,
            args.seed,
        )
        skill_pair_hourly = paired_hourly(skill, args.pair, skill_metrics)
        skill_pair_summary = summarize_hourly_values(
            skill_pair_hourly,
            ["pair", "run_a", "run_b", "metric"],
            args.block_length,
            args.bootstrap_resamples,
            args.seed,
        )
        skill_interaction = interaction_hourly(skill, args.interaction, skill_metrics)
        skill_interaction_summary = summarize_hourly_values(
            skill_interaction,
            ["interaction", "run_a", "run_b", "run_c", "run_d", "metric"],
            args.block_length,
            args.bootstrap_resamples,
            args.seed,
        )
        skill[["run", "station", "valid_time", *skill_metrics]].to_csv(
            args.out_dir / "surface_skill_station_timeseries.csv", index=False
        )
        skill_hourly.to_csv(args.out_dir / "surface_skill_hourly.csv", index=False)
        skill_summary.to_csv(args.out_dir / "surface_skill_summary.csv", index=False)
        skill_pair_hourly.to_csv(args.out_dir / "surface_skill_pair_hourly.csv", index=False)
        skill_pair_summary.to_csv(args.out_dir / "surface_skill_pair_summary.csv", index=False)
        skill_interaction.to_csv(args.out_dir / "surface_skill_interaction_hourly.csv", index=False)
        skill_interaction_summary.to_csv(
            args.out_dir / "surface_skill_interaction_summary.csv", index=False
        )

    metadata = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "command": sys.argv,
        "definitions": {
            "stability_k": f"theta({args.agl_top:g} m AGL) - theta({args.agl_bottom:g} m AGL)",
            "transport_wind_ms": (
                f"magnitude of height-weighted mean earth-relative U/V over "
                f"{args.agl_bottom:g}-{args.agl_top:g} m AGL"
            ),
            "layer_mean_speed_ms": (
                f"height-weighted mean earth-relative horizontal wind speed over "
                f"{args.agl_bottom:g}-{args.agl_top:g} m AGL"
            ),
            "alignment_ratio": (
                "transport_wind_ms / layer_mean_speed_ms; 1 indicates no loss from "
                "vertical directional cancellation"
            ),
            "pblh_m": "native WRF PBLH; scheme-dependent companion diagnostic",
            "uncertainty": (
                "descriptive circular moving-block sensitivity interval across hourly spatial "
                "medians; station field held together; not a formal confidence interval"
            ),
        },
        "window": {"start": start.isoformat(), "end": end.isoformat(), "n_hours": len(expected)},
        "common_agl_m": levels.tolist(),
        "block_length_hours": args.block_length,
        "interactions": [
            {"definition": "(A-B)-(C-D)", "a": a, "b": b, "c": c, "d": d}
            for a, b, c, d in args.interaction
        ],
        "bootstrap_resamples": args.bootstrap_resamples,
        "seed": args.seed,
        "stations": meta["stid"].tolist(),
        "runs": provenance,
        "inputs": {
            "stations": {"path": str(args.stations), "sha256": sha256(args.stations)},
            "observations": (
                {"path": str(args.obs), "sha256": sha256(args.obs)} if args.obs is not None else None
            ),
        },
        "software": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "polars": pl.__version__,
            "xarray": xr.__version__,
            "generator": {"path": str(Path(__file__).resolve()), "sha256": sha256(Path(__file__))},
        },
    }
    (args.out_dir / "retention_analysis_metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n"
    )
    print("\nRetention pair summary:")
    print(pair_summary.to_string(index=False))
    print("\nRetention interaction summary:")
    print(interaction_summary.to_string(index=False))
    print(f"\nwrote analysis to {args.out_dir}")


if __name__ == "__main__":
    main()
