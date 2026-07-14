#!/usr/bin/env python3
"""Smoke-test section, locator, and shared-axis profile plots with tiny WRF files.

Builds two fake wrfout files (Basin-covering lat/lon grid, 12 mass levels, an idealized
surface-based inversion that weakens between time steps) and runs the cross-section
script on them, so the real invocation on CHPC is known-good syntax-to-figure.

Run:
    python verification/scripts/smoke_test_cross_sections.py
Everything goes to a temp dir; nothing in the repo is touched.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import xarray as xr

SCRIPTS = Path(__file__).resolve().parent
G, NZ, NY, NX = 9.81, 12, 30, 30


def fake_wrfout(path: Path, stamps: list[str], inv_strength: float) -> None:
    nt = len(stamps)
    lat = np.linspace(39.7, 40.6, NY)
    lon = np.linspace(-110.5, -109.2, NX)
    xlon, xlat = np.meshgrid(lon, lat)
    hgt = 1450.0 + 800.0 * ((xlat - 39.7) / 0.9) ** 2  # floor rising to a NW bench

    z_stag = hgt[None, :, :] + np.linspace(0.0, 4000.0, NZ + 1)[:, None, None]
    ph_stag = np.broadcast_to(z_stag * G, (nt, NZ + 1, NY, NX)).copy()
    z_mass = 0.5 * (z_stag[:-1] + z_stag[1:])
    agl = z_mass - hgt[None, :, :]
    # theta: 300 K aloft, colder near the surface (the inversion), decaying with AGL height
    theta_pert = -inv_strength * np.exp(-agl / 500.0)
    t = np.stack([theta_pert * (1.0 - 0.3 * k) for k in range(nt)])  # weakens in time
    pressure = np.broadcast_to(
        np.linspace(85_000.0, 50_000.0, NZ)[None, :, None, None],
        (nt, NZ, NY, NX),
    ).copy()

    times = np.array([list(s.ljust(19)) for s in stamps], dtype="S1")
    ds = xr.Dataset(
        {
            "Times": (("Time", "DateStrLen"), times),
            "XLAT": (("Time", "south_north", "west_east"), np.broadcast_to(xlat, (nt, NY, NX))),
            "XLONG": (("Time", "south_north", "west_east"), np.broadcast_to(xlon, (nt, NY, NX))),
            "HGT": (("Time", "south_north", "west_east"), np.broadcast_to(hgt, (nt, NY, NX))),
            "T": (("Time", "bottom_top", "south_north", "west_east"), t),
            "P": (("Time", "bottom_top", "south_north", "west_east"), np.zeros_like(pressure)),
            "PB": (("Time", "bottom_top", "south_north", "west_east"), pressure),
            "PH": (("Time", "bottom_top_stag", "south_north", "west_east"), np.zeros_like(ph_stag)),
            "PHB": (("Time", "bottom_top_stag", "south_north", "west_east"), ph_stag),
            "U": (
                ("Time", "bottom_top", "south_north", "west_east_stag"),
                np.zeros((nt, NZ, NY, NX + 1)),
            ),
            "V": (
                ("Time", "bottom_top", "south_north_stag", "west_east"),
                np.zeros((nt, NZ, NY + 1, NX)),
            ),
        }
    )
    ds.to_netcdf(path)


def main() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="wrf_xsect_smoke_"))
    fake_wrfout(tmp / "wrfout_d02_2013-02-01_12:00:00", ["2013-02-01_12:00:00"], 12.0)
    fake_wrfout(tmp / "wrfout_d03_2013-02-01_12:00:00", ["2013-02-01_12:00:00"], 12.0)
    fake_wrfout(tmp / "wrfout_d03_2013-02-02_12:00:00", ["2013-02-02_12:00:00"], 8.0)

    cmd = [sys.executable, str(SCRIPTS / "plot_wrf_cross_sections.py"),
           "--wrf-dir", str(tmp), "--run-label", "fake",
           "--times", "2013-02-01_12:00:00", "2013-02-02_12:00:00"]
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

    for stem in ("wrf_xsect_theta_fake", "wrf_timeheight_theta_fake"):
        f = tmp / "figures" / f"{stem}.png"
        assert f.exists() and f.stat().st_size > 10_000, f"missing/empty {f}"

    locator_dir = tmp / "locator"
    locator_cmd = [sys.executable, str(SCRIPTS / "plot_wrf_transect_locator.py"),
                   "--wrf-dir", str(tmp), "--out-dir", str(locator_dir)]
    print(f"$ {' '.join(locator_cmd)}")
    subprocess.run(locator_cmd, check=True)
    for ext in ("png", "pdf"):
        f = locator_dir / f"wrf_transect_locator_d02_d03.{ext}"
        assert f.exists() and f.stat().st_size > 10_000, f"missing/empty {f}"

    profile_runs = {"gfs": tmp / "profile_gfs", "nam": tmp / "profile_nam"}
    for run_dir in profile_runs.values():
        run_dir.mkdir()
    for run_dir, strengths in (
        (profile_runs["gfs"], (7.0, 6.0)),
        (profile_runs["nam"], (11.0, 10.0)),
    ):
        for stamp, strength in zip(
            ("2013-02-02_12:00:00", "2013-02-02_13:00:00"), strengths
        ):
            fake_wrfout(run_dir / f"wrfout_d03_{stamp}", [stamp], strength)

    profile_dir = tmp / "profiles"
    profile_cmd = [
        sys.executable,
        str(SCRIPTS / "plot_wrf_profile_spinup.py"),
        "--config", str(SCRIPTS.parent / "config/figures/pelican2013.toml"),
        "--run", f"gfs={profile_runs['gfs']}",
        "--run", f"nam={profile_runs['nam']}",
        "--valid", "2013-02-02T12:00:00", "2013-02-02T13:00:00",
        "--out-dir", str(profile_dir),
    ]
    print(f"$ {' '.join(profile_cmd)}")
    subprocess.run(profile_cmd, check=True)
    for hour in ("12", "13"):
        for ext in ("png", "pdf"):
            f = profile_dir / f"theta_profiles_horsepool_gfs_nam_{hour}z.{ext}"
            assert f.exists() and f.stat().st_size > 10_000, f"missing/empty {f}"

    print(
        "\nOK: cross-section/time-height figures, locator, and shared-axis profiles "
        f"rendered -> {tmp}"
    )


if __name__ == "__main__":
    main()
