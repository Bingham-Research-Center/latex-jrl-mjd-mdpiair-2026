#!/usr/bin/env python
"""Design B (creative): cold-pool phase portrait, factorially decomposed.

Each run's diurnal trajectory (12->18Z) through STRENGTH x VENTILATION space at
Horsepool: y = Whiteman heat deficit (MJ/m^2), x = 10 m wind speed (m/s). One panel
per experimental knob (IC / nesting / terrain / physics), same axes, so you can read
HOW each factor moves the system:
  * slides runs along one strength-vs-wind curve  -> the factor acts THROUGH mixing.
  * shifts the whole curve (same wind, different strength) -> a thermodynamic/terrain
    offset that ventilation cannot explain.
"""
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

import numpy as np

sys.path.insert(0, "/uufs/chpc.utah.edu/common/home/u0737349/gits/brc-tools")
from brc_tools.nwp import wrf_output as wo  # noqa: E402

ARC = Path("/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive")
CREST_M = 2200.0
HP_LAT, HP_LON = 40.144, -109.467
HOURS = [12, 13, 14, 15, 16, 17, 18]
OUT = Path(__file__).parent / "coldpool_phase_portrait.png"

RUNS = {
    "X0": "pelican2013_nam_3_1_333m_75lev_oneway_terrain3s",
    "X1": "pelican2013_nam_3_1_333m_75lev_oneway_terrain3s_slope",
    "X2": "pelican2013_nam_3_1_333m_75lev_oneway_terrain3s_slope_myj",
    "X3": "pelican2013_nam_3_1_333m_75lev_oneway",
    "X4": "pelican2013_nam_3_1_333m_75lev_oneway_terrain5m",
    "X5": "pelican2013_nam_3_1_333m_75lev",
    "X6": "pelican2013_gfs_3_1_333m_75lev",
    "X9": "pelican2013_nam_3_1_333m_75lev_twoway_terrain3s",
    "X10": "pelican2013_gfs_3_1_333m_75lev_oneway",
}
PANELS = [
    ("IC — driving analysis", [("X6", "GFS 2-way"), ("X5", "NAM 2-way"),
                               ("X10", "GFS 1-way"), ("X3", "NAM 1-way")]),
    ("nesting / feedback", [("X3", "1-way default"), ("X5", "2-way default"),
                            ("X0", "1-way fine"), ("X9", "2-way fine")]),
    ("terrain source", [("X0", "fine ~90 m"), ("X3", "default ~900 m"),
                        ("X4", "coarse ~9 km")]),
    ("physics (Tran bridge)", [("X0", "baseline"), ("X1", "+slope/shading"),
                               ("X2", "+MYJ/Eta")]),
]
COLORS = ["#2166ac", "#b2182b", "#1a9850", "#762a83"]


def trajectory(case):
    """Return (winds, deficits) over HOURS at Horsepool for a run (innermost domain)."""
    run = wo.latest_run_dir(ARC / RUNS[case] / "full6h")
    dom = max(wo.discover_domains(run))
    winds, defs = [], []
    for h in HOURS:
        ds = wo.open_wrfout(wo.wrfout_path(run, dom, datetime(2013, 2, 2, h)))
        try:
            col = wo.extract_column(ds, HP_LAT, HP_LON)
            defs.append(wo.cold_pool_heat_deficit(col, CREST_M) / 1e6)
            j, i = wo.nearest_column_index(ds, HP_LAT, HP_LON)
            winds.append(float(np.hypot(wo.surface_field(ds, "U10")[j, i],
                                        wo.surface_field(ds, "V10")[j, i])))
        finally:
            ds.close()
    return np.array(winds), np.array(defs)


def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("Building trajectories (9 runs x 7 h at Horsepool)...")
    traj = {}
    for case in RUNS:
        traj[case] = trajectory(case)
        print(f"  {case}: wind {traj[case][0].min():.1f}-{traj[case][0].max():.1f} m/s  "
              f"H {traj[case][1].min():.1f}-{traj[case][1].max():.1f} MJ/m^2")

    all_w = np.concatenate([traj[c][0] for c in RUNS])
    all_h = np.concatenate([traj[c][1] for c in RUNS])
    xlim = (max(0.0, all_w.min() - 0.3), all_w.max() + 0.3)
    ylim = (all_h.min() - 0.3, all_h.max() + 0.5)

    fig, axes = plt.subplots(2, 2, figsize=(11.0, 11.0), constrained_layout=True)
    for (title, members), ax in zip(PANELS, axes.flat):
        for (case, label), color in zip(members, COLORS):
            w, d = traj[case]
            ax.plot(w, d, "-", color=color, lw=1.5, alpha=0.85, zorder=3, label=f"{case} — {label}")
            ax.scatter(w, d, s=8 + 5 * np.arange(len(w)), color=color, zorder=4)  # grows with time
            ax.plot(w[0], d[0], "o", mfc="white", mec=color, mew=1.4, ms=8, zorder=5)  # 12Z start
            ax.annotate("", xy=(w[-1], d[-1]), xytext=(w[-2], d[-2]),   # 18Z arrowhead
                        arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6), zorder=5)
        ax.legend(fontsize=8, loc="upper right", framealpha=0.9, handlelength=1.4)
        ax.set_xlim(*xlim); ax.set_ylim(*ylim)
        ax.set_box_aspect(1)
        ax.grid(True, alpha=0.25)
        ax.set_title(title, fontsize=11)
        ax.set_xlabel("Horsepool 10 m wind (m s$^{-1}$)  — ventilation →", fontsize=9)
        ax.set_ylabel("cold-pool heat deficit (MJ m$^{-2}$)  — strength ↑", fontsize=9)

    fig.suptitle("Cold-pool phase portrait — how each experimental knob moves the pool "
                 "(Horsepool, 12→18Z; ○ = 12Z, ▶ = 18Z, dots grow with time)", fontsize=11)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=200)
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
