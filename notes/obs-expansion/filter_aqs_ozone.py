#!/usr/bin/env python3
"""Filter EPA AQS 2013 bulk ozone files to Uinta Basin sites, Jan-Feb 2013.

Counties: Utah 49-013 (Duchesne), 49-047 (Uintah); Colorado 08-103 (Rio Blanco,
for Rangely). Reports which monitors exist, their coverage, and episode values.
"""
from __future__ import annotations

from pathlib import Path

import polars as pl

TMP = Path(__file__).parent

daily = pl.read_csv(TMP / "daily_44201_2013.csv", infer_schema_length=10000)
daily = daily.with_columns(pl.col("Date Local").str.to_date())
basin = daily.filter(
    (((pl.col("State Code") == 49) & pl.col("County Code").is_in([13, 47]))
     | ((pl.col("State Code") == 8) & (pl.col("County Code") == 103)))
    & (pl.col("Date Local") <= pl.date(2013, 2, 28))
)

print("=== AQS daily MDA8 ozone monitors, Jan-Feb 2013 ===")
g = (basin.group_by(["State Code", "County Code", "Site Num", "Local Site Name",
                     "Latitude", "Longitude", "Pollutant Standard"])
          .agg(pl.len().alias("n_days"),
               pl.col("Date Local").min().alias("first"),
               pl.col("Date Local").max().alias("last"),
               pl.col("1st Max Value").max().alias("max_val"))
          .sort(["State Code", "County Code", "Site Num", "Pollutant Standard"]))
for r in g.iter_rows(named=True):
    print(f"  {r['State Code']:02d}-{r['County Code']:03d}-{r['Site Num']:04d} "
          f"{str(r['Local Site Name'])[:28]:28s} ({r['Latitude']:.3f},{r['Longitude']:.3f}) "
          f"{str(r['Pollutant Standard'])[:14]:14s} n={r['n_days']:3d} {r['first']}..{r['last']} "
          f"max={r['max_val']}")

stds = basin.get_column("Pollutant Standard").unique().to_list()
print(f"\nPollutant standards present: {stds}")
std = sorted(stds)[0]

print(f"\n=== Daily max 8-h ozone (ppb), 29 Jan - 6 Feb 2013, std='{std}' ===")
ep = (basin.filter((pl.col("Date Local") >= pl.date(2013, 1, 29))
                   & (pl.col("Date Local") <= pl.date(2013, 2, 6))
                   & (pl.col("Pollutant Standard") == std))
           .with_columns((pl.col("County Code").cast(pl.Utf8) + "-"
                          + pl.col("Site Num").cast(pl.Utf8)).alias("site"))
           .select(["site", "Local Site Name", "Date Local", "1st Max Value"])
           .sort(["site", "Date Local"]))
for site in ep.get_column("site").unique(maintain_order=True):
    rows = ep.filter(pl.col("site") == site)
    name = rows.get_column("Local Site Name")[0]
    vals = " ".join(f"{d.strftime('%m-%d')}:{v*1000:3.0f}"
                    for d, v in zip(rows.get_column("Date Local"),
                                    rows.get_column("1st Max Value")))
    print(f"  {site:9s} {str(name)[:24]:24s} {vals}")

# Hourly: coverage + case-day values at basin sites
hourly = pl.scan_csv(TMP / "hourly_44201_2013.csv", infer_schema_length=10000)
hb = (hourly.filter(
        (((pl.col("State Code") == 49) & pl.col("County Code").is_in([13, 47]))
         | ((pl.col("State Code") == 8) & (pl.col("County Code") == 103))))
      .with_columns(pl.col("Date GMT").str.to_date())
      .filter(pl.col("Date GMT") <= pl.date(2013, 3, 1))
      .collect())

names = (basin.with_columns((pl.col("State Code").cast(pl.Utf8) + "-"
                             + pl.col("County Code").cast(pl.Utf8) + "-"
                             + pl.col("Site Num").cast(pl.Utf8)).alias("sid"))
              .group_by("sid").agg(pl.col("Local Site Name").first().alias("name")))
hb = (hb.with_columns((pl.col("State Code").cast(pl.Utf8) + "-"
                       + pl.col("County Code").cast(pl.Utf8) + "-"
                       + pl.col("Site Num").cast(pl.Utf8)).alias("sid"))
        .join(names, on="sid", how="left"))

print("\n=== Hourly ozone coverage, Jan-Feb 2013 ===")
g2 = (hb.group_by(["sid", "name"])
        .agg(pl.len().alias("n_hours"),
             pl.col("Sample Measurement").max().alias("max_ppm"))
        .sort("sid"))
for r in g2.iter_rows(named=True):
    print(f"  {r['sid']:12s} {str(r['name'])[:30]:30s} n={r['n_hours']:4d} max={r['max_ppm']}")

print("\n=== Hourly ozone (ppb), 2 Feb 2013 12-23 GMT ===")
case = (hb.filter((pl.col("Date GMT") == pl.date(2013, 2, 2))
                  & (pl.col("Time GMT") >= "12:00"))
          .select(["sid", "name", "Time GMT", "Sample Measurement"])
          .sort(["sid", "Time GMT"]))
for sid in case.get_column("sid").unique(maintain_order=True):
    rows = case.filter(pl.col("sid") == sid)
    name = rows.get_column("name")[0]
    vals = " ".join(f"{v*1000:3.0f}" for v in rows.get_column("Sample Measurement"))
    print(f"  {sid:12s} {str(name)[:20]:20s} {vals}")

hb.write_parquet(TMP / "aqs_hourly_ozone_basin_janfeb2013.parquet")
basin.write_parquet(TMP / "aqs_daily_ozone_basin_janfeb2013.parquet")
print("\nwrote basin parquets.")
