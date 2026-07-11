# Pelican 2013 Tran-Inspired Physics Bridge

**Reviewer-reserve evidence, not part of the frozen first-draft Results.**
Migrated from `wrf-nudge-ozone-air2026` commit `caf5c69`.
Run identity is authoritative in `verification/provenance/run-inventory.csv`;
CMP07/CMP08 in `verification/provenance/comparison-inventory.csv` control its
manuscript role, and claim C19 records the unresolved PBL interpretation.

## Question And Null

How much does terrain-aware solar radiation change the accepted 333 m
terrain3s solution, and what additional change follows from replacing the
YSU/revised-MM5 PBL/surface-layer pair with MYJ/Eta?

Null hypothesis: neither incremental treatment produces a coherent or
meaningful change in radiation, surface energy partitioning, inversion
structure, PBLH, or near-surface flow over this six-hour window.

## Matched Design

All runs retain NAM analysis forcing, 2013-02-02 12-18 UTC, one-way 3/1/0.333
km nests, 75 eta levels, custom 3s HGT_M, Thompson microphysics, RRTMG
radiation, Noah LSM, no cumulus parameterization, no FDDA, and hourly output.

| Role | Case | Namelist delta | Status |
| --- | --- | --- | --- |
| Control | `pelican2013_nam_3_1_333m_75lev_oneway_terrain3s` | None | Complete, job `13852034` |
| Treatment 1 | `pelican2013_nam_3_1_333m_75lev_oneway_terrain3s_slope` | `slope_rad=1`, `topo_shading=1`, `shadlen=25000.` on all domains where applicable | Complete and reviewed **GO**: prep `13876527`, WRF `13876534`, quicklooks `13877355`, paired review `13877599` |
| Treatment 2 | `pelican2013_nam_3_1_333m_75lev_oneway_terrain3s_slope_myj` | Treatment 1 plus `bl_pbl_physics=2` and `sf_sfclay_physics=2` on all domains | Complete: prep `13879078`, WRF `13879100`, quicklooks `13879973`, paired diagnostic `13880122`, publication generation `13879669` |

The normalized packet diffs prove treatment 1 changes only its three declared
terrain-radiation settings. The incremental treatment-1-to-treatment-2 report
proves only the two PBL/surface-layer settings change at step two.

## Evidence And Gates

- Exact archive paths and configuration fingerprints:
  `verification/provenance/run-inventory.csv`.
- Runnable manifests and renderer: `../brc-wrf/brc-cases/`; the paper-specific
  figure TOMLs are under `verification/config/figures/`.
- Treatment 1 completed `real.exe`, `wrf.exe`, its 21-file archive, an empty
  WRF error-marker scan, and 54-product quicklook checks.
- Paired review artifact:
  `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s_slope/control/run_20260710T003606Z/review_control_vs_slope_13877599/`.
- Separate publication-figure job `13877404` timed out after `02:00:13` on
  `notch392`. It produced only 23 slope-case and 4 cross-case PNGs, stopped
  advancing at 21:32:32 MDT, and is not accepted as a complete figure set.
  Recovery job `13878948` passed the original stall but was cancelled after a
  second cumulative stall; isolated and bounded jobs `13878999`, `13879006`,
  and `13879007` then completed the missing slope/control figures. Final
  convergence job `13879016` completed `0:0` with all selected products up to
  date. The six completed cases now have 63 per-case PNGs each and the
  cross-case root has 156 PNGs, 534 total. Slope+MYJ/Eta was excluded because
  it was still unrun during that publication recovery; its later completion is
  recorded below. This figure-workflow recovery does not change the completed
  WRF, quicklook, or paired-review evidence above.
- Treatment 2 completed `real.exe`, `wrf.exe`, its 21-file archive, an empty
  WRF error-marker scan, and 54-product quicklook checks. WRF job `13879100`
  completed `0:0` in `01:41:53` (`wrf.exe` 6047 seconds); quicklooks
  `13879973` completed `0:0` in `00:01:15`.
- Continue to use `SWDOWN`, `GLW`, `HFX`, `LH`, T2/theta, PBLH, 10 m wind,
  and vertical theta structure for the slope-to-MYJ increment.

## Treatment-2 Paired Review Result

- Publication generator `13879669` completed `0:0` in `00:11:53` with 604
  tasks and no per-figure errors. Final convergence `13880154` completed `0:0`.
  The seven per-case roots contain 441 PNGs and the cross-case root contains
  184 PNGs, including 21 `MYJ-Eta-slope` differences (625 total).
- Focused diagnostic job `13880122` completed `0:0` in `00:00:40`. Its 189
  matched field/time/domain rows contain zero nonfinite values and its artifact
  includes 12 paired surface, time-series, vertical-section, and Horsepool
  profile figures plus continuity, threshold, and extreme-cell audits.
- D03 mean T2 changes at 16/17/18Z are `+0.040/+0.157/+0.307 K`; mean absolute
  differences stay near `0.40-0.45 K`, and no d03 cell exceeds `5 K`.
- D03 mean PBLH changes are `-33.3/-69.6/-74.8 m`, with mean absolute
  differences `43.0/74.8/80.2 m`. Cells exceeding `100 m` reach
  `10.1/29.2/27.0%`; most are more than ten cells from the boundary. MYJ PBLH
  is visibly and quantitatively patchier, an explicit interpretation caveat.
- D03 mean 10 m wind-speed changes are `-0.086/+0.095/+0.065 m s-1`; mean
  absolute differences decline from `0.38` to `0.29 m s-1` over 16-18Z.
- D03 mean SWDOWN changes grow from `+1.8` to `+26.5 W m-2` from 16-18Z;
  HFX and LH become more positive while GLW becomes more negative. These are
  organized interior responses, not the boundary-only tails seen in the
  slope-versus-control review.
- D03 three-dimensional theta mean differences remain about `-0.04` to
  `-0.05 K`, with mean absolute differences `0.083-0.091 K`. Sections and
  Horsepool profiles show most response below roughly 700 m AGL and profile
  differences below about `0.6 K`.
- Preliminary verdict: the MYJ/Eta increment is mechanically stable and
  produces a coherent, materially non-null low-level response. It is not a
  pathological collapse, but its patchier PBLH and large interior radiation/
  mixing response require human scientific interpretation before any longer
  experiment is considered.

For this manuscript, that verdict remains **provisional** rather than a claim
that MYJ is worse or that the response is uniformly small below 700 m AGL.
Common-AGL profiles and scheme-aware PBLH/TKE interpretation are the gate in C19.

## Treatment-1 Review Result

- Slope WRF job `13876534` completed `0:0` in `01:45:09`; `wrf.exe` took
  `6233` seconds and wrote 21 hourly files across d01-d03.
- Quicklook job `13877355` completed `0:0` in `00:01:26`; each domain has 10
  standard, 4 supplemental, and 4 surface-energy PNGs.
- Review job `13877599` completed `0:0` in `00:00:38`. Its 189 paired
  field/time/domain rows contain zero nonfinite values.
- D03 radiation and flux changes are terrain-local. At 16/17/18Z, only
  7/4/34 of 22,500 `SWDOWN` cells exceeded `|20 W m-2|`; darkest absolute
  cells were already present in the control.
- D03 T2/theta2 mean absolute differences stayed near `0.03-0.07 K`, PBLH at
  `1.36-1.77 m`, and 10 m wind at `0.017-0.023 m s-1` from 16-18Z.
- The roughly `-6 K` d03 T2 tail at 17-18Z is confined to the one-cell lateral
  boundary. It is retained as a caveat, along with parent-domain boundary
  PBLH/T2 tails, rather than interpreted as basin-interior response.
- D03 75-level theta mean absolute differences stayed at `0.0021-0.0048 K`;
  central sections were about `+/-0.04 K`, Horsepool profiles differed by less
  than about `0.02 K`, and no d03 value exceeded `1 K`.
- Recommendation was **GO** for treatment 2 because no missing/nonfinite field,
  suspicious interior discontinuity, or pathological thermal-column collapse
  was found. The user approved and the run completed. The paired suite is now
  complete; current stop is human science review and figure selection. No
  additional WRF treatment is authorized.

## Interpretation Boundary

This is a configuration-response bridge, not a reproduction of Tran et al.
(2018). The paper text does not state the slope/shading switches. This phase
also omits its observed/SNODAS snow replacement, 33-category land use,
modified vegetation/max-snow-albedo inputs, 12 km Kain-Fritsch outer domain,
multi-day spin-up, and all FDDA. A longer surface reconstruction is justified
only by a later coauthor decision or reviewer request; it is not required for
the frozen first draft.
