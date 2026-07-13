#!/usr/bin/env python3
"""Vertical theta cross-sections + a station time-height panel from wrfout files.

The inversion itself, not its 2 m shadow: does the run build and HOLD the cold pool?
Two figures per run, following the same-case Neemann et al. 2015 templates:

1. wrf_xsect_theta_<run>  -- theta (shaded) on a vertical slice along a floor->bench
   transect (default Pariette Draw USU07 -> Mountain Home USU03), one panel per
   requested time. Terrain filled dark. Neemann Fig. 4 analog.
2. wrf_timeheight_theta_<run> -- theta time-height at one station (default Roosevelt
   QRS, the sounding site). Neemann Fig. 9 analog.

WRF specifics: ``T`` is *perturbation* potential temperature (theta = T + 300 K,
exact by construction); geopotential height z = (PH+PHB)/g destaggered to mass levels.
Endpoints falling outside the (small, 333 m) domain are clipped to the boundary with
a warning -- check the printed transect before trusting a slice.

Run on a CHPC compute node next to the staged wrfout files. Standalone: xarray +
netCDF4 + numpy + pandas + matplotlib only, NOT brc_tools.

    python plot_wrf_cross_sections.py --wrf-dir /scratch/.../gfs_2way --run-label gfs_2way \\
        --times 2013-02-01_12:00:00 2013-02-02_12:00:00
"""
from __future__ import annotations

import argparse
import glob
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr

from reduce_wrf_to_stations import DEFAULT_STATIONS_CSV, _decode_time, load_stations, nearest_cell

G = 9.81
THETA_BASE = 300.0
Z_TOP = 4500.0  # m ASL display ceiling; the CAP lives well below this
N_TRANSECT = 80


def open_run(wrf_dir: str, pattern: str) -> list[str]:
    files = sorted(f for f in glob.glob(str(Path(wrf_dir) / pattern)) if not f.endswith(".nc"))
    if not files:
        raise SystemExit(f"no wrfout files matched {wrf_dir}/{pattern}")
    return files


def times_of(ds: xr.Dataset) -> pd.DatetimeIndex:
    return pd.to_datetime([_decode_time(t) for t in ds["Times"].values],
                          format="%Y-%m-%d_%H:%M:%S")


def theta_z(ds: xr.Dataset, it: int) -> tuple[np.ndarray, np.ndarray]:
    """(theta, z) on mass levels at time index it; shapes (nz, ny, nx)."""
    theta = np.asarray(ds["T"].isel(Time=it)) + THETA_BASE
    ph = np.asarray(ds["PH"].isel(Time=it))
    phb = np.asarray(ds["PHB"].isel(Time=it))
    z_stag = (ph + phb) / G
    z = 0.5 * (z_stag[:-1] + z_stag[1:])
    return theta, z


def pad_surface(th: np.ndarray, z: np.ndarray, terr: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Prepend a surface row (theta of the lowest mass level at terrain height) so the
    contour fill reaches the ground instead of stopping at the first half-level."""
    return (np.vstack([th[:1], th]), np.vstack([terr[None, :], z]))


def transect_cells(xlat, xlon, p0, p1, n=N_TRANSECT) -> tuple[list, np.ndarray]:
    """(j,i) cells along the p0->p1 line + along-track distance (km). Clips to domain."""
    lats = np.linspace(p0[0], p1[0], n)
    lons = np.linspace(p0[1], p1[1], n)
    for name, (lat, lon) in (("start", p0), ("end", p1)):
        if not (xlat.min() <= lat <= xlat.max() and xlon.min() <= lon <= xlon.max()):
            print(f"WARNING: transect {name} point {lat:.3f},{lon:.3f} outside the domain "
                  f"(lat {xlat.min():.3f}..{xlat.max():.3f}, lon {xlon.min():.3f}..{xlon.max():.3f}); "
                  "slice clips to the boundary")
    cells = [nearest_cell(xlat, xlon, la, lo) for la, lo in zip(lats, lons)]
    km = np.zeros(n)
    km[1:] = np.cumsum(
        np.hypot(np.diff(lats) * 111.32, np.diff(lons) * 111.32 * np.cos(np.deg2rad(lats[:-1])))
    )
    return cells, km


def transect_panels(files, cells, want_times) -> list:
    """[(t, theta_slice, z_slice, terrain)] along the transect for each wanted time.
    theta/z slices are (nz+1, ncol) with a surface row prepended (see pad_surface)."""
    panels = []
    for f in files:
        ds = xr.open_dataset(f, decode_times=False)
        valid = times_of(ds)
        for it, t in enumerate(valid):
            if t in want_times:
                theta, z = theta_z(ds, it)
                hgt = np.asarray(ds["HGT"].isel(Time=0))
                th_s = np.stack([theta[:, j, i] for j, i in cells], axis=1)
                z_s = np.stack([z[:, j, i] for j, i in cells], axis=1)
                terr = np.array([hgt[j, i] for j, i in cells])
                th_s, z_s = pad_surface(th_s, z_s, terr)
                panels.append((t, th_s, z_s, terr))
        ds.close()
    return panels


def theta_levels(auto_min, auto_max, theta_min, theta_max) -> tuple[np.ndarray, str]:
    """0.5 K contour levels. With an explicit (theta_min, theta_max) the scale is
    FIXED so figures from different runs are directly comparable (extend='both'
    keeps out-of-range θ visible); otherwise each figure auto-scales to its data."""
    if theta_min is not None and theta_max is not None:
        return np.arange(theta_min, theta_max + 0.5, 0.5), "both"
    return np.arange(np.floor(auto_min), np.ceil(auto_max) + 0.5, 0.5), "neither"


def fig_xsect(files, cells, km, run, want_times, out_dir, endpoints,
              theta_min=None, theta_max=None) -> None:
    panels = transect_panels(files, cells, want_times)
    if not panels:
        raise SystemExit(f"none of the requested times found; got e.g. {want_times[:2]}")

    ncol = min(len(panels), 2)
    nrow = -(-len(panels) // ncol)
    fig, axes = plt.subplots(nrow, ncol, figsize=(7.5 * ncol, 4.2 * nrow),
                             sharex=True, sharey=True, squeeze=False)
    vmin = min(p[1][p[2] < Z_TOP].min() for p in panels)
    vmax = max(p[1][p[2] < Z_TOP].max() for p in panels)
    levels, extend = theta_levels(vmin, vmax, theta_min, theta_max)
    km2d = np.broadcast_to(km, panels[0][1].shape)
    for ax, (t, th_s, z_s, terr) in zip(axes.flat, panels):
        cf = ax.contourf(km2d, z_s, th_s, levels=levels, cmap="turbo", extend=extend)
        ax.contour(km2d, z_s, th_s, levels=levels[::4], colors="k", linewidths=0.3)
        ax.fill_between(km, 0, terr, color="0.15", zorder=3)
        ax.set_ylim(terr.min() - 50, Z_TOP)
        ax.set_title(f"{run} — {t:%d %b %H:%M} UTC", fontsize=10)
    for ax in axes.flat[len(panels):]:
        ax.set_visible(False)
    for ax in axes[:, 0]:
        ax.set_ylabel("Height ASL (m)")
    for ax in axes[-1, :]:
        ax.set_xlabel(f"Distance along transect (km), {endpoints[0]} → {endpoints[1]}")
    fig.colorbar(cf, ax=axes, shrink=0.85, label="θ (K)")
    out = out_dir / f"wrf_xsect_theta_{run}.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out}")


def fig_xsect_diff(files_a, files_b, cells, km, run_a, run_b, want_times, out_dir,
                   endpoints, dtheta_max=None) -> None:
    """θ(run_a) − θ(run_b) on the transect. Each run's columns are interpolated to a
    common height grid before differencing, so runs with slightly different level
    heights (or terrain) difference correctly; below-ground cells are masked."""
    pa = {t: (th, z, terr) for t, th, z, terr in transect_panels(files_a, cells, want_times)}
    pb = {t: (th, z, terr) for t, th, z, terr in transect_panels(files_b, cells, want_times)}
    times = [t for t in want_times if t in pa and t in pb]
    if not times:
        raise SystemExit(f"no shared times between runs; a={list(pa)[:2]} b={list(pb)[:2]}")
    zc = np.arange(min(pa[times[0]][2].min(), pb[times[0]][2].min()), Z_TOP + 1, 25.0)
    diffs = []
    for t in times:
        th_a, z_a, terr_a = pa[t]
        th_b, z_b, terr_b = pb[t]
        ground = np.maximum(terr_a, terr_b)
        d = np.full((zc.size, th_a.shape[1]), np.nan)
        for c in range(th_a.shape[1]):
            col = (np.interp(zc, z_a[:, c], th_a[:, c], left=np.nan, right=np.nan)
                   - np.interp(zc, z_b[:, c], th_b[:, c], left=np.nan, right=np.nan))
            col[zc < ground[c]] = np.nan
            d[:, c] = col
        diffs.append((t, d, ground))
    amax = float(np.ceil(dtheta_max or np.nanmax(np.abs(np.concatenate(
        [d.ravel() for _, d, _ in diffs])))))
    levels = np.linspace(-amax, amax, 25)
    ncol = min(len(diffs), 2)
    nrow = -(-len(diffs) // ncol)
    fig, axes = plt.subplots(nrow, ncol, figsize=(7.5 * ncol, 4.2 * nrow),
                             sharex=True, sharey=True, squeeze=False)
    km2d = np.broadcast_to(km, (zc.size, km.size))
    zc2d = np.repeat(zc[:, None], km.size, axis=1)
    for ax, (t, d, ground) in zip(axes.flat, diffs):
        cf = ax.contourf(km2d, zc2d, d, levels=levels, cmap="RdBu_r", extend="both")
        ax.contour(km2d, zc2d, d, levels=[0], colors="k", linewidths=0.4)
        ax.fill_between(km, 0, ground, color="0.15", zorder=3)
        ax.set_ylim(ground.min() - 50, Z_TOP)
        ax.set_title(f"{run_a} − {run_b} — {t:%d %b %H:%M} UTC", fontsize=10)
    for ax in axes.flat[len(diffs):]:
        ax.set_visible(False)
    for ax in axes[:, 0]:
        ax.set_ylabel("Height ASL (m)")
    for ax in axes[-1, :]:
        ax.set_xlabel(f"Distance along transect (km), {endpoints[0]} → {endpoints[1]}")
    fig.colorbar(cf, ax=axes, shrink=0.85, label=f"Δθ (K), {run_a} − {run_b}")
    out = out_dir / f"wrf_xsect_theta_diff_{run_a}_minus_{run_b}.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out}")


def fig_timeheight(files, cell, run, station, out_dir, theta_min=None, theta_max=None) -> None:
    j, i = cell
    ts, profs, zs = [], [], []
    for f in files:
        ds = xr.open_dataset(f, decode_times=False)
        valid = times_of(ds)
        for it, t in enumerate(valid):
            theta, z = theta_z(ds, it)
            ts.append(t)
            profs.append(theta[:, j, i])
            zs.append(z[:, j, i])
        ds.close()
    order = np.argsort(np.array(ts))
    t_arr = np.array(ts)[order]
    th = np.stack([profs[k] for k in order], axis=1)
    z = np.stack([zs[k] for k in order], axis=1)
    th, z = pad_surface(th, z, z[0] - (z[1] - z[0]) / 2.0)
    t2d = np.broadcast_to(t_arr, th.shape)

    fig, ax = plt.subplots(figsize=(9, 4.2))
    levels, extend = theta_levels(th[z < Z_TOP].min(), th[z < Z_TOP].max(), theta_min, theta_max)
    cf = ax.contourf(t2d, z, th, levels=levels, cmap="turbo", extend=extend)
    ax.contour(t2d, z, th, levels=levels[::4], colors="k", linewidths=0.3)
    ax.set_ylim(z.min() - 50, Z_TOP)
    ax.set_ylabel("Height ASL (m)")
    ax.set_xlabel("Valid time (UTC)")
    ax.set_title(f"θ time-height at {station} — {run}", fontsize=10)
    fig.colorbar(cf, ax=ax, label="θ (K)")
    fig.tight_layout()
    out = out_dir / f"wrf_timeheight_theta_{run}.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--wrf-dir", required=True)
    ap.add_argument("--run-label", required=True)
    ap.add_argument("--glob", default="wrfout_d03_2013-0[12]-*")
    ap.add_argument("--stations", type=Path, default=DEFAULT_STATIONS_CSV)
    ap.add_argument("--transect", nargs=2, default=["USU07", "USU03"], metavar="STID",
                    help="floor + bench station ids defining the slice")
    ap.add_argument("--time-height-station", default="QRS")
    ap.add_argument("--times", nargs="+", default=["2013-02-01_12:00:00", "2013-02-02_12:00:00"],
                    help="wrfout timestamps (UTC, YYYY-MM-DD_HH:MM:SS) for the slice panels")
    ap.add_argument("--out-dir", type=Path, default=None,
                    help="default: <wrf-dir>/figures")
    ap.add_argument("--theta-min", type=float, default=None,
                    help="fixed lower θ (K) for a shared color scale across runs; "
                         "pair with --theta-max (else each figure auto-scales, so "
                         "cross-run color comparison is only qualitative)")
    ap.add_argument("--theta-max", type=float, default=None,
                    help="fixed upper θ (K) for the shared color scale")
    ap.add_argument("--diff-wrf-dir", default=None,
                    help="second run's wrfout dir; if set, write θ(run)−θ(diff) on the "
                         "transect instead of the single-run x-section + time-height")
    ap.add_argument("--diff-run-label", default=None, help="label for the second (subtracted) run")
    ap.add_argument("--dtheta-max", type=float, default=None,
                    help="fixed ±Δθ (K) scale for the difference figure (else symmetric auto)")
    args = ap.parse_args()
    if (args.theta_min is None) != (args.theta_max is None):
        raise SystemExit("--theta-min and --theta-max must be given together")

    stations = load_stations(args.stations)
    for stid in (*args.transect, args.time_height_station):
        if stid not in stations:
            raise SystemExit(f"unknown station {stid}; have {sorted(stations)}")
    files = open_run(args.wrf_dir, args.glob)
    print(f"{len(files)} wrfout files")

    ds0 = xr.open_dataset(files[0], decode_times=False)
    xlat = np.asarray(ds0["XLAT"].isel(Time=0))
    xlon = np.asarray(ds0["XLONG"].isel(Time=0))
    ds0.close()

    out_dir = args.out_dir or Path(args.wrf_dir) / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    want = pd.to_datetime(args.times, format="%Y-%m-%d_%H:%M:%S")

    cells, km = transect_cells(xlat, xlon, stations[args.transect[0]], stations[args.transect[1]])
    print(f"transect {args.transect[0]} -> {args.transect[1]}: {km[-1]:.1f} km, {len(cells)} columns")
    if args.diff_wrf_dir:
        files_b = open_run(args.diff_wrf_dir, args.glob)
        fig_xsect_diff(files, files_b, cells, km, args.run_label,
                       args.diff_run_label or "runB", want, out_dir, args.transect,
                       dtheta_max=args.dtheta_max)
    else:
        fig_xsect(files, cells, km, args.run_label, want, out_dir, args.transect,
                  theta_min=args.theta_min, theta_max=args.theta_max)
        th_cell = nearest_cell(xlat, xlon, *stations[args.time_height_station])
        fig_timeheight(files, th_cell, args.run_label, args.time_height_station, out_dir,
                       theta_min=args.theta_min, theta_max=args.theta_max)


if __name__ == "__main__":
    main()
