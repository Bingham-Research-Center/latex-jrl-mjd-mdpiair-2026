# figures-draft harvest record — 14 July 2026

Working figures for the deliberately maximal draft of `_manuscript_v3.tex` began on
`jrl/chpc-20260713-maximal-draft` and received the bounded v3 recomputations below on
`jrl/chpc-20260714-v3-figure-review`. **Nothing in `figures-draft/` is promoted.** The
original table is an external-engine harvest (status `exploratory` in the sense of
`figures/MANIFEST.md`: tracked nowhere, admitted nowhere); the v3 table records the
selected task-scoped replacements and additions. Provenance for the original batch
renders is in `verification/figures/archive-inventory.md` (engine jobs
13896642/13896828/13902813 and predecessors). Signs below are the authoritative
operations from
`verification/provenance/comparison-inventory.csv` and the archive inventory — note the
two feedback families whose engine sign is the **reverse** of the CMP row.

Original harvest root: `ARC = /uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/pelican2013_pub_figures/compare`

## CHPC v3 selected recomputations — 14 July 2026

The recomputation used manuscript source
`29854aac5fe4a2acbcecb705591c064197b3a8c3`, brc-tools
`69ddbe07af2e38e5e2d4f12f681bb360ff506a1a`, and task root
`/scratch/general/vast/u0737349/latex_jrl_20260714_v3_figure_review`.
Jobs `13952694` (d02), `13952692` (d03), and `13952705` (profiles) completed
with exit code `0:0`. Every selected PNG was inspected before copying.

| File | Source | Bounded content | SHA-256 |
|---|---|---|---|
| `heatdeficit_terrain-3arcsec-5arcmin_16z.png` | job `13952694`; d02 `heatdeficit_map` | CMP11 X0−X4 at 16 UTC; 2200 m crest; fixed ±1.6 MJ m⁻² | `cd4b78803e261db20b5d9f9cfc71189f219c06be816205398347ed4f1123bbed` |
| `heatdeficit_terrain-3arcsec-5arcmin_d03_16z.png` | job `13952692`; d03 `heatdeficit_map` | CMP11 X0−X4 at 16 UTC; 2200 m crest; fixed ±1.6 MJ m⁻² | `a91bb32c8b7650e6306ddb7ab8220abdd41c44d2fa5a403ccf0a83ae16f85378` |
| `section_ns_terrain-3arcsec-5arcmin_d03_16z.png` | job `13952692`; d03 `diff_terrain_res` | CMP11 north--south potential-temperature difference; fixed ±4 K | `99405289757ebfdec70d354136fd9011712a37a9503a284a987127439b329d21` |
| `section_ew_terrain-3arcsec-5arcmin_d03_16z.png` | job `13952692`; d03 `diff_terrain_res` | CMP11 east--west potential-temperature difference; fixed ±4 K | `dd3726cf1b362c414acf1c9bd064e41a19518afdcdb5af58e8b3c3aaf09266df` |
| `theta_profiles_horsepool_gfs_nam_12z.png` | job `13952705`; manuscript profile script | X6 and X5 at Horsepool; pooled shared axes with the 13 UTC panel | `2df028ad6bbf1da293d90c96fc36554c67e14c225c95ae0bcd60bb6902e13895` |
| `theta_profiles_horsepool_gfs_nam_13z.png` | job `13952705`; manuscript profile script | X6 and X5 at Horsepool; pooled shared axes with the 12 UTC panel | `8a73e8dcdfd2d4f1db5aea6dc8ac9f19bce45f1e7c595a9a3a6c16a4e68da544` |

The profile pair shares x limits 271.188538--301.680206 K and y limits
1463.333252--3300 m MSL. Temperature-series companions, profile PDFs, per-run
heat-deficit maps, and the d03 2 m-theta difference remain inspected reserves in
scratch. Their hashes and dispositions are in
`verification/provenance/v3-figure-review-20260714.json`.

| File | Source family | Renders | CMP row (authoritative op) | Sign note |
|---|---|---|---|---|
| `theta2m_GFS-NAM_16z.png` | `diff_gfs_nam` | X6−X5 2 m θ, 16 UTC | CMP01 (X6−X5) | matches |
| `section_ew_GFS-NAM_16z.png` | `diff_gfs_nam` | X6−X5 θ EW section, 16 UTC | CMP01 | matches |
| `section_ns_GFS-NAM_16z.png` | `diff_gfs_nam` | X6−X5 θ NS section, 16 UTC | CMP01 | matches |
| `theta2m_GFS-NAM-1way_16z.png` | `diff_gfs_nam_oneway` | X10−X3 2 m θ, 16 UTC | CMP02 (X10−X3) | matches |
| `section_ew_GFS-NAM-1way_16z.png` | `diff_gfs_nam_oneway` | X10−X3 θ EW section, 16 UTC | CMP02 | matches |
| `theta2m_2way-1way_16z.png` | `diff_feedback` | X5−X3 2 m θ, 16 UTC | CMP03 is X3−X5 | **engine sign reversed vs CMP03** |
| `theta2m_GFS-2way-1way_16z.png` | `diff_feedback_gfs` | X6−X10 2 m θ, 16 UTC | CMP04 is X10−X6 | **engine sign reversed vs CMP04** |
| `theta2m_2way-1way-terrain3s_16z.png` | `diff_feedback_terrain3s` | X9−X0 2 m θ, 16 UTC | CMP06 (X9−X0) | matches |
| `section_ew_2way-1way-terrain3s_16z.png` | `diff_feedback_terrain3s` | X9−X0 θ EW section, 16 UTC | CMP06 | matches |
| `theta2m_slope-shading-control_14z.png` | `diff_slope_shading` | X1−X0 2 m θ, 14 UTC (near sunrise) | CMP07 (X1−X0) | matches |
| `theta2m_slope-shading-control_18z.png` | `diff_slope_shading` | X1−X0 2 m θ, 18 UTC (late morning) | CMP07 | matches |
| `theta2m_MYJ-Eta-slope_16z.png` | `diff_myj_eta` | X2−X1 2 m θ, 16 UTC | CMP08 (X2−X1) | matches |
| `section_ew_MYJ-Eta-slope_16z.png` | `diff_myj_eta` | X2−X1 θ EW section, 16 UTC | CMP08 | matches |
| `theta2m_terrain-900m-90m_16z.png` | `diff_terrain_fine` | X3−X0 2 m θ, 16 UTC | CMP09 (X3−X0, default−fine) | matches |
| `section_ew_terrain-900m-90m_16z.png` | `diff_terrain_fine` | X3−X0 θ EW section, 16 UTC | CMP09 | matches |
| `theta2m_terrain-900m-9km_16z.png` | `diff_terrain` | X3−X4 2 m θ, 16 UTC | CMP10 (X3−X4, default−coarse) | matches |
| `theta2m_terrain-3arcsec-5arcmin_16z.png` | `diff_terrain_res` | X0−X4 2 m θ, 16 UTC | CMP11 (X0−X4, fine−coarse) | matches |
| `heatdeficit_GFS-NAM_16z.png` | `heatdeficit_map` | X6−X5 Δ heat deficit, 16 UTC, fixed ±2.5 MJ m⁻² | CMP01 | matches |
| `heatdeficit_terrain-3arcsec-5arcmin_16z.png` | `heatdeficit_map` | X0−X4 Δ heat deficit, 16 UTC, fixed ±1.6 MJ m⁻² | CMP11 | matches |
| `heatdeficit_2way-1way-terrain3s_16z.png` | `heatdeficit_map` | X9−X0 Δ heat deficit, 16 UTC, fixed ±0.2 MJ m⁻² | CMP06 | matches |
| `heatdeficit_slope-shading-control_16z.png` | `heatdeficit_map` | X1−X0 Δ heat deficit, 16 UTC, adaptive scale | CMP07 | matches |
| `heatdeficit_MYJ-Eta-slope_16z.png` | `heatdeficit_map` | X2−X1 Δ heat deficit, 16 UTC, adaptive scale | CMP08 | matches |
| `heat_deficit_timeseries.png` | `heatdeficit` | multi-run engine heat-deficit time series | — | engine diagnostic; the committed ANA-16 trajectory (`verification/figures/candidates/wrf_heat_deficit_d02_13to18.pdf`) is the audited version |
| `nested_domains.png` | `domains` | d01/d02/d03 nest geometry | — | context |
| `theta_profiles_horsepool_12z.png` | `profiles` | Horsepool model θ profiles at initialization | — | model-only point; context |
| `skewt_horsepool_gfs_12z.png` | `skewt` | X6 Horsepool skew-T at initialization | — | model-only point; context |
| `skewt_horsepool_nam_12z.png` | `skewt` | X5 Horsepool skew-T at initialization | — | model-only point; context |

Selection rule: 16 UTC is the display hour (mid decision window) for every difference
family; CMP07 uses 14 and 18 UTC because shading is sun-angle dependent; profiles and
skew-Ts use 12 UTC because they illustrate the driving states at initialization.

## Local in-repo candidates the maximal draft references in place

From `verification/figures/candidates/` (tracked in `verification/figures/manifest.csv`
with full provenance; status diagnostic/provisional, not promoted):
`wrf_heat_deficit_d02_13to18.pdf` (ANA-16 trajectory, registered + inspected),
`wrf_xsect_theta_gfs_minus_nam2way_d02.png`, `wrf_upper_700hPa/500hPa` families,
`wrf_transect_locator_d02_d03.pdf`, `obs_theta_profiles_feb0102.pdf`,
`mechanism-decomposition/fig_heatdeficit_map_16z.png` (threshold-sensitive prototype).

## Locally plotted for this draft

`fig_common_pipeline_effects.pdf` — L04/FIG-12 common-pipeline contrast panel plotted
from the committed default-matrix, CMP06, CMP07, and CMP08 surface/common-AGL summaries
by `verification/scripts/plot_common_pipeline_effects.py` (no WRF inputs).
