# Results architecture decision packet

**Prepared 13 July 2026 on the writing host.**

**Decision recorded 13 July 2026:** John selected Architecture C, the hybrid package.
Continue through `rewrite/HYBRID-ARCHITECTURE-HANDOFF.md` before either manuscript is
changed; Architectures A and B remain documented alternatives, not active choices.

The X6/X10/X5/X3 factorial remains the verified floor.
It is not the paper's scope, and nest feedback is a bounded robustness result rather than
the default thesis.
No manuscript prose or figure admission changes are made by this packet.

## Authority, paths, and status shorthand

Run identity follows `verification/provenance/run-inventory.csv`.
Comparison meaning and sign follow
`verification/provenance/comparison-inventory.csv`.
External figure existence follows `verification/figures/archive-inventory.md`.
Claim status follows `notes/claim-evidence-ledger.md` plus the exact artifacts below.

- `ARC` = `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive`
- `CMPFIG` = `ARC/pelican2013_pub_figures/compare`
- `ALLX` = `/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/scored/wrf_runs_scores_feb0102_allx_14to18.csv`, SHA-256 `e49e70556e8abfa34189c41ce21ffe7f998149c04bfd3a43d051d3b93f808162`
- `RET` = `verification/provenance/retention-analysis-13896641.json`
- `CORE4` = `verification/data/surface_skill_pair_summary.csv`,
  `verification/data/surface_skill_interaction_summary.csv`,
  `verification/data/retention_pair_summary.csv`, and
  `verification/data/retention_interaction_summary.csv`
- `P` = promoted in both figure manifests; `T` = tracked local candidate; `E` = external engine render only; `none` = no valid or admitted figure

External existence, local tracking, and manuscript admission are separate states.
At present only the three PDFs in `figures/MANIFEST.md` are admitted.

## Freshness-aware CMP01--CMP13 candidate-result ledger

| ID | Scientific question | Isolated lever or design class | Exact supporting artifact | Current visual lead | Quantitative analysis | Claim status | Figure status | Freshness conflict or caution | Next gate |
|---|---|---|---|---|---|---|---|---|---|
| CMP01 | Does the GFS-minus-NAM driving-state response appear with two-way feedback? | Driving-product bundle plus its expected 27-versus-40 metgrid-level count; matched default terrain and YSU/MM5 | `verification/data/surface_skill_pair_summary.csv`; `verification/data/retention_pair_summary.csv`; `RET`; `CMPFIG/diff_gfs_nam/` | GFS is warmer at the floor, less stable from 50--500 m AGL, and faster in the fixed layer; the 700 hPa diagnostic is more coherent than 500 hPa at 14/16 UTC | GFS-minus-NAM: T2 bias `+1.79 degrees C`, stability `-3.63 K`, transport wind `+0.79 m s-1`; stability/wind retain sign in 5/5 hours | **confirmed**, C04/C17/C20/C25 | `P`: four-run retention figure; `T/E`: surface, upper-air, map, and section diagnostics | Some older labels say “IC”; initial versus lateral-boundary contributions are unresolved | Core prose needs coauthor wording review only; a spatial/vertical main figure still needs matched-time selection, shallow/common-AGL support, manifest registration, and promotion |
| CMP02 | Does that response persist with one-way feedback? | Same driving-product bundle under matched one-way default-terrain configuration | `verification/data/surface_skill_pair_summary.csv`; `verification/data/retention_pair_summary.csv`; `RET`; `CMPFIG/diff_gfs_nam_oneway/` | The qualitative lower-layer separation repeats under one-way feedback | GFS-minus-NAM: T2 bias `+1.76 degrees C`, stability `-3.65 K`, transport wind `+0.99 m s-1`; stability/wind retain sign in 5/5 hours | **confirmed**, C04/C17/C20/C25 | `P`: four-run retention figure; `E`: 21 spatial/section differences; no dedicated promoted spatial figure | “IC effect” remains too causal; the product-level bundle is the estimand | Core prose needs coauthor review; any dedicated map/section needs local provenance, visual review, and promotion |
| CMP03 | How much does feedback change the NAM solution over the frozen window? | X3-minus-X5, one-way minus two-way; feedback only at default terrain | `verification/data/surface_skill_pair_summary.csv` row `nam1_minus_nam2`; `verification/data/retention_pair_summary.csv`; `RET`; `CMPFIG/diff_feedback/` | Surface lines nearly overlap; basin-interior upper-air response is near zero, with stronger colors near terrain/mask edges | One-minus-two: T2 bias `-0.012 degrees C`, stability `+0.002 K`, transport wind `+0.006 m s-1`, PBLH `-0.056 m` | **confirmed near-null**, C18/C25 | `P`: included in four-run retention figure; `T/E`: dedicated diagnostics, none promoted | The engine directory renders **X5-minus-X3** (two-way minus one-way), the reverse of CMP03; never transfer its sign silently | Keep as a bounded five-hour result; a dedicated panel must use the authoritative sign and pass promotion |
| CMP04 | How much does feedback change the GFS solution over the frozen window? | X10-minus-X6, one-way minus two-way; feedback only at default terrain | `verification/data/surface_skill_pair_summary.csv`; `verification/data/retention_pair_summary.csv`; `RET`; `CMPFIG/diff_feedback_gfs/` | Small but more coherent than the NAM response; still much smaller than either driving-state contrast | One-minus-two: T2 bias `+0.065 degrees C`, stability `-0.066 K`, transport wind `+0.104 m s-1`, PBLH `+1.58 m` | **confirmed small response**, C18/C25 | `P`: included in four-run retention figure; `E`: 21 differences, none separately promoted | The engine directory renders **X6-minus-X10** (two-way minus one-way), the reverse of CMP04 | Retain as the source-conditioned companion to CMP03; promote a dedicated panel only if it adds a distinct decision |
| CMP05 | Is the feedback response source conditioned? | Paired interaction `(X10-X6)-(X3-X5)` | `verification/data/surface_skill_interaction_summary.csv`; `verification/data/retention_interaction_summary.csv`; `RET` | Source conditioning is visible in the four-run trajectories, but no dedicated effect display exists | Interaction: T2 bias `+0.041 degrees C`, stability `-0.103 K`, transport wind `+0.097 m s-1`, PBLH `+0.421 m` | **confirmed small interaction**, C18/C25 | `P`: underlying four-run figure; L04 effect-size panel not yet plotted | `rewrite/blueprint.md` had CMP03/CMP04 swapped; corrected in this pass | Use a table unless L04 earns a separate reader decision; any interval remains descriptive, not inferential |
| CMP06 | Does the small feedback result survive at the fine-terrain control? | X9-minus-X0; feedback only under NAM, fine static terrain, and YSU/MM5 | X9 run row; `CMPFIG/diff_feedback_terrain3s/` (21); `CMPFIG/heatdeficit_map/heatdeficit_2way-1way-terrain3s_{12..18}z.png`; `ALLX` | The diagnostic heat-deficit display uses a tight `+/-0.2 MJ m-2` scale and appears speckled over the floor; exploratory X9/X0 aggregate scores are close | `ALLX` gives X9/X0 T2 bias `0.819/0.824 degrees C`, wind bias `0.488/0.489 m s-1`, and bulk contrast `16.707/16.998 K`; these are unpaired exploratory means, not a CMP06 estimate | **design confirmed, result open**; C12 only | `E`: X9 standard 63, three `thetaz`, seven heat-deficit fields, and 21 pair differences; no manifest row or promoted figure | July 10 “no X9 full set” and “X9 next to render” statements were stale and are corrected; rendering did not create a claim | Recompute matched surface/common-AGL/process summaries on a frozen sample/window; add a ledger row; then register and promote a selected figure |
| CMP07 | Do slope-aware radiation and shading change the local fine-terrain solution? | X1-minus-X0; `slope_rad`, `topo_shading`, and `shadlen` only | X0/X1 run rows; `CMPFIG/diff_slope_shading/` (7); matching `heatdeficit_map` fields; `ALLX` | Aggregate scores are close, so a local treatment may be hidden by station means; no local radiation verdict exists | `ALLX` gives X1/X0 T2 bias `0.849/0.824 degrees C`, wind bias `0.491/0.489 m s-1`, and bulk contrast `17.177/16.998 K`; diagnostic only | **design confirmed, result open**; C12 only | `E`: complete per-run sets, seven surface differences, and seven heat-deficit differences; no manifest row | No coverage conflict; the unresolved source-code commit remains a provenance gate | Analyse `SWDOWN`, `GLW`, `TSK`, near-surface temperature/stability, slope/aspect, and time evolution; recover source commit; add claim and figure rows |
| CMP08 | How does MYJ/Eta versus YSU/MM5 change stable-layer and mixing structure? | X2-minus-X1; PBL and surface-layer scheme IDs only | X1/X2 run rows; `CMPFIG/diff_myj_eta/` (21); matching heat-deficit maps; `ALLX`; C19 | Engine notes report a coherent low-level response; the simple bulk contrast is larger under X2 | `ALLX` gives X2/X1 T2 bias `1.299/0.849 degrees C`, wind bias `0.411/0.491 m s-1`, and bulk contrast `18.490/17.177 K`; no scheme-aware common-AGL result | **provisional negative claim**, C19: a uniformly small response is not established | `E`: 21 surface/section differences plus heat-deficit maps; no manifest row | The inherited “small below 700 m” and prototype “physics null” readings are not supported | Recompute common-AGL theta/temperature/wind and fluxes; treat PBLH as scheme dependent and X2-only `TKE_PBL` as one-sided evidence; recover source commit; ledger and promote |
| CMP09 | Does default versus fine terrain alter the solution on the same WRF grid? | X3-minus-X0; WPS/static terrain source, identical WRF namelist | X0/X3 run rows; `CMPFIG/diff_terrain_fine/` (21); matching heat-deficit maps; `ALLX` | The family is spatially and vertically suggestive, but no inspected, frozen CMP09 process result is recorded | `ALLX` gives X3/X0 T2 bias `0.840/0.824 degrees C` and bulk contrast `17.004/16.998 K`; aggregate similarity does not test rim/floor geometry | **design confirmed, result open**; C12 only | `E`: 21 current differences plus heat-deficit maps; no manifest row | The old 42-file count included 21 stale `terrain-900m-30m` duplicates; now 21. Approximate source labels are not model-grid spacing | Define rim/floor/tributary and station-elevation diagnostics on a common window; quantify rather than infer from labels; ledger and promote |
| CMP10 | How different is default terrain from the deliberately coarse source? | X3-minus-X4; WPS/static terrain source, identical WRF namelist | X3/X4 run rows; `CMPFIG/diff_terrain/` (7); matching heat-deficit maps; `ALLX` | X4's near-zero mean pressure bias coincides with large terrain displacement at some sites and is not a skill result | `ALLX` gives X3/X4 T2 bias `0.840/0.595 degrees C`, wind bias `0.503/0.846 m s-1`, PSFC bias `-230.5/+0.5 Pa`, and bulk contrast `17.004/16.741 K`; exploratory only | **design confirmed with provenance caveat, result open**; C12 only | `E`: seven surface differences plus heat-deficit maps; no manifest row | X4's current `terrain5m` directory conflicts with the earlier `...oneway_hires_terrain` summary path; pressure is terrain sensitive | Resolve X4 lineage; pair elevation mismatch with geometry, energy, and stability diagnostics; ledger and promote |
| CMP11 | What changes across the widest fine-versus-coarse terrain-source bracket? | X0-minus-X4; WPS/static terrain source on the same NAM one-way YSU configuration | X0/X4 run rows; `CMPFIG/diff_terrain_res/` (21); `CMPFIG/heatdeficit_map/heatdeficit_terrain-3arcsec-5arcmin_{12..18}z.png`; local prototype `verification/figures/candidates/mechanism-decomposition/fig_heatdeficit_map_16z.png` | The inspected prototype suggests the strongest structure lies on rims, slopes, and tributaries rather than as a uniform floor offset | `ALLX` gives X0/X4 T2 bias `0.824/0.595 degrees C`, wind bias `0.489/0.846 m s-1`, and bulk contrast `16.998/16.741 K`; no matched terrain-capacity estimate | **design confirmed with provenance caveat, result open**; C12 only | `E` plus an unregistered local prototype; nothing admitted | The heat-deficit map is now productized, but the local triptych's capacity/geometry interpretation and X4 lineage remain gated | Resolve X4; freeze geometry and heat-deficit definitions and sensitivity; reproduce the lead over the post-spin-up trajectory; ledger, register, and promote |
| CMP12 | Does X7/X0/X8 establish a grid-resolution response? | Nominal spacing only; **not controlled** across initialization, age, domains, feedback, terrain placement, levels, radiation, and cadence | CMP12 row; X7/X0/X8 run rows; `verification/figures/evidence-longlist.md` confound table | A visual ladder would be tempting, but it would encode a false sensitivity; X8's exploratory score is from d02, not its 111 m d04 | No valid difference. `ALLX` complete-configuration scores cannot be attributed to resolution | **confirmed negative design finding**, C16 | `none` for sensitivity; domain/configuration context only | “1 km/333 m/111 m ladder” is shorthand for three heterogeneous configurations, not an experiment | Keep as confound table or design limitation; a result requires a new matched experiment |
| CMP13 | Can legacy nudged or SIP-era runs provide controlled historical comparison? | Heterogeneous identity/episode/WRF/FDDA context; **not controlled** | `verification/provenance/WRF-RUN-TO-REPORT-MAP.md`; `verification/docs/baseline-eval-2013.md`; context rows in `verification/figures/manifest.csv` | Existing cross-sections, time-heights, and January skill panels are useful only as lineage/design context | C08's roughly `6.8 degrees C` heterogeneous spread is provisional; Tran's published `5.5 degrees C` range is separate context and not comparable | **context/contradicted/open**, C05--C09 | `T` context rows only; none promoted | `trang_ref` is not the literal Tran et al. run; January is a different episode and production identities remain unresolved | Use only in Discussion after identity/window checks; a nudging result needs a same-case pair and independent or held-out observations |

## Small findings retained from the audit

These are paragraph-sized leads, not a list to paste into prose.

| Finding | Status now | Value to the paper | Gate or wording limit |
|---|---|---|---|
| Four elevation-spanning stations separate repeatedly from 31 January through 3 February | confirmed, C23 | Places the five modeled hours inside an evolving surface event | Provider QC, sensor metadata, licensing; no inversion-depth or basin-volume wording |
| d03 excludes most bench/end stations whereas d02 contains the full frozen sample | confirmed, C03 | Explains the evaluation/chemistry-grid choice | Promote the locator only if it clarifies Methods |
| Default-d02 nearest-cell elevation mismatch is median `-2.0 m`, range `-32.4` to `+14.3 m` across 11 columns | confirmed, C24 | Shows gross station displacement is not driving the four-run anchor | Do not generalize the fixed columns to basin area |
| GFS-minus-NAM T2, stability, and transport-wind signs repeat under both feedback modes | confirmed, C04/C17/C25 | Strongest headline result and architecture anchor | Five hours; product bundle only; transport wind is not export or residence time |
| Native PBLH does not reproduce the driving-state separation | confirmed, C20 | Rules out a simplistic PBLH explanation | Keep PBLH scheme dependent |
| The 700 hPa difference is more coherent at 14/16 UTC than the mixed 500 hPa response | diagnostic | Potential lower-tropospheric context | Complete five-hour/profile support and preserve the terrain mask |
| X1 and X0 have very close aggregate surface metrics | diagnostic | Warns that a local radiation response can disappear in bulk skill | Analyse radiation and slope/aspect before calling CMP07 null |
| X2's bulk contrast is `18.490 K` versus `17.177 K` for X1 | provisional, C19 | Makes CMP08 a real process candidate rather than automatic reserve | Common-AGL, flux, PBLH, and TKE-aware analysis |
| X4's near-zero mean pressure bias accompanies terrain displacement | diagnostic | Demonstrates why terrain geometry and pressure skill must be separated | Resolve X4 and quantify elevation adjustment |
| The productized 16 UTC heat-deficit lead is spatially coherent for GFS-minus-NAM | diagnostic | Candidate bridge from static warm bias to maintenance failure | Freeze definition and verify the full post-spin-up trajectory |
| X9-minus-X0 render coverage is complete and visually small on the basin floor | analysis-ready | Tests feedback robustness under a second terrain regime | Recompute the matched summaries and add a result claim |
| The apparent resolution sequence is confounded | confirmed, C16 | Useful negative design result | Confound table only, never a sensitivity curve |

## Architecture comparison

| Architecture | One-sentence thesis | Current readiness | Choose it if | Principal risk |
|---|---|---|---|---|
| **A. Broad configuration** | Several controlled configuration choices alter different parts of the short-window cold-pool state, with the driving-state response the confirmed anchor rather than a universal winner. | Design-ready, result-incomplete: CMP01--CMP05 confirmed; CMP06--CMP11 still need targeted analyses | At least two of terrain, radiation, and PBL/surface-layer analyses yield coherent, distinct findings; X4 must close if coarse terrain is retained | Can become a catalogue of knobs or imply a skill ranking without process evidence |
| **B. Maintenance/mechanism** | The main scientific distinction is whether the modeled pool is maintained after spin-up, where driving state, terrain geometry, and feedback act on different spatial/process components. | High-payoff hypothesis, not yet claim-ready: the central heat-deficit trajectory is still diagnostic | The productized post-spin-up heat-deficit trajectory survives definition/mask sensitivity and agrees with common-AGL and spatial/vertical diagnostics | A compelling 16 UTC map or Horsepool prototype may be mistaken for a basin-wide, time-resolved mechanism |
| **C. Hybrid** | Lead with the confirmed driving-state response and validated maintenance mechanism, then use only the strongest one or two controlled configuration pairs to explain or bound it. | Best-balanced conditional target; it preserves the verified floor while allowing evidence-earned breadth | Heat deficit passes its gate and at least one terrain/radiation/PBL result adds a distinct decision | Requires disciplined curation so “hybrid” does not quietly become the broad package |

## A. Broad-configuration figure package

**Editorial job:** give each controlled lever one defensible process question without
ranking configurations by a single skill score.

| Tier | Figure and exact reader decision | Supporting artifact | Remaining gate |
|---|---|---|---|
| Main A1 | **Observed evolution:** did the modeled window occur within a strong, spatially structured surface event? | `figures/obs_temp_timeseries_feb0102.pdf` | Already promoted; close observation provider/QC/sensor/licensing metadata |
| Main A2 | **Sampling geometry:** why is d02 the common evaluation grid, and which bench/end stations does d03 omit? | `verification/figures/candidates/wrf_transect_locator_d02_d03.pdf` | Provisional style; decide Methods need; register/promote if selected |
| Main A3 | **Confirmed anchor:** does the GFS-minus-NAM lower-layer response repeat under both feedback modes? | `figures/wrf_retention_ventilation_d02_14to18.pdf`; `CORE4` | Already promoted; coauthor wording review and five-hour limits |
| Main A4 | **Spatial/vertical driving response:** is the confirmed response basin-floor/shallow rather than another aggregate score? | `CMPFIG/diff_gfs_nam/theta2m_GFS-NAM_16z.png`; `CMPFIG/diff_gfs_nam/section_{ew,ns}_GFS-NAM_16z.png`; `verification/figures/candidates/wrf_xsect_theta_gfs_minus_nam2way_d02.png` | Select post-spin-up hour without outcome shopping; add shallow/common-AGL support; pin generator/input provenance; register/promote |
| Main A5 | **Terrain geometry:** do fine/default/coarse static sources change rim, tributary, and floor structure on the same WRF grid? | `CMPFIG/diff_terrain_fine/`; `CMPFIG/diff_terrain/`; `CMPFIG/diff_terrain_res/`; `CMPFIG/heatdeficit_map/heatdeficit_terrain-3arcsec-5arcmin_16z.png` | Resolve X4 if coarse terrain is retained; freeze rim/floor/elevation diagnostics; quantify selected CMP09--CMP11 rows; ledger and promote |
| Main A6 | **Slope/shading process:** is a small aggregate CMP07 response locally coherent in radiation and surface energy? | `CMPFIG/diff_slope_shading/`; X0/X1 `SWDOWN`, `GLW`, `TSK`, flux, theta, and wind fields at run-inventory paths | Recover source commit; analyse by slope/aspect and time; create a decision-grade multipanel; ledger and promote |
| Main A7 | **PBL/surface-layer process:** does CMP08 alter common-AGL stability, mixing, and flux evolution after scheme-aware interpretation? | `CMPFIG/diff_myj_eta/`; X1/X2 common fields and X2-only `TKE_PBL` at run-inventory paths | Common-AGL and flux analysis; no raw PBLH contest or missing-TKE-as-zero; recover source commit; ledger and promote |
| Supplement A1 | **Feedback robustness:** are small default-terrain effects reproduced at fine terrain? | `CORE4`; `CMPFIG/diff_feedback_terrain3s/`; `CMPFIG/heatdeficit_map/heatdeficit_2way-1way-terrain3s_{12..18}z.png` | Complete CMP06 analysis and sign-safe CMP03/CMP04 display; plot L04 only if it adds beyond a table |
| Supplement A2 | **Station and synoptic detail:** which stations and lower-tropospheric levels contribute to the anchor? | `verification/figures/candidates/wrf_temp_timeseries_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf`; `verification/figures/candidates/wrf_upper_{500,700}hPa_gfs_minus_nam2way_d02.pdf` | Observation metadata; complete pressure/profile interpretation; promote selected panels only |
| Supplement A3 | **Full process families:** do extra hours, sections, and profiles support each selected small result? | Exact controlled-pair directories under `CMPFIG`; per-run `thetaz` and `heatdeficit_map` directories in `archive-inventory.md` | Use only the families attached to selected ledger claims; no image dump |
| Reserve A1 | **Resolution-design limitation:** why can X7/X0/X8 not support a resolution curve? | CMP12 and run-inventory confound rows; domain locator | Label as a confound table or complete-configuration context, never a difference result |
| Reserve A2 | **Legacy/nudging context:** what design requirements follow from unresolved prior lineages? | `verification/figures/candidates/wrf_*trang*`; `verification/figures/candidates/baseline_*`; provenance map | Resolve identity/window; Discussion only; held-out observations required for a nudging claim |

## B. Cold-pool maintenance/mechanism figure package

**Editorial job:** replace a static warm-bias story only if time-resolved, spatially
integrated maintenance evidence survives its definition checks.

| Tier | Figure and exact reader decision | Supporting artifact | Remaining gate |
|---|---|---|---|
| Main B1 | **Observed evolution:** was the short forecast embedded in an evolving floor-to-bench surface event? | `figures/obs_temp_timeseries_feb0102.pdf` | Already promoted; observation metadata and wording limits |
| Main B2 | **Sampling geometry:** does the evaluation grid contain the stations and basin transects used to diagnose maintenance? | `verification/figures/candidates/wrf_transect_locator_d02_d03.pdf` | Promote only if it clarifies the spatial estimand |
| Main B3 | **Lower-layer state:** do the four runs retain different 50--500 m stability and fixed-layer wind states after spin-up? | `figures/wrf_retention_ventilation_d02_14to18.pdf` | Already promoted; no export/residence-time wording |
| Main B4 | **Spatial and vertical confinement:** where is the GFS-minus-NAM difference, and is it shallow enough to matter to the chemistry-input layer? | `CMPFIG/diff_gfs_nam/theta2m_GFS-NAM_16z.png`; `CMPFIG/diff_gfs_nam/section_{ew,ns}_GFS-NAM_16z.png`; `verification/figures/candidates/wrf_xsect_theta_gfs_minus_nam2way_d02.png` | Matched hour plus five-hour/profile support; shallow/common-AGL presentation; provenance and promotion |
| Main B5 | **Maintenance test:** does the GFS-driven state start with a pool but lose heat deficit faster after spin-up than NAM under both feedback modes? | `CMPFIG/heatdeficit/heat_deficit_timeseries.png`; `CMPFIG/heatdeficit_map/heatdeficit_GFS-NAM_{14,16,18}z.png`; `ARC/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s/full6h/run_20260708T021809Z/full-figures/heatdeficit_map/heatdeficit_nam_terrain3s_{14,16,18}z.png`; corresponding X5/X6/X10 fields from the run paths in the inventory | Highest-priority gate: freeze basin/crest, units, masks, common domain, 13--18 UTC trajectory, spatial summary, and reasonable-definition sensitivity; reconcile prototype Horsepool values; ledger and promote |
| Main B6 | **Mechanism decomposition:** are terrain effects concentrated on geometry/rims while feedback remains a smaller robustness term on the floor? | `CMPFIG/heatdeficit_map/heatdeficit_terrain-3arcsec-5arcmin_16z.png`; `CMPFIG/heatdeficit_map/heatdeficit_2way-1way-terrain3s_16z.png`; local triptych | Resolve X4 and analyse CMP06/CMP11; do not call speckle noise or capacity geometry-locked without quantitative sensitivity; register/promote |
| Supplement B1 | **Lower-tropospheric context:** is the driving-state difference more coherent at 700 than 500 hPa? | `verification/figures/candidates/wrf_upper_500hPa_gfs_minus_nam2way_d02.pdf`; `verification/figures/candidates/wrf_upper_700hPa_gfs_minus_nam2way_d02.pdf` | Complete profile/terrain-mask interpretation and full-window support |
| Supplement B2 | **Alternative process explanations:** can PBL/surface-layer or slope/shading treatment reproduce or modify the maintenance lead? | `CMPFIG/diff_myj_eta/`; `CMPFIG/diff_slope_shading/`; their files under `CMPFIG/heatdeficit_map/` | Complete CMP07/CMP08 process analyses; use as falsifiers/bounds, not a configuration ranking |
| Supplement B3 | **Feedback detail:** does the bounded result hold by forcing product and terrain regime? | `CORE4`; `CMPFIG/diff_feedback/`; `CMPFIG/diff_feedback_gfs/`; `CMPFIG/diff_feedback_terrain3s/`; fine-terrain heat-deficit maps | Analyse CMP06; preserve pair signs; promote only one compact display |
| Reserve B1 | **Phase portrait and reservoir anatomy:** do basin-mean strength/erosion and threshold sensitivity support the proposed mechanism? | `verification/figures/candidates/mechanism-decomposition/fig_phase_portrait.png`; `verification/figures/candidates/mechanism-decomposition/fig_reservoir_anatomy.png` | Single-point and threshold-sensitive prototypes; productize and test before any evidentiary use |
| Reserve B2 | **Confounded/legacy context:** what experiments are still needed? | CMP12/CMP13 artifacts | Design limitation only |

## C. Hybrid figure package

**Editorial job:** keep the confirmed anchor, earn one mechanism figure, and promote only
the strongest controlled configuration result that explains or bounds it.

| Tier | Figure and exact reader decision | Supporting artifact | Remaining gate |
|---|---|---|---|
| Main C1 | **Observed event:** did the model window occur during a spatially structured winter cold-pool episode? | `figures/obs_temp_timeseries_feb0102.pdf` | Already promoted; observation metadata |
| Main C2 | **Confirmed response:** does the lower-layer GFS-minus-NAM separation repeat under both feedback modes? | `figures/wrf_retention_ventilation_d02_14to18.pdf` | Already promoted; coauthor wording and short-window limits |
| Main C3 | **Where/height:** is that response a coherent basin-floor, shallow-layer feature? | `CMPFIG/diff_gfs_nam/theta2m_GFS-NAM_16z.png`; `CMPFIG/diff_gfs_nam/section_{ew,ns}_GFS-NAM_16z.png`; `verification/figures/candidates/wrf_xsect_theta_gfs_minus_nam2way_d02.png` | Matched selection, common-AGL/profile support, exact provenance, promotion |
| Main C4 | **Maintenance:** does a validated post-spin-up heat-deficit trajectory turn the static response into a maintenance result? | `CMPFIG/heatdeficit/heat_deficit_timeseries.png`; `CMPFIG/heatdeficit_map/heatdeficit_GFS-NAM_{14,16,18}z.png` | Complete ANA-16 definition/mask/trajectory/sensitivity gate and add a confirmed claim |
| Main C5 | **Selected structural modifier:** does the strongest verified terrain comparison explain a rim/floor geometry response distinct from driving state? | `CMPFIG/diff_terrain_fine/`; `CMPFIG/diff_terrain/`; `CMPFIG/diff_terrain_res/`; corresponding files under `CMPFIG/heatdeficit_map/` | Resolve X4 if CMP10/CMP11 is selected and run terrain-aware analysis; omit this slot if no distinct result survives |
| Main C6 | **Selected process modifier:** does either CMP07 or CMP08 add one distinct local-energy or mixing decision? | `CMPFIG/diff_slope_shading/` or `CMPFIG/diff_myj_eta/`, chosen after analysis; corresponding heat-deficit maps | Complete both targeted screens before choosing; promote one, not both, unless both answer nonredundant questions |
| Supplement C1 | **Sampling geometry:** why d02 and which sites/lines define the analysis? | Tracked locator PDF | Promote if Methods needs it |
| Supplement C2 | **Feedback robustness:** are default/fine feedback effects bounded relative to the driver response? | `CORE4`; `CMPFIG/diff_feedback/`; `CMPFIG/diff_feedback_gfs/`; `CMPFIG/diff_feedback_terrain3s/`; fine-terrain heat-deficit fields | Complete CMP06; use a table or one compact panel |
| Supplement C3 | **Station and upper-air support:** which sites and levels support or limit the main interpretation? | `verification/figures/candidates/wrf_temp_timeseries_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf`; tracked 500/700 hPa GFS-minus-NAM PDFs | Metadata/profile/terrain-mask gates; selected promotion only |
| Supplement C4 | **Unselected controlled process:** what small/null result bounds the chosen C6 mechanism? | The unused `CMPFIG/diff_slope_shading/` or `CMPFIG/diff_myj_eta/` family plus its completed analysis outputs | Keep reproducible and explicit; no main-text promotion unless it adds a new decision |
| Reserve C1 | **Threshold/single-point mechanism prototypes** | Local phase portrait and reservoir anatomy | Not evidence until productized and sensitivity tested |
| Reserve C2 | **Resolution and legacy design limits** | CMP12/CMP13 artifacts | Context only |

## Evidence-based recommendation and fallback rules

**Selected architecture: Architecture C, hybrid.**
It best preserves the confirmed driving-state anchor while allowing the paper to become
scientifically broader only where targeted analysis earns the breadth.
It also keeps feedback in its proper role and avoids requiring every available knob to
produce a positive result.

The recommendation is conditional:

1. If the productized heat-deficit trajectory fails its definition, mask, or
   post-spin-up checks, drop Main C4 and do not use a maintenance-failure thesis.
2. If X4 provenance cannot be resolved, exclude coarse-terrain claims and use CMP09 only,
   or omit Main C5.
3. Promote Main C6 only if CMP07 or CMP08 produces a coherent process result on the
   predeclared diagnostics; a well-bounded null belongs in the supplement.
4. If none of CMP06--CMP11 closes its claim gate, retain the current minimum scaffold
   rather than manufacturing breadth.

Architecture A is preferable if the editorial aim is explicitly a configuration audit and
at least two non-feedback process threads survive.
Architecture B is preferable if the maintenance trajectory survives strongly enough to
carry the thesis without terrain/PBL/radiation breadth.

All CHPC-only analysis and rendering should be issued through
`rewrite/CHPC-CODEX-PROMPT.md` in the order set by
`rewrite/HYBRID-ARCHITECTURE-HANDOFF.md`.

## Stale-note reconciliation completed with this packet

| File | Correction |
|---|---|
| `verification/figures/chpc-figure-inventory-2026-07-10.md` | Replaced repeated X9-gap rows, the 42-file terrain over-count, incomplete comparison counts, and obsolete X9 rendering tasks with current coverage while retaining the unmatched-analysis gate |
| `verification/figures/gfs-feedback-factorial-2026-07-10.md` | Marked 247 PNGs as the 10 July checkpoint and recorded the current 324-PNG compare root |
| `verification/figures/candidates/mechanism-decomposition/NARRATIVE.md` | Recorded `heatdeficit_map` productization, kept phase/reservoir prototypes gated, and converted overstrong “IC/terrain/physics decomposition” language into hypotheses to test |
| `rewrite/blueprint.md` | Corrected the swapped CMP03/CMP04 IDs without changing the four-run evidence |
| `verification/figures/evidence-longlist.md` | Replaced causal “Driving IC” labels with the supported driving-state wording |

The archive inventory remains the sole authority for current external coverage.
