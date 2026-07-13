#!/usr/bin/env python
"""Prototype (Design A): cold-pool heat-deficit SPATIAL map + IC/terrain/feedback triptych.

Vectorizes the Whiteman valley heat deficit (brc_tools cold_pool_heat_deficit, single
column) over the whole d02 grid at 16Z, then a 2x2 square panel:
  (0,0) X0 control field    (0,1) IC        = X6 − X5 (GFS − NAM)
                            (1,0) terrain   = X0 − X4 (fine − coarse GEOG)
                            (1,1) feedback  = X9 − X0 (2-way − 1-way)
Positive difference = the first case has the DEEPER/colder pool.
"""
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

import numpy as np

sys.path.insert(0, "/uufs/chpc.utah.edu/common/home/u0737349/gits/brc-tools")
from brc_tools.nwp import wrf_output as wo  # noqa: E402

ARC = Path("/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive")
CREST_M, CP, G = 2200.0, 1004.0, 9.80665
VALID, DOM = datetime(2013, 2, 2, 16), 2
OUT = Path(__file__).parent / "heatdeficit_map_triptych.png"

CASES = {
    "X0": "pelican2013_nam_3_1_333m_75lev_oneway_terrain3s",
    "X4": "pelican2013_nam_3_1_333m_75lev_oneway_terrain5m",
    "X5": "pelican2013_nam_3_1_333m_75lev",
    "X6": "pelican2013_gfs_3_1_333m_75lev",
    "X9": "pelican2013_nam_3_1_333m_75lev_twoway_terrain3s",
}
WAYPOINTS = {  # basin orientation
    "Horsepool": (40.144, -109.467), "Ouray": (40.089, -109.688),
    "Roosevelt": (40.300, -109.989), "Vernal": (40.455, -109.530),
}


def heat_deficit_field(ds, crest_m=CREST_M):
    """Whiteman heat deficit (MJ m^-2) below crest, per column — vectorized over the grid."""
    theta = wo.potential_temperature(ds)     # (nz,ny,nx) K
    z = wo.geopotential_height_mass(ds)      # (nz,ny,nx) m ASL
    p = wo.pressure_pa(ds)                    # (nz,ny,nx) Pa
    below = z <= crest_m
    k = np.clip(below.sum(axis=0) - 1, 0, z.shape[0] - 2)     # last level below crest

    def gather(a, idx):
        return np.take_along_axis(a, idx[None], axis=0)[0]

    z0, z1 = gather(z, k), gather(z, k + 1)
    t0, t1 = gather(theta, k), gather(theta, k + 1)
    w = np.clip((crest_m - z0) / np.maximum(z1 - z0, 1e-6), 0.0, 1.0)
    theta_crest = t0 + w * (t1 - t0)                          # (ny,nx) K at crest
    f = np.where(below, np.clip(theta_crest[None] - theta, 0.0, None), 0.0)
    from scipy.integrate import trapezoid
    return np.abs((CP / G) * trapezoid(f, x=p, axis=0)) / 1e6    # MJ m^-2


def load(case):
    run = wo.latest_run_dir(ARC / CASES[case] / "full6h")
    ds = wo.open_wrfout(wo.wrfout_path(run, DOM, VALID))
    try:
        return (heat_deficit_field(ds), wo.surface_field(ds, "XLONG"),
                wo.surface_field(ds, "XLAT"), wo.surface_field(ds, "HGT"))
    finally:
        ds.close()


def add_waypoints(ax):
    for name, (la, lo) in WAYPOINTS.items():
        ax.plot(lo, la, "o", ms=3, mfc="white", mec="k", mew=0.6, zorder=6)
        ax.annotate(name, (lo, la), fontsize=6, ha="left", va="bottom",
                    xytext=(2, 2), textcoords="offset points", zorder=6)


def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("Computing heat-deficit fields (16Z, d02)...")
    D = {c: load(c) for c in CASES}
    H = {c: D[c][0] for c in CASES}
    lon, lat, hgt = D["X0"][1], D["X0"][2], D["X0"][3]
    # geographic aspect: 1 deg lat vs 1 deg lon*cos(lat).  The basin domain is ~1:1 after
    # this correction, so panels come out near-square AND fill the cell (no row gaps).
    geo_asp = 1.0 / np.cos(np.deg2rad(float(lat.mean())))
    for c in CASES:
        print(f"  {c}: H max {np.nanmax(H[c]):.1f}  mean {np.nanmean(H[c]):.1f} MJ/m^2")

    diffs = [
        ("IC:  GFS − NAM  (X6 − X5)", H["X6"] - H["X5"]),
        ("terrain:  fine − coarse  (X0 − X4)", H["X0"] - H["X4"]),
        ("feedback:  2-way − 1-way  (X9 − X0)", H["X9"] - H["X0"]),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(11.0, 11.0), constrained_layout=True)
    ext = [lon.min(), lon.max(), lat.min(), lat.max()]

    # (0,0) control field — sequential
    ax = axes[0, 0]
    im = ax.pcolormesh(lon, lat, H["X0"], cmap="viridis", shading="auto")
    ax.contour(lon, lat, hgt, levels=[CREST_M], colors="w", linewidths=0.7, alpha=0.7)
    add_waypoints(ax)
    ax.set_aspect(geo_asp)
    ax.set_title(f"X0 control — cold-pool heat deficit\n16Z (crest {int(CREST_M)} m contour)", fontsize=10)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03, label="MJ m$^{-2}$")

    # (0,1),(1,0),(1,1) differences — per-panel symmetric diverging
    for (title, dfield), ax in zip(diffs, [axes[0, 1], axes[1, 0], axes[1, 1]]):
        vmax = float(np.nanpercentile(np.abs(dfield), 98)) or 1.0
        im = ax.pcolormesh(lon, lat, dfield, cmap="RdBu_r", vmin=-vmax, vmax=vmax, shading="auto")
        ax.contour(lon, lat, hgt, levels=[CREST_M], colors="k", linewidths=0.5, alpha=0.4)
        add_waypoints(ax)
        ax.set_aspect(geo_asp)
        ax.set_title(f"{title}\n(±{vmax:.1f} MJ m$^{{-2}}$; red = 1st deeper)", fontsize=10)
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03, label="ΔMJ m$^{-2}$")

    for ax in axes.flat:
        ax.set_xlabel("lon", fontsize=8); ax.set_ylabel("lat", fontsize=8)
        ax.tick_params(labelsize=7)
    fig.suptitle("Cold-pool heat deficit — where the pool lives, and what moves it (pelican2013, d02, 16Z)",
                 fontsize=12)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=200)
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
