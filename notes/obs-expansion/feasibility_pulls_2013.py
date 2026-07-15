#!/usr/bin/env python3
"""Feasibility pulls for the Feb-2013 Uinta Basin obs recommendations.

Exercises each recommended stream end-to-end against the Synoptic archive:
  1/2. wind direction + moisture at the frozen eval stations (DATA00 vars)
  3.   visibility + present-weather codes at METAR/UDOT sites
  4.   solar radiation at in-basin sites (clear-sky check for 2 Feb)
  5.   SNOTEL snow depth / SWE stability across the episode
Writes exploratory parquet caches to this directory; read-only w.r.t. the repo.
"""
from __future__ import annotations

import os
import tomllib
from pathlib import Path

import polars as pl

_cfg = Path.home() / ".config/SynopticPy/config.toml"
with open(_cfg, "rb") as f:
    os.environ["SYNOPTIC_TOKEN"] = tomllib.load(f)["default"]["token"]

from synoptic.services import Metadata, TimeSeries  # noqa: E402

OUT = Path(__file__).parent
START = "2013-01-31 00:00"
END = "2013-02-04 00:00"

EVAL_STATIONS = ["USU01", "USU02", "USU03", "USU04", "USU05", "USU06", "USU07",
                 "USU08", "UUT01", "KVEL", "QV4", "QRS"]
WX_STATIONS = ["KVEL", "K74V", "KPUC", "UTHLP", "UTICS", "UTSTV"]
SOLAR_STATIONS = ["UUT01", "A1622", "A1633", "MHMU1", "DIAU1", "UINU1"]
SNOTEL = ["KGCU1", "MMTU1", "TCKU1", "CWHU1", "LKFU1", "FPLU1", "HPSU1"]

CASE_HOURS = (pl.col("date_time") >= pl.datetime(2013, 2, 2, 14, time_zone="UTC")) & (
    pl.col("date_time") <= pl.datetime(2013, 2, 2, 18, time_zone="UTC"))


def pull(stids, variables, tag):
    try:
        df = TimeSeries(stid=stids, start=START, end=END, vars=variables).df()
    except Exception:
        print(f"[{tag}] pull FAILED (no data or access) for vars={variables}")
        return None
    df.write_parquet(OUT / f"probe_{tag}.parquet")
    return df


def nn_counts(df, tag, window_expr=None, label=""):
    d = df.filter(window_expr) if window_expr is not None else df
    if "value" not in d.columns:
        print(f"[{tag}] unexpected columns: {d.columns}")
        return
    g = (d.filter(pl.col("value").is_not_null())
           .group_by(["stid", "variable"]).agg(pl.len().alias("n"))
           .sort(["variable", "stid"]))
    print(f"\n[{tag}] non-null obs counts {label}:")
    for row in g.iter_rows(named=True):
        print(f"  {row['stid']:7s} {row['variable']:28s} {row['n']:5d}")


# ── 1/2: eval stations, DATA00-equivalent variables ─────────────────────
df = pull(EVAL_STATIONS,
          ["air_temp", "dew_point_temperature", "relative_humidity",
           "wind_speed", "wind_direction", "pressure", "altimeter"],
          "eval_stations")
if df is not None:
    nn_counts(df, "eval", label="(full 31 Jan-4 Feb window)")
    nn_counts(df, "eval", CASE_HOURS, "(2 Feb 14-18 UTC decision window)")
    wd = df.filter((pl.col("variable") == "wind_direction") & CASE_HOURS
                   & pl.col("value").is_not_null())
    ws = df.filter((pl.col("variable") == "wind_speed") & CASE_HOURS
                   & pl.col("value").is_not_null())
    if wd.height:
        g = wd.group_by("stid").agg(pl.col("value").median().alias("med_dir"),
                                    pl.len().alias("n")).sort("stid")
        print("\n[eval] median 10m wind direction, 2 Feb 14-18 UTC (deg):")
        for r in g.iter_rows(named=True):
            print(f"  {r['stid']:7s} {r['med_dir']:6.0f}  (n={r['n']})")
    if ws.height:
        print(f"[eval] all-station median 10m speed 14-18 UTC: "
              f"{ws.get_column('value').median():.2f} (native units)")

# ── 3: visibility + weather codes ────────────────────────────────────────
md = Metadata(stid=WX_STATIONS).df()
print("\n[wx] station identities:")
for r in md.select(["stid", "name", "latitude", "longitude", "elevation"]).iter_rows(named=True):
    print(f"  {r['stid']:6s} {str(r['name'])[:44]:44s} {r['latitude']:.3f} {r['longitude']:.3f} {r['elevation']}")

wx = pull(WX_STATIONS, ["visibility", "weather_cond_code", "weather_condition"], "wx")
if wx is not None:
    vis = wx.filter((pl.col("variable") == "visibility") & pl.col("value").is_not_null())
    if vis.height:
        g = (vis.with_columns(pl.col("date_time").dt.date().alias("day"))
                .group_by(["stid", "day"])
                .agg(pl.col("value").min().alias("min_vis"),
                     pl.col("value").max().alias("max_vis"), pl.len().alias("n"))
                .sort(["stid", "day"]))
        print("\n[wx] visibility per day (native units, statute miles):")
        for r in g.iter_rows(named=True):
            print(f"  {r['stid']:6s} {r['day']}  min={r['min_vis']:5.2f} max={r['max_vis']:5.2f} n={r['n']}")
    codes = wx.filter(pl.col("variable").str.contains("weather"))
    if codes.height:
        valcol = "value_string" if "value_string" in codes.columns else "value"
        g = (codes.filter(pl.col(valcol).is_not_null())
                  .group_by(["stid", "variable", valcol]).agg(pl.len().alias("n"))
                  .sort("n", descending=True).head(25))
        print("\n[wx] weather code/condition value counts (top 25):")
        for r in g.iter_rows(named=True):
            print(f"  {r['stid']:6s} {r['variable']:20s} {str(r[valcol])[:36]:36s} {r['n']:4d}")

# ── 4: solar radiation ───────────────────────────────────────────────────
sol = pull(SOLAR_STATIONS, ["solar_radiation"], "solar")
if sol is not None:
    s = sol.filter(pl.col("value").is_not_null()).with_columns(
        pl.col("date_time").dt.date().alias("day"))
    g = (s.group_by(["stid", "day"]).agg(pl.col("value").max().alias("day_max"))
          .sort(["stid", "day"]))
    print("\n[solar] daily max downwelling shortwave (W m-2):")
    for r in g.iter_rows(named=True):
        print(f"  {r['stid']:6s} {r['day']}  {r['day_max']:6.0f}")

# ── 5: SNOTEL snow ───────────────────────────────────────────────────────
snow = pull(SNOTEL, ["snow_depth", "snow_water_equiv"], "snotel")
if snow is not None:
    s = snow.filter(pl.col("value").is_not_null()).with_columns(
        pl.col("date_time").dt.date().alias("day"))
    g = (s.group_by(["stid", "variable", "day"]).agg(pl.col("value").mean().alias("val"))
          .sort(["stid", "variable", "day"]))
    print("\n[snotel] daily mean snow depth / SWE (native units, mm):")
    cur = None
    for r in g.iter_rows(named=True):
        key = (r["stid"], r["variable"])
        if key != cur:
            print(f"  {r['stid']:6s} {r['variable']}:", end="")
            cur = key
        print(f"  {r['day'].strftime('%m-%d')}={r['val']:6.0f}", end="")
        # newline handled by next key change
    print()
print("\ndone.")
