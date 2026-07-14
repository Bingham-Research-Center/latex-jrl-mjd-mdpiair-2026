#!/usr/bin/env python3
"""Spatial/vertical coherence of the driving-product response for gate ANA-19 (Main C3).

Reads exact archived d02 files for the two GFS-minus-NAM pairs (CMP01: X6-X5 two-way;
CMP02: X10-X3 one-way) and tests whether the confirmed fixed-column response (C04/C17)
is coherent over the registered basin-floor evaluation footprint and vertically
confined to the shallow layer.  All criteria below were fixed in this script before it
was run on any model output, and every summary quantity is written to CSV so no
decision rests on visual inspection alone.

Predeclared criteria over the registered primary footprint (the ANA-16
``combined_crest2200`` definition, rebuilt here from the same inputs), evaluated at
every retained hour (14:00--18:00 UTC) for both pairs:

* P1 (floor coherence): the cell-area-weighted fraction of footprint cells whose
  GFS-minus-NAM 2 m potential-temperature difference shares the sign of the
  footprint's area-weighted median must be at least 2/3.
* P2 (shallow confinement): the area-weighted footprint mean of |dtheta| averaged
  over 50--500 m AGL must exceed the same quantity for 1500--2000 m AGL.
* P3 (fixed-column consistency): the area-weighted footprint mean of the
  50--500 m stability difference (theta at 500 m minus theta at 50 m, GFS minus NAM)
  must be negative, and the area-weighted footprint mean 2 m theta difference must be
  positive, matching the signs of ledger rows C17 and C04.

The gate passes only if P1, P2, and P3 hold for all ten pair-hours.  Display rules are
likewise fixed in advance: maps show 14:00, 16:00, and 18:00 UTC (no data-driven hour
selection), and the section figure uses 16:00 UTC, the middle of the decision window.
The section is drawn along the registered USU07-to-USU03 transect used by the
promoted two-site index.  Layer means use linear interpolation at 25 m steps, the
same interpolation rule as the promoted retention diagnostics.

Real WRF work belongs on a CHPC batch node through
``verification/slurm/run_spatial_response.slurm``.
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
import analyze_heat_deficit as hd  # noqa: E402  (reuse audited footprint/grid helpers)
from plot_obs_feb0102 import FULL_W, panel_letter, save, style_axes  # noqa: E402

from brc_tools.nwp import wrf_output as wo  # noqa: E402

LOW_LAYER_M = np.arange(50.0, 500.0 + 1e-6, 25.0)
ALOFT_LAYER_M = np.arange(1500.0, 2000.0 + 1e-6, 25.0)
STABILITY_TOP_M = 500.0
STABILITY_BOTTOM_M = 50.0
COHERENCE_FRACTION = 2.0 / 3.0
MAP_LIMIT_K = 4.0
SECTION_LIMIT_K = 4.0
SECTION_TOP_MSL_M = 4000.0
SECTION_STEP_M = 50.0


def interp_at_agl(theta: np.ndarray, agl: np.ndarray, target: float) -> np.ndarray:
    """Linear interpolation of theta to one AGL height for every column."""
    above = agl >= target
    k_hi = np.clip(above.argmax(axis=0), 1, theta.shape[0] - 1)
    k_lo = k_hi - 1
    take = np.take_along_axis
    a_hi = take(agl, k_hi[None], 0)[0]
    a_lo = take(agl, k_lo[None], 0)[0]
    t_hi = take(theta, k_hi[None], 0)[0]
    t_lo = take(theta, k_lo[None], 0)[0]
    weight = (target - a_lo) / (a_hi - a_lo)
    return t_lo + weight * (t_hi - t_lo)


def layer_mean(theta: np.ndarray, agl: np.ndarray, targets: np.ndarray) -> np.ndarray:
    return np.mean([interp_at_agl(theta, agl, float(h)) for h in targets], axis=0)


def weighted_mean(field: np.ndarray, weights: np.ndarray, mask: np.ndarray) -> float:
    good = mask & np.isfinite(field)
    return float(np.sum(field[good] * weights[good]) / np.sum(weights[good]))


def weighted_median_sign(field: np.ndarray, weights: np.ndarray, mask: np.ndarray) -> float:
    good = mask & np.isfinite(field)
    values = field[good]
    order = np.argsort(values)
    cum = np.cumsum(weights[good][order])
    median = values[order][np.searchsorted(cum, 0.5 * cum[-1])]
    return float(np.sign(median))


def run_fields(path: Path) -> dict[str, np.ndarray]:
    with wo.open_wrfout(path) as ds:
        observed = hd.internal_valid_time(ds)
        loaded = ds[["T", "P", "PB", "PH", "PHB", "T2", "PSFC", "HGT"]].load()
    theta = wo.potential_temperature(loaded)
    agl = wo.height_agl(loaded)
    z_msl = wo.geopotential_height_mass(loaded)
    return {
        "valid": observed,
        "theta2m": wo.theta_2m(loaded),
        "low": layer_mean(theta, agl, LOW_LAYER_M),
        "aloft": layer_mean(theta, agl, ALOFT_LAYER_M),
        "stability": interp_at_agl(theta, agl, STABILITY_TOP_M)
        - interp_at_agl(theta, agl, STABILITY_BOTTOM_M),
        "theta3d": theta,
        "z_msl": z_msl,
        "terrain": wo.surface_field(loaded, "HGT"),
    }


def section_ladder(theta: np.ndarray, z_msl: np.ndarray, cells: list) -> np.ndarray:
    """theta on a fixed MSL ladder along transect cells; NaN below terrain."""
    ladder = np.arange(1200.0, SECTION_TOP_MSL_M + 1e-6, SECTION_STEP_M)
    out = np.full((ladder.size, len(cells)), np.nan)
    for idx, (j, i) in enumerate(cells):
        z_col = z_msl[:, j, i]
        t_col = theta[:, j, i]
        inside = (ladder >= z_col[0]) & (ladder <= z_col[-1])
        out[inside, idx] = np.interp(ladder[inside], z_col, t_col)
    return out


def transect(lat: np.ndarray, lon: np.ndarray, stations: pd.DataFrame, stids: list[str], n: int = 80):
    points = []
    for stid in stids:
        row = stations[stations["stid"] == stid]
        if len(row) != 1:
            raise SystemExit(f"transect station {stid} not found exactly once")
        points.append((float(row["latitude"].iloc[0]), float(row["longitude"].iloc[0])))
    lats = np.linspace(points[0][0], points[1][0], n)
    lons = np.linspace(points[0][1], points[1][1], n)
    cells = []
    for la, lo in zip(lats, lons):
        j, i = np.unravel_index(np.argmin((lat - la) ** 2 + (lon - lo) ** 2), lat.shape)
        cells.append((int(j), int(i)))
    seg = np.hypot(np.diff(lats) * 111.32, np.diff(lons) * 111.32 * np.cos(np.deg2rad(lats[:-1])))
    distance = np.concatenate([[0.0], np.cumsum(seg)])
    return cells, distance


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run", action="append", required=True, type=lambda s: hd.parse_key_value(s, "run"))
    ap.add_argument("--pair", action="append", required=True, type=hd.parse_pair, metavar="A,B")
    ap.add_argument("--pair-label", action="append", default=[], type=lambda s: hd.parse_key_value(s, "pair-label"))
    ap.add_argument("--mask-run", required=True)
    ap.add_argument("--domain", type=int, default=2)
    ap.add_argument("--stations", type=Path, default=Path("verification/data/stations_2013_selection.csv"))
    ap.add_argument("--figure-config", type=Path, default=Path("verification/config/figures/pelican2013.toml"))
    ap.add_argument("--start", default="2013-02-02T14:00:00")
    ap.add_argument("--end", default="2013-02-02T18:00:00")
    ap.add_argument("--display-hours", nargs="+", type=int, default=[14, 16, 18])
    ap.add_argument("--section-hour", type=int, default=16)
    ap.add_argument("--transect", nargs=2, default=["USU07", "USU03"], metavar="STID")
    ap.add_argument("--out-dir", type=Path, required=True)
    args = ap.parse_args()

    runs = {key: Path(value) for key, value in args.run}
    pair_labels = dict(args.pair_label)
    times = pd.date_range(args.start, args.end, freq="1h")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    first_paths = {run: hd.input_path(path, args.domain, times[0]) for run, path in runs.items()}
    static = {run: hd.surface_fields(path) for run, path in first_paths.items()}
    grid_checks = hd.validate_grids(static, list(args.pair), args.mask_run)
    reference = static[args.mask_run]
    lat = np.asarray(reference["lat"], dtype=float)
    lon = np.asarray(reference["lon"], dtype=float)
    hgt = np.asarray(reference["hgt"], dtype=float)
    mapfac = np.asarray(reference["mapfac"], dtype=float)
    definitions, footprint_records = hd.build_definitions(hgt, lat, lon, args.stations, args.figure_config)
    primary = np.asarray(definitions["combined_crest2200"]["mask"], dtype=bool)
    cell_area = float(reference["dx"]) * float(reference["dy"]) / np.square(mapfac)

    stations = pd.read_csv(args.stations)
    cells, distance = transect(lat, lon, stations, list(args.transect))

    fields: dict[str, dict[pd.Timestamp, dict[str, np.ndarray]]] = {}
    input_records: dict[str, dict[str, object]] = {}
    for run, run_dir in runs.items():
        fields[run] = {}
        for valid in times:
            path = hd.input_path(run_dir, args.domain, valid)
            data = run_fields(path)
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
    for a, b in args.pair:
        label = f"{a}_minus_{b}"
        for valid in times:
            fa, fb = fields[a][valid], fields[b][valid]
            d2m = fa["theta2m"] - fb["theta2m"]
            dlow = fa["low"] - fb["low"]
            daloft = fa["aloft"] - fb["aloft"]
            dstab = fa["stability"] - fb["stability"]
            median_sign = weighted_median_sign(d2m, cell_area, primary)
            good = primary & np.isfinite(d2m)
            share = float(
                np.sum(cell_area[good & (np.sign(d2m) == median_sign)])
                / np.sum(cell_area[good])
            )
            low_sign = weighted_median_sign(dlow, cell_area, primary)
            good_low = primary & np.isfinite(dlow)
            share_low = float(
                np.sum(cell_area[good_low & (np.sign(dlow) == low_sign)])
                / np.sum(cell_area[good_low])
            )
            rows.append(
                {
                    "pair": label,
                    "valid_time": valid.isoformat(),
                    "theta2m_mean_k": weighted_mean(d2m, cell_area, primary),
                    "theta2m_median_sign": median_sign,
                    "theta2m_sign_share": share,
                    "low_mean_k": weighted_mean(dlow, cell_area, primary),
                    "low_abs_mean_k": weighted_mean(np.abs(dlow), cell_area, primary),
                    "low_sign_share": share_low,
                    "aloft_mean_k": weighted_mean(daloft, cell_area, primary),
                    "aloft_abs_mean_k": weighted_mean(np.abs(daloft), cell_area, primary),
                    "stability_mean_k": weighted_mean(dstab, cell_area, primary),
                    "confinement_ratio": weighted_mean(np.abs(dlow), cell_area, primary)
                    / weighted_mean(np.abs(daloft), cell_area, primary),
                }
            )

    summary = pd.DataFrame(rows)
    summary.to_csv(args.out_dir / "spatial_response_summary.csv", index=False)

    p1 = bool((summary["theta2m_sign_share"] >= COHERENCE_FRACTION).all())
    p2 = bool((summary["low_abs_mean_k"] > summary["aloft_abs_mean_k"]).all())
    p3 = bool(
        (summary["stability_mean_k"] < 0.0).all() and (summary["theta2m_mean_k"] > 0.0).all()
    )
    criteria = pd.DataFrame(
        [
            {"criterion": "P1_floor_coherence", "threshold": COHERENCE_FRACTION, "passed": p1},
            {"criterion": "P2_shallow_confinement", "threshold": "low>aloft", "passed": p2},
            {"criterion": "P3_fixed_column_consistency", "threshold": "stab<0 and theta2m>0", "passed": p3},
            {"criterion": "ANA19_gate", "threshold": "P1 and P2 and P3", "passed": bool(p1 and p2 and p3)},
        ]
    )
    criteria.to_csv(args.out_dir / "spatial_response_criteria.csv", index=False)

    display = [t for t in times if t.hour in set(args.display_hours)]
    pair_titles = {
        f"{a}_minus_{b}": pair_labels.get(a + "," + b, f"{a} $-$ {b}") for a, b in args.pair
    }

    def draw_maps(stem: str, field_key: str, cbar_label: str) -> None:
        fig, axes = plt.subplots(
            len(args.pair), len(display), figsize=(FULL_W, 4.4), layout="constrained",
            sharex=True, sharey=True,
        )
        mesh = None
        for r, (a, b) in enumerate(args.pair):
            for c, valid in enumerate(display):
                ax = axes[r, c]
                diff = fields[a][valid][field_key] - fields[b][valid][field_key]
                mesh = ax.pcolormesh(
                    lon, lat, diff, cmap="RdBu_r", vmin=-MAP_LIMIT_K, vmax=MAP_LIMIT_K,
                    shading="nearest", rasterized=True,
                )
                ax.contour(lon, lat, hgt, levels=[1700.0, 2200.0], colors="0.35", linewidths=0.5)
                ax.contour(lon, lat, primary.astype(float), levels=[0.5], colors="k", linewidths=0.9)
                if r == 0:
                    ax.set_title(f"{valid:%H:%M} UTC", fontsize=9)
                if c == 0:
                    ax.set_ylabel(pair_titles[f"{a}_minus_{b}"], fontsize=8.5)
                ax.set_aspect(1.0 / np.cos(np.deg2rad(float(lat.mean()))))
                ax.tick_params(labelsize=6.5)
                panel_letter(ax, "abcdefghijkl"[r * len(display) + c])
        fig.colorbar(mesh, ax=axes, shrink=0.85, label=cbar_label)
        save(fig, stem, out_dir=args.out_dir)

    draw_maps("wrf_spatial_theta2m_diff_d02", "theta2m", "$\\Delta\\theta_{2\\,\\mathrm{m}}$ (K)")
    draw_maps("wrf_spatial_agl50to500_diff_d02", "low", "$\\Delta\\theta_{50-500\\,\\mathrm{m}}$ (K)")

    section_time = next(t for t in times if t.hour == args.section_hour)
    fig, axes = plt.subplots(1, len(args.pair), figsize=(FULL_W, 3.1), layout="constrained", sharey=True)
    ladder = np.arange(1200.0, SECTION_TOP_MSL_M + 1e-6, SECTION_STEP_M)
    mesh = None
    for ax, (a, b), letter in zip(np.atleast_1d(axes), args.pair, "ab"):
        fa, fb = fields[a][section_time], fields[b][section_time]
        sec = section_ladder(fa["theta3d"], fa["z_msl"], cells) - section_ladder(
            fb["theta3d"], fb["z_msl"], cells
        )
        mesh = ax.pcolormesh(
            distance, ladder, sec, cmap="RdBu_r", vmin=-SECTION_LIMIT_K, vmax=SECTION_LIMIT_K,
            shading="nearest", rasterized=True,
        )
        terrain_line = np.array([fields[args.mask_run][section_time]["terrain"][j, i] for j, i in cells])
        ax.fill_between(distance, 0.0, terrain_line, color="0.55", zorder=3)
        ax.set_ylim(1200.0, SECTION_TOP_MSL_M)
        ax.set_title(pair_titles[f"{a}_minus_{b}"], fontsize=9)
        style_axes(ax)
        panel_letter(ax, letter)
    fig.supxlabel(
        f"Distance along transect (km), {args.transect[0]} → {args.transect[1]}", fontsize=9.5
    )
    np.atleast_1d(axes)[0].set_ylabel("Height (m MSL)")
    fig.colorbar(mesh, ax=np.atleast_1d(axes), shrink=0.85, label="$\\Delta\\theta$ (K)")
    save(fig, f"wrf_spatial_theta_sections_d02_{args.section_hour:02d}z", out_dir=args.out_dir)

    provenance = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "host": socket.getfqdn(),
        "platform": platform.platform(),
        "python": sys.version,
        "argv": sys.argv,
        "git_head": hd.git_output(Path(__file__).resolve().parents[2], "rev-parse", "HEAD"),
        "runs": {run: str(path) for run, path in runs.items()},
        "pairs": [list(p) for p in args.pair],
        "mask_run": args.mask_run,
        "layers": {
            "low_m": [float(LOW_LAYER_M[0]), float(LOW_LAYER_M[-1]), 25.0],
            "aloft_m": [float(ALOFT_LAYER_M[0]), float(ALOFT_LAYER_M[-1]), 25.0],
        },
        "criteria": {
            "P1_floor_coherence_threshold": COHERENCE_FRACTION,
            "P1": p1,
            "P2": p2,
            "P3": p3,
            "ANA19_gate_passed": bool(p1 and p2 and p3),
        },
        "display_rule": {
            "map_hours_utc": args.display_hours,
            "section_hour_utc": args.section_hour,
            "rule": "fixed in advance; no data-driven hour selection",
        },
        "grid_checks": grid_checks,
        "footprint": footprint_records,
        "primary_definition": "combined_crest2200",
        "inputs": input_records,
        "environment": {k: os.environ.get(k, "") for k in ("SLURM_JOB_ID", "SLURM_JOB_NODELIST")},
    }
    (args.out_dir / "spatial_response_provenance.json").write_text(
        json.dumps(provenance, indent=2, sort_keys=True) + "\n"
    )
    print(summary.to_string(index=False))
    print(criteria.to_string(index=False))
    print(f"wrote analysis to {args.out_dir}")


if __name__ == "__main__":
    main()
