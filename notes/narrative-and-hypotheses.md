# Narrative and candidate hypotheses

## Working position

The paper asks whether the meteorological state supplied to an air-chemistry model is credible enough for chemical attribution.
It does not argue that emissions inventories, deposition, photolysis, or chemical mechanisms are settled.
Instead, it treats the simulated depth, persistence, and ventilation of the 2 February 2013 Uinta Basin cold-air pool as a prerequisite for interpreting winter ozone.
The practical target is not a generic WRF ranking: it is whether the meteorological field represents the shallow mixing volume and weak ventilation that a downstream chemistry model actually receives.

The CHPC inventory and common-AGL analysis support a minimum four-run result core, but
that core no longer defines the intended breadth of the paper.
`rewrite/RESULTS-EXPANSION-HANDOFF.md` reopens the controlled X0--X10 terrain,
slope/shading, PBL/surface-layer, fine-terrain-feedback, spatial, vertical, and
heat-deficit threads.
The forcing response remains the strongest confirmed result; feedback is a bounded
robustness check rather than the necessary organizing thesis.
The current blank-slate manuscript remains a minimum scaffold until the expanded
architecture is chosen.

## Plain-language comparison-to-story map

The machine-readable authority is `verification/provenance/comparison-inventory.csv`.
Use this shorter view when deciding what story a run can support.

| Story role | Comparison IDs | What the evidence can support | What it cannot support |
|---|---|---|---|
| Primary result | CMP01 and CMP02 | The GFS-minus-NAM response is coherent under both feedback modes over the matched five-hour d02 sample. | It cannot yet separate initial-condition effects from lateral-boundary effects or establish multi-day persistence. |
| Secondary bounded result | CMP03, CMP04, and CMP05 | Feedback is nearly null under NAM, small under GFS, and much smaller than the forcing response; the interaction is source conditioned. | It is not general evidence that one-way and two-way nesting are equivalent. |
| Candidate Results | CMP06--CMP11 | Fine-terrain feedback, slope/shading, PBL/surface-layer, and terrain-source pairs are controlled or configuration-controlled and have current external figures. | A render does not close their named quantitative, provenance, interpretation, or claim-ledger gates. |
| Excluded or context only | CMP12 and CMP13 | The apparent resolution ladder and legacy nudged lineage expose design and provenance limitations. | They cannot support a resolution ranking, a nudging-effect estimate, or attribution to the literal Tran et al. run. |

In practical planning terms, retain CMP01/CMP02 as the confirmed anchor, use
CMP03--CMP06 to bound feedback without letting it dominate, and test CMP07--CMP11 as
real candidate Results through their named gates.
Use the expansion handoff to choose broad-configuration, maintenance/mechanism, or hybrid
architecture before returning to manuscript prose.

## Title candidates

The experimental title in `_manuscript_test.tex` is **Short-Window Response of WRF Cold-Pool Retention to Driving Data and Nest Feedback during a Uinta Basin Winter-Ozone Episode**.
The audited baseline title remains in `main.tex`.
Four nearby alternatives, to revisit during coauthor review, are:

1. **WRF Simulation of a Uinta Basin Winter Ozone Episode: A Meteorological Evaluation**
2. **Sensitivity of WRF Meteorology during a Uinta Basin Winter Ozone Episode**
3. **Evaluation of WRF Configurations for a Uinta Basin Winter Ozone Episode**
4. **WRF Cold-Pool Structure and Evolution during a Uinta Basin Winter Ozone Episode**

## Literature basis

Use extracted Markdown and critiques rather than rereading the PDFs during normal work:

- `~/reviews/ahmadov-ubwo-2015-acp/_paper.md` and `critique.md`
- `~/reviews/matichuk-cmaq-ub-2017/_paper.md` and `critique.md`
- `~/reviews/neemann-2015-UB-CAP/_paper.md` and `critique.md`
- Tran et al. (2018) publication/extraction, the local
  `notes/literature/tran-2018-fdda/critique.md`, and
  `verification/provenance/tran-2018-paper-archive-reconciliation.md`
- `~/reviews/wrf-ozone-studies/seth-notes-on-papers.md` and its targeted `_extracts/*-critique.md`

These paths normally exist on the Akamai/Linode writing host and should not be assumed available on CHPC.

The literature does not support the simple claim that chemistry and inventories are adequate while meteorology alone is deficient.
Ahmadov and Matichuk show strong emissions and process sensitivities, but both designs retain meteorology--emissions degeneracies.
Neemann and Tran show that snow, clouds, mixing, initialization, and nudging can change the cold pool, while their critiques identify confounded controls and incomplete validation.
The useful synthesis is therefore a controlled hierarchy of meteorological questions with an air-chemistry consequence attached to each.

Three later BRC/USU-orbit report slices give that consequence a concrete failure mode.
Their CAMx applications missed ozone accumulation when the driving meteorology diluted or vented the modeled cold pool, including a mechanism-only comparison in which changing chemistry did not recover the event.
Because the reports span different episodes, share an institutional lineage, and do not expose reconstructible run identities, they motivate retention diagnostics but do not prove that meteorology is universally dominant.

## Cross-study synthesis constraints

The four 10 July 2026 synthesis collections are registered in `notes/literature-synthesis-register.md`.
They add seven constraints to the narrative:

1. Shared episode and model lineage do not make cross-paper effect sizes additive or controlled.
2. “Nudging” must be decomposed by variable, height/radius gate, coefficient, input dataset, and assimilated sites.
3. Snow affects WRF cold-pool structure and chemistry-model photolysis through separate interfaces that both need verification.
4. WRF version, snow initialization, surface physics, microphysics, and nudging interact strongly enough that bias sign is not portable between configurations.
5. The reviewed sequences never cross their best meteorology with their best chemistry, so none can establish that meteorology, inventory, or mechanism is universally dominant.
6. Aggregate surface or episode scores can hide premature inversion breakup, excessive ventilation, and failure to accumulate a confined quantity.
7. Mechanism and emissions sensitivities diagnosed in a diluted model state are conditional on that regime and may not transfer to a realistically trapped pool.

These constraints strengthen the case for a meteorology-first evaluation while narrowing the causal claims it can support.

## Five candidate experiment threads

| Thread | Constructively critical literature question | Candidate experiment | Candidate hypothesis | Falsifier or limiting result | Air-chemistry consequence | Status |
|---|---|---|---|---|---|---|
| 1. Initial and boundary state | Is an apparent WRF physics error inherited from a biased driving analysis or created during forecast evolution? Tran's NAM warm/moist premise was load-bearing but not shown; repeated reinitialization can reset a mature pool. | X6 versus X5 under two-way feedback and X10 versus X3 under one-way feedback, with matched d02 grid, physics, terrain, initialization time, and valid window. | Lower-tropospheric differences in the driving analysis produce a first-order difference in cold-pool maintenance over the short forecast under both feedback modes. | The common-window temperature, common-AGL stability, and transport-wind differences are negligible, change sign, or vanish under the second feedback mode. | Initial-state error changes dilution volume before chemistry starts. | **Primary result:** the state difference is coherent under both feedback modes; inherited initial versus lateral-boundary contributions remain unresolved. |
| 2. Domain, resolution, and nest feedback | Are the meteorological fields evaluated at the same scale that would drive chemistry? Neemann evaluated a finer nest than the CMAQ-driving domain; the current 333 m nest excludes many bench stations. | X10 versus X6 under GFS and X3 versus X5 under NAM, with feedback as the only reconciled within-source change. | Feedback is small relative to the forcing response over this six-hour run. | A coherent feedback or forcing-by-feedback response approaches the GFS--NAM response. | A chemistry grid cannot recover cold-pool structure absent from its meteorological driver. | **Secondary bounded interaction:** NAM is nearly null; GFS and the paired interaction are coherent but small on the five-hour d02 sample; no general equivalence claim. |
| 3. Stable-layer representation | Do vertical levels, model top, PBL treatment, or WRF version resolve and retain the shallow stable layer? Tran showed diagnosed PBL height can silently redefine nudging reach; later evaluations found version effects larger than several other changes. | Controlled X2-X1 MYJ/Eta-versus-YSU/MM5 pair; the apparent level/resolution sequence remains confounded. | The scheme pair changes common-AGL mixing, stability, fluxes, and evolution in a physically interpretable way. | The response disappears under scheme-aware common coordinates, or cannot be separated from diagnostic definitions. | Excess mixing dilutes precursors; too little mixing can exaggerate nighttime trapping and titration. | **Analysis-ready:** C19 blocks the inherited small-response claim; common-AGL and scheme-aware turbulence analysis is required. |
| 4. Surface, terrain, and radiation physics | Are terrain, slope-aware radiation, land-surface energy fields, and related treatments represented consistently? Neemann bounded snow and cloud effects; Matichuk showed WRF albedo changes need not reach CMAQ photolysis. | Controlled X1-X0 slope/shading pair and configuration-controlled X3-X0, X3-X4, and X0-X4 terrain pairs. No clean local snow, microphysics, or cloud pair is currently identified. | Terrain and radiation choices change rim/floor geometry or local energy/stability evolution even when aggregate surface scores are similar. | Process fields show no coherent response, or X4 provenance prevents interpretation. | Meteorology affects confinement, while chemistry separately needs the correct snow photolysis and deposition treatment. | **Analysis-ready:** figures exist; radiation needs a local process diagnostic and terrain needs X4 lineage plus elevation-aware interpretation. |
| 5. Data assimilation versus a free forecast | Does nudging correct the cold pool or impose the bias of the analysis being assimilated? Verification is not independent when scored observations were also assimilated. | Same-case nudged and un-nudged pairs if recoverable; otherwise literature/context only. | A short free forecast can provide competitive surface meteorology without the stable-layer distortions possible under biased nudging. | No same-case controlled pair exists, or independent observations favor the nudged structure. | Assimilation can improve apparent scores without guaranteeing the transport and mixing fields needed by chemistry. | No clean same-case pair currently established. |

## Required diagnostic spine

Every promoted comparison should answer both a conventional performance question and a retention question.
At minimum, the analysis should show the time evolution of near-surface temperature and wind together with the strongest defensible lower-tropospheric stability or inversion-depth diagnostic available on the matched sample.
Run differences should be followed through time so inherited initial-state error can be separated from developed mixing or ventilation error.

The frozen 14--18 UTC window contains only five hourly samples.
It can test short-window structure and evolution, but it cannot demonstrate multi-day cold-pool persistence or reproduce the downstream CAMx failure sequence described in the report literature.
Window-mean scores therefore cannot stand alone, and any longer-timescale claim requires a longer provenance-checked run and matched observations.

## Promotion rules

A thread becomes a manuscript hypothesis only when:

1. The CHPC inventory identifies the exact run IDs and as-run namelists.
2. The comparison isolates the named lever or lists every remaining confound.
3. Both members cover the identical domain, stations, and evaluation window.
4. The predicted diagnostic and a falsifying outcome are specified before interpreting the figure.
5. The result has a direct, carefully scoped air-chemistry implication.

If fewer than five controlled tests exist, the paper must not manufacture five positive findings.
An unsupported thread remains a literature gap or future experiment.

## Frozen first-draft arc

1. Winter ozone depends on chemistry occurring inside a difficult-to-model cold-air pool.
2. Downstream chemical applications show the practical failure mode when that pool is diluted or vented, without establishing that meteorology is the only controlling uncertainty.
3. Prior emissions, chemistry, and meteorology studies expose recurring configuration questions but often mix controls, operating regimes, or validation targets.
4. The matched GFS and NAM runs test the response to driving analysis under both feedback modes, using time-resolved 50--500 m AGL stability and transport wind alongside surface scores.
5. The two within-source feedback pairs and their paired interaction provide a bounded secondary result, while terrain, PBL, resolution, and nudging results remain outside the first-draft core.
6. The conclusion answers only these promoted questions within the five-hour verified window and does not claim multi-day persistence or settled chemistry.
