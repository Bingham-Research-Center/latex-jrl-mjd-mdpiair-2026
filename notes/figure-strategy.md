# Defensive figure longlist and narrative options

This is a drafting aid, not another provenance manifest.
Use `verification/figures/manifest.csv` for tracked candidate status,
`figures/MANIFEST.md` for manuscript admission, and
`verification/figures/archive-inventory.md` for the external full-figure catalogue.

## Scope correction and freshness note — 13 July 2026

The four-run factorial and its two-figure experimental manuscript are a verified minimum,
not the chosen scope of the paper.
The active route is `rewrite/RESULTS-EXPANSION-HANDOFF.md`, which reopens X0--X10,
smaller findings, and a larger main/supplement figure architecture.
When availability statements below disagree with
`verification/figures/archive-inventory.md`, the archive inventory wins.

## Historical minimum-draft recommendation

The earlier bounded rewrite drafted around **Narrative A**, used **Narrative B** to explain
why the evaluated layer matters to air chemistry, and kept **Narrative C** in
Discussion/reviewer reserve.
The experimental manuscript uses L01 for observed context and L03 as the principal
result.
Hold L02 until CHPC regenerates it without the non-equivalent 8 K line and the horizontally
separated two-site proxy earns a distinct role.

That was a safe fallback, not a present instruction to add only L04.
The next session should evaluate terrain, slope/shading, PBL/surface-layer, heat-deficit,
spatial, and vertical figures before choosing the paper architecture.

| Choice | One-sentence thesis | Figure burden | Scope risk |
|---|---|---|---|
| **A — driving-state response** | The GFS--NAM meteorological separation recurs under both nest-feedback modes over the matched short window. | L01 and L03; optionally L04 | Low; verified minimum, not automatically the final paper. |
| **B — air-quality-ready meteorology** | Cold-pool depth and ventilation must be evaluated before chemical attribution, because surface agreement alone does not define the volume supplied to chemistry. | L01 and L03; optionally corrected L02 or L10 | Low to moderate; keep chemistry claims explicitly out of scope. |
| **C — sensitivity hierarchy** | Driving-state differences exceed the short-window feedback response, while terrain and PBL treatments remain bounded questions rather than rankings. | L03/L04 plus selected reserve panels | High; use mainly in Discussion. |

## What exists now

| Collection | Contents | What it is good for |
|---|---|---|
| Manuscript spine | Two promoted PDFs currently used by `main.tex`; one bulk-theta PDF withheld | A safe minimum story while CHPC regenerates the supporting surface-contrast panel. |
| Tracked candidate manifest | 13 logical figures with the current status recorded in both manifests | Provenance-complete alternatives and reviewer-reserve panels. |
| Standard external per-run sets | X0--X6, X9, and X10 each have 63 standard PNGs, plus optional `thetaz` and `heatdeficit_map` families | Selecting spatial, vertical, or mechanism examples for every controlled lever. |
| Other external cases | X7 has 216 standard-family PNGs; X8 has about 86 in a non-standard layout | Longer-run and fine-domain context; neither forms a controlled resolution ladder. |
| Cross-case external catalogue | 324 PNGs across ten difference pairs plus domain, profile, skew-T, heat-deficit, and heat-deficit-map families | Broad result discovery. The stale 21-file terrain-label duplicate set was removed on 12 July. |

Quicklooks are operational evidence, not manuscript figures.
An archive PNG is not eligible for the paper until it receives a row in
`verification/figures/manifest.csv`, a visual/provenance review, and promotion.

## Figure longlist

| ID | Figure or family | Availability | Question answered | Narrative fit | Rewrite decision |
|---|---|---|---|---|---|
| L01 | Observed floor-to-bench 2 m-temperature evolution | **Promoted** | Did a strong, spatially structured cold-air-pool event occur? | A, B | Keep as Figure 1. |
| L02 | Observed/model Mountain Home-minus-Pariette Draw bulk theta contrast | **Withheld pending line-free regeneration** | Does each forcing family reproduce the observed floor-to-bench thermal contrast? | A, B | Supporting only; it shows the two-way pair, is not a vertical profile, and must be regenerated without the non-equivalent 8 K line before re-promotion. |
| L03 | Four-run 50--500 m AGL stability, transport wind, and PBLH | **Promoted** | Does the GFS--NAM response persist under both feedback modes, and is feedback smaller? | A, B, C | Keep as the main Results figure. |
| L04 | Factorial effect-size summary for stability, transport wind, T2 error, and PBLH | **Not plotted; all inputs verified** in DATA17, DATA19, DATA24, and DATA26 | How large are the two forcing rows, two feedback columns, and their interaction on one comparable display? | A, C | Best optional new plot; no WRF required. |
| L05 | GFS-minus-NAM two-way 2 m-theta maps (`diff_gfs_nam`) | **21 external PNGs** | Where is the forcing response located under two-way feedback? | A, B | Select one hour only if spatial structure is discussed. |
| L06 | GFS-minus-NAM one-way 2 m-theta maps (`diff_gfs_nam_oneway`) | **21 external PNGs** | Does the spatial forcing response survive the feedback change? | A | Pair the same hour with L05; otherwise omit. |
| L07 | GFS-minus-NAM EW/NS theta sections under both feedback modes | **External and complete** | Is the forcing response shallow and basin-confined or distributed aloft? | A, B | Strong supplement/reviewer option; needs a focused two-panel selection. |
| L08 | NAM and GFS feedback difference maps/sections (`diff_feedback*`) | **21 PNGs per forcing family** | Is the feedback response visibly smaller and source conditioned? | A, C | Reserve unless a reviewer asks to see the bounded null. |
| L09 | WRF-versus-observation 2 m-temperature station overlays | **Provisional tracked candidates** | Which stations drive aggregate warm-bias differences? | A, B | Useful supplement; current draft can proceed without them. |
| L10 | d02/d03 terrain, station, and transect locator | **Diagnostic tracked candidate** | Why is d02 the common evaluation grid and what does d03 omit? | B, Methods | Promote if domain representativeness is confusing to coauthors/reviewers. |
| L11 | GFS-minus-NAM 500/700 hPa theta and wind differences | **Diagnostic tracked candidates** | Is the driving-state difference stronger in the lower troposphere than aloft? | A | Reviewer reserve; 700 hPa terrain masking prevents a simple causal claim. |
| L12 | Multi-run heat-deficit time series plus productized heat-deficit maps | **External existing family; maps rendered across all standard cases and ten pairs** | How does the modeled energy required to erase the cold pool evolve, and where? | B, C | High-value mechanism candidate; freeze the metric and verify the post-spin-up trajectory before promotion. |
| L13 | Horsepool theta profiles and model/RAOB skew-Ts | **External existing figures** | How different are the vertical driving states at initialization? | A, B | Context only: Horsepool is model-only and operational RAOBs are outside the basin. |
| L14 | X2-minus-X1 MYJ/Eta response (`diff_myj_eta`) | **21 external difference PNGs plus paired diagnostics** | How does PBL/surface-layer choice change low-level mixing and energy fields? | C | Provisional reviewer reserve; C19 and the PBL note block a simple skill verdict. |
| L15 | Fine/default/coarse terrain differences | **External figures complete; stale labels cleaned** | Does terrain-source choice materially change the solution on the same WRF grid? | C | Analyse as a candidate Result after resolving X4 provenance and defining terrain-aware diagnostics. |
| L16 | X9-minus-X0 fine-terrain feedback | **Complete 63-PNG X9 set plus 21 differences** | Is the small feedback result reproduced at the fine-terrain control? | C | Analysis-ready robustness result; needs a matched quantitative analysis and ledger row, not another WRF run. |
| L17 | X7/X0/X8 apparent resolution ladder | **Many figures exist** | Does nominal grid refinement improve the forecast? | None defensibly | Do not use as a sensitivity figure; CMP12 lists the confounds. |
| L18 | Observed station pseudo-profile/heat-deficit diagnostic | **Diagnostic/provisional tracked candidates** | How does apparent surface thermal structure span floor-to-bench sites? | B | Supplement only; it is not a colocated free-air profile. |

## Important holes

- There is no accepted in-basin observed free-air profile for the plotted event;
  surface pseudo-profiles cannot substitute for one.
- There is no controlled initialization-versus-lateral-boundary attribution.
  The safe wording is "driving-state response," not "initial-condition effect."
- There is no controlled resolution experiment; L17 cannot support a refinement story.
- X9 is rendered and its X9-minus-X0 pair is complete; it remains unanalysed for manuscript purposes.
- X8 remains non-standard and confounded as a resolution comparison.
- The full external catalogue records batch-level renderer/configuration state, not a
  generator sidecar for every PNG.
- There is no chemistry output in the promoted evidence.
  Figures can establish meteorological confinement and ventilation as a prerequisite,
  not prove an ozone or emissions mechanism.

## Earlier bounded narrative packages

These remain useful components, but they are not exhaustive alternatives after the
results-expansion decision.

### Narrative A — driving-state response robust to nest feedback (recommended)

**Argument:** Over the matched five-hour d02 sample, GFS produces a warmer, less stable,
more strongly ventilated cold-pool environment than NAM, and that separation appears
under both one-way and two-way nesting. Feedback is smaller and source conditioned.

- Minimum figures: L01 and L03.
- Optional supporting figure: corrected L02 only if the surface proxy adds a distinct decision.
- Best optional figure: L04.
- Spatial/mechanism supplement: one matched-hour pair from L05/L06 or L07.
- Defensive limits: five hours; no initial-versus-boundary attribution; no formal
  inference; no multi-day persistence claim.

### Narrative B — meteorological confinement supplied to an air-quality model

**Argument:** A credible chemistry simulation first requires a credible shallow,
weakly ventilated meteorological volume. The observed event and model comparisons show
that aggregate surface agreement alone is insufficient; stability and layer transport
must also be evaluated.

- Minimum figures: L01 and L03.
- Best optional figures: corrected L02 or L10; L12 requires a validated mechanism role, and L13 remains context only.
- Defensive limits: meteorology is necessary, not uniquely dominant; no promoted
  chemical concentrations, inventory test, photolysis test, or deposition test exists.

### Narrative C — a hierarchy of configuration sensitivities

**Argument:** In this archive the reconciled driving-state contrast is larger than the
short-window feedback response, while terrain, slope/shading, and PBL pairs identify
additional controlled questions rather than settled rankings.

- Minimum figures: L03 and ideally L04.
- Reviewer-reserve figures: L08, L14, and L15.
- Defensive limits: do not rank PBL or terrain configurations by skill yet; do not use
  the resolution ladder; several reserve comparisons still have named provenance or
  interpretation gates.
- Scope assessment: useful Discussion framing, but too broad for the experimental main
  Results narrative.

## Results-expansion order before more drafting

1. Use `rewrite/RESULTS-EXPANSION-HANDOFF.md` to classify every CMP01--CMP13 row by
   freshness, control, analysis, claim, and figure status.
2. Retain L01/L03 as the safe floor while evaluating spatial/vertical driving response,
   heat-deficit maintenance, terrain, slope/shading, and PBL/surface-layer threads.
3. Treat feedback as a bounded robustness result across default and fine terrain, not the
   organizing thesis.
4. Propose broad configuration, maintenance/mechanism, and hybrid main/supplement figure
   packages before adding manuscript prose.
5. Hold L02 until regeneration and a distinct role; keep L17 explicitly confounded.
6. Promote only the selected figures after their named quantitative and provenance gates.
