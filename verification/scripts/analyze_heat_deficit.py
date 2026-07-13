#!/usr/bin/env python3
"""Definition-tested basin heat-deficit trajectories for Architecture C gate ANA-16.

This manuscript-specific analysis reads exact archived WRF d02 files and uses the
maintained ``brc_tools.nwp.wrf_output.heat_deficit_field`` implementation.  It
area-weights the column diagnostic over a registered d02 evaluation footprint,
evaluates predeclared crest and boundary sensitivities, and tests two distinct
questions:

* weaker state: is GFS-minus-NAM negative at every retained hour; and
* stronger maintenance: is the GFS 14--18 UTC change more negative than NAM's?

The deterministic sensitivity range is not a confidence interval.  Real WRF work
belongs on a CHPC batch node through
``verification/slurm/run_heat_deficit_analysis.slurm``.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import socket
import subprocess
import sys
import tomllib

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
from matplotlib.path import Path as MplPath
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import ndimage
from scipy.spatial import ConvexHull
import xarray as xr

from brc_tools.nwp import wrf_output as wo


DEFAULT_START = "2013-02-02T13:00:00"
DEFAULT_END = "2013-02-02T18:00:00"
DEFAULT_RETAINED_START = "2013-02-02T14:00:00"
DEFAULT_RETAINED_END = "2013-02-02T18:00:00"
PRIMARY_CREST_M = 2200.0
CREST_SENSITIVITIES_M = (2100.0, 2200.0, 2300.0)
AREA_THRESHOLDS_MJ_M2 = (0.5, 1.0, 2.0)
RUN_STYLES = {
    "gfs2": ("#0072B2", "-", "GFS two-way"),
    "gfs1": ("#56B4E9", "--", "GFS one-way"),
    "nam2": ("#D55E00", "-", "NAM two-way"),
    "nam1": ("#E69F00", "--", "NAM one-way"),
}


def parse_key_value(spec: str, kind: str) -> tuple[str, str]:
    if "=" not in spec:
        raise argparse.ArgumentTypeError(f"{kind} must be KEY=VALUE, got {spec!r}")
    key, value = (part.strip() for part in spec.split("=", 1))
    if not key or not value:
        raise argparse.ArgumentTypeError(f"{kind} must be KEY=VALUE, got {spec!r}")
    return key, value


def parse_pair(spec: str) -> tuple[str, str]:
    bits = [part.strip() for part in spec.split(",")]
    if len(bits) != 2 or not all(bits) or bits[0] == bits[1]:
        raise argparse.ArgumentTypeError(f"pair must be distinct A,B, got {spec!r}")
    return bits[0], bits[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_output(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def touches_edge(mask: np.ndarray) -> bool:
    return bool(mask[0, :].any() or mask[-1, :].any() or mask[:, 0].any() or mask[:, -1].any())


def convex_hull_mask(lat: np.ndarray, lon: np.ndarray, points: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    if points.ndim != 2 or points.shape[0] < 3 or points.shape[1] != 2:
        raise ValueError(f"convex hull needs at least three lon/lat points, found {points.shape}")
    hull = ConvexHull(points)
    vertices = points[hull.vertices]
    grid = np.column_stack([lon.ravel(), lat.ravel()])
    closed_vertices = np.vstack([vertices, vertices[0]])
    mask = MplPath(closed_vertices, closed=True).contains_points(grid, radius=1.0e-10).reshape(lat.shape)
    if not mask.any():
        raise ValueError("registered convex-hull footprint contains no d02 cells")
    return mask, vertices


def registered_points(stations_path: Path, figure_config: Path) -> tuple[np.ndarray, np.ndarray, dict[str, object]]:
    stations = pd.read_csv(stations_path)
    required = {"stid", "latitude", "longitude", "in_case_window"}
    missing = required - set(stations.columns)
    if missing:
        raise ValueError(f"station file lacks required columns: {sorted(missing)}")
    selected = stations[stations["in_case_window"].astype(str).str.lower().isin({"true", "1"})]
    station_points = selected[["longitude", "latitude"]].to_numpy(dtype=float)
    with figure_config.open("rb") as stream:
        config = tomllib.load(stream)
    waypoints = config.get("waypoints", {})
    waypoint_points = np.array(
        [[float(value["lon"]), float(value["lat"])] for value in waypoints.values()],
        dtype=float,
    )
    records = {
        "station_count": len(station_points),
        "station_ids": selected["stid"].astype(str).tolist(),
        "waypoint_count": len(waypoint_points),
        "waypoint_names": list(waypoints),
        "stations_path": str(stations_path),
        "stations_sha256": sha256(stations_path),
        "figure_config_path": str(figure_config),
        "figure_config_sha256": sha256(figure_config),
    }
    if len(station_points) != 11:
        raise ValueError(f"expected 11 in-window reporting stations, found {len(station_points)}")
    return station_points, waypoint_points, records


def surface_fields(path: Path) -> dict[str, object]:
    with wo.open_wrfout(path) as ds:
        required = {"HGT", "XLAT", "XLONG", "MAPFAC_M", "T", "P", "PB", "PH", "PHB"}
        missing = sorted(required - set(ds.variables))
        if missing:
            raise ValueError(f"{path} lacks required variables: {missing}")
        dx, dy = wo.dx_dy(ds)
        return {
            "lat": wo.surface_field(ds, "XLAT"),
            "lon": wo.surface_field(ds, "XLONG"),
            "hgt": wo.surface_field(ds, "HGT"),
            "mapfac": wo.surface_field(ds, "MAPFAC_M"),
            "dx": dx,
            "dy": dy,
        }


def validate_grids(
    static: dict[str, dict[str, object]],
    pairs: list[tuple[str, str]],
    mask_run: str,
) -> dict[str, object]:
    reference = static[mask_run]
    checks: dict[str, object] = {"coordinate_reference_run": mask_run, "runs": {}, "pairs": {}}
    tolerances = {"lat": 1.0e-5, "lon": 1.0e-5, "mapfac": 5.0e-7}
    for run, fields in static.items():
        run_checks: dict[str, object] = {}
        for name in ("lat", "lon", "mapfac"):
            left = np.asarray(reference[name], dtype=float)
            right = np.asarray(fields[name], dtype=float)
            if left.shape != right.shape:
                raise ValueError(f"grid shape mismatch for {run} {name}: {right.shape} != {left.shape}")
            max_abs = float(np.nanmax(np.abs(left - right)))
            run_checks[f"{name}_max_abs_difference"] = max_abs
            if max_abs > tolerances[name]:
                raise ValueError(f"grid mismatch for {run} {name}: max abs {max_abs:g}")
        reference_hgt = np.asarray(reference["hgt"], dtype=float)
        run_hgt = np.asarray(fields["hgt"], dtype=float)
        if reference_hgt.shape != run_hgt.shape:
            raise ValueError(f"grid shape mismatch for {run} hgt: {run_hgt.shape} != {reference_hgt.shape}")
        run_checks["hgt_max_abs_difference_from_mask_run_m"] = float(
            np.nanmax(np.abs(reference_hgt - run_hgt))
        )
        for name in ("dx", "dy"):
            difference = abs(float(reference[name]) - float(fields[name]))
            run_checks[f"{name}_difference"] = difference
            if difference > 1.0e-6:
                raise ValueError(f"grid mismatch for {run} {name}: {difference:g}")
        checks["runs"][run] = run_checks
    for a, b in pairs:
        left = np.asarray(static[a]["hgt"], dtype=float)
        right = np.asarray(static[b]["hgt"], dtype=float)
        max_abs = float(np.nanmax(np.abs(left - right)))
        checks["pairs"][f"{a}_minus_{b}"] = {"hgt_max_abs_difference_m": max_abs}
        if max_abs > 1.0e-3:
            raise ValueError(f"paired terrain mismatch for {a},{b}: max abs {max_abs:g} m")
    return checks


def build_definitions(
    hgt: np.ndarray,
    lat: np.ndarray,
    lon: np.ndarray,
    stations_path: Path,
    figure_config: Path,
) -> tuple[dict[str, dict[str, object]], dict[str, object]]:
    station_points, waypoint_points, records = registered_points(stations_path, figure_config)
    combined_points = np.vstack([station_points, waypoint_points])
    combined_hull, combined_vertices = convex_hull_mask(lat, lon, combined_points)
    station_hull, station_vertices = convex_hull_mask(lat, lon, station_points)
    waypoint_hull, waypoint_vertices = convex_hull_mask(lat, lon, waypoint_points)
    finite = np.isfinite(hgt)
    primary = combined_hull & finite & (hgt < PRIMARY_CREST_M)
    structure = np.ones((3, 3), dtype=bool)
    eroded = ndimage.binary_erosion(primary, structure=structure, border_value=0)
    dilated = ndimage.binary_dilation(primary, structure=structure) & finite & (hgt < 2300.0)
    if not eroded.any() or not dilated.any():
        raise ValueError("one-cell boundary sensitivity produced an empty mask")
    definitions = {
        "combined_crest2100": {"crest_m": 2100.0, "mask": combined_hull & finite & (hgt < 2100.0), "boundary": "combined_hull"},
        "combined_crest2200": {"crest_m": 2200.0, "mask": primary, "boundary": "combined_hull"},
        "combined_crest2300": {"crest_m": 2300.0, "mask": combined_hull & finite & (hgt < 2300.0), "boundary": "combined_hull"},
        "stations_crest2200": {"crest_m": 2200.0, "mask": station_hull & finite & (hgt < 2200.0), "boundary": "station_hull"},
        "waypoints_crest2200": {"crest_m": 2200.0, "mask": waypoint_hull & finite & (hgt < 2200.0), "boundary": "waypoint_hull"},
        "crest2200_eroded1": {"crest_m": 2200.0, "mask": eroded, "boundary": "eroded_one_cell"},
        "crest2200_dilated1": {"crest_m": 2200.0, "mask": dilated, "boundary": "dilated_one_cell_below_2300m"},
    }
    invalid = [name for name, spec in definitions.items() if not np.asarray(spec["mask"]).any() or touches_edge(np.asarray(spec["mask"]))]
    if invalid:
        raise ValueError(f"registered footprints are empty or intersect d02 boundary: {invalid}")
    records["hulls"] = {
        "combined_vertices_lon_lat": combined_vertices.tolist(),
        "station_vertices_lon_lat": station_vertices.tolist(),
        "waypoint_vertices_lon_lat": waypoint_vertices.tolist(),
    }
    return definitions, records


def metric_row(
    field_j_m2: np.ndarray,
    cell_area_m2: np.ndarray,
    definition: str,
    spec: dict[str, object],
) -> dict[str, object]:
    mask = np.asarray(spec["mask"], dtype=bool) & np.isfinite(field_j_m2) & np.isfinite(cell_area_m2)
    if not mask.any():
        raise ValueError(f"definition {definition} contains no finite cells")
    weights = cell_area_m2[mask]
    values = field_j_m2[mask]
    area = float(weights.sum())
    row: dict[str, object] = {
        "definition": definition,
        "crest_m": float(spec["crest_m"]),
        "boundary": str(spec["boundary"]),
        "n_cells": int(mask.sum()),
        "mask_area_km2": area / 1.0e6,
        "mean_mj_m2": float(np.sum(values * weights) / area / 1.0e6),
        "integral_tj": float(np.sum(values * weights) / 1.0e12),
    }
    values_mj = values / 1.0e6
    for threshold in AREA_THRESHOLDS_MJ_M2:
        key = f"area_fraction_ge_{threshold:g}_mj_m2".replace(".", "p")
        row[key] = float(weights[values_mj >= threshold].sum() / area)
    return row


def input_path(run_dir: Path, domain: int, valid: pd.Timestamp) -> Path:
    path = wo.wrfout_path(run_dir, domain, valid.to_pydatetime())
    if not path.is_file():
        raise FileNotFoundError(f"missing exact input {path}")
    return path


def internal_valid_time(ds: xr.Dataset) -> datetime:
    values = np.asarray(ds["Times"].values)
    if values.ndim == 2 and values.shape[0] == 1:
        stamp = b"".join(values[0].tolist()).decode("ascii")
    elif values.ndim == 1 and values.shape[0] == 1:
        item = values[0]
        stamp = item.decode("ascii") if isinstance(item, (bytes, np.bytes_)) else str(item)
    else:
        raise ValueError(f"expected one WRF Times record, found shape {values.shape}")
    return datetime.strptime(stamp, "%Y-%m-%d_%H:%M:%S")


def analyze(
    runs: dict[str, Path],
    pairs: list[tuple[str, str]],
    domain: int,
    times: pd.DatetimeIndex,
    retained_start: pd.Timestamp,
    retained_end: pd.Timestamp,
    hash_inputs: bool,
    mask_run: str,
    stations_path: Path,
    figure_config: Path,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, object]]:
    first_paths = {run: input_path(path, domain, times[0]) for run, path in runs.items()}
    static = {run: surface_fields(path) for run, path in first_paths.items()}
    grid_checks = validate_grids(static, pairs, mask_run)
    reference = static[mask_run]
    lat = np.asarray(reference["lat"], dtype=float)
    lon = np.asarray(reference["lon"], dtype=float)
    hgt = np.asarray(reference["hgt"], dtype=float)
    mapfac = np.asarray(reference["mapfac"], dtype=float)
    if not np.all(np.isfinite(mapfac)) or np.any(mapfac <= 0):
        raise ValueError("MAPFAC_M contains nonfinite or nonpositive values")
    definitions, footprint_records = build_definitions(hgt, lat, lon, stations_path, figure_config)
    cell_area = float(reference["dx"]) * float(reference["dy"]) / np.square(mapfac)

    input_records: dict[str, dict[str, object]] = {}
    rows: list[dict[str, object]] = []
    for run, run_dir in runs.items():
        for valid in times:
            path = input_path(run_dir, domain, valid)
            with wo.open_wrfout(path) as ds:
                observed_valid = internal_valid_time(ds)
                if observed_valid != valid.to_pydatetime():
                    raise ValueError(
                        f"internal Times mismatch for {path}: {observed_valid} != {valid.to_pydatetime()}"
                    )
                # One file at a time; load only the fields used by the productized diagnostic.
                loaded = ds[["T", "P", "PB", "PH", "PHB"]].load()
                fields = {
                    crest: wo.heat_deficit_field(loaded, crest)
                    for crest in CREST_SENSITIVITIES_M
                }
            stat = path.stat()
            input_records[str(path)] = {
                "internal_valid_time": observed_valid.isoformat(),
                "size_bytes": stat.st_size,
                "mtime_ns": stat.st_mtime_ns,
                "sha256": sha256(path) if hash_inputs else None,
            }
            for definition, spec in definitions.items():
                row = metric_row(fields[float(spec["crest_m"])], cell_area, definition, spec)
                row.update({"run": run, "valid_time": valid.isoformat(), "input_path": str(path)})
                rows.append(row)
    trajectory = pd.DataFrame(rows).sort_values(["definition", "run", "valid_time"]).reset_index(drop=True)

    retained = trajectory[
        (pd.to_datetime(trajectory["valid_time"]) >= retained_start)
        & (pd.to_datetime(trajectory["valid_time"]) <= retained_end)
    ]
    pair_rows: list[dict[str, object]] = []
    for a, b in pairs:
        for definition in definitions:
            aa = retained[(retained["run"] == a) & (retained["definition"] == definition)].set_index("valid_time")
            bb = retained[(retained["run"] == b) & (retained["definition"] == definition)].set_index("valid_time")
            if list(aa.index) != list(bb.index) or len(aa) != 5:
                raise ValueError(f"retained pairing failed for {a},{b},{definition}")
            differences = aa["mean_mj_m2"] - bb["mean_mj_m2"]
            a_change = float(aa.iloc[-1]["mean_mj_m2"] - aa.iloc[0]["mean_mj_m2"])
            b_change = float(bb.iloc[-1]["mean_mj_m2"] - bb.iloc[0]["mean_mj_m2"])
            difference_in_change = a_change - b_change
            pair_rows.append(
                {
                    "pair": f"{a}_minus_{b}",
                    "a": a,
                    "b": b,
                    "definition": definition,
                    "retained_start": retained_start.isoformat(),
                    "retained_end": retained_end.isoformat(),
                    "retained_hours": len(differences),
                    "negative_hours": int((differences < 0).sum()),
                    "minimum_difference_mj_m2": float(differences.min()),
                    "maximum_difference_mj_m2": float(differences.max()),
                    "mean_difference_mj_m2": float(differences.mean()),
                    "a_change_14to18_mj_m2": a_change,
                    "b_change_14to18_mj_m2": b_change,
                    "difference_in_change_mj_m2": difference_in_change,
                    "weaker_state_pass": bool((differences < 0).all()),
                    "gfs_loss_pass": bool(a_change < 0),
                    "maintenance_pass": bool(a_change < 0 and difference_in_change < 0),
                }
            )
    pair_summary = pd.DataFrame(pair_rows).sort_values(["pair", "definition"]).reset_index(drop=True)

    sensitivity_rows: list[dict[str, object]] = []
    for pair, group in pair_summary.groupby("pair", sort=True):
        sensitivity_rows.append(
            {
                "scope": pair,
                "definitions": len(group),
                "weaker_state_definitions_pass": int(group["weaker_state_pass"].sum()),
                "gfs_loss_definitions_pass": int(group["gfs_loss_pass"].sum()),
                "maintenance_definitions_pass": int(group["maintenance_pass"].sum()),
                "weaker_state_pass": bool(group["weaker_state_pass"].all()),
                "maintenance_pass": bool(group["maintenance_pass"].all()),
                "difference_in_change_min_mj_m2": float(group["difference_in_change_mj_m2"].min()),
                "difference_in_change_max_mj_m2": float(group["difference_in_change_mj_m2"].max()),
                "retained_hourly_difference_min_mj_m2": float(group["minimum_difference_mj_m2"].min()),
                "retained_hourly_difference_max_mj_m2": float(group["maximum_difference_mj_m2"].max()),
            }
        )
    pair_sensitivity = pd.DataFrame(sensitivity_rows)
    overall = {
        "scope": "both_feedback_modes",
        "definitions": int(pair_sensitivity["definitions"].sum()),
        "weaker_state_definitions_pass": int(pair_sensitivity["weaker_state_definitions_pass"].sum()),
        "gfs_loss_definitions_pass": int(pair_sensitivity["gfs_loss_definitions_pass"].sum()),
        "maintenance_definitions_pass": int(pair_sensitivity["maintenance_definitions_pass"].sum()),
        "weaker_state_pass": bool(pair_sensitivity["weaker_state_pass"].all()),
        "maintenance_pass": bool(pair_sensitivity["maintenance_pass"].all()),
        "difference_in_change_min_mj_m2": float(pair_sensitivity["difference_in_change_min_mj_m2"].min()),
        "difference_in_change_max_mj_m2": float(pair_sensitivity["difference_in_change_max_mj_m2"].max()),
        "retained_hourly_difference_min_mj_m2": float(pair_sensitivity["retained_hourly_difference_min_mj_m2"].min()),
        "retained_hourly_difference_max_mj_m2": float(pair_sensitivity["retained_hourly_difference_max_mj_m2"].max()),
    }
    sensitivity = pd.concat([pair_sensitivity, pd.DataFrame([overall])], ignore_index=True)
    mask_records = {
        name: {
            "crest_m": float(spec["crest_m"]),
            "boundary": str(spec["boundary"]),
            "n_cells": int(np.asarray(spec["mask"], dtype=bool).sum()),
            "area_km2": float(cell_area[np.asarray(spec["mask"], dtype=bool)].sum() / 1.0e6),
        }
        for name, spec in definitions.items()
    }
    provenance = {
        "grid_validation": grid_checks,
        "registered_footprint": footprint_records,
        "definitions": mask_records,
        "inputs": input_records,
        "decision": overall,
    }
    return trajectory, pair_summary, sensitivity, provenance


def plot_trajectory(
    trajectory: pd.DataFrame,
    pairs: list[tuple[str, str]],
    displays: dict[str, str],
    out_png: Path,
    out_pdf: Path,
) -> None:
    primary = trajectory[trajectory["definition"] == "combined_crest2200"].copy()
    primary["valid_time"] = pd.to_datetime(primary["valid_time"])
    all_times = sorted(primary["valid_time"].unique())
    all_definitions = sorted(trajectory["definition"].unique())
    fig, axes = plt.subplots(2, 1, figsize=(7.2, 7.0), sharex=True, constrained_layout=True)

    ax = axes[0]
    for run in sorted(primary["run"].unique()):
        group = primary[primary["run"] == run].sort_values("valid_time")
        color, linestyle, default_label = RUN_STYLES.get(run, (None, "-", run))
        ax.plot(
            group["valid_time"],
            group["mean_mj_m2"],
            marker="o",
            color=color,
            linestyle=linestyle,
            linewidth=1.7,
            label=displays.get(run, default_label),
        )
    ax.set_ylabel("Footprint-mean heat deficit\n(MJ m$^{-2}$)")
    ax.set_title("a) Registered-footprint trajectory; 2200 m ASL reference")
    ax.legend(frameon=False, ncol=2, fontsize=8)
    ax.grid(alpha=0.25)

    ax = axes[1]
    pair_colors = ["#6A3D9A", "#009E73"]
    for (a, b), color in zip(pairs, pair_colors):
        primary_a = primary[primary["run"] == a].set_index("valid_time")["mean_mj_m2"]
        primary_b = primary[primary["run"] == b].set_index("valid_time")["mean_mj_m2"]
        difference = primary_a - primary_b
        lower, upper = [], []
        for when in all_times:
            values = []
            for definition in all_definitions:
                subset = trajectory[
                    (trajectory["definition"] == definition)
                    & (pd.to_datetime(trajectory["valid_time"]) == when)
                ]
                va = float(subset[subset["run"] == a]["mean_mj_m2"].iloc[0])
                vb = float(subset[subset["run"] == b]["mean_mj_m2"].iloc[0])
                values.append(va - vb)
            lower.append(min(values))
            upper.append(max(values))
        label = f"{displays.get(a, a)} minus {displays.get(b, b)}"
        ax.fill_between(all_times, lower, upper, color=color, alpha=0.16, linewidth=0)
        ax.plot(difference.index, difference.values, marker="o", color=color, linewidth=1.7, label=label)
    ax.axhline(0.0, color="0.25", linewidth=0.8)
    ax.set_ylabel("GFS minus NAM\n(MJ m$^{-2}$)")
    ax.set_title("b) Primary difference with seven-definition sensitivity envelope")
    ax.legend(frameon=False, fontsize=8)
    ax.grid(alpha=0.25)
    ax.xaxis.set_major_locator(mdates.HourLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%HZ"))
    axes[0].axvline(pd.Timestamp(DEFAULT_RETAINED_START), color="0.35", linestyle=":", linewidth=1.0)
    axes[1].axvline(pd.Timestamp(DEFAULT_RETAINED_START), color="0.35", linestyle=":", linewidth=1.0)
    fig.suptitle("WRF cold-pool heat-deficit gate, d02, 2 February 2013\n13 UTC is trajectory context; decision window is 14--18 UTC")
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=220)
    fig.savefig(out_pdf)
    plt.close(fig)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="append", required=True, help="KEY=exact run directory")
    parser.add_argument("--display", action="append", default=[], help="KEY=display label")
    parser.add_argument("--pair", action="append", required=True, help="GFS_KEY,NAM_KEY")
    parser.add_argument("--domain", type=int, default=2)
    parser.add_argument("--mask-run", required=True, help="run key whose static HGT defines every mask")
    parser.add_argument("--stations", type=Path, required=True)
    parser.add_argument("--figure-config", type=Path, required=True)
    parser.add_argument("--start", default=DEFAULT_START)
    parser.add_argument("--end", default=DEFAULT_END)
    parser.add_argument("--retained-start", default=DEFAULT_RETAINED_START)
    parser.add_argument("--retained-end", default=DEFAULT_RETAINED_END)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--brc-tools-dir", type=Path, required=True)
    parser.add_argument("--hash-inputs", action=argparse.BooleanOptionalAction, default=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    started = datetime.now(timezone.utc)
    runs = dict(parse_key_value(spec, "run") for spec in args.run)
    displays = dict(parse_key_value(spec, "display") for spec in args.display)
    pairs = [parse_pair(spec) for spec in args.pair]
    for a, b in pairs:
        if a not in runs or b not in runs:
            raise SystemExit(f"pair {a},{b} references an undefined run")
    if args.mask_run not in runs:
        raise SystemExit(f"mask run {args.mask_run!r} is undefined")
    start = pd.Timestamp(args.start)
    end = pd.Timestamp(args.end)
    retained_start = pd.Timestamp(args.retained_start)
    retained_end = pd.Timestamp(args.retained_end)
    times = pd.date_range(start, end, freq="1h")
    if retained_start not in times or retained_end not in times or retained_start >= retained_end:
        raise SystemExit("retained window must be a nonempty subset of the trajectory window")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    trajectory, pair_summary, sensitivity, provenance = analyze(
        runs,
        pairs,
        args.domain,
        times,
        retained_start,
        retained_end,
        args.hash_inputs,
        args.mask_run,
        args.stations,
        args.figure_config,
    )
    paths = {
        "trajectory": args.out_dir / "heat_deficit_trajectory.csv",
        "pair_summary": args.out_dir / "heat_deficit_pair_summary.csv",
        "sensitivity": args.out_dir / "heat_deficit_sensitivity.csv",
        "figure_png": args.out_dir / "wrf_heat_deficit_d02_13to18.png",
        "figure_pdf": args.out_dir / "wrf_heat_deficit_d02_13to18.pdf",
    }
    trajectory.to_csv(paths["trajectory"], index=False)
    pair_summary.to_csv(paths["pair_summary"], index=False)
    sensitivity.to_csv(paths["sensitivity"], index=False)
    plot_trajectory(trajectory, pairs, displays, paths["figure_png"], paths["figure_pdf"])

    repo = Path(__file__).resolve().parents[2]
    output_hashes = {name: {"path": str(path), "sha256": sha256(path)} for name, path in paths.items()}
    metadata = {
        "request_id": "20260713-c4-ana16",
        "analysis_id": "ANA-16",
        "started_utc": started.isoformat(),
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "host": socket.getfqdn(),
        "slurm_job_id": os.environ.get("SLURM_JOB_ID"),
        "command": [sys.executable, *sys.argv],
        "repository": {
            "path": str(repo),
            "commit": git_output(repo, "rev-parse", "HEAD"),
            "dirty": bool(git_output(repo, "status", "--porcelain")),
            "script_sha256": sha256(Path(__file__).resolve()),
        },
        "brc_tools": {
            "path": str(args.brc_tools_dir.resolve()),
            "commit": git_output(args.brc_tools_dir, "rev-parse", "HEAD"),
            "dirty": bool(git_output(args.brc_tools_dir, "status", "--porcelain")),
            "heat_deficit_source_sha256": sha256(args.brc_tools_dir / "brc_tools/nwp/wrf_output.py"),
        },
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "xarray": xr.__version__,
            "scipy": scipy.__version__,
            "matplotlib": matplotlib.__version__,
        },
        "scope": {
            "domain": args.domain,
            "trajectory_start": start.isoformat(),
            "trajectory_end": end.isoformat(),
            "retained_start": retained_start.isoformat(),
            "retained_end": retained_end.isoformat(),
            "runs": {key: str(value) for key, value in runs.items()},
            "mask_run": args.mask_run,
            "pairs": [{"a": a, "b": b, "sign": f"{a} minus {b}"} for a, b in pairs],
        },
        "metric": {
            "formula": "(cp/g) integral max(theta_crest-theta,0) dp below crest",
            "column_units": "J m-2",
            "mean_units": "MJ m-2",
            "horizontal_integral_units": "TJ",
            "cell_area": "DX*DY/MAPFAC_M^2",
            "area_fraction_thresholds_mj_m2": list(AREA_THRESHOLDS_MJ_M2),
            "implementation": "brc_tools.nwp.wrf_output.heat_deficit_field",
        },
        "predeclared_decision": {
            "weaker_state": "both GFS-minus-NAM pairs negative at all 14-18 UTC hours under all seven definitions",
            "maintenance": "both GFS changes and both GFS-minus-NAM differences in 14-18 UTC change negative under all seven definitions",
            "trajectory_context": "13 UTC is excluded from the decision",
        },
        **provenance,
        "outputs": output_hashes,
    }
    metadata_path = args.out_dir / "heat-deficit-analysis.json"
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(json.dumps(metadata["decision"], indent=2, sort_keys=True))
    print(f"wrote {metadata_path}")


if __name__ == "__main__":
    main()
