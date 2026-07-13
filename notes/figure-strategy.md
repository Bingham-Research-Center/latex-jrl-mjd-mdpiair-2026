# Defensive figure longlist and narrative options

This is a drafting aid, not another provenance manifest.
Use `verification/figures/manifest.csv` for tracked candidate status,
`figures/MANIFEST.md` for manuscript admission, and
`verification/figures/archive-inventory.md` for the external full-figure catalogue.

## Recommendation for the blank-slate rewrite

Draft around **Narrative A**, use **Narrative B** to explain why the evaluated layer
matters to air chemistry, and keep **Narrative C** in Discussion/reviewer reserve.
The experimental manuscript uses L01 for observed context and L03 as the principal
result.
Hold L02 until CHPC regenerates the corrected 8 K annotation and the horizontally
separated two-site proxy earns a distinct role.

If one new plot is justified after the prose is coherent, make L04 from the tracked
pair and interaction summaries.
It should replace or materially improve the factorial table rather than duplicate it.
No new WRF integration, X8/X9 cleanup, or broad supplemental suite is required for the
bounded rewrite.

| Choice | One-sentence thesis | Figure burden | Scope risk |
|---|---|---|---|
| **A — driving-state response** | The GFS--NAM meteorological separation recurs under both nest-feedback modes over the matched short window. | L01 and L03; optionally L04 | **Low; recommended.** |
| **B — air-quality-ready meteorology** | Cold-pool depth and ventilation must be evaluated before chemical attribution, because surface agreement alone does not define the volume supplied to chemistry. | L01 and L03; optionally corrected L02 or L10 | Low to moderate; keep chemistry claims explicitly out of scope. |
| **C — sensitivity hierarchy** | Driving-state differences exceed the short-window feedback response, while terrain and PBL treatments remain bounded questions rather than rankings. | L03/L04 plus selected reserve panels | High; use mainly in Discussion. |

## What exists now

| Collection | Contents | What it is good for |
|---|---|---|
| Manuscript spine | Three promoted PDFs already used by `main.tex` | A complete minimum story: observed event, bulk surface stability, and four-run retention/ventilation. |
| Tracked candidate manifest | 13 logical figures: 3 promoted, 4 provisional, 6 diagnostic | Provenance-complete alternatives and reviewer-reserve panels. |
| Standard external per-run sets | X0--X6 and X10 each have 63 PNGs: 14 sections, 35 surface panels, and 14 upper-air panels | Selecting spatial or vertical examples after the prose identifies a need. |
| Other external cases | X7 has 216; X8 has 86 non-standard; X9 has no full figures | Resolution context and an unrendered cleaner fine-terrain feedback pair; not first-draft requirements. |
| Cross-case external catalogue | 247 PNGs across forcing, feedback, terrain, PBL, profile, skew-T, heat-deficit, and domain families | Mechanism panels and reviewer reserve. The fine-terrain family has 42 rather than the expected 21 files; if the excess files prove stale, the deduplicated set would contain 226. |

Quicklooks are operational evidence, not manuscript figures.
An archive PNG is not eligible for the paper until it receives a row in
`verification/figures/manifest.csv`, a visual/provenance review, and promotion.

## Figure longlist

| ID | Figure or family | Availability | Question answered | Narrative fit | Rewrite decision |
|---|---|---|---|---|---|
| L01 | Observed floor-to-bench 2 m-temperature evolution | **Promoted** | Did a strong, spatially structured cold-air-pool event occur? | A, B | Keep as Figure 1. |
| L02 | Observed/model Mountain Home-minus-Pariette Draw bulk theta contrast | **Promoted but held from the experimental rewrite pending regeneration** | Does each forcing family reproduce the observed floor-to-bench thermal contrast? | A, B | Supporting only; it shows the two-way pair, is not a vertical profile, and needs the corrected 8 K annotation. |
| L03 | Four-run 50--500 m AGL stability, transport wind, and PBLH | **Promoted** | Does the GFS--NAM response persist under both feedback modes, and is feedback smaller? | A, B, C | Keep as the main Results figure. |
| L04 | Factorial effect-size summary for stability, transport wind, T2 error, and PBLH | **Not plotted; all inputs verified** in DATA17, DATA19, DATA24, and DATA26 | How large are the two forcing rows, two feedback columns, and their interaction on one comparable display? | A, C | Best optional new plot; no WRF required. |
| L05 | GFS-minus-NAM two-way 2 m-theta maps (`diff_gfs_nam`) | **21 external PNGs** | Where is the forcing response located under two-way feedback? | A, B | Select one hour only if spatial structure is discussed. |
| L06 | GFS-minus-NAM one-way 2 m-theta maps (`diff_gfs_nam_oneway`) | **21 external PNGs** | Does the spatial forcing response survive the feedback change? | A | Pair the same hour with L05; otherwise omit. |
| L07 | GFS-minus-NAM EW/NS theta sections under both feedback modes | **External and complete** | Is the forcing response shallow and basin-confined or distributed aloft? | A, B | Strong supplement/reviewer option; needs a focused two-panel selection. |
| L08 | NAM and GFS feedback difference maps/sections (`diff_feedback*`) | **21 PNGs per forcing family** | Is the feedback response visibly smaller and source conditioned? | A, C | Reserve unless a reviewer asks to see the bounded null. |
| L09 | WRF-versus-observation 2 m-temperature station overlays | **Provisional tracked candidates** | Which stations drive aggregate warm-bias differences? | A, B | Useful supplement; current draft can proceed without them. |
| L10 | d02/d03 terrain, station, and transect locator | **Diagnostic tracked candidate** | Why is d02 the common evaluation grid and what does d03 omit? | B, Methods | Promote if domain representativeness is confusing to coauthors/reviewers. |
| L11 | GFS-minus-NAM 500/700 hPa theta and wind differences | **Diagnostic tracked candidates** | Is the driving-state difference stronger in the lower troposphere than aloft? | A | Reviewer reserve; 700 hPa terrain masking prevents a simple causal claim. |
| L12 | Multi-run heat-deficit time series | **External existing figure** | How does the modeled energy required to erase the cold pool evolve? | B | Promising Air-oriented supplement; requires provenance/promotion before use. |
| L13 | Horsepool theta profiles and model/RAOB skew-Ts | **External existing figures** | How different are the vertical driving states at initialization? | A, B | Context only: Horsepool is model-only and operational RAOBs are outside the basin. |
| L14 | X2-minus-X1 MYJ/Eta response (`diff_myj_eta`) | **21 external difference PNGs plus paired diagnostics** | How does PBL/surface-layer choice change low-level mixing and energy fields? | C | Provisional reviewer reserve; C19 and the PBL note block a simple skill verdict. |
| L15 | Fine/default/coarse terrain differences | **External figures exist** | Does terrain-source choice materially change the solution on the same WRF grid? | C | Hold: X4 provenance and stale `30m`/`90m` labels need cleanup. |
| L16 | X9-minus-X0 fine-terrain feedback | **WRF complete; full figures missing** | Is the small feedback result reproduced at the fine-terrain control? | C | No need for the draft; plotting only, not a WRF rerun. |
| L17 | X7/X0/X8 apparent resolution ladder | **Many figures exist** | Does nominal grid refinement improve the forecast? | None defensibly | Do not use as a sensitivity figure; CMP12 lists the confounds. |
| L18 | Observed station pseudo-profile/heat-deficit diagnostic | **Diagnostic/provisional tracked candidates** | How does apparent surface thermal structure span floor-to-bench sites? | B | Supplement only; it is not a colocated free-air profile. |

## Important holes

- There is no accepted in-basin observed free-air profile for the plotted event;
  surface pseudo-profiles cannot substitute for one.
- There is no controlled initialization-versus-lateral-boundary attribution.
  The safe wording is "driving-state response," not "initial-condition effect."
- There is no controlled resolution experiment; L17 cannot support a refinement story.
- X9 is unrendered and X8 is non-standard, but neither blocks the frozen first draft.
- The full external catalogue records batch-level renderer/configuration state, not a
  generator sidecar for every PNG.
- There is no chemistry output in the promoted evidence.
  Figures can establish meteorological confinement and ventilation as a prerequisite,
  not prove an ozone or emissions mechanism.

## Three defensible narrative packages

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

## Blank-slate drafting order

1. Write the Results around CMP01--CMP05 with L03 as the only model-result figure.
2. Use L01 to establish observed surface context without claiming a vertical profile.
3. Use Narrative A as the Results structure and Narrative B as the Introduction/
   Discussion air-quality motivation.
4. Hold L02, and add L04 only if either supplies information not already carried by the
   effect table.
5. Mention Narrative C only as bounded future/reviewer reserve.
6. Treat every other longlist row as optional until a paragraph creates a specific need.
