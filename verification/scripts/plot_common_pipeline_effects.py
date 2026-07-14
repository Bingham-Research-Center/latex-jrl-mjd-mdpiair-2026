#!/usr/bin/env python3
"""Common-pipeline contrast panel (longlist L04 / FIG-12) from committed summaries.

Plots every controlled contrast evaluated with the frozen station/common-AGL
pipeline: driving product, PBL/surface-layer scheme, slope-aware radiation, nest
feedback at two terrain regimes, and the driving-product-by-feedback interaction.
Inputs are the committed derived summaries only; no WRF data are read.

Whiskers are the descriptive two-hour circular moving-block sensitivity interval
(2.5--97.5 percentiles) already recorded in the summaries.  They are deliberately
called sensitivity intervals, not confidence intervals: five hourly medians cannot
establish a population sampling distribution.

Every row retains the orientation stored in its source table and comparison record.
CMP03/CMP04 are one-way minus two-way, whereas CMP06 is two-way minus one-way; the
row labels state that difference rather than silently flipping a sign.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from plot_obs_feb0102 import FULL_W, panel_letter, save, style_axes  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "verification" / "data"
DEFAULT_OUT = REPO / "figures-draft"

# Okabe-Ito, matching the repository figure conventions; marker shape is the
# color-independent secondary encoding for the four contrast families.
FAMILY_STYLE = {
    "driving": ("#0072B2", "o"),
    "process": ("#CC79A7", "^"),
    "feedback": ("#E69F00", "s"),
    "interaction": ("#009E73", "D"),
}

# (row label, source table, pair/interaction key, family, sign)
ROWS = [
    ("Driving product, two-way\n(GFS $-$ NAM; CMP01)", "pair", "gfs2_minus_nam2", "driving", 1.0),
    ("Driving product, one-way\n(GFS $-$ NAM; CMP02)", "pair", "gfs1_minus_nam1", "driving", 1.0),
    (
        "PBL/surface-layer treatment\n(MYJ/Eta $-$ YSU/MM5; CMP08)",
        "process",
        "x2_minus_x1",
        "process",
        1.0,
    ),
    (
        "Slope radiation/shading\n(on $-$ off; CMP07)",
        "process",
        "x1_minus_x0",
        "process",
        1.0,
    ),
    ("Feedback, NAM default\n(one $-$ two; CMP03)", "pair", "nam1_minus_nam2", "feedback", 1.0),
    ("Feedback, GFS default\n(one $-$ two; CMP04)", "pair", "gfs1_minus_gfs2", "feedback", 1.0),
    (
        "Feedback, NAM fine terrain\n(two $-$ one; CMP06)",
        "cmp06",
        "x9_minus_x0",
        "feedback",
        1.0,
    ),
    (
        "Product $\\times$ feedback\ninteraction (CMP05)",
        "interaction",
        "gfs1_minus_gfs2__minus__nam1_minus_nam2",
        "interaction",
        1.0,
    ),
]

# (metric key, source family, panel title, x-label)
PANELS = [
    ("t2_bias_c", "surface", "2 m temperature bias", "$\\Delta$ bias ($^{\\circ}$C)"),
    (
        "wind10_abs_error_ms",
        "surface",
        "10 m wind-speed\nabsolute error",
        "$\\Delta$ absolute error (m s$^{-1}$)",
    ),
    (
        "psfc_abs_error_pa",
        "surface",
        "Surface-pressure\nabsolute error",
        "$\\Delta$ absolute error (Pa)",
    ),
    ("stability_k", "retention", "50–500 m AGL stability", "$\\Delta\\theta$ contrast (K)"),
    ("transport_wind_ms", "retention", "50–500 m transport wind", "$\\Delta$ (m s$^{-1}$)"),
    ("pblh_m", "retention", "PBL height\n(scheme-dependent)", "$\\Delta$ (m)"),
]


def load_frames(args: argparse.Namespace) -> dict[str, dict[str, pd.DataFrame]]:
    def read(path: Path, key_col: str) -> pd.DataFrame:
        frame = pd.read_csv(path)
        return frame.rename(columns={key_col: "key"})

    frames = {
        "surface": {
            "pair": read(args.surface_pair, "pair"),
            "interaction": read(args.surface_interaction, "interaction"),
            "cmp06": read(args.cmp06_surface, "pair"),
            "process": read(args.process_surface, "pair"),
        },
        "retention": {
            "pair": read(args.retention_pair, "pair"),
            "interaction": read(args.retention_interaction, "interaction"),
            "cmp06": read(args.cmp06_retention, "pair"),
            "process": read(args.process_retention, "pair"),
        },
    }
    return frames


def one_row(table: pd.DataFrame, key: str, metric: str) -> pd.Series:
    part = table[(table["key"] == key) & (table["metric"] == metric)]
    if len(part) != 1:
        raise SystemExit(f"expected exactly one row for {key}/{metric}, got {len(part)}")
    return part.iloc[0]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--surface-pair", type=Path, default=DATA / "surface_skill_pair_summary.csv")
    ap.add_argument(
        "--surface-interaction", type=Path, default=DATA / "surface_skill_interaction_summary.csv"
    )
    ap.add_argument("--retention-pair", type=Path, default=DATA / "retention_pair_summary.csv")
    ap.add_argument(
        "--retention-interaction", type=Path, default=DATA / "retention_interaction_summary.csv"
    )
    ap.add_argument(
        "--cmp06-surface", type=Path, default=DATA / "cmp06_surface_skill_pair_summary.csv"
    )
    ap.add_argument(
        "--cmp06-retention", type=Path, default=DATA / "cmp06_retention_pair_summary.csv"
    )
    ap.add_argument(
        "--process-surface",
        type=Path,
        default=DATA / "process_pairs_surface_skill_pair_summary.csv",
    )
    ap.add_argument(
        "--process-retention",
        type=Path,
        default=DATA / "process_pairs_retention_pair_summary.csv",
    )
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()

    frames = load_frames(args)

    fig, axes = plt.subplots(
        2, 3, figsize=(FULL_W, 6.2), sharey=True, layout="constrained"
    )
    y_positions = list(range(len(ROWS) - 1, -1, -1))

    for ax, (metric, source, title, xlabel), letter in zip(
        axes.flat, PANELS, "abcdef"
    ):
        for y, (label, table_key, key, family, sign) in zip(y_positions, ROWS):
            row = one_row(frames[source][table_key], key, metric)
            color, marker = FAMILY_STYLE[family]
            mean = sign * row["mean_hourly_spatial_median"]
            lo, hi = sorted(
                (
                    sign * row["block_sensitivity_p025"],
                    sign * row["block_sensitivity_p975"],
                )
            )
            ax.plot([lo, hi], [y, y], color=color, linewidth=1.3, solid_capstyle="butt")
            ax.plot(
                mean,
                y,
                marker=marker,
                color=color,
                markersize=4.6,
                markeredgecolor="white",
                markeredgewidth=0.5,
                zorder=3,
            )
        ax.axvline(0.0, color="0.35", linewidth=0.7, linestyle="--", zorder=0)
        ax.set_title(title, fontsize=9)
        ax.set_xlabel(xlabel)
        ax.set_ylim(-0.6, len(ROWS) - 0.4)
        style_axes(ax)
        ax.grid(axis="y", alpha=0.0)
        panel_letter(ax, letter)

    for ax in axes[:, 0]:
        ax.set_yticks(y_positions)
        ax.set_yticklabels([label for label, *_ in ROWS], fontsize=6.8)

    save(fig, "fig_common_pipeline_effects", out_dir=args.out_dir)


if __name__ == "__main__":
    main()
