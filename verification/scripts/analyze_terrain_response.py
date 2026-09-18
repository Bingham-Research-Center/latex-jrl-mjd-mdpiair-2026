#!/usr/bin/env python3
"""Terrain-source geometry response for gate ANA-17 (Main C5).

Analyses CMP09 (X3 minus X0: default minus fine 3-arc-second static terrain on an
otherwise identical NAM one-way configuration) with predeclared elevation-band and
terrain-correlation diagnostics, and evaluates CMP10 (X3 minus X4) and CMP11
(X0 minus X4) only if the X4 lineage check passes.  All criteria and definitions
below were fixed in this script before it was run on any model output.

X4 lineage check (both parts must pass before any X4-based number is reported):

* L1: the archived ``namelist.input`` in the X4 run directory hashes to the same
  SHA-256 as the X0/X3 namelist recorded in the run inventory
  (``36ebe14b72e128116fb9a44848ad3c7d62cce2d17dec587ff7b2d8b995822b77``), so the
  only lever left is the WPS static input; and
* L2: the X4 terrain is materially smoother than the default-terrain member on the
  same grid: its mean absolute nearest-neighbor height difference is less than half
  of X3's (a 5-arc-minute source on a 1 km grid must be much smoother).

Predeclared response diagnostics, evaluated at every retained hour
(14:00--18:00 UTC), on the d02 grid excluding a 5-cell edge margin, with elevation
bands fixed from the fine-terrain control X0: floor below 1700 m, slopes 1700--2200 m,
above 2200 m.

* G1 (slope organization): the cell-area-weighted mean of |d theta_2m| in the slopes
  band is at least 1.5 times the floor-band value at every retained hour.
* G2 (terrain correlation): the area-weighted Pearson correlation between
  d theta_2m and the terrain-height difference of the pair has magnitude at least
  0.3 at every retained hour.

The CMP09 gate verdict is G1 AND G2 at all five hours.  Station-sample means at the
eleven registered columns and per-station model-minus-station elevations for
X0/X3/X4 are reported as context (the aggregate-cancellation and pressure-artifact
legs), not as gate criteria.  The display hour for maps is fixed in advance at
16:00 UTC.  Real WRF work belongs on a CHPC batch node through
``verification/slurm/run_terrain_response.slurm``.
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
from analyze_spatial_response import interp_at_agl  # noqa: E402
from plot_obs_feb0102 import FULL_W, panel_letter, save, style_axes  # noqa: E402

from brc_tools.nwp import wrf_output as wo  # noqa: E402

EXPECTED_NAMELIST_SHA256 = "36ebe14b72e128116fb9a44848ad3c7d62cce2d17dec587ff7b2d8b995822b77"
EDGE_MARGIN_CELLS = 5
BAND_EDGES_M = (1700.0, 2200.0)
G1_SLOPE_TO_FLOOR_RATIO = 1.5
G2_MIN_ABS_CORRELATION = 0.3
L2_SMOOTHNESS_RATIO = 0.5
DISPLAY_HOUR_UTC = 16
STABILITY_TOP_M = 500.0
STABILITY_BOTTOM_M = 50.0


def roughness(hgt: np.ndarray, region: np.ndarray) -> float:
    """Mean absolute nearest-neighbor height difference (m) within a region."""
    diffs = []
    for shift in ((0, 1), (1, 0)):
        rolled = np.roll(hgt, shift, axis=(0, 1))
        valid = region & np.roll(region, shift, axis=(0, 1))
        diffs.append(np.abs(hgt - rolled)[valid])
    return float(np.concatenate(diffs).mean())


def weighted_corr(x: np.ndarray, y: np.ndarray, w: np.ndarray, mask: np.ndarray) -> float:
    good = mask & np.isfinite(x) & np.isfinite(y)
    xw, yw, ww = x[good], y[good], w[good]
    wsum = ww.sum()
    mx, my = (xw * ww).sum() / wsum, (yw * ww).sum() / wsum
    cov = ((xw - mx) * (yw - my) * ww).sum() / wsum
    sx = np.sqrt(((xw - mx) ** 2 * ww).sum() / wsum)
    sy = np.sqrt(((yw - my) ** 2 * ww).sum() / wsum)
    return float(cov / (sx * sy))


def band_mean_abs(field: np.ndarray, weights: np.ndarray, band: np.ndarray) -> float:
    good = band & np.isfinite(field)
    return float(np.sum(np.abs(field[good]) * weights[good]) / np.sum(weights[good]))


def surface_and_stability(path: Path) -> dict[str, object]:
    with wo.open_wrfout(path) as ds:
        observed = hd.internal_valid_time(ds)
        loaded = ds[["T", "P", "PB", "PH", "PHB", "T2", "PSFC", "HGT"]].load()
    theta = wo.potential_temperature(loaded)
    agl = wo.height_agl(loaded)
    return {
        "valid": observed,
        "theta2m": wo.theta_2m(loaded),
        "stability": interp_at_agl(theta, agl, STABILITY_TOP_M)
        - interp_at_agl(theta, agl, STABILITY_BOTTOM_M),
        "terrain": wo.surface_field(loaded, "HGT"),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run", action="append", required=True, type=lambda s: hd.parse_key_value(s, "run"))
    ap.add_argument("--domain", type=int, default=2)
    ap.add_argument("--stations", type=Path, default=Path("verification/data/stations_2013_selection.csv"))
    ap.add_argument("--start", default="2013-02-02T14:00:00")
    ap.add_argument("--end", default="2013-02-02T18:00:00")
    ap.add_argument("--out-dir", type=Path, required=True)
    args = ap.parse_args()

    runs = {key: Path(value) for key, value in args.run}
    for required in ("x0", "x3", "x4"):
        if required not in runs:
            raise SystemExit(f"--run {required}=DIR is required")
    times = pd.date_range(args.start, args.end, freq="1h")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    # --- static terrain, grids, region, bands -------------------------------------
    first_paths = {run: hd.input_path(path, args.domain, times[0]) for run, path in runs.items()}
    static = {run: hd.surface_fields(path) for run, path in first_paths.items()}
    # Coordinates must agree; terrain deliberately differs, so validate lat/lon/mapfac
    # against x0 without the paired-terrain check used by the feedback analyses.
    reference = static["x0"]
    for run, fields in static.items():
        for name, tol in (("lat", 1e-5), ("lon", 1e-5), ("mapfac", 5e-7)):
            gap = float(np.nanmax(np.abs(np.asarray(reference[name]) - np.asarray(fields[name]))))
            if gap > tol:
                raise SystemExit(f"grid mismatch for {run} {name}: {gap:g}")
    lat = np.asarray(reference["lat"], dtype=float)
    hgt = {run: np.asarray(fields["hgt"], dtype=float) for run, fields in static.items()}
    mapfac = np.asarray(reference["mapfac"], dtype=float)
    cell_area = float(reference["dx"]) * float(reference["dy"]) / np.square(mapfac)

    region = np.zeros(lat.shape, dtype=bool)
    region[EDGE_MARGIN_CELLS:-EDGE_MARGIN_CELLS, EDGE_MARGIN_CELLS:-EDGE_MARGIN_CELLS] = True
    floor = region & (hgt["x0"] < BAND_EDGES_M[0])
    slopes = region & (hgt["x0"] >= BAND_EDGES_M[0]) & (hgt["x0"] < BAND_EDGES_M[1])
    above = region & (hgt["x0"] >= BAND_EDGES_M[1])
    bands = {"floor": floor, "slopes": slopes, "above": above}

    # --- X4 lineage ----------------------------------------------------------------
    x4_namelist = runs["x4"] / "namelist.input"
    l1_hash = hd.sha256(x4_namelist) if x4_namelist.is_file() else "missing"
    l1 = bool(l1_hash == EXPECTED_NAMELIST_SHA256)
    rough = {run: roughness(hgt[run], region) for run in ("x0", "x3", "x4")}
    l2 = bool(rough["x4"] < L2_SMOOTHNESS_RATIO * rough["x3"])
    lineage_passed = bool(l1 and l2)
    lineage = {
        "L1_namelist_sha256": l1_hash,
        "L1_expected": EXPECTED_NAMELIST_SHA256,
        "L1_passed": l1,
        "L2_roughness_m": rough,
        "L2_ratio_threshold": L2_SMOOTHNESS_RATIO,
        "L2_passed": l2,
        "lineage_passed": lineage_passed,
    }

    pairs = [("x3", "x0", "cmp09")]
    if lineage_passed:
        pairs += [("x3", "x4", "cmp10"), ("x0", "x4", "cmp11")]

    # --- station columns -----------------------------------------------------------
    stations = pd.read_csv(args.stations)
    selected = stations[stations["in_case_window"].astype(str).str.lower().isin({"true", "1"})]
    lon = np.asarray(reference["lon"], dtype=float)
    columns = []
    for _, row in selected.iterrows():
        j, i = np.unravel_index(
            np.argmin((lat - row["latitude"]) ** 2 + (lon - row["longitude"]) ** 2), lat.shape
        )
        columns.append({"stid": row["stid"], "j": int(j), "i": int(i), "elev_m": float(row["elev_m"])})
    elevation_rows = [
        {
            "stid": col["stid"],
            "station_elev_m": col["elev_m"],
            **{f"{run}_model_minus_station_m": float(hgt[run][col["j"], col["i"]] - col["elev_m"]) for run in ("x0", "x3", "x4")},
        }
        for col in columns
    ]
    pd.DataFrame(elevation_rows).to_csv(args.out_dir / "terrain_station_elevation.csv", index=False)

    # --- hourly response fields ----------------------------------------------------
    fields: dict[str, dict[pd.Timestamp, dict[str, object]]] = {run: {} for run in runs}
    input_records: dict[str, dict[str, object]] = {}
    for run, run_dir in runs.items():
        for valid in times:
            path = hd.input_path(run_dir, args.domain, valid)
            data = surface_and_stability(path)
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
    for a, b, cmp_id in pairs:
        dh = hgt[a] - hgt[b]
        for valid in times:
            d2m = fields[a][valid]["theta2m"] - fields[b][valid]["theta2m"]
            dstab = fields[a][valid]["stability"] - fields[b][valid]["stability"]
            station_mean = float(np.mean([d2m[c["j"], c["i"]] for c in columns]))
            row = {
                "comparison": cmp_id,
                "pair": f"{a}_minus_{b}",
                "valid_time": valid.isoformat(),
                "terrain_rms_m": float(np.sqrt(np.mean(dh[region] ** 2))),
                "terrain_min_m": float(dh[region].min()),
                "terrain_max_m": float(dh[region].max()),
                "corr_theta2m_terrain": weighted_corr(d2m, dh, cell_area, region),
                "station_sample_mean_k": station_mean,
            }
            for band_name, band in bands.items():
                row[f"{band_name}_mean_abs_theta2m_k"] = band_mean_abs(d2m, cell_area, band)
                row[f"{band_name}_mean_abs_stability_k"] = band_mean_abs(dstab, cell_area, band)
            row["slope_to_floor_ratio"] = row["slopes_mean_abs_theta2m_k"] / row["floor_mean_abs_theta2m_k"]
            rows.append(row)
    summary = pd.DataFrame(rows)
    summary.to_csv(args.out_dir / "terrain_response_summary.csv", index=False)

    cmp09 = summary[summary["comparison"] == "cmp09"]
    g1 = bool((cmp09["slope_to_floor_ratio"] >= G1_SLOPE_TO_FLOOR_RATIO).all())
    g2 = bool((cmp09["corr_theta2m_terrain"].abs() >= G2_MIN_ABS_CORRELATION).all())
    criteria = pd.DataFrame(
        [
            {"criterion": "L1_namelist_identity", "passed": l1},
            {"criterion": "L2_terrain_smoothness", "passed": l2},
            {"criterion": "G1_slope_organization", "threshold": G1_SLOPE_TO_FLOOR_RATIO, "passed": g1},
            {"criterion": "G2_terrain_correlation", "threshold": G2_MIN_ABS_CORRELATION, "passed": g2},
            {"criterion": "ANA17_cmp09_gate", "threshold": "G1 and G2", "passed": bool(g1 and g2)},
        ]
    )
    criteria.to_csv(args.out_dir / "terrain_response_criteria.csv", index=False)

    # --- figure: terrain difference, response, bands, correlation ------------------
    display = next(t for t in times if t.hour == DISPLAY_HOUR_UTC)
    dh09 = hgt["x3"] - hgt["x0"]
    d2m09 = fields["x3"][display]["theta2m"] - fields["x0"][display]["theta2m"]
    fig, axes = plt.subplots(2, 2, figsize=(FULL_W, 6.4), layout="constrained")
    aspect = 1.0 / np.cos(np.deg2rad(float(lat.mean())))

    ax = axes[0, 0]
    mesh = ax.pcolormesh(lon, lat, np.where(region, dh09, np.nan), cmap="RdBu_r", vmin=-60, vmax=60, shading="nearest", rasterized=True)
    ax.contour(lon, lat, hgt["x0"], levels=list(BAND_EDGES_M), colors="0.35", linewidths=0.5)
    ax.set_aspect(aspect)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Terrain difference X3 $-$ X0 (m)", fontsize=9)
    fig.colorbar(mesh, ax=ax, shrink=0.85)
    panel_letter(ax, "a")

    ax = axes[0, 1]
    mesh = ax.pcolormesh(lon, lat, np.where(region, d2m09, np.nan), cmap="RdBu_r", vmin=-3, vmax=3, shading="nearest", rasterized=True)
    ax.contour(lon, lat, hgt["x0"], levels=list(BAND_EDGES_M), colors="0.35", linewidths=0.5)
    ax.set_aspect(aspect)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"$\\Delta\\theta_{{2\\,\\mathrm{{m}}}}$ X3 $-$ X0, {display:%H:%M} UTC (K)", fontsize=9)
    fig.colorbar(mesh, ax=ax, shrink=0.85)
    panel_letter(ax, "b")

    ax = axes[1, 0]
    hours = [pd.Timestamp(t).hour for t in cmp09["valid_time"].map(pd.Timestamp)]
    for band_name, marker in (("floor", "o"), ("slopes", "s"), ("above", "^")):
        ax.plot(hours, cmp09[f"{band_name}_mean_abs_theta2m_k"], marker=marker, markersize=4, label=band_name)
    ax.set_xlabel("Hour (UTC)")
    ax.set_ylabel("Mean $|\\Delta\\theta_{2\\,\\mathrm{m}}|$ (K)")
    ax.legend(fontsize=7.5)
    style_axes(ax)
    panel_letter(ax, "c")

    ax = axes[1, 1]
    good = region & np.isfinite(d2m09)
    sample = np.random.default_rng(20130202).choice(np.flatnonzero(good), size=min(20000, int(good.sum())), replace=False)
    ax.hexbin(dh09.ravel()[sample], d2m09.ravel()[sample], gridsize=45, cmap="Greys", mincnt=1)
    ax.set_xlabel("$\\Delta$ terrain height (m)")
    ax.set_ylabel("$\\Delta\\theta_{2\\,\\mathrm{m}}$ (K)")
    r16 = float(cmp09[cmp09["valid_time"] == display.isoformat()]["corr_theta2m_terrain"].iloc[0])
    ax.text(0.97, 0.05, f"weighted r = {r16:+.2f}", transform=ax.transAxes, fontsize=8, ha="right", va="bottom")
    style_axes(ax)
    panel_letter(ax, "d")

    save(fig, "wrf_terrain_response_cmp09_d02", out_dir=args.out_dir)

    provenance = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "host": socket.getfqdn(),
        "platform": platform.platform(),
        "python": sys.version,
        "argv": sys.argv,
        "git_head": hd.git_output(Path(__file__).resolve().parents[2], "rev-parse", "HEAD"),
        "runs": {run: str(path) for run, path in runs.items()},
        "pairs_evaluated": [p[2] for p in pairs],
        "lineage": lineage,
        "bands_m": {"floor_below": BAND_EDGES_M[0], "slopes": list(BAND_EDGES_M), "above": BAND_EDGES_M[1]},
        "edge_margin_cells": EDGE_MARGIN_CELLS,
        "criteria": {
            "G1_ratio": G1_SLOPE_TO_FLOOR_RATIO,
            "G2_abs_corr": G2_MIN_ABS_CORRELATION,
            "G1": g1,
            "G2": g2,
            "ANA17_cmp09_gate_passed": bool(g1 and g2),
        },
        "display_hour_utc": DISPLAY_HOUR_UTC,
        "inputs": input_records,
        "environment": {k: os.environ.get(k, "") for k in ("SLURM_JOB_ID", "SLURM_JOB_NODELIST")},
    }
    (args.out_dir / "terrain_response_provenance.json").write_text(
        json.dumps(provenance, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(lineage, indent=2))
    print(summary.to_string(index=False))
    print(criteria.to_string(index=False))
    print(f"wrote analysis to {args.out_dir}")


if __name__ == "__main__":
    main()
