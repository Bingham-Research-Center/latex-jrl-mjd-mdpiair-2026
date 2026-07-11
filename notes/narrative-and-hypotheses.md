# Narrative and candidate hypotheses

## Working position

The paper asks whether the meteorological state supplied to an air-chemistry model is credible enough for chemical attribution.
It does not argue that emissions inventories, deposition, photolysis, or chemical mechanisms are settled.
Instead, it treats the simulated depth, persistence, and ventilation of the 2 February 2013 Uinta Basin cold-air pool as a prerequisite for interpreting winter ozone.
The practical target is not a generic WRF ranking: it is whether the meteorological field represents the shallow mixing volume and weak ventilation that a downstream chemistry model actually receives.

The CHPC inventory and common-AGL analysis now support a narrow first-draft result core.
The forcing response replicated across both feedback modes is primary, the small source-conditioned feedback interaction is secondary, and the remaining candidate hypotheses stay outside the first-draft Results.

## Title candidates

The deliberately plain working title in `main.tex` is **Evaluation of WRF Meteorology for a Uinta Basin Winter Ozone Episode**.
Four nearby alternatives, to revisit once the defensible experiment matrix is known, are:

1. **WRF Simulation of a Uinta Basin Winter Ozone Episode: A Meteorological Evaluation**
2. **Sensitivity of WRF Meteorology during a Uinta Basin Winter Ozone Episode**
3. **Evaluation of WRF Configurations for a Uinta Basin Winter Ozone Episode**
4. **WRF Cold-Pool Structure and Evolution during a Uinta Basin Winter Ozone Episode**

## Literature basis

Use extracted Markdown and critiques rather than rereading the PDFs during normal work:

- `~/reviews/ahmadov-ubwo-2015-acp/_paper.md` and `critique.md`
- `~/reviews/matichuk-cmaq-ub-2017/_paper.md` and `critique.md`
- `~/reviews/neemann-2015-UB-CAP/_paper.md` and `critique.md`
- `~/reviews/tran-2018-fdda/_paper.md`, `critique.md`, and `wrf-data-paper-contradictions.md`
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
| 3. Stable-layer representation | Do vertical levels, model top, PBL treatment, or WRF version resolve and retain the shallow stable layer? Tran showed diagnosed PBL height can silently redefine nudging reach; later evaluations found version effects larger than several other changes. | Level-count, vertical-grid, PBL, and version pairs identified by the inventory. | Enhanced or better-placed lower-tropospheric resolution changes near-surface mixing, inversion strength, and their evolution more than nominal grid refinement alone. | No controlled pair exists, or differences are inseparable from physics/version changes. | Excess mixing dilutes precursors; too little mixing can exaggerate nighttime trapping and titration. | TBC inventory. |
| 4. Surface, terrain, and cloud physics | Are snow, albedo, terrain, land surface, and cloud phase represented consistently? Neemann bounded snow and cloud effects; Matichuk showed WRF albedo changes need not reach CMAQ photolysis. | Terrain-resolution, snow/land, microphysics, radiation, and surface-scheme variants from the inventory. | Surface and cloud choices materially affect radiative cooling and cold-pool persistence in this case. | The tested choices do not alter process fields, or the experiment changes multiple levers without a control. | Meteorology affects confinement, while chemistry separately needs the correct snow photolysis and deposition treatment. | TBC inventory. |
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
