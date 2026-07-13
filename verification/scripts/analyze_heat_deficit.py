#!/usr/bin/env python3
"""Definition-tested basin heat-deficit trajectories for Architecture C gate ANA-16.

This manuscript-specific analysis reads exact archived WRF d02 files and uses the
maintained ``brc_tools.nwp.wrf_output.heat_deficit_field`` implementation.  It
area-weights the column diagnostic over a terrain-connected Uinta Basin mask,
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

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import ndimage
import xarray as xr

from brc_tools.nwp import wrf_output as wo


DEFAULT_START = "2013-02-02T13:00:00"
DEFAULT_END = "2013-02-02T18:00:00"
DEFAULT_RETAINED_START = "2013-02-02T14:00:00"
DEFAULT_RETAINED_END = "2013-02-02T18:00:00"
PRIMARY_CREST_M = 2200.0
CREST_SENSITIVITIES_M = (2100.0, 2200.0, 2300.0)
AREA_THRESHOLDS_MJ_M2 = (0.5, 1.0, 2.0)
HORSEPOOL_LAT = 40.144
HORSEPOOL_LON = -109.467
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


def connected_component(mask: np.ndarray, seed: tuple[int, int]) -> np.ndarray:
    if not bool(mask[seed]):
        raise ValueError(f"mask excludes Horsepool seed cell {seed}")
    labels, _count = ndimage.label(mask, structure=np.ones((3, 3), dtype=int))
    selected = labels == labels[seed]
    if not selected.any():
        raise ValueError("terrain-connected basin mask is empty")
    return selected


def touches_edge(mask: np.ndarray) -> bool:
    return bool(mask[0, :].any() or mask[-1, :].any() or mask[:, 0].any() or mask[:, -1].any())


def nearest_cell(lat: np.ndarray, lon: np.ndarray, target_lat: float, target_lon: float) -> tuple[int, int]:
    scale = np.cos(np.deg2rad(target_lat))
    distance2 = (lat - target_lat) ** 2 + ((lon - target_lon) * scale) ** 2
    return tuple(int(index) for index in np.unravel_index(np.nanargmin(distance2), lat.shape))


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


def build_definitions(hgt: np.ndarray, seed: tuple[int, int]) -> dict[str, dict[str, object]]:
    components = {
        crest: connected_component(np.isfinite(hgt) & (hgt < crest), seed)
        for crest in CREST_SENSITIVITIES_M
    }
    open_components = [crest for crest, mask in components.items() if touches_edge(mask)]
    if open_components:
        values = ", ".join(f"{crest:g} m" for crest in open_components)
        raise ValueError(f"terrain-connected basin mask intersects the d02 boundary at {values}")
    primary = components[PRIMARY_CREST_M]
    structure = np.ones((3, 3), dtype=bool)
    eroded = ndimage.binary_erosion(primary, structure=structure, border_value=0)
    dilated = ndimage.binary_dilation(primary, structure=structure) & components[2300.0]
    if not eroded.any() or not dilated.any():
        raise ValueError("one-cell boundary sensitivity produced an empty mask")
    return {
        "crest2100": {"crest_m": 2100.0, "mask": components[2100.0], "boundary": "connected"},
        "crest2200": {"crest_m": 2200.0, "mask": primary, "boundary": "connected"},
        "crest2300": {"crest_m": 2300.0, "mask": components[2300.0], "boundary": "connected"},
        "crest2200_eroded1": {"crest_m": 2200.0, "mask": eroded, "boundary": "eroded_one_cell"},
        "crest2200_dilated1": {"crest_m": 2200.0, "mask": dilated, "boundary": "dilated_one_cell_below_2300m"},
    }


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
    if values.ndim != 2 or values.shape[0] != 1:
        raise ValueError(f"expected one WRF Times record, found shape {values.shape}")
    stamp = b"".join(values[0].tolist()).decode("ascii")
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
    seed = nearest_cell(lat, lon, HORSEPOOL_LAT, HORSEPOOL_LON)
    definitions = build_definitions(hgt, seed)
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
                    "maintenance_pass": bool(difference_in_change < 0),
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
        "horsepool_seed": {
            "j": seed[0],
            "i": seed[1],
            "grid_latitude": float(lat[seed]),
            "grid_longitude": float(lon[seed]),
            "terrain_m": float(hgt[seed]),
        },
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
    primary = trajectory[trajectory["definition"] == "crest2200"].copy()
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
    ax.set_ylabel("Basin-mean heat deficit\n(MJ m$^{-2}$)")
    ax.set_title("a) Area-weighted trajectory; connected terrain mask below 2200 m ASL")
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
    ax.set_title("b) Primary difference with five-definition sensitivity envelope")
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
            "weaker_state": "both GFS-minus-NAM pairs negative at all 14-18 UTC hours under all five definitions",
            "maintenance": "both pair differences in 14-18 UTC change negative under all five definitions",
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
