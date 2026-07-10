#!/usr/bin/env python3
"""Plan-view upper-air maps from wrfout files: theta + winds on a pressure level.

Where does the run-to-run CAP difference originate aloft? One figure per requested
time x pressure level: theta (shaded) + wind vectors, terrain contoured for context.
With --diff-dir, plots the theta DIFFERENCE (this run minus the other) on a diverging
scale instead — the GFS-minus-NAM panel. Both runs must share the grid (same WPS
domains; true for the touchstones, NOT for Tran's runs).

WRF specifics: theta = T + 300 K; full pressure = P + PB (Pa); U/V destaggered to
mass points. Levels below ground (p_level > surface pressure) are masked.

Run on a CHPC compute node next to the staged wrfout files. Standalone: xarray +
netCDF4 + numpy + pandas + matplotlib only, NOT brc_tools.

    python plot_wrf_upper_air.py --wrf-dir gfs_2way --run-label gfs_2way_d02 \\
        --glob 'wrfout_d02*' --times 2013-02-02_16:00:00 --levels 700 500
    python plot_wrf_upper_air.py --wrf-dir gfs_2way --run-label gfs_minus_nam_d02 \\
        --glob 'wrfout_d02*' --diff-dir nam_2way --times 2013-02-02_16:00:00
"""
from __future__ import annotations

import argparse
import glob
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator
import numpy as np
import pandas as pd
import xarray as xr

from plot_wrf_cross_sections import open_run, times_of
from reduce_wrf_to_stations import DEFAULT_STATIONS_CSV

THETA_BASE = 300.0
QUIVER_STRIDE = 12


def interp_plevel(field: np.ndarray, p: np.ndarray, p0: float) -> np.ndarray:
    """Linear-in-p interpolation of (nz,ny,nx) field to p0 (Pa); below-ground -> NaN."""
    k = np.clip((p >= p0).sum(axis=0) - 1, 0, p.shape[0] - 2)
    take = lambda a, kk: np.take_along_axis(a, kk[None], 0)[0]
    pk, pk1 = take(p, k), take(p, k + 1)
    fk, fk1 = take(field, k), take(field, k + 1)
    with np.errstate(invalid="ignore", divide="ignore"):
        out = fk + (pk - p0) / (pk - pk1) * (fk1 - fk)
    out[p0 > p[0]] = np.nan  # level is underground here
    return out


def level_fields(ds: xr.Dataset, it: int, p0: float) -> dict[str, np.ndarray]:
    p = np.asarray(ds["P"].isel(Time=it)) + np.asarray(ds["PB"].isel(Time=it))
    theta = np.asarray(ds["T"].isel(Time=it)) + THETA_BASE
    u = np.asarray(ds["U"].isel(Time=it))
    v = np.asarray(ds["V"].isel(Time=it))
    u = 0.5 * (u[:, :, :-1] + u[:, :, 1:])
    v = 0.5 * (v[:, :-1, :] + v[:, 1:, :])
    theta_p = interp_plevel(theta, p, p0)
    u_grid = interp_plevel(u, p, p0)
    v_grid = interp_plevel(v, p, p0)
    cosa = np.asarray(ds["COSALPHA"].isel(Time=it))
    sina = np.asarray(ds["SINALPHA"].isel(Time=it))
    # WRF U/V are grid-relative; maps are drawn in latitude/longitude, so rotate
    # vectors to earth-relative components before plotting or differencing runs.
    u_earth = u_grid * cosa - v_grid * sina
    v_earth = v_grid * cosa + u_grid * sina
    return {"theta": theta_p, "u": u_earth, "v": v_earth}


def collect(files: list[str], want_times: pd.DatetimeIndex, p0: float) -> list[tuple]:
    out = []
    for f in files:
        ds = xr.open_dataset(f, decode_times=False)
        for it, t in enumerate(times_of(ds)):
            if t in want_times:
                out.append((t, level_fields(ds, it, p0)))
        ds.close()
    if not out:
        raise SystemExit(f"none of the requested times found; wanted {list(want_times)}")
    return sorted(out, key=lambda x: x[0])


def plot_level(panels, xlat, xlon, hgt, run, lev_hpa, out_dir, diff_of=None,
               theta_min=None, theta_max=None, diff_limit=None, stations=None,
               wind_key=None, dpi=300, display_label=None) -> None:
    ncol = min(len(panels), 2)
    nrow = -(-len(panels) // ncol)
    fig, axes = plt.subplots(nrow, ncol, figsize=(7.0 * ncol, 5.6 * nrow),
                             sharex=True, sharey=True, squeeze=False)
    if diff_of is None:
        vals = np.concatenate([p[1]["theta"][np.isfinite(p[1]["theta"])] for p in panels])
        lo = float(np.floor(vals.min())) if theta_min is None else float(theta_min)
        hi = float(np.ceil(vals.max())) if theta_max is None else float(theta_max)
        levels = np.linspace(lo, hi, 25)
        ticks = np.linspace(lo, hi, 7)
        cmap, label = "turbo", f"θ at {lev_hpa} hPa (K)"
    else:
        amax = (max(np.nanmax(np.abs(p[1]["theta"])) for p in panels) or 0.1
                if diff_limit is None else float(diff_limit))
        levels = np.linspace(-amax, amax, 21)
        ticks = np.linspace(-amax, amax, 5)
        cmap, label = "RdBu_r", f"Δθ at {lev_hpa} hPa (K), {display_label or run}"
    s = QUIVER_STRIDE
    for panel_index, (ax, (t, f)) in enumerate(zip(axes.flat, panels)):
        ax.set_facecolor("0.86")
        cf = ax.contourf(xlon, xlat, f["theta"], levels=levels, cmap=cmap, extend="both")
        ax.contour(xlon, xlat, hgt, levels=[1700, 2000, 2300], colors="0.35",
                   linewidths=0.5, linestyles="--")
        q = ax.quiver(xlon[::s, ::s], xlat[::s, ::s], f["u"][::s, ::s], f["v"][::s, ::s],
                      scale=250, width=0.002, color="k")
        if stations is not None:
            ax.scatter(stations["longitude"], stations["latitude"], s=14, facecolor="white",
                       edgecolor="black", linewidth=0.5, zorder=4)
            for row in stations.itertuples():
                ax.annotate(row.stid, (row.longitude, row.latitude), xytext=(2, 2),
                            textcoords="offset points", fontsize=5.5, color="0.1", zorder=5)
        if panel_index == 0:
            key = wind_key if wind_key is not None else (1.0 if diff_of else 5.0)
            key_label = f"{key:g} m s⁻¹" + (" wind difference" if diff_of else " wind")
            ax.quiverkey(q, 0.96, 0.07, key, key_label, coordinates="axes",
                         labelpos="W", fontproperties={"size": 7})
            if any(np.isnan(item[1]["theta"]).any() for item in panels):
                ax.text(0.02, 0.03, "gray = below ground", transform=ax.transAxes, fontsize=6.5,
                        bbox={"facecolor": "white", "edgecolor": "0.7", "alpha": 0.85, "pad": 2})
        ax.set_title(f"{display_label or run} — {t:%d %b %H:%M} UTC", fontsize=10)
        ax.set_aspect(1.0 / np.cos(np.deg2rad(np.mean(xlat))))
        ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5))
        ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{abs(x):.1f}°W"))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.1f}°N"))
    for ax in axes.flat[len(panels):]:
        ax.set_visible(False)
    fig.colorbar(cf, ax=axes, shrink=0.85, label=label, ticks=ticks)
    out = out_dir / f"wrf_upper_{lev_hpa}hPa_{run}.png"
    fig.savefig(out, dpi=dpi, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out} + .pdf")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--wrf-dir", required=True)
    ap.add_argument("--run-label", required=True)
    ap.add_argument("--display-label", default=None,
                    help="human-readable title/colorbar label; filenames still use --run-label")
    ap.add_argument("--glob", default="wrfout_d03_2013-0[12]-*")
    ap.add_argument("--times", nargs="+", default=["2013-02-02_16:00:00"],
                    help="wrfout timestamps (UTC, YYYY-MM-DD_HH:MM:SS)")
    ap.add_argument("--levels", nargs="+", type=float, default=[700.0, 500.0],
                    help="pressure levels in hPa")
    ap.add_argument("--diff-dir", default=None,
                    help="second run dir on the SAME grid; plot theta difference "
                         "(wrf-dir minus diff-dir)")
    ap.add_argument("--theta-min", type=float, default=None,
                    help="fixed lower θ bound for absolute maps; use with --theta-max")
    ap.add_argument("--theta-max", type=float, default=None,
                    help="fixed upper θ bound for absolute maps; use with --theta-min")
    ap.add_argument("--diff-limit", type=float, default=None,
                    help="fixed symmetric ±K bound for difference maps")
    ap.add_argument("--stations", type=Path, default=DEFAULT_STATIONS_CSV)
    ap.add_argument("--mark-stations", nargs="*", default=["USU07", "USU03", "QRS", "KVEL"],
                    help="station IDs to mark for basin context; pass no values to disable")
    ap.add_argument("--wind-key", type=float, default=None,
                    help="quiver-key magnitude in m/s (absolute or wind difference)")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--out-dir", type=Path, default=None, help="default: <wrf-dir>/figures")
    args = ap.parse_args()
    if (args.theta_min is None) != (args.theta_max is None):
        raise SystemExit("--theta-min and --theta-max must be supplied together")

    files = open_run(args.wrf_dir, args.glob)
    print(f"{len(files)} wrfout files")
    want = pd.to_datetime(args.times, format="%Y-%m-%d_%H:%M:%S")

    ds0 = xr.open_dataset(files[0], decode_times=False)
    xlat = np.asarray(ds0["XLAT"].isel(Time=0))
    xlon = np.asarray(ds0["XLONG"].isel(Time=0))
    hgt = np.asarray(ds0["HGT"].isel(Time=0))
    ds0.close()
    out_dir = args.out_dir or Path(args.wrf_dir) / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    station_rows = None
    if args.mark_stations:
        station_meta = pd.read_csv(args.stations)
        station_rows = station_meta[station_meta["stid"].isin(args.mark_stations)].copy()
        missing = sorted(set(args.mark_stations) - set(station_rows["stid"]))
        if missing:
            raise SystemExit(f"unknown --mark-stations values: {missing}")

    diff_files = open_run(args.diff_dir, args.glob) if args.diff_dir else None
    for lev in args.levels:
        p0 = lev * 100.0
        panels = collect(files, want, p0)
        if diff_files:
            other = dict(collect(diff_files, want, p0))
            panels = [(t, {**f, "theta": f["theta"] - other[t]["theta"],
                           "u": f["u"] - other[t]["u"], "v": f["v"] - other[t]["v"]})
                      for t, f in panels if t in other]
        plot_level(panels, xlat, xlon, hgt, args.run_label, int(lev), out_dir,
                   diff_of=args.diff_dir, theta_min=args.theta_min, theta_max=args.theta_max,
                   diff_limit=args.diff_limit, stations=station_rows,
                   wind_key=args.wind_key, dpi=args.dpi, display_label=args.display_label)


if __name__ == "__main__":
    main()
