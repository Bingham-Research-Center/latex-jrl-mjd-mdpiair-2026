#!/usr/bin/env python3
"""Synthetic smoke test for the offline geographic locator pipeline."""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import xarray as xr

SCRIPTS = Path(__file__).resolve().parent


def write_static(path: Path, west: float, east: float, south: float, north: float,
                 ny: int, nx: int) -> None:
    lon_1d = np.linspace(west, east, nx)
    lat_1d = np.linspace(south, north, ny)
    lon, lat = np.meshgrid(lon_1d, lat_1d)
    hgt = 1400.0 + 700.0 * (lat - south) / (north - south)
    hgt += 550.0 * np.cos((lon - west) / (east - west) * np.pi) ** 2
    xr.Dataset({
        "XLAT": (("Time", "south_north", "west_east"), lat[None, :, :]),
        "XLONG": (("Time", "south_north", "west_east"), lon[None, :, :]),
        "HGT": (("Time", "south_north", "west_east"), hgt[None, :, :]),
    }).to_netcdf(path, engine="scipy")


def main() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="locator_smoke_"))
    write_static(tmp / "wrfout_d01_2013-02-02_12:00:00", -112.1, -107.8, 38.8, 41.8,
                 18, 24)
    write_static(tmp / "wrfout_d02_2013-02-02_12:00:00", -110.8, -108.9, 39.5, 40.9,
                 28, 38)
    write_static(tmp / "wrfout_d03_2013-02-02_12:00:00", -110.5, -109.2, 39.75, 40.7,
                 34, 46)
    out = tmp / "figures"
    cmd = [
        sys.executable,
        str(SCRIPTS / "plot_wrf_transect_locator.py"),
        "--wrf-dir", str(tmp),
        "--out-dir", str(out),
    ]
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout, end="")
    assert not result.stderr.strip(), f"locator emitted stderr: {result.stderr}"
    for extension in ("png", "pdf"):
        path = out / f"wrf_geographic_locator_d01_d03.{extension}"
        assert path.exists() and path.stat().st_size > 10_000, f"missing/empty {path}"
    print(f"OK: offline locator with geographic context and d01--d03 inset -> {out}")


if __name__ == "__main__":
    main()
