#!/usr/bin/env python
"""Design C: cold-air reservoir anatomy — capacity vs intensity.

Cold air = grid cells below crest with theta < theta_crest(column) (the air a mixing
event would have to warm).  Four square panels (d02):
  (0,0) hypsometric anatomy  — cold-air volume per elevation band (16Z)
  (0,1) capacity vs intensity — total volume (km^3) vs Horsepool heat deficit (16Z)
  (1,0) volume erosion        — total cold-air volume 12->18Z (does GFS drain it?)
  (1,1) cold-air pyramid      — X0 volume in (height x theta-deficit) space
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
DEFICIT_THRESH = 2.0        # K: trapped-pool air is >= this much colder than crest air
HP_LAT, HP_LON = 40.144, -109.467
DOM = 2
EDGES = np.arange(1300.0, 2250.0, 100.0)              # elevation bands (MSL)
OUT = Path(__file__).parent / "coldair_reservoir.png"

RUNS = {
    "X0": "pelican2013_nam_3_1_333m_75lev_oneway_terrain3s",
    "X3": "pelican2013_nam_3_1_333m_75lev_oneway",
    "X4": "pelican2013_nam_3_1_333m_75lev_oneway_terrain5m",
    "X5": "pelican2013_nam_3_1_333m_75lev",
    "X6": "pelican2013_gfs_3_1_333m_75lev",
    "X9": "pelican2013_nam_3_1_333m_75lev_twoway_terrain3s",
}
LABEL = {"X0": "fine ~90 m", "X3": "default ~900 m", "X4": "coarse ~9 km",
         "X5": "NAM 2-way", "X6": "GFS 2-way", "X9": "2-way fine"}
COL = {"X0": "#2166ac", "X3": "#5aae61", "X4": "#1a9850",
       "X5": "#b2182b", "X6": "#f46d43", "X9": "#762a83"}
TS_RUNS = ["X0", "X4", "X6", "X9"]


def reservoir(ds, crest_m=CREST_M):
    """Return (total_km3, z_cold, defic_cold, vol_cold) for cold cells below crest."""
    theta = wo.potential_temperature(ds)
    z = wo.geopotential_height_mass(ds)
    dz = np.diff(wo.geopotential_height_w(ds), axis=0)        # (nz,ny,nx) layer thickness
    below = z <= crest_m
    k = np.clip(below.sum(axis=0) - 1, 0, z.shape[0] - 2)

    def gather(a, idx):
        return np.take_along_axis(a, idx[None], axis=0)[0]

    z0, z1 = gather(z, k), gather(z, k + 1)
    t0, t1 = gather(theta, k), gather(theta, k + 1)
    w = np.clip((crest_m - z0) / np.maximum(z1 - z0, 1e-6), 0.0, 1.0)
    theta_crest = t0 + w * (t1 - t0)
    deficit = theta_crest[None] - theta
    cold = below & (deficit >= DEFICIT_THRESH)   # trapped pool, not the weak near-crest background
    dx, dy = wo.dx_dy(ds)
    vol = np.where(cold, dx * dy * dz, 0.0)                   # m^3
    m = cold
    return vol.sum() / 1e9, z[m], deficit[m], vol[m]


def band_volumes(z_cold, vol_cold):
    idx = np.digitize(z_cold, EDGES) - 1
    out = np.zeros(len(EDGES) - 1)
    for b in range(len(out)):
        out[b] = vol_cold[idx == b].sum() / 1e9
    return out


def hp_deficit(ds):
    return wo.cold_pool_heat_deficit(wo.extract_column(ds, HP_LAT, HP_LON), CREST_M) / 1e6


def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("16Z reservoir for all runs...")
    tot16, bands16, hpdef16, pyramid = {}, {}, {}, None
    for c in RUNS:
        run = wo.latest_run_dir(ARC / RUNS[c] / "full6h")
        ds = wo.open_wrfout(wo.wrfout_path(run, DOM, datetime(2013, 2, 2, 16)))
        try:
            tot, zc, dc, vc = reservoir(ds)
            tot16[c] = tot
            bands16[c] = band_volumes(zc, vc)
            hpdef16[c] = hp_deficit(ds)
            if c == "X0":
                pyramid = (zc, dc, vc)
            print(f"  {c}: V={tot:.1f} km^3  HPdef={hpdef16[c]:.1f} MJ/m^2")
        finally:
            ds.close()

    print("volume time series (key runs)...")
    ts = {c: [] for c in TS_RUNS}
    hours = list(range(12, 19))
    for c in TS_RUNS:
        run = wo.latest_run_dir(ARC / RUNS[c] / "full6h")
        for h in hours:
            ds = wo.open_wrfout(wo.wrfout_path(run, DOM, datetime(2013, 2, 2, h)))
            try:
                ts[c].append(reservoir(ds)[0])
            finally:
                ds.close()

    fig, ax = plt.subplots(2, 2, figsize=(11.5, 11.5), constrained_layout=True)
    centers = 0.5 * (EDGES[:-1] + EDGES[1:])

    # (0,0) hypsometric anatomy
    a = ax[0, 0]
    for c in RUNS:
        a.plot(bands16[c], centers, "-o", ms=3, color=COL[c], label=f"{c} — {LABEL[c]}")
    a.axhline(CREST_M, color="k", lw=0.7, ls="--"); a.text(a.get_xlim()[1], CREST_M, " crest",
                                                           fontsize=7, va="bottom", ha="right")
    a.set_xlabel("cold-air volume per 100 m band (km$^3$)"); a.set_ylabel("elevation (m MSL)")
    a.set_title("hypsometric anatomy — where the cold air sits (16Z)", fontsize=10)
    a.legend(fontsize=7.5); a.grid(alpha=0.25); a.set_box_aspect(1)

    # (0,1) capacity vs intensity
    a = ax[0, 1]
    for c in RUNS:
        a.scatter(tot16[c], hpdef16[c], s=70, color=COL[c], zorder=3, edgecolor="k", linewidth=0.5)
        a.annotate(f" {c}", (tot16[c], hpdef16[c]), fontsize=8, va="center")
    a.set_xlabel("total cold-air volume (km$^3$)  — capacity →")
    a.set_ylabel("Horsepool heat deficit (MJ m$^{-2}$)  — intensity ↑")
    a.set_title("capacity vs intensity — reservoir ≠ strength (16Z)", fontsize=10)
    a.grid(alpha=0.25); a.set_box_aspect(1)

    # (1,0) volume erosion time series
    a = ax[1, 0]
    for c in TS_RUNS:
        a.plot(hours, ts[c], "-o", ms=4, color=COL[c], label=f"{c} — {LABEL[c]}")
    a.set_xlabel("valid hour (UTC)"); a.set_ylabel("total cold-air volume (km$^3$)")
    a.set_title("volume erosion 12→18Z — does GFS drain the reservoir?", fontsize=10)
    a.legend(fontsize=7.5); a.grid(alpha=0.25); a.set_box_aspect(1)

    # (1,1) cold-air pyramid (X0)
    a = ax[1, 1]
    zc, dc, vc = pyramid
    H2, xe, ye = np.histogram2d(dc, zc, bins=[np.linspace(2, 8, 25), EDGES], weights=vc / 1e9)
    pm = a.pcolormesh(xe, ye, H2.T, cmap="magma_r", shading="auto")
    a.axhline(CREST_M, color="w", lw=0.7, ls="--")
    a.set_xlabel(r"$\theta$-deficit below crest air (K)  — intensity →")
    a.set_ylabel("elevation (m MSL)")
    a.set_title("cold-air pyramid — X0 volume in height × intensity", fontsize=10)
    a.set_box_aspect(1)
    fig.colorbar(pm, ax=a, fraction=0.046, pad=0.03, label="km$^3$ / bin")

    fig.suptitle(f"Cold-air reservoir anatomy — trapped pool (θ-deficit ≥ {DEFICIT_THRESH:g} K below "
                 f"crest), capacity vs strength (pelican2013, d02)", fontsize=12)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=200)
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
