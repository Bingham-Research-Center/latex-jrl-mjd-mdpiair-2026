# Promoted manuscript figures

`main.tex` may include only files recorded here with status `promoted`.
Candidate and diagnostic outputs belong under `verification/figures/candidates/`.

| Figure file | Status | Script and commit | Run/data IDs | Valid window | Style check | Notes |
|---|---|---|---|---|---|---|
| `episode_context_snow_ozone_janfeb2013.pdf` | promoted | `verification/scripts/plot_episode_context.py`, `59fa4a0` | DATA39; registered NASA GIBS/MODIS browse candidate | AQS 1 January--28 February 2013 local dates; MODIS daily layer for 2 February | deterministic PDF; candidate raster visually inspected 15 July 2026 | Episode context only. AQS values are reported daily eight-hour maxima with low-coverage markers; no threshold or attainment claim. The MODIS panel is a qualitative calendar-day browse image, not a quantitative snow retrieval or WRF validation field. PDF SHA-256 `ea945fbbc3ec1496e25a0fb4965de87fe54da930ee6ecb5db63b7ea95f6aad87`. |
| `wrf_geographic_locator_d01_d03.pdf` | promoted | `verification/scripts/plot_wrf_transect_locator.py`, `92d96b1` | X0 static fields; DATA30--DATA31; Slurm 13968404 | 2 February 12 UTC static fields | PDF and raster visually inspected 15 July 2026; manuscript-native vector style | One coherent geographic map and d01--d03 inset. Domain outlines orient the full-network d02 sample; they are not a resolution comparison. PDF SHA-256 `2800ce284c4bff6bc02cd87c4e3811aec5c73e6f61ca32b27d7d3b57ec681387`. |
| `obs_temp_timeseries_feb0102.pdf` | promoted | `verification/scripts/plot_obs_feb0102.py`, `041183f` | observations; cache SHA-256 `733181afd09db704aafe2c148cf19b41bca83e8b020b9839768d7618217eeb64` | 31 January 00 UTC--4 February 00 UTC | visually inspected 10 July 2026; manuscript-native vector style | Observed floor-to-bench temperature evolution; four sites do not define basin volume. |
| `fig_common_pipeline_effects.pdf` | promoted | `verification/scripts/plot_common_pipeline_effects.py`, `c43237e` | CMP01--CMP08 registered summary tables | 2 February 14--18 UTC | regenerated and visually inspected 15 July 2026; manuscript-native vector style | Controlled-response hierarchy only. Whiskers are descriptive sensitivity intervals, not confidence intervals; the panel is not an overall configuration ranking. PDF SHA-256 `6c450304f31bf94e2d6cf8bc2727aabe0820d590253d20804050f5536dd8f5ab`. |
| `wrf_retention_ventilation_d02_14to18.pdf` | promoted | `verification/scripts/analyze_wrf_retention.py`, `10e5d34` | X6; X10; X5; X3; Slurm 13896641 | 2 February 14--18 UTC | visually inspected 14 July 2026; compact two-panel manuscript-native vector style | Solid lines are two-way and dashed lines are one-way; lines are station medians and shading is station IQR; stability and transport wind are plotted; PBLH remains in the tables but is omitted from the figure; transport wind is a fixed-layer proxy, not basin export. |
| `wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf` | promoted | `verification/scripts/plot_wrf_vs_obs_feb0102.py`, `92d96b1` | X6; X5; DATA32--DATA33; observations; Slurm 13968404 | 2 February 14--18 UTC | PDF and raster visually inspected 15 July 2026; manuscript-native vector style | The exact five-hour means are observations 16.94 K, NAM 17.03 K, and GFS 9.95 K. This horizontal bench-minus-floor contrast corroborates one surface index; it is not inversion strength or depth. PDF SHA-256 `e0b3f578b0c7b51b4fa103302a48e9a4fdea841ca25cafa514db32eb9e07c660`. |
| `wrf_heat_deficit_d02_13to18.pdf` | promoted | `verification/scripts/plot_heat_deficit_summary.py`, `10e5d34` | X6; X10; X5; X3; DATA27--DATA29; Slurm 13934123 | 2 February 13--18 UTC; 14--18 UTC decision window | PDF and raster visually inspected 15 July 2026; compact manuscript-native vector style | Main C4 remains failed: GFS has less heat deficit under every tested definition, but no member loses heat deficit over the window. The figure supports a state offset, not faster loss. PDF SHA-256 `272f3c865be0cf360a3e25024ef1fdcc43cacc942b2ec582a10771fc96fa9962e`. |
| `theta_profiles_horsepool_gfs_nam_12z.pdf`; `theta_profiles_horsepool_gfs_nam_13z.pdf` | promoted | `verification/scripts/plot_wrf_profile_spinup.py`, `92d96b1` | X6; X5; DATA34; Slurm 13968404 | 2 February 12 and 13 UTC | paired PDFs and rasters visually inspected 15 July 2026; shared-axis vector style | Appendix supplied-state context only. The model-only profiles neither separate initialization from boundary forcing nor validate inversion depth. PDF SHA-256 values `c819212e7cbc513f4d9f78ee20125416c71b122577d0de120ebbf3c6984f8562` and `1fbe04873859ddf82c3e1bc25aec5268131f61cd82dfc9c1871177c7a69af7b8`. |

Promotion requires a real-data check, matched evaluation window, complete provenance, visual inspection, and canonical WRF styling review.
Synthetic or smoke-test output is never eligible.

## Supplement-admitted figure

This file is admitted only to `supplement.tex`; it must not enter `main.tex` or
the manuscript source package.

| Figure file | Status | Script and commit | Run/data IDs | Valid window | Style check | Notes |
|---|---|---|---|---|---|---|
| `wrf_radiation_response_cmp07_d02.pdf` | supplement-admitted | `verification/scripts/analyze_radiation_response.py`, `29854aa` | X1; X0; archived d02 WRF output | 2 February 2013, 14--18 UTC; display at 16 UTC | manuscript-native vector; visually inspected 14 July 2026 | A descriptive aspect-organised skin-temperature response. The predeclared station-based screen remains failed because the archived flat-plane shortwave field cannot test the mechanism. PDF SHA-256 `56c5015210d98731e2bee061ad11922b526c99bcad94160cc4fb090b1c2a0ac2`. |

## Review-only v3 Appendix B candidates

These X8 files are deliberately **not promoted** and therefore may not enter
`main.tex`. They are grouped in the temporary in-manuscript ``Supplementary
Material'' section of `_manuscript_v3.tex` only for review; exact status and hashes
live in `verification/figures/manifest.csv`.

| Candidate basename | Status | Scientific boundary |
|---|---|---|
| `x8_deficit_transport_map_15z` | diagnostic | Within-run redistribution; no basin boundary or resolution contrast. |
| `x8_deficit_transport_gates_12to18` | diagnostic | Signed model-terrain transects with neutral names; no basin export. |
| `x8_deficit_convergence_15z` | diagnostic | Horizontal convergence contribution only; not total advection. |
| `x8_deficit_bulk_15z` | diagnostic | Exploratory layer and bulk proxy; no hydraulic-control diagnosis. |
| `x8_deficit_budget_12to18` | diagnostic | Unresolved storage difference; no closed or uniquely diabatic budget. |
