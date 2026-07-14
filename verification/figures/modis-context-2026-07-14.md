# MODIS snow-context render — 2 February 2013

Status: **diagnostic candidate; not promoted**.

## Selection

- Target: 2013-02-02 18:00:00 UTC.
- Map extent: 111.8--108.2 degrees W, 39.2--41.5 degrees N.
- Selection rule: smallest absolute difference between the target and the temporal
  midpoint of a daytime Terra or Aqua MOD02HKM/MYD02HKM Collection 6.1 granule whose
  CMR footprint covers the map center at 110.0 degrees W, 40.35 degrees N.
- Selected: Terra `MOD02HKM.A2013033.1815.061.2017294153853.hdf`, acquired
  18:15--18:20 UTC; midpoint 18:17:30 UTC, 17.5 minutes after the target.
- Nearest Aqua alternative: `MYD02HKM.A2013033.1955.061.2018044031526.hdf`, acquired
  19:55--20:00 UTC; midpoint 19:57:30 UTC.

NASA CMR supplies the granule timing and identity.
NASA GIBS supplies the daily, georeferenced
`MODIS_Terra_CorrectedReflectance_Bands721` WMS image for 2 February 2013.
The WMS layer has a calendar-date time dimension and is not represented as a raw
granule crop.

## Generator and command

- Reusable renderer: sibling `../brc-tools`, commit
  `2c79fc7b0b8e5acbad08cd2c135cefcbb80e3ebd`.
- Module SHA-256:
  `011a121f7963a06717983a94bb43ef59e028ddf08b3a2d58c54d2e8891417dee`.
- Runtime: CPython 3.13.12; Matplotlib 3.10.8; NumPy 2.4.3; Pillow 12.1.1;
  requests 2.32.5.

Final render command, run from the sibling `brc-tools` checkout after the NASA cache
was populated:

```bash
env MPLCONFIGDIR=/tmp/mpl-modis-manuscript PYTHONDONTWRITEBYTECODE=1 \
  conda run -n brc-tools python scripts/render_modis_context.py \
  --target 2013-02-02T18:00:00Z \
  --bbox -111.8 39.2 -108.2 41.5 \
  --output ../latex-jrl-mjd-mdpiair-2026/verification/figures/candidates/modis_uinta_snow_false_color_20130202_near1800 \
  --products snow-false-color \
  --marker Vernal,-109.529,40.455 \
  --marker Ouray,-109.677,40.090 \
  --marker Roosevelt,-109.989,40.299 \
  --cache-dir /tmp/brc-tools-modis-cache \
  --width 1800 \
  --formats png,pdf \
  --title 'Uinta Basin snow context near 18:00 UTC, 2 February 2013' \
  --offline
```

Remove `--offline` to populate or refresh the host-local cache directly from NASA.
No WRF, Slurm, GDAL, rasterio, SatPy, or Earthdata login is required.

## Outputs

| File | SHA-256 |
|---|---|
| `candidates/modis_uinta_snow_false_color_20130202_near1800.png` | `35f5ada9a7a0180c1e88134cf92a361e607ae2ddb70fdb4515b7207aa5ebb8cc` |
| `candidates/modis_uinta_snow_false_color_20130202_near1800.pdf` | `9092cfb993faeed931a84e7ac9c553c5b00eccdec683dbf8a3534f68d353e4c8` |
| `candidates/modis_uinta_snow_false_color_20130202_near1800.provenance.json` | `207fcf9bc819730f4829599413dd1e0e855eac5b0aca8ffc982bf72511263395` |
| cached raw GIBS PNG | `3f3d941162d90de64e98adb567a1c069f0b1e2e798019da9f8cdbece2f182c84` |

The PNG and PDF were visually inspected on 14 July 2026.
In the 7-2-1 composite, snow and ice generally appear cyan and most liquid cloud
appears white; ice cloud may also appear cyan.
Use this as episode snow context, not as a quantitative snow-cover retrieval or WRF
validation field.

The satellite half of the proposed early episode-context figure now exists.
Promotion remains blocked on the observed-ozone companion panel, final combined layout,
caption review, and figure-manifest admission.
