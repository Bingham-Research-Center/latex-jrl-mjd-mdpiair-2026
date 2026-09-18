#!/usr/bin/env python3
"""Render the heat-deficit figure from the committed trajectory summary.

This plot-only route avoids reopening WRF output when a manuscript layout change
does not alter the audited diagnostic.  The input must be the complete trajectory
table written by ``analyze_heat_deficit.py`` so the primary footprint and all seven
sensitivity definitions remain available.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from analyze_heat_deficit import plot_trajectory


def parse_pair(value: str) -> tuple[str, str]:
    parts = tuple(part.strip() for part in value.split(","))
    if len(parts) != 2 or not all(parts) or parts[0] == parts[1]:
        raise argparse.ArgumentTypeError(f"pair must be distinct A,B, got {value!r}")
    return parts


def parse_display(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError(f"display must be KEY=LABEL, got {value!r}")
    key, label = (part.strip() for part in value.split("=", 1))
    if not key or not label:
        raise argparse.ArgumentTypeError(f"display must be KEY=LABEL, got {value!r}")
    return key, label


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trajectory", type=Path, required=True)
    parser.add_argument("--pair", action="append", type=parse_pair, required=True)
    parser.add_argument("--display", action="append", type=parse_display, default=[])
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    trajectory = pd.read_csv(args.trajectory)
    required = {"definition", "valid_time", "run", "mean_mj_m2"}
    missing = required - set(trajectory.columns)
    if missing:
        raise SystemExit(f"trajectory table missing columns: {sorted(missing)}")

    available = set(trajectory["run"].unique())
    requested = {run for pair in args.pair for run in pair}
    if requested - available:
        raise SystemExit(f"pairs missing from trajectory table: {sorted(requested - available)}")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    displays = dict(args.display)
    plot_trajectory(
        trajectory,
        args.pair,
        displays,
        args.out_dir / "wrf_heat_deficit_d02_13to18.png",
        args.out_dir / "wrf_heat_deficit_d02_13to18.pdf",
    )


if __name__ == "__main__":
    main()
