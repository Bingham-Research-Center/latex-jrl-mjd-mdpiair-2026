#!/usr/bin/env python3
"""Render matched WRF theta profiles at two valid times with shared axes.

This manuscript-specific layout keeps only the named driving-product members and
computes one potential-temperature range across every requested profile before
writing the individual panels.  The shared range makes the initialization and
one-hour panels visually comparable without treating their change as pure model
spin-up.
"""
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from plot_obs_feb0102 import save, style_axes

from brc_tools.nwp import wrf_output as wo
from brc_tools.nwp.wrf_figures import CaseConfig
from brc_tools.visualize.timeseries import DEFAULT_RUN_STYLES


def keyed_path(value: str) -> tuple[str, Path]:
    key, sep, raw_path = value.partition("=")
    if not sep or not key.strip() or not raw_path.strip():
        raise argparse.ArgumentTypeError("expected CASE=/absolute/run/path")
    return key.strip(), Path(raw_path).expanduser()


def valid_time(value: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid ISO valid time: {value}") from exc


def focus_slug(name: str) -> str:
    return "_".join(name.lower().split())


def open_wrfout(path: Path):
    """Use the brc-tools reader, with xarray fallback when netCDF4 is absent."""
    try:
        return wo.open_wrfout(path)
    except ModuleNotFoundError as exc:
        if exc.name != "netCDF4":
            raise
        import xarray as xr

        return xr.open_dataset(path, decode_times=False)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--run", action="append", required=True, type=keyed_path)
    ap.add_argument("--valid", nargs="+", required=True, type=valid_time)
    ap.add_argument("--out-dir", required=True, type=Path)
    ap.add_argument("--top-m", type=float, default=3300.0)
    args = ap.parse_args()

    cfg = CaseConfig.from_toml(args.config)
    runs = dict(args.run)
    if len(runs) != 2:
        raise SystemExit("this review figure requires exactly two distinct --run cases")
    unknown = sorted(set(runs) - set(cfg.runs))
    if unknown:
        raise SystemExit(f"unknown config cases: {unknown}")
    if len(set(args.valid)) != len(args.valid):
        raise SystemExit("--valid times must be unique")

    columns: dict[datetime, dict[str, object]] = {}
    sources: list[Path] = []
    terrain_values: list[float] = []
    for when in sorted(args.valid):
        at_time: dict[str, object] = {}
        for case, run_dir in runs.items():
            domains = wo.discover_domains(run_dir)
            if not domains:
                raise SystemExit(f"no WRF domains found under {run_dir}")
            domain = max(domains)
            source = wo.wrfout_path(run_dir, domain, when)
            if not source.is_file():
                raise SystemExit(f"missing exact input: {source}")
            with open_wrfout(source) as ds:
                column = wo.extract_column(
                    ds,
                    cfg.focus_point.lat,
                    cfg.focus_point.lon,
                    label=cfg.runs[case].label,
                )
            at_time[cfg.runs[case].label] = column
            terrain_values.append(float(column.terrain_m))
            sources.append(source)
        columns[when] = at_time

    if max(terrain_values) - min(terrain_values) > 0.5:
        raise SystemExit(
            "focus-point terrain differs by more than 0.5 m across members/times; "
            "shared terrain shading would be misleading"
        )
    terrain_m = float(np.mean(terrain_values))

    visible_theta: list[np.ndarray] = []
    for at_time in columns.values():
        for column in at_time.values():
            theta = np.asarray(column.theta, dtype=float)
            height = np.asarray(column.height_asl, dtype=float)
            visible_theta.append(theta[(height >= terrain_m) & (height <= args.top_m)])
    pooled = np.concatenate([values for values in visible_theta if values.size])
    if not pooled.size or not np.isfinite(pooled).any():
        raise SystemExit("no finite profile values inside the requested height range")
    xlim = (float(np.nanmin(pooled)) - 1.0, float(np.nanmax(pooled)) + 2.0)
    ylim = (terrain_m - 100.0, args.top_m)

    case_slug = "_".join(runs)
    for when, at_time in sorted(columns.items()):
        fig, ax = plt.subplots(figsize=(3.05, 4.9), layout="constrained")
        for index, (label, column) in enumerate(at_time.items()):
            ax.plot(
                np.asarray(column.theta),
                np.asarray(column.height_asl),
                label=label,
                **dict(DEFAULT_RUN_STYLES.get(index, {})),
            )
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.axhline(terrain_m, color="0.4", lw=0.8, ls=":")
        ax.fill_between(xlim, ylim[0], terrain_m, color="0.7", alpha=0.6, zorder=0)
        ax.axhline(cfg.crest_m, color="black", lw=0.7, ls="--")
        ax.text(xlim[1], cfg.crest_m, " crest", fontsize=7, va="bottom", ha="right")
        ax.text(0.97, 0.97, f"{when:%H} UTC", transform=ax.transAxes,
                ha="right", va="top", fontsize=8)
        ax.set_xlabel(r"potential temperature $\theta$ (K)")
        ax.set_ylabel("height (m MSL)")
        ax.legend(loc="upper left")
        style_axes(ax)
        stem = f"theta_profiles_{focus_slug(cfg.focus_point.name)}_{case_slug}_{when:%H}z"
        save(fig, stem, args.out_dir)

    print(f"shared_xlim_k={xlim[0]:.6f},{xlim[1]:.6f}")
    print(f"shared_ylim_m={ylim[0]:.6f},{ylim[1]:.6f}")
    for source in sources:
        print(f"source={source}")


if __name__ == "__main__":
    main()
