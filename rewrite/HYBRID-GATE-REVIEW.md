# Architecture C hybrid gate review

This is the writing-host decision record required by
`rewrite/HYBRID-ARCHITECTURE-HANDOFF.md`.
It records gate outcomes, not manuscript prose or figure promotion.
C1 and C2 remain the fixed anchors.

| Slot / analysis | Exact reader question and evidence scope | Numerical and visual finding | Claim / figure status | Decision, falsifier, and remaining gate | Disposition |
|---|---|---|---|---|---|
| Main C4 / ANA-16 | Do X6-X5 and X10-X3 show a weaker GFS cold pool after spin-up, and does GFS actually lose more heat deficit? Exact d02 files from 13--18 UTC; 14--18 UTC decision window; X3 static terrain; cell-area weighting; combined station/waypoint footprint; seven crest/footprint/boundary definitions. Command: `sbatch verification/slurm/run_heat_deficit_analysis.slurm`; final job 13934123; exact argv, 24 input hashes, environment, masks, and output hashes in `verification/provenance/heat-deficit-analysis.json`. | All 70 retained GFS-minus-NAM pair-hour/definition differences are negative, from -1.805 to -0.703 MJ m^-2. Primary 2200 m mean effects are -1.226 MJ m^-2 two-way and -1.253 MJ m^-2 one-way. From 14 to 18 UTC, GFS changes by +0.317/+0.297 MJ m^-2 and NAM by +0.145/+0.130 MJ m^-2, giving +0.171/+0.167 MJ m^-2 differences in change. Actual GFS loss passes 0/14 definitions. The inspected PNG and rendered PDF show both GFS curves below NAM but increasing after 14 UTC; both sensitivity envelopes remain below zero. | C26 confirmed. DATA27--DATA29 verified. `wrf_heat_deficit_d02_13to18` registered as diagnostic, visually inspected, not promoted. | **Fail.** The weaker-state test passes 14/14 pair-definitions, but the Main C4 falsifier requires actual negative GFS change and a more negative change than NAM under both feedback modes and all seven definitions; the stronger maintenance test passes 0/14. No maintenance-failure wording is allowed. | **Dropped from Main C4.** Retain the footprint-scoped weaker-state result as support for C2 or reviewer reserve; do not describe it as basin volume, failure to maintain, or persistence. |
| Main C3 / ANA-19 | Is the driving-state response coherent over the basin floor and shallow layer at matched 14/16/18 UTC times? | Not evaluated in this dispatch. | Existing artifacts remain diagnostic; no new claim or admission. | **Unresolved.** Next gate in the frozen order: verify common-AGL interpolation, masks, matched-time rule, pair sign, exact provenance, and consistency with C17/C26 before selection. | Pending main-or-drop decision. |
| Main C5 / ANA-17 | Does controlled terrain comparison CMP09 add a distinct rim/floor/tributary geometry result? | Not evaluated in this dispatch. | No claim or admitted figure. | **Unresolved.** Analyse CMP09 first; use CMP10/CMP11 only if X4 lineage closes. Omit if aggregate-only, redundant, or identity-gated. | Pending main-or-drop decision. |
| Main C6 / ANA-18 | Does CMP07 slope/shading or CMP08 PBL/surface-layer treatment add one coherent, nonredundant process result? | Not evaluated in this dispatch. | C19 remains provisional; no selected figure. | **Unresolved.** Screen both predeclared diagnostic sets before choosing at most one; appearance or aggregate bias cannot choose the slot. | Pending main, supplement, or drop decision. |
| Supplement C2 / ANA-20 | Is the small feedback response robust under fine terrain in CMP06? | Not evaluated in this dispatch. | CMP06 remains open; no manifest row. | **Unresolved.** Recompute the matched surface, common-AGL, and process metrics and compare honestly with the driving-state magnitude. | Pending compact supplement table/panel or drop decision. |

## C4 interpretation limits

- The footprint is the convex hull of the 11 registered reporting stations plus the
  configured basin waypoints, intersected with X3 terrain below the reference surface.
  It is an evaluation footprint, not a hydrologic basin boundary or observed basin volume.
- The 13 UTC value is trajectory context; the deterministic decision uses 14--18 UTC.
- The result does not separate initial from lateral-boundary contributions and does not
  establish inversion depth, export, residence time, or multi-day persistence.
- Main C4 remains empty after this failure.  No point-scale or visually suggestive
  substitute may fill it.
