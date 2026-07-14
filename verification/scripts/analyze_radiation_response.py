#!/usr/bin/env python3
"""Slope-radiation and shading screen for gate ANA-18 (CMP07 leg, Main C6).

CMP07 (X1 minus X0) changes only ``slope_rad``, ``topo_shading``, and ``shadlen`` on
an otherwise identical configuration whose members are bitwise identical at
initialization.  The station-column response is near null, which cannot distinguish
a genuinely small treatment from a spatially local one that cancels in aggregate.
This script therefore tests the treatment where its physics acts: on sloped,
sun-facing versus sun-averted terrain.

Predeclared definitions (fixed before running on any model output):

* Slope and aspect are computed from the shared static terrain of the pair (X0/X1
  are terrain-identical); "steep" cells have slope of at least 2 degrees, and
  south-facing / north-facing cells have downslope azimuths within 45 degrees of
  south / north.  A 5-cell edge margin is excluded.
* R1 (radiation organization): the difference between south-facing-steep and
  north-facing-steep cell-area-weighted mean downward-shortwave changes
  (dSWDOWN, X1 minus X0) is at least +5 W m^-2 at every hour from 16:00 to
  18:00 UTC.  Hours 14:00--15:00 UTC are reported as context only because local
  sunrise (about 14:40 UTC) makes shortwave contrasts degenerate there.
* R2 (surface response follows the radiation): the same south-minus-north contrast
  in skin-temperature change (dTSK) is positive at every hour from 16:00 to
  18:00 UTC.

The CMP07 screen verdict is R1 AND R2.  Archived outputs contain no surface heat
fluxes (no HFX/LH), so TSK and 2 m theta are the surface-energy responses available;
this limit is recorded.  The display hour for maps is fixed at 16:00 UTC.
Real WRF work belongs on a CHPC batch node through
``verification/slurm/run_radiation_response.slurm``.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import socket
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analyze_heat_deficit as hd  # noqa: E402
from plot_obs_feb0102 import FULL_W, panel_letter, save, style_axes  # noqa: E402

from brc_tools.nwp import wrf_output as wo  # noqa: E402

EDGE_MARGIN_CELLS = 5
MIN_SLOPE_DEG = 2.0
ASPECT_HALF_WIDTH_DEG = 45.0
R1_MIN_CONTRAST_W_M2 = 5.0
DECISION_HOURS_UTC = (16, 17, 18)
CONTEXT_HOURS_UTC = (14, 15)
DISPLAY_HOUR_UTC = 16
FIELDS = ("SWDOWN", "GLW", "TSK")


def slope_aspect(hgt: np.ndarray, dx: float, dy: float) -> tuple[np.ndarray, np.ndarray]:
    """Slope (deg) and downslope azimuth (deg from north, clockwise)."""
    gy, gx = np.gradient(hgt, dy, dx)
    slope = np.degrees(np.arctan(np.hypot(gx, gy)))
    azimuth = (np.degrees(np.arctan2(-gx, -gy)) + 360.0) % 360.0
    return slope, azimuth


def facing_masks(slope: np.ndarray, azimuth: np.ndarray, region: np.ndarray) -> dict[str, np.ndarray]:
    steep = region & (slope >= MIN_SLOPE_DEG)
    south = steep & (np.abs(azimuth - 180.0) <= ASPECT_HALF_WIDTH_DEG)
    north = steep & ((azimuth <= ASPECT_HALF_WIDTH_DEG) | (azimuth >= 360.0 - ASPECT_HALF_WIDTH_DEG))
    return {"steep": steep, "south": south, "north": north}


def wmean(field: np.ndarray, weights: np.ndarray, mask: np.ndarray) -> float:
    good = mask & np.isfinite(field)
    return float(np.sum(field[good] * weights[good]) / np.sum(weights[good]))


def surface_bundle(path: Path) -> dict[str, object]:
    with wo.open_wrfout(path) as ds:
        observed = hd.internal_valid_time(ds)
        loaded = ds[[*FIELDS, "T2", "PSFC", "HGT"]].load()
    return {
        "valid": observed,
        **{name: wo.surface_field(loaded, name) for name in FIELDS},
        "theta2m": wo.theta_2m(loaded),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run", action="append", required=True, type=lambda s: hd.parse_key_value(s, "run"))
    ap.add_argument("--domain", type=int, default=2)
    ap.add_argument("--start", default="2013-02-02T14:00:00")
    ap.add_argument("--end", default="2013-02-02T18:00:00")
    ap.add_argument("--out-dir", type=Path, required=True)
    args = ap.parse_args()

    runs = {key: Path(value) for key, value in args.run}
    for required in ("x0", "x1"):
        if required not in runs:
            raise SystemExit(f"--run {required}=DIR is required")
    times = pd.date_range(args.start, args.end, freq="1h")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    first_paths = {run: hd.input_path(path, args.domain, times[0]) for run, path in runs.items()}
    static = {run: hd.surface_fields(path) for run, path in first_paths.items()}
    grid_checks = hd.validate_grids(static, [("x1", "x0")], "x0")
    reference = static["x0"]
    lat = np.asarray(reference["lat"], dtype=float)
    lon = np.asarray(reference["lon"], dtype=float)
    hgt = np.asarray(reference["hgt"], dtype=float)
    mapfac = np.asarray(reference["mapfac"], dtype=float)
    cell_area = float(reference["dx"]) * float(reference["dy"]) / np.square(mapfac)

    region = np.zeros(lat.shape, dtype=bool)
    region[EDGE_MARGIN_CELLS:-EDGE_MARGIN_CELLS, EDGE_MARGIN_CELLS:-EDGE_MARGIN_CELLS] = True
    slope, azimuth = slope_aspect(hgt, float(reference["dy"]), float(reference["dx"]))
    masks = facing_masks(slope, azimuth, region)
    mask_counts = {name: int(mask.sum()) for name, mask in masks.items()}

    fields: dict[str, dict[pd.Timestamp, dict[str, object]]] = {run: {} for run in runs}
    input_records: dict[str, dict[str, object]] = {}
    for run, run_dir in runs.items():
        for valid in times:
            path = hd.input_path(run_dir, args.domain, valid)
            data = surface_bundle(path)
            if data["valid"] != valid.to_pydatetime():
                raise SystemExit(f"internal Times mismatch for {path}")
            fields[run][valid] = data
            stat = path.stat()
            input_records[f"{run}:{valid.isoformat()}"] = {
                "path": str(path),
                "bytes": stat.st_size,
                "sha256": hd.sha256(path),
            }

    rows: list[dict[str, object]] = []
    for valid in times:
        deltas = {
            name: fields["x1"][valid][name] - fields["x0"][valid][name]
            for name in (*FIELDS, "theta2m")
        }
        row: dict[str, object] = {"valid_time": valid.isoformat(), "hour_utc": valid.hour}
        for name, delta in deltas.items():
            row[f"{name}_region_mean"] = wmean(delta, cell_area, region)
            row[f"{name}_south_mean"] = wmean(delta, cell_area, masks["south"])
            row[f"{name}_north_mean"] = wmean(delta, cell_area, masks["north"])
            row[f"{name}_south_minus_north"] = row[f"{name}_south_mean"] - row[f"{name}_north_mean"]
            row[f"{name}_region_abs_p99"] = float(
                np.nanpercentile(np.abs(np.where(region, delta, np.nan)), 99)
            )
        rows.append(row)
    summary = pd.DataFrame(rows)
    summary.to_csv(args.out_dir / "radiation_response_summary.csv", index=False)

    decision = summary[summary["hour_utc"].isin(DECISION_HOURS_UTC)]
    r1 = bool((decision["SWDOWN_south_minus_north"] >= R1_MIN_CONTRAST_W_M2).all())
    r2 = bool((decision["TSK_south_minus_north"] > 0.0).all())
    criteria = pd.DataFrame(
        [
            {"criterion": "R1_aspect_organized_swdown", "threshold": R1_MIN_CONTRAST_W_M2, "passed": r1},
            {"criterion": "R2_tsk_follows", "threshold": ">0", "passed": r2},
            {"criterion": "ANA18_cmp07_screen", "threshold": "R1 and R2", "passed": bool(r1 and r2)},
        ]
    )
    criteria.to_csv(args.out_dir / "radiation_response_criteria.csv", index=False)

    display = next(t for t in times if t.hour == DISPLAY_HOUR_UTC)
    aspect_ratio = 1.0 / np.cos(np.deg2rad(float(lat.mean())))
    fig, axes = plt.subplots(2, 2, figsize=(FULL_W, 6.4), layout="constrained")

    for ax, (name, limit, label), letter in zip(
        axes.flat[:2],
        (("SWDOWN", 40.0, "$\\Delta$SWDOWN (W m$^{-2}$)"), ("TSK", 1.5, "$\\Delta$TSK (K)")),
        "ab",
    ):
        delta = fields["x1"][display][name] - fields["x0"][display][name]
        mesh = ax.pcolormesh(
            lon, lat, np.where(region, delta, np.nan), cmap="RdBu_r",
            vmin=-limit, vmax=limit, shading="nearest", rasterized=True,
        )
        ax.contour(lon, lat, hgt, levels=[1700.0, 2200.0], colors="0.35", linewidths=0.5)
        ax.set_aspect(aspect_ratio)
        ax.set_title(f"{label}, {display:%H:%M} UTC", fontsize=9)
        fig.colorbar(mesh, ax=ax, shrink=0.85)
        panel_letter(ax, letter)

    hours = summary["hour_utc"].to_numpy()
    ax = axes[1, 0]
    ax.plot(hours, summary["SWDOWN_south_mean"], marker="o", markersize=4, label="south-facing steep")
    ax.plot(hours, summary["SWDOWN_north_mean"], marker="s", markersize=4, label="north-facing steep")
    ax.axhline(0.0, color="0.35", linewidth=0.7, linestyle="--")
    ax.axvspan(13.7, 15.5, color="0.85", alpha=0.5, zorder=0)
    ax.set_xlabel("Hour (UTC)")
    ax.set_ylabel("Mean $\\Delta$SWDOWN (W m$^{-2}$)")
    ax.legend(fontsize=7.5)
    style_axes(ax)
    panel_letter(ax, "c")

    ax = axes[1, 1]
    ax.plot(hours, summary["TSK_south_minus_north"], marker="o", markersize=4, label="$\\Delta$TSK")
    ax.plot(hours, summary["theta2m_south_minus_north"], marker="s", markersize=4, label="$\\Delta\\theta_{2\\,\\mathrm{m}}$")
    ax.axhline(0.0, color="0.35", linewidth=0.7, linestyle="--")
    ax.axvspan(13.7, 15.5, color="0.85", alpha=0.5, zorder=0)
    ax.set_xlabel("Hour (UTC)")
    ax.set_ylabel("South $-$ north facing contrast (K)")
    ax.legend(fontsize=7.5)
    style_axes(ax)
    panel_letter(ax, "d")

    save(fig, "wrf_radiation_response_cmp07_d02", out_dir=args.out_dir)

    provenance = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "host": socket.getfqdn(),
        "platform": platform.platform(),
        "python": sys.version,
        "argv": sys.argv,
        "git_head": hd.git_output(Path(__file__).resolve().parents[2], "rev-parse", "HEAD"),
        "runs": {run: str(path) for run, path in runs.items()},
        "definitions": {
            "min_slope_deg": MIN_SLOPE_DEG,
            "aspect_half_width_deg": ASPECT_HALF_WIDTH_DEG,
            "edge_margin_cells": EDGE_MARGIN_CELLS,
            "mask_cell_counts": mask_counts,
            "decision_hours_utc": list(DECISION_HOURS_UTC),
            "context_hours_utc": list(CONTEXT_HOURS_UTC),
            "context_reason": "local sunrise near 14:40 UTC makes shortwave contrasts degenerate before 16 UTC",
        },
        "criteria": {
            "R1_min_contrast_w_m2": R1_MIN_CONTRAST_W_M2,
            "R1": r1,
            "R2": r2,
            "ANA18_cmp07_screen_passed": bool(r1 and r2),
        },
        "limits": "archived outputs contain no HFX/LH; TSK and theta2m are the available surface-energy responses",
        "grid_checks": grid_checks,
        "inputs": input_records,
        "environment": {k: os.environ.get(k, "") for k in ("SLURM_JOB_ID", "SLURM_JOB_NODELIST")},
    }
    (args.out_dir / "radiation_response_provenance.json").write_text(
        json.dumps(provenance, indent=2, sort_keys=True) + "\n"
    )
    print(summary[[c for c in summary.columns if "SWDOWN" in c or "TSK" in c or c == "valid_time"]].to_string(index=False))
    print(criteria.to_string(index=False))
    print(f"wrote analysis to {args.out_dir}")


if __name__ == "__main__":
    main()
