#!/usr/bin/env python3
"""Probe extra Synoptic variables for the Feb 2013 Uinta Basin case window.

Follows verification/scripts/select_proxies_2013.py (bbox, window, token-safe
error handling) but sweeps variables that the committed availability check did
not probe. Read-only; writes nothing to the repo.
"""
from __future__ import annotations

import datetime as dt
import os
import tomllib
from pathlib import Path

import polars as pl

# The local config.toml uses the legacy [default] section, which the installed
# SynopticPy (>=2025) does not read (it expects top-level `token = "..."`).
# Load it here and export for this process only; never printed.
_cfg = Path.home() / ".config/SynopticPy/config.toml"
with open(_cfg, "rb") as f:
    _tok = tomllib.load(f)["default"]["token"]
os.environ["SYNOPTIC_TOKEN"] = _tok

from synoptic.services import Metadata, TimeSeries  # noqa: E402

BBOX = [-110.9, 39.4, -108.5, 41.1]
START = "2013-02-01 00:00"
END = "2013-02-04 00:00"
START_D = dt.date(2013, 2, 1)
END_D = dt.date(2013, 2, 4)

CANDIDATES = [
    "wind_gust",
    "wind_direction",
    "dew_point_temperature",
    "relative_humidity",
    "ceiling",
    "weather_cond_code",
    "cloud_layer_1_code",
    "air_temp",
    "altimeter",
]


def por_covering(var: str):
    try:
        md = Metadata(bbox=BBOX, vars=var).df()
    except Exception:
        print(f"  {var}: metadata call failed (var name or access)")
        return []
    if not md.height or not {"period_of_record_start", "period_of_record_end"} <= set(md.columns):
        return []
    return md.filter(
        (pl.col("period_of_record_start").dt.date() <= END_D)
        & (pl.col("period_of_record_end").dt.date() >= START_D)
    ).get_column("stid").to_list()


def real_data(stids, var):
    if not stids:
        return [], 0
    try:
        ts = TimeSeries(stid=stids, start=START, end=END, vars=[var]).df()
    except Exception:
        print(f"  {var}: no 2013 data returned (no data or no account access)")
        return [], 0
    if not ts.height:
        return [], 0
    if {"variable", "value"} <= set(ts.columns):
        got = ts.filter((pl.col("variable") == var))
        vcols = [c for c in ("value", "value_string") if c in got.columns]
        if vcols:
            got = got.filter(pl.any_horizontal(pl.col(c).is_not_null() for c in vcols))
    elif var in ts.columns:
        got = ts.filter(pl.col(var).is_not_null())
    else:
        got = ts
    real = sorted(got.get_column("stid").unique().to_list()) if got.height else []
    return real, got.height


for var in CANDIDATES:
    por = por_covering(var)
    real, n_obs = real_data(por, var)
    shown = ",".join(real[:18]) + ("..." if len(real) > 18 else "")
    print(f"{var:24s} POR={len(por):3d}  real={len(real):3d}  obs={n_obs:6d}  [{shown}]")
