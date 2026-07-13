# CHPC figure inventory — 10 July 2026

## Purpose and status

This report inventories the existing manuscript candidates, the larger Pelican
figure catalogue, and a small set of provenance-complete rerenders for the
2 February 2013 Uinta Basin WRF case.  It is an exploratory handoff, not a
figure freeze or a Results draft.

- Repository baseline: `fe5a41c` on `origin/main`.
- Working branch: `jrl/chpc-figure-inventory`.
- Inventory/code commits used by retained figures: `c5bbe1a`, `5deba95`, and
  `041183f`.
- Host inspected: `notchpeak1.int.chpc.utah.edu`; retained renders ran on
  `notch137` through Slurm.
- Durable WRF root tested and readable:
  `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/`.
- The out-of-band archive `wrf_provenance_20260709T224907Z.tgz` was not found
  in the tested home, scratch, group, or `/tmp` locations.  Its documented
  SHA-256 remains
  `b616ec6b4ff70f3a36048904d5cad7a99a2563ba4a19fd79198fbf923332a958`.
- The `wrf-full-figures` skill was not installed as a readable Codex skill.
  Retained styling therefore follows the repository/`brc-tools` Matplotlib
  conventions and is explicitly provisional.
- No archive PNG was opened.  Archive completeness was checked only with the
  compact, exact paths in the sibling study inventory and file counts.  The
  37 manuscript-tracked candidates that existed at cold start, and every new
  retained candidate, were visually inspected.
- Nothing was promoted into `figures/`, and `main.tex` was not edited.

The sibling study handoff was reconciled against as-run WRF headers and
namelists rather than accepted as a second source of truth.  In particular,
X0 is the control, X2/MYJ is a treatment, `terrain3s` is a 3-arcsecond WPS
static grid, and neither `trang_ref` nor the January nudged run is a controlled
member of the February experiment matrix.

## Evidence retained outside Git

Bulk data and raw listings remain outside the repository.  The useful working
artifacts from this pass are:

| Artifact | Location or fingerprint | Use |
|---|---|---|
| Exact d02 WRF headers, X0–X9 | `/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/headers/`; Slurm job `13886350` | WRF version, grid, variables, FDDA state |
| Real observation cache | `/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet`; SHA-256 `733181afd09db704aafe2c148cf19b41bca83e8b020b9839768d7618217eeb64` | 5,097 rows, 11 reporting stations, 31 Jan 00 UTC–4 Feb 00 UTC |
| X0–X9 d02 station reductions | `/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/reduced_d02/`; Slurm job `13886703` | Common station evaluation |
| Matched scores | `/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/scored/wrf_runs_scores_feb0102_allx_14to18.csv`; SHA-256 `e49e70556e8abfa34189c41ce21ffe7f998149c04bfd3a43d051d3b93f808162` | Five-hour, all-run diagnostic |
| Across-run spread | `/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/scored/wrf_runs_spread_feb0102_allx_14to18.csv`; SHA-256 `d8bdad478713d1cbeef3ad2c73338665d6a8d2b87c2633038f9b4759ce74d140` | Diagnostic spread, not uncertainty |
| Locator scratch render | `/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/rerenders/locator/` | Pre-retention inspection |
| Exploratory overlays and pressure maps | `/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/rerenders/` | Iteration history; not committed |

The observation cache contains no USU06 reports in the case window.  The final
score sample has 11 temperature stations, 10 wind-speed stations, and 9
pressure stations.  QRS and QV4 do not supply pressure.  A five-hour score is
not an uncertainty estimate and must not be described as persistent skill.

## Reconciled run map

The complete machine-readable record, including archive paths, hashes, physics,
and output fields, is `verification/provenance/run-inventory.csv`.  X-codes are
only a compact cross-reference to the sibling study inventory.

| X | Stable run ID | Reconciled configuration | Window and d02 use | Confidence and caveat |
|---|---|---|---|---|
| X0 | `pelican_nam_1way_terrain3s_ysu_20130202` | NAM; 3/1/0.333 km; 75 levels; one-way; 3-arcsecond terrain; YSU/MM5 | 12–18 UTC hourly; d02 1 km common domain | High. **Control.** Static `index` gives `dx=dy=0.000833333°`; do not quote the unverified resolution of the source DEM. |
| X1 | `pelican_nam_1way_terrain3s_slope_ysu_20130202` | X0 plus `slope_rad=1`, `topo_shading=1`, `shadlen=25000` | 12–18 UTC hourly | High configuration confidence; archived source-code commit unresolved. |
| X2 | `pelican_nam_1way_terrain3s_slope_myj_20130202` | X1 with MYJ PBL/Eta surface layer in place of YSU/MM5 | 12–18 UTC hourly | High configuration confidence; **treatment, not control**; only run with `TKE_PBL`; archived source-code commit unresolved. |
| X3 | `pelican_nam_1way_default_ysu_20130202` | NAM; one-way; default terrain; YSU/MM5 | 12–18 UTC hourly | High. Default-terrain one-way leg. |
| X4 | `pelican_nam_1way_terrain5m_ysu_20130202` | X3 with 5-arcminute terrain | 12–18 UTC hourly | Medium. Namelist is byte-identical to X3, but its run summary records an earlier `...oneway_hires_terrain` path rather than the current `terrain5m` path. |
| X5 | `pelican_nam_2way_default_ysu_20130202` | X3 with two-way nest feedback | 12–18 UTC hourly | High. Default-terrain feedback leg. |
| X6 | `pelican_gfs_2way_default_ysu_20130202` | GFS driving state; otherwise X5 configuration | 12–18 UTC hourly | High. Difference from X5 is driving data plus the expected 27-versus-40 `num_metgrid_levels` consequence of GFS versus NAM input. |
| X7 | `pelican_nam_2way_1km_24h_ysu_20130202` | NAM; 3/1 km; two domains; two-way; default terrain; 75 levels | 00 UTC 2 Feb–00 UTC 3 Feb; 25 boundary-inclusive hourly files/domain | Medium. Exact staged forcing manifest unresolved. Not a controlled resolution leg relative to X0 or X8. |
| X8 | `pelican_nam_1way_111m_50lev_terrain3s_ysu_20130202` | NAM; four domains through 111 m; 50 levels; one-way; 3-arcsecond terrain only on d04; slope/shading on d02–d04 | 12–18 UTC; d01/d02 hourly, d03/d04 10-minute; this pass evaluates its **d02**, not its 111 m d04 | High identity confidence. Domain geometry, vertical levels, radiation cadence, terrain placement, and slope settings confound a resolution comparison. |
| X9 | `pelican_nam_2way_terrain3s_ysu_20130202` | X0 with two-way nest feedback | 12–18 UTC hourly | High configuration confidence; clean fine-terrain feedback pair, but no archived full-figure set and no archived source-code commit. |

All ten headers identify WRF 4.8.0 and `GRID_FDDA=0`.  The February Pelican
runs are unnudged free forecasts.  This does not establish equivalence to the
Tran et al. (2018) simulations; it establishes only design heritage for some
choices.

The NAM input manifest identifies `namanl_218` zero-hour analyses at 12 and
18 UTC (manifest SHA-256
`75518b8747d51f5c680b75a0aacb115c4695e7a9ed72550765cb7f0ae04bf301`).
The GFS manifest identifies `gfsanl_4` at the same cycles (manifest SHA-256
`912ae1e8bccda076798011ac769ace49b1ea985a61d8a33007aaf43b18b78209`).
The exact GRIB fingerprints are recorded in the working notes for this pass;
the raw manifests and GRIBs remain outside Git.

## Controlled-comparison matrix

“Controlled” below means that the as-run namelists, grids, window, and relevant
static inputs were reconciled.  It does not mean that five samples supply a
formal significance test.

| Priority | Pair and sign | Isolated question | Evidence of control | Current diagnostic status |
|---|---|---|---|---|
| Primary | X6 − X5 | GFS versus NAM driving state | Same d02 grid, physics, feedback, terrain, vertical grid, init/window; only driving product and its metgrid-level count differ | Defensible. Retained surface overlays and 500/700 hPa direct differences. |
| Secondary | X3 − X5 | NAM one-way minus NAM two-way feedback | As-run WRF namelists differ only by `feedback=0/1`; same default terrain and window | Defensible. Surface response is nearly null; retained pressure-level differences show small basin-interior response and terrain-edge structure. |
| Secondary/next | X9 − X0 | Feedback at the control's fine terrain | As-run namelists differ only by feedback; same NAM, 3-arcsecond static, physics, and window | Cleaner feedback test than X3/X5, but X9 lacks a full-figure set and a registered study-repo run key. |
| Diagnostic | X1 − X0 | Slope/shading radiation | Only `slope_rad`, `topo_shading`, and `shadlen` differ | Controlled pair; no matched process figure retained yet. |
| Diagnostic | X2 − X1 | MYJ/Eta versus YSU/MM5 | Only PBL and surface-layer scheme IDs differ | Controlled pair; scheme-aware profiles are still needed. The current surface metric is not uniformly negligible. |
| Diagnostic | X3 − X0 | Default versus 3-arcsecond terrain | WRF namelist byte-identical; terrain enters through WPS/static input | Controlled at the configuration level; requires terrain-aware station and pressure treatment. |
| Diagnostic | X3 − X4 | Default versus 5-arcminute terrain | WRF namelist byte-identical; WPS/static differs | Configuration axis is controlled, but X4's archive-name discrepancy lowers provenance confidence. |
| Diagnostic | X0 − X4 | 3-arcsecond versus 5-arcminute terrain | Same NAM/one-way/YSU physics and window | Potential headline terrain-resolution pair after X4 provenance is closed. |
| Not controlled | X7, X0, X8 | Apparent 1 km/333 m/111 m “resolution ladder” | — | Do not interpret as resolution sensitivity: initialization, forecast age, domain count/geometry, feedback, terrain, vertical levels, slope/shading, and cadence differ. |
| Context only | `trang_ref`, January analysis-nudged run, Pelican runs | Heritage or historical comparison | Heterogeneous WRF versions, grids, levels, run lengths, physics/FDDA, and episodes | Never a controlled sensitivity. Do not call `trang_ref` the literal Tran et al. (2018) run. |

## Variable-availability matrix

Header inspection used one exact d02 file from every X0–X9 archive path.  A
field's presence permits a diagnostic; it does not make an uncontrolled pair a
sensitivity experiment.

| Process or requested diagnostic | X0–X9 availability | Units/source | Interpretation gate |
|---|---|---|---|
| 2 m temperature and moisture | `T2`, `Q2` in all runs | K; kg kg⁻¹ | Available at all five common hours and all d02 stations. |
| 10 m wind | `U10`, `V10`, `COSALPHA`, `SINALPHA` in all runs | m s⁻¹ | Must rotate grid-relative components earth-relative before speed/direction or differences. |
| Surface pressure | `PSFC` in all runs | Pa | Useful synoptic check, but station pressure bias is strongly affected by model-versus-observed elevation. |
| Lower-tropospheric stability/depth | `T`, `P/PB`, `PH/PHB` in all runs | θ in K; pressure Pa; height m | Derive on common AGL/pressure coordinates with identical interpolation and masks. |
| Layer wind/ventilation | 3-D `U`, `V`, height/pressure in all runs | m s⁻¹ | Define the layer and metric before viewing differences. |
| PBL height | `PBLH` in all runs | m | Scheme-dependent diagnostic; not a universally equivalent physical depth. |
| Turbulent kinetic energy | `TKE_PBL` only in X2/MYJ | m² s⁻² in WRF output | Absence in YSU is not zero TKE. Compare scheme-aware turbulence diagnostics, not the raw field alone. |
| Snow | `SNOW`, `SNOWH`, `SNOWC` in all runs | WRF metadata units | Inventory and compare only within controlled pairs; distinguish initial/static snow from evolving state. |
| Skin temperature and albedo | `TSK`, `ALBEDO` in all runs | K; fraction | Supports surface-energy diagnostics; no sensitivity inference without a controlled surface pair. |
| Radiation | `SWDOWN`, `GLW`, `OLR` in all runs | W m⁻² | Suitable for slope/shading and surface-energy budgets after common sampling. |
| Surface fluxes | `HFX`, `LH`, `GRDFLX`, `UST` in all runs | W m⁻² except friction velocity | Useful retention/mixing process checks; sign conventions must be stated. |
| Cloud and condensate | `CLDFRA`, `QCLOUD`, `QICE`, `QRAIN`, `QSNOW`, `QGRAUP` in all runs | fraction or kg kg⁻¹ | Can diagnose cloud/fog plausibility, but there is no direct visibility field and no verified fog observation in the current cache. |
| Observations | Temperature: 11 stations; wind speed: 10; pressure: 9 | °C, m s⁻¹, Pa | Real Synoptic cache; USU06 absent. The bench–floor metric uses USU03 minus USU07. |

## Large archive catalogue

The consolidated `verification/figures/archive-inventory.md`
provides exact compact paths, and targeted counts were independently checked.
No archive image was opened.

| Run | Sections | Surface | Upper air | Other | Total/status |
|---|---:|---:|---:|---:|---|
| X0–X6, each | 14 | 35 | 14 | 0 | 63 PNG each; complete standard set |
| X7 | 48 | 120 | 48 | 0 | 216 PNG; catalogue treats 24 valid times although raw WRF output has 25 boundary-inclusive timestamps |
| X8 | 28 | 35 | 7 | profiles 7, skew-T 7, domains 1, heat deficit 1 | 86 non-standard PNG; nested layout and crest-only upper air |
| X9 | 0 | 0 | 0 | 30 quicklook PNG | No `full-figures/` set |

Cross-case catalogue counts are: X6−X5 `diff_gfs_nam` 21; X5−X3
`diff_feedback` 7; X3−X4 `diff_terrain` 7; X3−X0
`diff_terrain_fine` 42 (over-counted, likely stale extras); X1−X0
`diff_slope_shading` 7; X2−X1 `diff_myj_eta` 21; X0−X4
`diff_terrain_res` 21; plus domains 1, heat deficit 1, profiles 1, and
skew-T 55.

Those images are readily regenerable, but they are not added to the manuscript
manifest here.  The exact runtime generator commit for each archived set is not
pinned by the output directory, and X0's image mtimes predate later figure-engine
commits.  The current sibling `brc-tools` checkout at inventory time was
`89883ce`, but that is not evidence that `89883ce` generated an older file.

## Audit of the 37 cold-start tracked candidate files

The 37 files represented 34 logical figures: three observation figures with
PNG/PDF variants, seven January context figures, eight cross-sections, eight
time-height figures, and eight upper-air maps.  Common provenance is stated once
per family; each logical row then records its question, visual reading,
alternative explanations, required change, and status.

### Observations: three logical figures, six files

Common record:

- Runs/configurations: none; observations only.
- Window: 31 January 00 UTC–4 February 00 UTC, including the 2 February episode.
- Stations: 11 reporting stations; pseudo-profiles use stations with pressure;
  temperature evolution highlights USU07/USU05/USU04/USU03.
- Variables: 2 m temperature (°C), surface pressure (Pa), potential temperature
  (K), station elevation (m), bench-minus-floor Δθ (K), and pseudo-profile heat
  deficit (MJ m⁻²).
- Input: verified real cache and SHA-256 listed above; station metadata in
  `verification/data/stations_2013_selection.csv`.
- Generator: `verification/scripts/plot_obs_feb0102.py`; exact command is in
  the reproduction section; commit `041183f`; CHPC job `13891235` on
  `notch137`; high provenance confidence.
- Candidate state: diagnostic/provisional style.  All PNG/PDF pairs were
  regenerated and visually inspected; manifest rows are populated.

| Logical figure and files | Scientific question | What it appears to show | Plausible alternative or limitation | Required improvement | Status |
|---|---|---|---|---|---|
| `obs_theta_profiles_feb0102.{png,pdf}` | How does apparent thermal structure vary from basin floor to bench through the episode? | Strong positive floor-to-bench θ differences recur; the shape changes markedly between night and day. | This is a horizontal station pseudo-profile, not a colocated free-air sounding. Surface exposure and local slope/bench effects can mimic vertical structure. | Add uncertainty/site-exposure notes; pair with a sounding or model/observed AGL profile if available. | Diagnostic; main-text support only with the pseudo-profile caveat, otherwise supplement. |
| `obs_temp_timeseries_feb0102.{png,pdf}` | Does the observed floor/bench temperature contrast evolve through the episode? | The basin floor repeatedly cools well below higher sites while the high bench can warm during daylight. | Station exposure, data gaps, and horizontal gradients contribute; four sites do not define basin volume. | Add coverage/quality marks and, if useful, a compact station locator reference. | Strongest current observed-evolution candidate; provisional style. |
| `obs_inversion_index_feb0102.{png,pdf}` | When is the bulk CAP strong, and how does a pseudo-profile heat deficit evolve? | USU03−USU07 Δθ is commonly well above 8 K, and the pseudo-profile heat deficit varies on the diurnal cycle. | The 8 K line is a literature yardstick, not a case-specific physical threshold; heat deficit depends on sparse horizontal stations and the selected top station. | Sensitivity to station subset/top height and uncertainty; avoid treating it as measured inversion depth. | Diagnostic; likely main/supplement split after robustness work. |

### January analysis-nudged context: seven logical PNGs

Common record:

- Context label: archived `WRF_TRANG_frozone/WRF_anlnudge`; this is not X0 and
  not the February baseline to beat.
- Domain/window: inherited d03 (approximately 1.33 km), 15 January 12 UTC–
  21 January 00 UTC 2013, 133 hourly frames; no reconciled spin-up exclusion.
- Stations: USU01, USU05, USU08, KVEL, QV4, QRS; QV4/QRS lack pressure.
- Variables: 2 m temperature (°C), 10 m wind speed (m s⁻¹), surface pressure
  (hPa/Pa), station bias/RMSE, and diurnal bias.
- Inputs: inherited `wrf_trang_2013_per_station.csv`, January Synoptic cache,
  and `verification/data/baseline_scores_jan1521.csv`; raw source identity and
  cache fingerprints were not recovered in this pass.
- Generator: `verification/scripts/plot_baseline_eval.py`; documented command
  is `python verification/scripts/plot_baseline_eval.py` with data under the
  configured `brc-tools/data` directory.  Script lineage is commit `dd2b846`,
  and the candidate files were last touched by `095928e`; the exact runtime
  generator commit is unresolved.  Provenance confidence is medium for the
  analysis and low for a controlled comparison.  No manifest rows are added.

| File | Scientific question | Rough visual reading | Alternative/limitation | Required improvement | Status |
|---|---|---|---|---|---|
| `baseline_temp_timeseries_jan1521.png` | Does the January nudged run follow observed 2 m temperature? | Broad warm offset at all six sites. | Different episode, FDDA, run length, grid, and physics from Pelican; not a February control. | Preserve only with an explicit context banner and complete source provenance. | Context only; reviewer reserve. |
| `baseline_windspeed_timeseries_jan1521.png` | Does it reproduce calm periods? | Often too windy; timing weak. | Calm wind observations and representativeness are difficult; heterogeneous case. | Add observation availability and calm-direction handling. | Context only. |
| `baseline_pressure_timeseries_jan1521.png` | Is the synoptic mass-field evolution plausible? | Good tracking at pressure-reporting sites. | Empty QRS/QV4 pressure panels can look like missing-model data; terrain/elevation bias is hidden. | Remove empty panels and state station-versus-model elevation. | Context only. |
| `baseline_skill_bars_jan1521.png` | Which station/variable errors dominate? | Temperature error is systematically large; pressure is comparatively small. | Aggregate bars conceal timing and mix units/scales across panels. | Retain only alongside time-resolved panels; reconcile circular wind metrics. | Reviewer reserve. |
| `baseline_temp_scatter_jan1521.png` | Is the temperature error an offset or loss of covariance? | Points generally lie above 1:1. | Serial dependence and site clustering make the cloud look more independent than it is. | Add site/time grouping or uncertainty if retained. | Reviewer reserve. |
| `baseline_temp_diurnal_bias_jan1521.png` | Is warm bias concentrated at cold-pool times? | Bias varies by hour and site. | UTC/local-time framing and unequal sample counts can mislead. | Local-time labels, sample counts, and uncertainty bands. | Context diagnostic. |
| `baseline_inversion_night_zoom_jan1521.png` | What happens near the coldest observed January period? | The model does not match the deepest observed cooling. | Window selected after seeing the minimum; not independent and not the February episode. | Treat selection as descriptive and keep outside the main comparison. | Context diagnostic only. |

### Vertical θ cross-sections: eight logical PNGs

Common record for the first six:

- Runs: X6/GFS two-way, X5/NAM two-way, and X3/NAM one-way.
- Domain/grid: d02, 1 km, 75 levels; current transect USU07
  (40.0346, −109.8301, 1465 m) to USU03
  (40.4319, −110.3821, 2228 m), 64.5 km.
- Variables: perturbation θ + 300 K, geopotential height (m ASL), WRF terrain.
- Inputs: reconciled archive paths in the run inventory, but the exact staging
  artifacts and runtime commands for these tracked PNGs are unresolved.
- Generator lineage: `verification/scripts/plot_wrf_cross_sections.py`, current
  family implementation introduced by `7be5faa` and altered in `c31a68b`;
  files last touched by `095928e`.  Exact runtime generator commit is not
  asserted.  Provenance confidence is medium for X3/X5/X6 identity, low for
  publication reproducibility.  No manifest rows are added.
- Each absolute figure currently chooses its own θ range, so color comparisons
  across runs are qualitative only.  The 4,500 m ASL ceiling compresses the
  shallow cold pool.
- **Update 2026-07-11 (JRL + Opus):** both caveats in the two bullets above are now
  addressed. `plot_wrf_cross_sections.py` gained `--theta-min/--theta-max`; the
  GFS/NAM-2way and NAM-1way θ x-sections + QRS time-heights were re-rendered on a
  **shared 266–306 K scale** (so cross-run color is now quantitative), and all 29
  previously-unregistered `candidates/` PNGs now carry `manifest.csv` rows
  (statuses: diagnostic/rejected/superseded/context). Decision-by-decision exhibit
  map: `evidence-longlist.md`. The frame-zero `wrf_xsect_theta_*_d02.png` remain
  **rejected** (init artifact); prefer the `_16z` shared-scale versions.

| File | Time/spin-up and question | Rough visual reading | Alternative/limitation | Required rerender | Status |
|---|---|---|---|---|---|
| `wrf_xsect_theta_gfs_2way_d02.png` | Frame zero; what lower-tropospheric structure enters from GFS? | Contains conspicuous block/initialization structure. | Initialization interpolation artifact dominates. | Do not use; replace with common 14–18 UTC panels/difference. | Rejected. |
| `wrf_xsect_theta_gfs_2way_d02_16z.png` | 16 UTC post-spin-up; does GFS retain a shallow pool? | Shallower/weaker-looking structure than NAM. | Independent color range and one diagonal transect can exaggerate contrast. | Fixed shared θ levels, GFS−NAM difference, shallow AGL companion. | Diagnostic. |
| `wrf_xsect_theta_nam_2way_d02.png` | Frame zero; what structure enters from NAM? | Cold-pool structure is present but frame-zero comparison is contaminated. | Same initialization problem. | Supersede with post-spin-up matched panels. | Rejected. |
| `wrf_xsect_theta_nam_2way_d02_16z.png` | 16 UTC; does the primary NAM member retain the pool? | Deeper/stronger-looking low-level θ structure than GFS. | Scale and slice-selection limitations; no direct observed vertical profile. | Shared scale, direct difference, AGL/low-layer zoom. | Diagnostic. |
| `wrf_xsect_theta_nam_1way_d02.png` | Frame zero; does feedback alter the initial slice? | Very similar to NAM two-way at initialization. | Expected shared IC; not an evolved feedback test. | Do not interpret; use post-spin-up differences. | Rejected/redundant. |
| `wrf_xsect_theta_nam_1way_d02_16z.png` | 16 UTC; is there an evolved feedback response? | Visually close to NAM two-way. | Independent scales and a short window can hide small differences. | Direct X3−X5 panel on identical levels and coordinates. | Diagnostic/null candidate. |
| `wrf_xsect_theta_trang_ref.png` | Same-case heterogeneous context; how does the SIP-lineage field look? | A deeper/colder structure than some touchstones. | Run identity is not the literal Tran et al. simulation; configuration, grid, forecast age, and run length differ. | Recover exact source and use only as context with matched coordinates/window. | Context only. |
| `wrf_xsect_theta_trang_anlnudge_jan17.png` | January context; how does the nudged run represent a winter inversion? | Strong January structure is visible. | Different date and configuration; cannot rank February runs. | Keep only as historical/reviewer context. | Context only. |

### θ time-height figures: eight logical PNGs

Common record:

- X3/X5/X6 rows use d02 at QRS and the broad 12–18 UTC sequence; the
  `_16z` suffix does **not** make the time-height figure a 16 UTC snapshot.
  For each touchstone, suffixed and unsuffixed files are duplicate
  interpretations of the same sequence.
- Variables are θ (K) versus height ASL (m); each file has an independent θ
  range and a 4,500 m top.
- Input/generator lineage and confidence match the cross-section family.
  Exact runtime commands and commits are unresolved; no manifest rows are added.

| File | Scientific question | Rough visual reading | Alternative/limitation | Required change | Status |
|---|---|---|---|---|---|
| `wrf_timeheight_theta_gfs_2way_d02.png` | Does GFS retain low-level stability through 12–18 UTC at QRS? | Weaker/shallower structure than NAM. | Includes initialization; independent scale; a single point is not basin retention. | Restrict/mark 14–18, share levels, use AGL and a direct difference. | Diagnostic. |
| `wrf_timeheight_theta_gfs_2way_d02_16z.png` | Same question | Same broad sequence as the unsuffixed file. | Naming implies a snapshot that the content does not represent. | Keep one canonical filename after rerender. | Redundant duplicate interpretation. |
| `wrf_timeheight_theta_nam_2way_d02.png` | Does NAM two-way retain the stable layer? | Persistent-looking low-level stability over the short sequence. | Five post-spin-up samples cannot establish persistence. | Common AGL levels, direct GFS/NAM and feedback differences. | Diagnostic. |
| `wrf_timeheight_theta_nam_2way_d02_16z.png` | Same question | Same broad sequence. | Misleading suffix. | Rationalize naming. | Redundant duplicate interpretation. |
| `wrf_timeheight_theta_nam_1way_d02.png` | Does one-way nesting change retention? | Very similar to NAM two-way. | Small effects may be hidden by independent ranges. | Direct X3−X5 difference with fixed limits. | Diagnostic/null candidate. |
| `wrf_timeheight_theta_nam_1way_d02_16z.png` | Same question | Same broad sequence. | Misleading suffix. | Rationalize naming. | Redundant duplicate interpretation. |
| `wrf_timeheight_theta_trang_ref.png` | How does the heterogeneous same-case lineage evolve? | Strong/deep stability relative to some short runs. | Not controlled and not the literal Tran et al. simulation. | Exact identity and matched window before any contextual use. | Context only. |
| `wrf_timeheight_theta_trang_anlnudge_jan17.png` | How does the January nudged context evolve? | Stable January structure. | Different episode and assimilation. | Reviewer reserve only. | Context only. |

### Upper-air maps: eight cold-start logical PNGs

The six absolute maps were generated before the current earth-relative wind
rotation and use independent θ scales.  Their scientific run mapping is known
(X6, X5, X3 on d02), but exact runtime generator commits and inputs are not.
They are retained only as rough diagnostics.  The two GFS−NAM difference PNGs
were replaced in this pass and paired with vector PDFs.

| Logical figure/file | Scientific question | Rough visual reading | Alternative/limitation | Required change | Status |
|---|---|---|---|---|---|
| `wrf_upper_500hPa_gfs_2way_d02.png` | What is the GFS 500 hPa state? | Broad synoptic θ/wind structure. | Independent color scale and legacy grid-relative arrows. | Rerender absolute GFS/NAM panels with identical θ bounds and earth-relative winds. | Superseded rough diagnostic. |
| `wrf_upper_500hPa_nam_2way_d02.png` | What is the NAM two-way 500 hPa state? | Visually similar broad state. | Color cannot be compared quantitatively. | Same shared-scale rerender. | Superseded rough diagnostic. |
| `wrf_upper_500hPa_nam_1way_d02.png` | Does feedback visibly affect the 500 hPa absolute field? | Nearly indistinguishable by eye. | Independent scales can hide or manufacture apparent differences. | Use retained direct X3−X5 difference instead. | Superseded. |
| `wrf_upper_700hPa_gfs_2way_d02.png` | What lower-tropospheric state accompanies GFS? | Warmer-looking basin layer. | Independent scale; white high terrain is below-ground masking, not missing data. | Shared scale and explicit gray mask if an absolute panel is retained. | Superseded rough diagnostic. |
| `wrf_upper_700hPa_nam_2way_d02.png` | What lower-tropospheric state accompanies NAM? | Cooler-looking than GFS. | Same scale/mask/wind limitations. | Shared-scale absolute pair. | Superseded rough diagnostic. |
| `wrf_upper_700hPa_nam_1way_d02.png` | Does feedback affect the absolute 700 hPa field? | Very close to NAM two-way. | Terrain mask and scale dominate subtle changes. | Use direct difference and distinguish basin interior from mask edges. | Superseded. |
| `wrf_upper_500hPa_gfs_minus_nam2way_d02.{png,pdf}` | Does the driving-state difference persist at 500 hPa? | Difference changes sign/structure between 14, 16, and 18 UTC; no persistent basin-wide offset comparable to 700 hPa. | Three snapshots, interpolation, and lateral-boundary evolution; no causal attribution to mixing alone. | Add full five-hour evolution or a layer/profile companion if promoted. | Provenance-complete diagnostic; manifest populated. |
| `wrf_upper_700hPa_gfs_minus_nam2way_d02.{png,pdf}` | Is the driving-state disagreement concentrated lower in the troposphere? | Coherent positive GFS−NAM θ over much of the basin at 14/16 UTC, weakening and becoming patchier by 18 UTC. | 700 hPa intersects terrain; interpolation/masking and inherited boundary state are competing explanations. | Pair with pressure/AGL profiles and quantify basin-interior distributions. | Provenance-complete diagnostic; manifest populated. |

## New provenance-complete candidates

The final manifest contains 12 logical rows: the three regenerated observation
figures, four real-data surface overlays, the locator, two primary pressure-level
differences, and two secondary feedback differences.  No row is promoted.

| Candidate | Run/data support | Window/domain | Visual finding and use | Status |
|---|---|---|---|---|
| GFS two-way versus NAM two-way 2 m temperature | X6, X5, real observations | d02 stations, 14–18 UTC, five hours | GFS is much warmer at the floor and generally warmer/more weakly stratified than NAM; station behavior is heterogeneous. | Primary diagnostic; dependence-aware surface summaries completed in job 13893307. |
| GFS two-way versus NAM two-way bench−floor Δθ | X6, X5, real observations | USU03−USU07, 14–18 UTC | NAM stays near the observed bulk contrast; GFS is much weaker and briefly below 8 K at 14 UTC. | Primary diagnostic; not a measured inversion depth. |
| NAM one-way versus NAM two-way 2 m temperature | X3, X5, real observations | d02 stations, 14–18 UTC | Lines almost overlap at all four highlighted stations. | Secondary null diagnostic. |
| NAM one-way versus NAM two-way bench−floor Δθ | X3, X5, real observations | USU03−USU07, 14–18 UTC | Differences are small relative to observation evolution. | Secondary null diagnostic. |
| d02/d03 terrain and transect locator | X0 static fields and station metadata | Static 12 UTC fields | Shows d03 excludes most bench/end stations; all proposed full transects must be evaluated on d02. | Diagnostic locator; provisional style. |
| GFS−NAM 500 hPa θ/wind differences | X6−X5 | d02, 14/16/18 UTC | Mixed-sign, time-changing upper-level difference. | Primary mechanism diagnostic/reviewer reserve. |
| GFS−NAM 700 hPa θ/wind differences | X6−X5 | d02, 14/16/18 UTC | Stronger coherent lower-tropospheric θ difference at 14/16 UTC. | Candidate main/supplement mechanism panel after profile support. |
| NAM one-way−two-way 500 hPa θ/wind differences | X3−X5 | d02, 14/16/18 UTC | Basin-interior response is close to zero on the fixed ±0.5 K scale. | Secondary null diagnostic. |
| NAM one-way−two-way 700 hPa θ/wind differences | X3−X5 | d02, 14/16/18 UTC | Interior response remains small; stronger colors cluster near terrain/mask edges. | Reviewer-reserve diagnostic; edge interpretation required. |

## Exploratory matched diagnostics

The following are station means of the per-station bias, not pooled biases or
uncertainty estimates.  Temperature uses 11 stations, wind speed 10, pressure
9.  The bulk Δθ column is USU03 minus USU07 and includes all five hourly
samples.  X8 values are from its common **d02**, not its 111 m d04.

| Run | T2 bias (°C) | 10 m speed bias (m s⁻¹) | PSFC bias (Pa) | Mean Δθ (K) |
|---|---:|---:|---:|---:|
| X0 control | +0.824 | +0.489 | −211.8 | 16.998 |
| X1 slope/shading YSU | +0.849 | +0.491 | −211.9 | 17.177 |
| X2 slope/shading MYJ | +1.299 | +0.411 | −205.5 | 18.490 |
| X3 NAM one-way default | +0.840 | +0.503 | −230.5 | 17.004 |
| X4 NAM one-way 5 arcmin | +0.595 | +0.846 | +0.5 | 16.741 |
| X5 NAM two-way default | +0.831 | +0.510 | −230.2 | 17.027 |
| X6 GFS two-way default | +2.123 | +1.231 | −248.7 | 9.950 |
| X7 NAM two-way 1 km/24 h | +2.641 | +0.238 | −282.8 | 13.481 |
| X8 four-domain run, sampled on d02 | +0.881 | +0.529 | −232.0 | 16.798 |
| X9 NAM two-way 3 arcsec | +0.819 | +0.488 | −211.7 | 16.707 |
| Observed | — | — | — | 16.942 |

Observed Δθ ranges from 12.63 to 20.21 K.  X6 ranges from 7.35 to
11.74 K; X5 from 16.44 to 18.07 K; X3 from 16.27 to 17.59 K; and X2
from 15.20 to 20.74 K.

Provisional leads, with their competing explanations, are:

1. **Driving state is the strongest reconciled short-window contrast.** X6 is
   warmer and windier at the surface and has a much weaker bench−floor θ
   contrast than X5.  The 700 hPa difference is larger and more coherent than
   the 500 hPa difference at 14/16 UTC.  This can reflect inherited GFS/NAM
   initial and lateral-boundary structure, not only WRF-developed mixing.
2. **Default-terrain nest feedback is close to a null result over six hours.**
   X3 and X5 nearly overlap in the surface plots, and their pressure-level
   basin-interior differences are small.  A short forecast, a d02 sample, or
   weak feedback during this period could all explain the null.
3. **The MYJ treatment is not demonstrably “small below 700 m” from the current
   evidence.** X2's surface bulk contrast differs from X1 and evolves more.
   The sibling archive description may refer to another vertical/profile
   definition; a common AGL profile is required before accepting or rejecting
   it.
4. **Pressure scores are terrain-sensitive.** The 5-arcminute run's near-zero
   station-mean PSFC bias is not evidence of a superior synoptic solution.  Its
   model terrain shifts substantially at some stations (for example, USU04 is
   about 109 m lower than observed), directly changing station pressure.
5. **The apparent resolution ladder cannot support a resolution story.** X7,
   X0, and X8 differ in too many controls.  Their scores remain diagnostics of
   those complete configurations only.

## Analytical changes versus cosmetic changes

Analytical changes made in this branch:

- reconciled ten exact run IDs and as-run namelists rather than using filename
  labels;
- constrained both scoring and overlays to 14–18 UTC with an explicit maximum
  time, preventing X7's longer run from contributing extra samples;
- regenerated overlays from real observations;
- rotated pressure-level U/V grid-relative components to earth-relative before
  plotting or differencing;
- generated signed direct differences X6−X5 and X3−X5 on the same d02 grid;
- treated below-ground pressure-level points as masked rather than missing;
- kept station-pressure interpretation separate from terrain mismatch.

Cosmetic/presentation changes:

- hourly ticks for the five-hour overlays and non-clipped threshold labels;
- fixed symmetric θ-difference scales (±2 K at 500 and ±3 K at 700 for
  X6−X5; ±0.5 K for X3−X5);
- gray below-ground fill, station markers, degree-format axes, vector keys, and
  fixed per-figure quiver scales;
- PNG/PDF output pairs and a dedicated d02/d03 locator.

The distinction matters: changing a colormap or arrow length does not strengthen
the scientific comparison; rotating winds and enforcing the common window do.

## Transect locator and alternatives

The retained locator is
`verification/figures/candidates/wrf_transect_locator_d02_d03.{png,pdf}`.
It uses X0 d02/d03 terrain at 12 UTC and all reporting stations.

| Transect | Exact endpoints | Length and d02 terrain | Named hypothesis and domain note |
|---|---|---|---|
| Current diagonal | USU07/Pariette Draw: 40.0346, −109.8301, 1465 m → USU03/Mountain Home: 40.4319, −110.3821, 2228 m | 64.5 km; sampled terrain 1462–2219 m | Does the model connect the cold basin floor to the high northwest bench while retaining a shallow stable layer? d02 covers it; USU03 is outside d03. |
| Proposed floor-to-bench | USU07: 40.0346, −109.8301, 1465 m → USU04/Seep Ridge: 39.7539, −109.5460, 1933 m | 39.6 km; terrain 1451–1954 m | Tests floor-to-southern-bench inversion structure with a shorter elevation transition and a named observed endpoint. d02 only; USU04 is outside d03. |
| Proposed along-basin ventilation | UUT01/Uintah Basin Research Trailer: 40.2656, −110.0412, 1561 m → USU08/USU Trailer: 40.1437, −109.4672, 1570 m | 50.7 km; terrain 1420–1574 m | Tests whether west-to-east layer wind and θ gradients indicate along-basin ventilation between nearly equal-elevation endpoints. d02 covers the full line; d03 covers only part. |

Neither alternative was selected because its result looked strongest; both were
selected from topography, station endpoints, and a pre-stated hypothesis.  The
next cross-section rerender should show both ASL context and a shallow
terrain-following/AGL companion (for example, the lowest 0–1,000 m AGL).  The
current 4,500 m ASL limit compresses the cold pool.

## Candidate figure ladder, not a frozen story

| Ladder step | Question | Supporting observation/comparison | Falsifier or competing explanation | Placement now |
|---|---|---|---|---|
| 1. Observed structure/evolution | Was a strong, evolving cold pool present? | Real temperature, bench−floor Δθ, heat deficit, and station pseudo-profiles | Pseudo-profile/site exposure dominates; sparse stations do not represent basin volume | Main: temperature/Δθ after robustness; pseudo-profile likely supplement. |
| 2. Surface fidelity | Which matched WRF driving state follows observed floor/bench evolution? | X6 versus X5 on d02, identical five hours/stations | Observation representativeness or inherited forcing differences rather than developed WRF behavior | Bulk theta-contrast PDF promoted with horizontal-profile caveat. |
| 3. Retention/inversion response | Does each run retain the shallow stable layer and weak ventilation through the window? | Completed common-AGL stability, layer transport wind, PBLH, T2/U10, and PSFC summaries | Fixed station columns do not measure basin volume; PBLH is scheme dependent | Common-AGL PDF promoted; five-hour scope retained. |
| 4. Lower-tropospheric origin | Is GFS−NAM disagreement larger near 700 than 500 hPa and connected to the basin layer? | Retained signed 500/700 hPa differences plus future profiles | Pressure-surface terrain/masking and lateral-boundary structure explain the map | Main/supplement candidate; profile support required. |
| 5. Nest feedback test | Does one-way versus two-way nesting matter over six hours? | X3−X5 now; cleaner X9−X0 next | A defensible null result, or effects limited to d03/longer integration | Supplement/reviewer reserve; main only if the null is central and bounded. |
| 6. Trang/January context | How do heterogeneous lineage runs frame limitations? | January figures and `trang_ref` diagnostics | They are mistaken for controlled members or literal published simulations | Reviewer reserve/supplement only. |
| 7. Air-chemistry implication | Is the meteorological mixing volume/ventilation credible enough for chemical attribution? | Promoted retention and ventilation diagnostics, not meteorology scores alone | Chemistry, inventory, deposition, snow photolysis, or cloud errors remain material | Carefully scoped discussion implication; no stand-alone chemistry result figure yet. |

## Prioritized next five rerenders or diagnostics

1. **Completed in Slurm job 13893307: time-resolved retention and ventilation
   spine for X6/X5, with X3/X5 as secondary.** On common d02 and all five hours, combine T2, earth-relative
   U10/V10, PSFC, PBLH, lower-tropospheric θ/stability or inversion depth, and a
   pre-defined layer-wind/ventilation metric.  Use common AGL coordinates and
   state observation counts and uncertainty.
2. **Matched cross-sections and direct differences.** Rerender the current
   USU07→USU03 section at 14–18 UTC with identical levels, then X6−X5 and
   X3−X5 difference panels.  Add a 0–1,000 m AGL or shallow-ASL companion and
   test the two hypothesis-led alternatives without choosing by outcome.
3. **Complete the clean fine-terrain feedback comparison.** Add X9 as a
   registered run key in the study case file, generate its standard set, and
   define X9−X0.  The unavailable `wrf-full-figures` skill means styling remains
   provisional until that workflow is restored or a documented `brc-tools`
   equivalent is used.
4. **Scheme-aware X2−X1 PBL diagnostic.** Plot common θ/temperature/wind
   profiles, PBLH, surface fluxes, and X2 TKE in a way that does not interpret
   missing YSU `TKE_PBL` as zero.  Reconcile the sibling claim of changes below
   about 700 m AGL against an explicitly defined profile metric.
5. **Design a genuinely controlled resolution experiment.** Rerun a
   1 km/333 m/111 m set with the same initialization, forecast age, domain
   footprint, feedback, terrain, vertical grid, slope/shading, and output
   cadence.  Do not spend narrative effort on the current confounded ladder.

## Evidence-first closeout: Slurm job 13893307

The first-draft retention/ventilation gate was completed after the inventory
pass without launching another WRF treatment.  The analysis read the accepted
X6, X5, and X3 d02 archives, retained the same 11 reporting-station columns and
14--18 UTC window, and verified that all three latitude/longitude grids were
identical to machine precision.

The preregistered model-layer diagnostics were:

- **stability:** theta at 500 m AGL minus theta at 50 m AGL;
- **transport wind:** magnitude of the height-weighted mean earth-relative U/V
  vector from 50 to 500 m AGL; this is a fixed-layer ventilation proxy, not
  basin export or a chemistry-model ventilation coefficient; and
- **PBLH:** the native WRF diagnostic, retained only as a scheme-dependent
  companion field.

Run differences were paired at each station and hour.  The spatially dependent
station field was then reduced to one hourly median, and a two-hour circular
moving-block resample was applied across the five hourly medians.  The interval
below is a descriptive sensitivity interval, not a formal confidence interval.

| Pair and metric | Mean hourly spatial-median difference | Two-hour block sensitivity interval | Hourly sign |
|---|---:|---:|---:|
| X6 GFS minus X5 NAM, 50--500 m stability | -3.63 K | -4.94 to -2.22 K | weaker GFS stability in 5/5 hours |
| X6 GFS minus X5 NAM, transport wind | +0.79 m s-1 | +0.58 to +0.99 m s-1 | stronger GFS wind in 5/5 hours |
| X6 GFS minus X5 NAM, PBLH | +1.14 m | -11.24 to +10.48 m | mixed, 3 positive/2 negative |
| X3 one-way minus X5 two-way, stability | +0.002 K | -0.039 to +0.053 K | mixed |
| X3 one-way minus X5 two-way, transport wind | +0.006 m s-1 | -0.017 to +0.026 m s-1 | mixed |
| X3 one-way minus X5 two-way, PBLH | -0.056 m | -0.110 to -0.015 m | consistently signed but physically tiny |

The surface check supports the same hierarchy.  Relative to X5, X6 increased
the mean hourly station-median 2 m-temperature bias by 1.79 degrees C (block
interval +0.57 to +3.08 degrees C) and absolute temperature error by 1.41
degrees C (+0.64 to +2.17 degrees C).  Its 10 m-wind bias was 0.91 m s-1 larger
(+0.03 to +1.89 m s-1), although the absolute-wind-error interval crossed zero.
X3-minus-X5 surface differences were very small; the T2-bias interval spanned
zero and the wind-bias difference was -0.038 m s-1.

The resulting figure is
`verification/figures/candidates/wrf_retention_ventilation_d02_14to18.{png,pdf}`.
It was inspected at full resolution and the PDF was promoted into `figures/`
with the observed evolution and bulk theta-contrast PDFs as the deliberately
small first-draft figure spine.

The exact wrapper is
`verification/slurm/run_retention_analysis.slurm`, generator commit `bc4fa96`.
Job `13893307` ran on `notch392` from 22:53:12 to 22:53:58 UTC and wrote the
review packet under
`/scratch/general/vast/u0737349/latex_jrl_retention_13893307/`.  `sacct` was
unavailable through `slurmdbd`, so completion was verified from the wrapper's
terminal `done_utc`, the complete output set, nonempty figure pairs, matching
generator/station/observation hashes, and the artifact SHA-256 manifest.

This closes the first-draft experiment choice.  X6/X5 is the primary result;
X3/X5 is a bounded secondary null.  No additional WRF treatment is needed
before drafting, and the present evidence does not establish multi-day
persistence or distinguish initial-state from lateral-boundary causation.

## Exact reproduction commands

The Python executable used below was:

```text
/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python
```

The real observation cache was regenerated with configured Synoptic archive
access (credential not printed or committed):

```bash
env PYTHONPATH=../brc-tools \
  /uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python \
  verification/scripts/case_study_2013_obs.py \
  --start '2013-01-31 00Z' --end '2013-02-04 00Z' \
  --out /scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet

/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python \
  verification/scripts/verify_pull.py \
  /scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet
```

Each d02 run was reduced on Slurm job `13886703` with this exact template,
instantiated using the ten archive paths and stable IDs in
`run-inventory.csv`:

```bash
/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python \
  verification/scripts/reduce_wrf_to_stations.py \
  --wrf-dir '<exact archive_path from run-inventory.csv>' \
  --glob 'wrfout_d02_*' \
  --run-label '<stable run_id without trailing _20130202>' \
  --out '/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/reduced_d02/wrf_<run-label>_per_station.csv'
```

The matched all-run score command was:

```bash
env PYTHONPATH=../brc-tools \
  /uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python \
  verification/scripts/verify_runs_feb0102.py \
  --wrf /scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/reduced_d02/wrf_*_per_station.csv \
  --obs /scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet \
  --min-time 2013-02-02T14:00 --max-time 2013-02-02T18:00 \
  --out-suffix _allx_14to18 \
  --out-dir /scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/scored
```

The two retained overlay commands were run on Slurm job `13888050`:

```bash
env PYTHONPATH=../brc-tools \
  /uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python \
  verification/scripts/plot_wrf_vs_obs_feb0102.py \
  --wrf verification/data/wrf_gfs_2way_d02_per_station.csv verification/data/wrf_nam_2way_d02_per_station.csv \
  --labels 'GFS two-way' 'NAM two-way' \
  --obs /scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet \
  --min-time 2013-02-02T14:00 --max-time 2013-02-02T18:00 \
  --out-suffix _gfs2way_vs_nam2way_d02_14to18 \
  --out-dir verification/figures/candidates

env PYTHONPATH=../brc-tools \
  /uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python \
  verification/scripts/plot_wrf_vs_obs_feb0102.py \
  --wrf verification/data/wrf_nam_1way_d02_per_station.csv verification/data/wrf_nam_2way_d02_per_station.csv \
  --labels 'NAM one-way' 'NAM two-way' \
  --obs /scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet \
  --min-time 2013-02-02T14:00 --max-time 2013-02-02T18:00 \
  --out-suffix _nam1way_vs_nam2way_d02_14to18 \
  --out-dir verification/figures/candidates
```

The locator command on the same job was:

```bash
/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python \
  verification/scripts/plot_wrf_transect_locator.py \
  --wrf-dir /uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s/full6h/run_20260708T021809Z \
  --d02-glob 'wrfout_d02_2013-02-02_12:00:00' \
  --d03-glob 'wrfout_d03_2013-02-02_12:00:00' \
  --out-dir verification/figures/candidates
```

The pressure-level command pattern below was run four times on job `13888846`.
For X6−X5, `A=X6`, `B=X5`, limits were 2 K/40 at 500 hPa and 3 K/40 at
700 hPa.  For X3−X5, `A=X3`, `B=X5`, the limit/quiver scale was 0.5 K/10
at both levels.  `--wind-key` was 1 m s⁻¹ for X6−X5 and 0.5 m s⁻¹ for X3−X5.

```bash
/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python \
  verification/scripts/plot_wrf_upper_air.py \
  --wrf-dir "$A" --diff-dir "$B" --glob 'wrfout_d02_2013-02-02_*' \
  --times 2013-02-02_14:00:00 2013-02-02_16:00:00 2013-02-02_18:00:00 \
  --levels "$LEVEL" --run-label "$LABEL" --display-label "$DISPLAY" \
  --diff-limit "$LIMIT" --wind-key "$WIND_KEY" --quiver-scale "$QUIVER_SCALE" \
  --mark-stations USU07 USU03 QRS KVEL \
  --out-dir verification/figures/candidates
```

The observation-only figures were regenerated from commit `041183f` on job
`13891235`:

```bash
/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python \
  verification/scripts/plot_obs_feb0102.py \
  --obs /scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet \
  --out-dir verification/figures/candidates
```

## Unresolved provenance and decisions needed

1. Recover or retransmit the out-of-band provenance tarball and verify its
   documented SHA-256 before using its raw remote listings.
2. Identify the exact code commits that generated the existing X0–X8 archive
   `full-figures/` directories.  Current checkout state is not a substitute.
3. Recover archived run/source summaries for X1, X2, and X9.
4. Reconcile X4's current `terrain5m` directory with the earlier
   `...oneway_hires_terrain` path recorded in its summary.
5. Recover X7's exact forcing manifest and decide whether archive figure counts
   should document 24 intervals or 25 boundary-inclusive WRF timestamps.
6. Register X9 in the authoritative case TOML and define X9−X0 before treating
   the clean fine-terrain feedback comparison as figure-complete.
7. Reconcile the precise staged artifact behind `trang_ref`; continue to call it
   SIP-era/context lineage, never the literal Tran et al. (2018) run.
8. Treat the completed two-hour block resampling as a descriptive sensitivity
   interval only; stronger inferential uncertainty would require a longer or
   replicated experiment.
9. Confirm observation archive metadata/licensing, station pressure/elevation
   handling, and whether an independent sounding or vertical profile can anchor
   inversion depth.
10. Restore/read the canonical `wrf-full-figures` skill or perform a documented
    canonical style review before promotion.

Questions for John are principally X4 naming, X1/X2/X9 source commits, X7
forcing/count semantics, X9 registration, and recovery of the provenance
tarball.  Questions for Michael are the observation archive/provenance record,
pressure/elevation treatment, uncertainty plan, and whether the pseudo-profile
figures should remain main-text candidates or move to the supplement.

## Checks and visual review

- `make smoke` passed after the analytical changes; all synthetic outputs were
  isolated under `/tmp`.
- The upper-air targeted smoke recovered the expected uniform 2 K synthetic
  difference after earth-relative rotation.
- The observation smoke now exercises all three obs-only figures and passed
  after the NumPy `trapezoid` compatibility repair.
- `python -m py_compile` passed for every modified Python script.
- `git diff --check` passed for each committed batch.
- Every retained PNG was inspected at full resolution; PDF counterparts were
  checked for successful generation.  Legacy manuscript candidates were
  inspected through family contact sheets, while archive PNGs were not opened.
- `make check` passed with the CHPC `texlive/20260330` module path.  The resulting
  two-page `main.pdf` was visually inspected; this branch does not insert any
  candidate figure into the manuscript.
