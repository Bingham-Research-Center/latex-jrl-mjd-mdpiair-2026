# Manuscript roadmap

Current phase: **targeted gate-closing for the selected Architecture C hybrid before
blank-slate prose continues**.

`main.tex` is the audited review baseline.
`_manuscript_test.tex` and `rewrite/` are the isolated reconstruction workbench; no experimental prose replaces the baseline until its evidence, figure, methods, and coauthor gates close.
`_manuscript_test.tex` currently demonstrates the minimum verified four-run story; it is not a decision that the final paper has only four experiments or two figures.
John selected Architecture C on 13 July 2026.
The active handoff is `rewrite/HYBRID-ARCHITECTURE-HANDOFF.md`; the completed audit and
alternative packages remain in `rewrite/RESULTS-ARCHITECTURE-DECISION-PACKET.md`.

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

The verified four-run result supports a compact fallback article, but the matrix is now
explicitly reopened for an evidence-gated broader paper.
Controlled terrain, slope/shading, PBL/surface-layer, and fine-terrain feedback pairs must
be evaluated as candidate Results rather than excluded by the earlier minimum-draft choice.
The confounded resolution sequence and heterogeneous nudging lineage remain context only.

## Phases and exit gates

| Phase | Outcome | Exit gate |
|---|---|---|
| 0. Repository foundation | Current MDPI template, sparse manuscript, evidence gates, safe submission builder | Complete in commits `3e21a28`--`e84c751`. |
| 1. Inventory reconciliation | Stable run IDs and fingerprints for every candidate comparison | `verification/provenance/run-inventory.csv` contains exact archive path, version, window, grid, physics, forcing, feedback, FDDA, and evidence hashes for each promoted run. |
| 2. Experiment design freeze | A classified X0--X10 matrix of controlled, configuration-controlled, confounded, and contextual comparisons | Each row isolates a named lever or lists every confound; each proposed result has its own common domain/sample/window. |
| 3. Evidence longlist | Recomputed statistics and diagnostic figures from provenance-checked real data | Small and null findings are retained; commands are reproducible; uncertainty and missingness are explicit; synthetic output is absent. |
| 4. Narrative freeze | Selected Architecture C with an evidence-gated main/supplement/reserve spine | C3--C6 and supplement C2 receive pass/fail dispositions, and every retained paragraph-level claim links to a ledger row and a table/figure or cited source. |
| 5. Manuscript build | Reconstruct the paper from the chosen evidence spine, critique lessons, and decision-grade figures | The expanded rewrite passes its acceptance tests, methods placeholders close, and coauthors confirm configuration, interpretation, roles, funding, data availability, and attribution. |
| 6. Figure and reproducibility freeze | Promoted figures, supplement/reviewer reserve, and public data/code plan | Both manifests are complete; canonical WRF styling reviewed; clean source ZIP compiles independently. |
| 7. Coauthor review and submission | Reviewed MDPI Air package | Michael reviews provenance/diagnostics; Loknath and Seth review chemistry framing; all authors approve. |

Run rows exist for X0--X10, and derived manuscript summaries are complete only for the
default-terrain X6/X10/X5/X3 factorial.
Figure coverage is substantially broader than those summaries.
The architecture choice is frozen, but prose remains frozen until the selected controlled
pairs, observation metadata, source-level citations, figure admissions, and coauthor
interpretation are reconciled.

## Workstreams

### Run and data truth

- Reconcile the July 9 CHPC inventory archive with the canonical run-inventory CSV.
- Fingerprint the three JRL touchstones first, then the SIP-era comparator and any controlled sensitivity pairs.
- Preserve the January nudged evaluation as historical context unless a same-case design makes it relevant.

### Analysis and verification

- Preserve the frozen d02, reporting-station sample, 14--18 UTC window, and two-hour spin-up exclusion when extending the confirmed factorial; define and justify a matched domain/sample/window separately for each additional result thread.
- Use the two-hour circular block sensitivity interval across hourly spatial medians as a descriptive dependence check, not a formal confidence interval.
- Pair aggregate scores with the completed common-AGL stability and transport-wind diagnostic; a five-hour sample cannot support a multi-day persistence claim.
- Use independent or held-out observations for any nudging claim.

### Literature and argument

- Use critiques before extracted papers; use extracted sections before PDFs.
- Carry the Matichuk/Ahmadov warning that tuning emissions can absorb meteorology, photolysis, and deposition errors.
- Carry the Neemann/Tran warning that on/off experiments, nudging labels, PBL diagnostics, and chemistry-grid mismatches can hide confounding.
- Use `notes/literature-synthesis-register.md` to carry the four synthesis collections' shared challenge to any claim that meteorology is uniquely dominant.
- Use the downstream CAMx failure set to motivate retention and ventilation diagnostics, while treating its related institutional reports, unresolved run identities, and mixed 2013/2019 episodes as context rather than independent proof.

### Figures and result expansion

- Start with `rewrite/HYBRID-ARCHITECTURE-HANDOFF.md`; use the Architecture C table in the
  decision packet for figure roles and `verification/figures/archive-inventory.md` only
  for current external coverage.
- Generate a broad diagnostic longlist on CHPC, then promote only figures that answer a named hypothesis.
- Keep useful rejected or secondary diagnostics reproducible for supplements and reviewer requests.
- Do not promote an inherited image solely because it looks publication-ready.

## Minimum verified scaffold, not current scope

- **Primary:** GFS versus NAM driving analysis under both two-way (X6 minus X5) and one-way (X10 minus X3) default-terrain configurations.
- **Secondary:** within-source one-way-versus-two-way feedback (X10 minus X6 and X3 minus X5) plus the paired forcing-by-feedback interaction.
- **Available promoted figure pool:** observed floor-to-bench evolution, observed/model bulk theta contrast, and four-run common-AGL retention/ventilation.
- **Experimental rewrite core:** observed evolution plus common-AGL retention/ventilation; hold the bulk-theta panel until CHPC regenerates the corrected annotation and the proxy earns a distinct narrative role.
- **Active expansion candidates:** X1-X0 slope/shading, X2-X1 PBL/surface layer, X3-X0/X3-X4/X0-X4 terrain, X9-X0 fine-terrain feedback, spatial/vertical driving-response panels, and productized heat-deficit fields.
- **Still excluded as sensitivity results:** the confounded X7/X0/X8 resolution ladder and heterogeneous nudging lineage.

No additional WRF integration is needed to audit the broader existing matrix.
Use the completed outputs for targeted analysis and figure selection first.
CHPC metadata recovery, the held figure regeneration, and selected diagnostic checks remain gates before coauthor circulation; propose a new integration only when the existing archive cannot answer a selected question.

The active granular queue is in `tasks/microtasks.md`.
The source-mining order and legacy to-do location are in `notes/resource-map.md`.
