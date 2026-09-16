# CHPC first-round review closure: job 15610800

Checked 16 September 2026 on `notchpeak1.int.chpc.utah.edu`.
All four requested checks are complete: the original archive matches; all nine diagnostics have a shared layout issue but pass numerical consistency checks; a nearby sounding was recovered outside the exact window; and Seep Ridge provider metadata/QC were recovered, with exposure history still missing.

Original output root `R` is `/scratch/general/vast/u0737349/latex_jrl_review_layers/15610800`.
Closure directory is `/scratch/general/vast/u0737349/peer-review-round1-followup-15610800.V8mRbu`.
The writing checkout was at `f99da0c6991b152f3ca339e507b68f06abc463b4` during these checks; the clean pinned analysis worktree remains at `658bd005e20401f9ad8c8e88c5c2b506bb60e1a8`.
No WRF integration, analysis rerun, original-file replacement, manuscript change or scientific promotion was performed.

## 1. Original transferred archive — verified

Exact command and output:

```text
sha256sum /scratch/general/vast/u0737349/latex_jrl_review_layers/15610800/latex_jrl_review_layers_15610800_handoff.tar.gz
19e83bc0eb5fc533577394fe1cc839a00b6df774bfafeb50165d4ded84836363  /scratch/general/vast/u0737349/latex_jrl_review_layers/15610800/latex_jrl_review_layers_15610800_handoff.tar.gz
```

This is the existing original archive, not a repacked copy, and matches the Akamai receipt exactly.

## 2. Nine diagnostic inspections — issue in every configuration

Each row identifies both inspected files below `R`; `{pdf,png}` means both extensions were opened visually, with PDFs rasterised using `pdftoppm`.
**D1:** the lower-panel wind-axis label overlaps the upper-panel axis label and is clipped at the bottom in both formats.
All four run curves, five hourly points, IQR shading, legends and UTC axes are present in every row.
The intended layer bounds and units agree with the adjacent metadata and extracted PDF text; D1 impairs their readability.

| Layer / increment (m) | Status | Inspected paths below R | Findings |
| --- | --- | --- | --- |
| 50–500 / 10 | issue | `raw/50-500_step-10/wrf_retention_ventilation_d02_14to18.{pdf,png}` | D1; curves/data verified |
| 50–500 / 25 | issue | `raw/50-500_step-25/wrf_retention_ventilation_d02_14to18.{pdf,png}` | D1; curves/data verified |
| 50–500 / 50 | issue | `raw/50-500_step-50/wrf_retention_ventilation_d02_14to18.{pdf,png}` | D1; curves/data verified |
| 50–250 / 10 | issue | `raw/50-250_step-10/wrf_retention_ventilation_d02_14to18.{pdf,png}` | D1; curves/data verified |
| 50–250 / 25 | issue | `raw/50-250_step-25/wrf_retention_ventilation_d02_14to18.{pdf,png}` | D1; curves/data verified |
| 50–250 / 50 | issue | `raw/50-250_step-50/wrf_retention_ventilation_d02_14to18.{pdf,png}` | D1; curves/data verified |
| 100–500 / 10 | issue | `raw/100-500_step-10/wrf_retention_ventilation_d02_14to18.{pdf,png}` | D1; curves/data verified |
| 100–500 / 25 | issue | `raw/100-500_step-25/wrf_retention_ventilation_d02_14to18.{pdf,png}` | D1; curves/data verified |
| 100–500 / 50 | issue | `raw/100-500_step-50/wrf_retention_ventilation_d02_14to18.{pdf,png}` | D1; curves/data verified |

`check_diagnostics.py` checks each adjacent `retention_station_timeseries.csv`, `retention_hourly_summary.csv`, `retention_pair_hourly.csv`, `retention_pair_summary.csv` and `retention_analysis_metadata.json`.
Each configuration contains 220 finite station/run/hour rows: X6=`gfs2`, X10=`gfs1`, X5=`nam2`, X3=`nam1`; d02; 11 stations; 2 February 2013, 1400–1800 UTC inclusive.
Recomputed hourly statistics agree within `2.85e-14`; paired station medians agree within `7.11e-15`.
Both paired GFS-minus-NAM vector and scalar wind differences are positive, and endpoint theta differences negative, in all five hours for both feedback pairs and all nine configurations.
The pair-summary and metadata files are byte-identical to their corresponding files under `R/return/`.
Numerical results and all 63 inspected source hashes are attached separately.

The plots show medians of absolute run values, whereas the claims use medians of paired station differences.
For example, at 1500 UTC in `50-250_step-25`, the vector-wind medians are 1.424722 m s−1 for GFS two-way and 1.739438 m s−1 for NAM two-way, while the median paired GFS-minus-NAM difference is +0.282935 m s−1.
That crossing is consistent with the CSVs and does not reverse the paired result.
Repair D1 by shortening or wrapping labels and rendering from existing hourly CSVs into a new directory; no recalculation is indicated by these checks.
Preserve the original plots as the defect record.

## 3. Independent vertical profiles — not found in searched locations for the exact window

One bounded pass covered the locations below; this is not an exhaustive CHPC or campaign inventory.

| Location / search | Status and outcome |
| --- | --- |
| Repository `verification/data/manifest.csv` and `verification/provenance/*.md`; instrument/observation keyword search | not found in searched locations: no registered measured vertical profile matching the five-hour window; registered Horsepool profiles are model output |
| `/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710` (registered surface cache DATA00) | unavailable: directory missing at check time; does not establish absence of observations |
| `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/brc-tools-data/archive`, depth 2; `/scratch/general/vast/u0737349/brc-tools`, depth 3; sibling `brc-tools/data`, depth 3 | not found in searched locations: archive contains `map_obs_20251001-20260807.tar.gz`, scratch contains terrain, and checkout data contains schema/example files; the existing map-archive filename inventory has no 2013/profile candidates |
| `/scratch/general/vast/u0737349/latex_jrl_20260715_v3_finishing_pass` and `latex_jrl_20260714_v3_figure_review`, depth 3, observation/metadata/sonde/profile filenames | not found in searched locations: recovered provenance and model-only Horsepool plots, not measured profiles |
| `/uufs/chpc.utah.edu/common/home/u0198116/public_html/ubos` | unavailable: filesystem permission denied; public university web endpoint was accessible |
| [University of Utah UBOS observation index](https://www.inscc.utah.edu/~u0198116/ubos/obs.html) and its linked 2 February sounding | verified recovery of out-of-window context, detailed below |

The [linked Roosevelt data file](https://www.inscc.utah.edu/~u0198116/UINTAH_TEMP_DIRECTORY/Roosevelt_02022013_1802UTC.txt) is a University of Utah Graw rawinsonde record, probe 201085; the exact instrument model is not stated.
Initial coordinates are 40.2656 N, 110.0412 W; the header gives ground-station altitude 1561.50 m.
Although the index labels it 1800 UTC, launch detection is **18:01:54 UTC**, 114 seconds after the fixed window ends.
It contains 3956 one-second rows through 19:07:49 UTC and spans 0–13266.9 m above launch.
The first samples at or above 50, 100, 250 and 500 m occur at 18:02:17, 18:02:26, 18:03:07 and 18:04:28 UTC respectively.
Variables include pressure, temperature, relative humidity, wind speed/direction, dew point, position, altitude and geopotential height.
The provider explicitly states: “All data is considered provisional and has not been quality controlled”.
No scientific QC or WRF comparison was performed here.
This is useful nearby context, but it supplies no sample inside the exact requested window and does not close vertical validation or establish inversion depth.
The index also lists other dates and aerosol-layer products; those were not treated as matching thermodynamic profiles.

## 4. Seep Ridge — verified metadata/QC return; exposure history not found in searched locations

At approximately 06:24 UTC on 16 September 2026, two successful Synoptic requests returned station USU04, ID 39901, network 1009 (UBOS).
Coordinates are 39.75390 N, 109.54600 W; provider elevation is 6343 ft = 1933.3464 m, consistent with the rounded 1933 m register.
The station period is 1 January–11 March 2013; the API identifies the station timezone as `America/Denver`.
The timeseries request explicitly selected UTC and returned `Z` timestamps; [Synoptic documents UTC request times](https://docs.synopticdata.com/services/time-series).
This verifies the API time convention, not the original logger clock history.

For 31 January 00:00–3 February 23:59 UTC, the response contains 384 quarter-hour timestamps: 383 non-null temperature, humidity and wind-speed values each, and 355 wind-direction values.
Temperature, humidity and speed are missing at 2 February 06:00 UTC; direction has 29 missing values, listed in the attached summary.
All four requested variables have 17/17 non-null samples during 2 February 1400–1800 UTC.
With `qc=on`, `qc_remove_data=off`, `qc_flags=on`, and `qc_checks=synopticlabs,madis,mesowest`, the response reports `QC_FLAGGED=false` and zero flagged observations.
This describes the returned provider checks; it is not independent proof of accurate measurements or good exposure, and [Synoptic treats its observations as provisional](https://docs.synopticdata.com/services/mesonet-data-qc).

The complete metadata response has `SITING=[]`; sensor positions are null for all seven listed variables, and no instrument model, calibration, shielding, obstruction or maintenance history is supplied.
Those details were **not found in searched locations**, even with `complete=1`, `sensorvars=1` and `sitinghistory=1` ([metadata documentation](https://docs.synopticdata.com/services/metadata)).
The existing X3 cell separation of 132.7 m and terrain offset of +2.9 m remain sampling descriptors, with no causal attribution established.
This fresh provider pull does not replace the registered historical observation cache or reproduce its original processing.

## Commands, evidence and next actions

This repository copy and the five small receipts below can be synchronised by pulling `jrl/peer-review-round1` on Akamai.

- [Numerical diagnostic checks](../verification/data/diagnostic-numerical-checks.csv).
- [Observation evidence summary](../verification/provenance/observation-evidence-summary.json).
- [USU04 provider metadata](../verification/provenance/USU04-metadata.json).
- [USU04 request receipt](../verification/provenance/USU04-request-receipt.json).
- [Hashes of inspected original files](../verification/provenance/inspected-original-files.sha256).

The full evidence packet remains in the CHPC closure directory above, including the raw sounding, observation timeseries, downloaded index, audit scripts and original report.
Transfer `peer-review-round1-chpc-closure-15610800.tar.gz` and its `.sha256` sidecar separately; its SHA-256 is `b594c63981330228e0e9c489ef181b9cdc648c47ea106e1b7b4d2673981fb4f7`.
After transfer, run `sha256sum --check peer-review-round1-chpc-closure-15610800.tar.gz.sha256`, extract the packet, then run `sha256sum --check closure-files.sha256` inside the extraction directory.
The packet's `closure-files.sha256` covers its original report and attachments; this repository copy has amended paths and transfer instructions.
The original 19-file return bundle and diagnostic images are not duplicated.
`inspected-original-files.sha256` records hashes of the originals in place.
On CHPC, reproduce the lightweight audits from the full packet directory with:

```bash
python check_diagnostics.py
python summarise_observations.py
# Optional live refresh; uses the existing private credential without printing it:
python fetch_usu04.py
```

The last command refreshes provider JSONs and therefore changes their hashes; preserve this receipt before any refresh.
`USU04-request-receipt.json` records both exact endpoints, all non-secret parameters, retrieval times and API responses.
The public recovery commands were `curl -fLsS --connect-timeout 10 --max-time 30 URL -o FILE`, using the two University of Utah URLs above and filenames `ubos-obs.html` and `Roosevelt_02022013_1802UTC.txt`.
The bounded local searches used `find PATH -maxdepth N -type d -print` to identify holdings, `find PATH -maxdepth N -type f -printf '%P\n'` for the small data directories, and `find PATH -maxdepth 3 -type f \( -iname '*obs*' -o -iname '*metadata*' -o -iname '*sonde*' -o -iname '*profile*' \) -print` for the two figure-job roots.
The repository search was `rg -n -i 'sonde|lidar|ceilometer|radiometer|observ' verification/data/manifest.csv`, with a corresponding rawinsonde/tethersonde/radiosonde/ceilometer/radiometer/lidar/USU04/Seep Ridge search of `verification/provenance/*.md`.

1. Akamai can import the previously validated CSVs, metadata and original job receipts, binding them to the now-matched archive hash.
2. Record D1 and repair any diagnostics needed for review by rendering existing CSVs separately, then inspect those derivatives; current images are not publication-ready.
3. Qualify layer-bound dependence and reconcile R3-C001/C015/C016/C018 using the exact paired statistics and the observation dispositions above.
   Retain the vertical-validation limitation and missing Seep Ridge exposure history; any use of the 18:01:54 sounding requires an explicitly declared time tolerance, QC and a separate matched analysis.
4. Akamai runs `make final-draft-check`, `make submission-check` and PDF inspection after integration; John reviews final response wording.

All failed scientific gates remain closed, including inversion-depth, basin-export, chemistry and persistence claims.
Manuscript/package checks were not rerun on CHPC because neither the manuscript nor its analysis sources changed in this follow-up.
