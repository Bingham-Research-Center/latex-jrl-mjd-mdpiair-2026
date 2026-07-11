# Manuscript roadmap

Current phase: **review and refine the compact short-window first draft**.

The paper's durable claim is that credible cold-pool meteorology is a prerequisite for interpreting winter-ozone chemistry.
Its air-focused evaluation target is whether WRF retains the shallow, weakly ventilated layer in which precursor and ozone accumulation would occur, not merely which run has the smallest aggregate surface bias.
It must not claim that chemistry, emissions, deposition, or photolysis are already settled.

## Candidate large-scale narratives

| Narrative | Role if supported | Evidence already present | Gate before promotion |
|---|---|---|---|
| Driving-analysis state affects a short cold-pool forecast | Primary result | Matched GFS and NAM runs under both one-way and two-way feedback; surface scores; common-AGL retention and ventilation | Keep the claim within 14--18 UTC and distinguish the driving-state response from its unresolved initial-versus-lateral-boundary origin. |
| Domain design and nest feedback affect the structure seen by a chemistry grid | Secondary bounded interaction | Matched GFS and NAM one-way/two-way pairs; paired forcing-by-feedback interaction; d02/d03 coverage contrast | Report the small source-conditioned five-hour response without claiming general equivalence or extrapolating to longer integrations. |
| Stable-layer, surface, snow, terrain, or cloud choices control cold-pool persistence | Experiment-led candidate | Several local run families and literature sensitivities | Inventory must yield controlled pairs; do not infer a physics sensitivity from unrelated configurations. |
| Nudging can correct or manufacture cold-pool structure | Context or result, depending on recovered runs | Tran critique, SIP-era comparator, January historical evaluation | A same-case controlled nudged/free pair and held-out verification are required for a result. |
| Meteorological error changes the volume available for ozone chemistry | Air-focused bridge | Literature rationale plus downstream reports of dilution and premature ventilation | Verify and cite the underlying reports; phrase as an implication of evaluated structure, not proof that meteorology dominates inventory or mechanism error. |

The frozen paper is a compact original-research article led by a driving-state result replicated across feedback modes and a bounded nest-feedback interaction.
Physics, terrain, resolution, and nudging comparisons remain Discussion, supplement, reviewer reserve, or future work unless a later coauthor decision reopens the matrix.

## Phases and exit gates

| Phase | Outcome | Exit gate |
|---|---|---|
| 0. Repository foundation | Current MDPI template, sparse manuscript, evidence gates, safe submission builder | Complete in commits `3e21a28`--`e84c751`. |
| 1. Inventory reconciliation | Stable run IDs and fingerprints for every candidate comparison | `verification/provenance/run-inventory.csv` contains exact archive path, version, window, grid, physics, forcing, feedback, FDDA, and evidence hashes for each promoted run. |
| 2. Experiment design freeze | A short matrix of controlled comparisons and preregistered diagnostics/falsifiers | Each row isolates a named lever or lists every confound; common domain/stations/window selected. |
| 3. Evidence longlist | Recomputed statistics and diagnostic figures from provenance-checked real data | Commands are reproducible; uncertainty and missingness are explicit; synthetic output is absent. |
| 4. Narrative freeze | One primary result arc, one or two secondary arcs, and a limitations spine | Every paragraph-level claim is linked to a ledger row and a table/figure or cited source. |
| 5. Manuscript build | Methods, Results, Discussion, abstract, and required MDPI back matter | Coauthors confirm configuration, interpretation, roles, funding, data availability, and attribution. |
| 6. Figure and reproducibility freeze | Promoted figures, supplement/reviewer reserve, and public data/code plan | Both manifests are complete; canonical WRF styling reviewed; clean source ZIP compiles independently. |
| 7. Coauthor review and submission | Reviewed MDPI Air package | Michael reviews provenance/diagnostics; Loknath and Seth review chemistry framing; all authors approve. |

Phases 1--4 are complete for the default-terrain X6/X10/X5/X3 factorial, and Phase 5 is underway with a compiled first draft.
Unresolved heterogeneous lineage, terrain, physics, and resolution records do not block the first draft because they are excluded from the frozen result core.

## Workstreams

### Run and data truth

- Reconcile the July 9 CHPC inventory archive with the canonical run-inventory CSV.
- Fingerprint the three JRL touchstones first, then the SIP-era comparator and any controlled sensitivity pairs.
- Preserve the January nudged evaluation as historical context unless a same-case design makes it relevant.

### Analysis and verification

- Use the frozen d02, reporting-station sample, 14--18 UTC window, and two-hour spin-up exclusion for every primary or feedback result.
- Use the two-hour circular block sensitivity interval across hourly spatial medians as a descriptive dependence check, not a formal confidence interval.
- Pair aggregate scores with the completed common-AGL stability and transport-wind diagnostic; a five-hour sample cannot support a multi-day persistence claim.
- Use independent or held-out observations for any nudging claim.

### Literature and argument

- Use critiques before extracted papers; use extracted sections before PDFs.
- Carry the Matichuk/Ahmadov warning that tuning emissions can absorb meteorology, photolysis, and deposition errors.
- Carry the Neemann/Tran warning that on/off experiments, nudging labels, PBL diagnostics, and chemistry-grid mismatches can hide confounding.
- Use `notes/literature-synthesis-register.md` to carry the four synthesis collections' shared challenge to any claim that meteorology is uniquely dominant.
- Use the downstream CAMx failure set to motivate retention and ventilation diagnostics, while treating its related institutional reports, unresolved run identities, and mixed 2013/2019 episodes as context rather than independent proof.

### Figures and reviewer reserve

- Use `notes/figure-strategy.md` for the deadline-focused longlist, three defensible
  narrative packages, and the minimum three-figure draft spine.
- Generate a broad diagnostic longlist on CHPC, then promote only figures that answer a named hypothesis.
- Keep useful rejected or secondary diagnostics reproducible for supplements and reviewer requests.
- Do not promote an inherited image solely because it looks publication-ready.

## Frozen first-draft matrix

- **Primary:** GFS versus NAM driving analysis under both two-way (X6 minus X5) and one-way (X10 minus X3) default-terrain configurations.
- **Secondary:** within-source one-way-versus-two-way feedback (X10 minus X6 and X3 minus X5) plus the paired forcing-by-feedback interaction.
- **Promoted figure spine:** observed floor-to-bench evolution, observed/model bulk theta contrast, and four-run common-AGL retention/ventilation.
- **Excluded from first-draft Results:** the confounded X7/X0/X8 resolution ladder, heterogeneous nudging lineage, and incompletely interpreted terrain/PBL treatments.

No additional WRF treatment is needed before the first draft.
New experiments are reserved for a coauthor decision or a reviewer request after the present evidence is written clearly.

The active granular queue is in `tasks/microtasks.md`.
The source-mining order and legacy to-do location are in `notes/resource-map.md`.
