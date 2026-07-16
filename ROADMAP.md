# Manuscript roadmap

Current phase: **final author draft and coauthor closure after audited Architecture C
promotion**.

`main.tex` is the audited 17-page final-draft starting point.
`_manuscript_test.tex` and `rewrite/` are the isolated reconstruction workbench;
`_manuscript_v3.tex` is the frozen 26-page over-inclusive caretaker snapshot.
`_manuscript_test.tex` currently demonstrates the minimum verified four-run story; it is not a decision that the final paper has only four experiments or two figures.
John selected Architecture C on 13 July 2026.
All five gates have executed, with pass/fail dispositions in
`rewrite/HYBRID-GATE-REVIEW.md`.
The active handoff is `notes/final-draft-readiness-2026-07-15.md` and the ordered
register is `tasks/final-draft-100.md`.
The v3 integration plan and architecture alternatives remain decision history.

The paper's durable result is that the supplied driving analysis produces a repeatable
short-window offset in WRF cold-pool state under both nest-feedback settings.
Its air-focused bridge is that credible cold-pool meteorology is a prerequisite for
interpreting winter-ozone chemistry, not merely a ranking by aggregate surface bias.
It must not claim that chemistry, emissions, deposition, or photolysis are already settled.

## Candidate large-scale narratives

| Narrative | Role if supported | Evidence already present | Gate before promotion |
|---|---|---|---|
| Driving-analysis state affects a short cold-pool forecast | Primary result | Matched GFS and NAM runs under both one-way and two-way feedback; surface scores; common-AGL retention and ventilation | Keep the claim within 14--18 UTC and distinguish the driving-state response from its unresolved initial-versus-lateral-boundary origin. |
| Domain design and nest feedback affect the structure seen by a chemistry grid | Secondary bounded interaction | Matched GFS and NAM one-way/two-way pairs; paired forcing-by-feedback interaction; d02/d03 coverage contrast | Report the small source-conditioned five-hour response without claiming general equivalence or extrapolating to longer integrations. |
| Stable-layer, surface, snow, terrain, or cloud choices control cold-pool persistence | Experiment-led candidate | Several local run families and literature sensitivities | Inventory must yield controlled pairs; do not infer a physics sensitivity from unrelated configurations. |
| Nudging can correct or manufacture cold-pool structure | Context or result, depending on recovered runs | Tran critique, SIP-era comparator, January historical evaluation | A same-case controlled nudged/free pair and held-out verification are required for a result. |
| Meteorological error changes the volume available for ozone chemistry | Air-focused bridge | Literature rationale plus downstream reports of dilution and premature ventilation | Verify and cite the underlying reports; phrase as an implication of evaluated structure, not proof that meteorology dominates inventory or mechanism error. |

The verified four-run result is the final-draft core.
Terrain, slope/shading, PBL/surface-layer, fine-terrain feedback, nudging, and longer
windows are optional future opportunities, not final-draft blockers.
The confounded resolution sequence and heterogeneous nudging lineage remain context only.

## Phases and exit gates

| Phase | Outcome | Exit gate |
|---|---|---|
| 0. Repository foundation — complete | Current MDPI template, sparse manuscript, evidence gates, safe submission builder | Completed in commits `3e21a28`--`e84c751`; build contract hardened in `234ec7c`. |
| 1. Inventory reconciliation — complete for promoted core | Stable run IDs and fingerprints for every promoted comparison | Exact archive path, version, window, grid, physics, forcing, feedback, FDDA, and evidence hashes exist for the four core runs. |
| 2. Experiment design freeze — complete | Classified X0--X10 matrix of controlled, configuration-controlled, confounded, and contextual comparisons | Each comparison isolates a lever or lists its confounds. |
| 3. Evidence longlist — complete | Recomputed statistics and registered diagnostics from provenance-checked real data | Small/null findings retained, commands reproducible, uncertainty/missingness explicit, synthetic output excluded. |
| 4. Narrative freeze — complete | Selected Architecture C with main/supplement/reserve dispositions | Every gate has a pass/fail record; failed gates remain failed. |
| 5. Manuscript build — in final-author pass | Audited main candidate plus maximal donor snapshot | Close required evidence/citation/front-matter rows and obtain configuration/interpretation review. |
| 6. Figure and reproducibility freeze — next | Promoted figures, supplement decision, and public data/code plan | Freeze both manifests; inspect print layout; compile the clean source ZIP independently. |
| 7. Coauthor review and submission — later | Reviewed MDPI Air package | Michael reviews provenance/diagnostics; Loknath and Seth review chemistry framing; all authors approve. |

Run rows exist for X0--X10, but the promoted quantitative argument remains the
default-terrain X6/X10/X5/X3 factorial plus bounded observational context.
Figure coverage is broader than the admitted paper, and that is intentional.
The architecture choice, failed gates, and maximal-v3 lineage are frozen.
Final-draft work should verify or remove unresolved statements in `main.tex`, not
mine v3 for additional breadth by default.

## Workstreams

### Required evidence closure

- Obtain Michael's review of the four promoted run identities, configurations, and
  diagnostic meanings.
- Close or explicitly bound observation QC/licensing and product/model citation gaps.
- Recheck every number and mathematical definition against exact registered artefacts.

### Final prose and review

- Keep the thesis on a deterministic 14--18 UTC supplied-state response.
- Separate absolute run states, matched contrasts, small feedback effects, and
  literature implications.
- Add citations only from John's complete Paperpile export and verified passages.
- Close author metadata, CRediT, funding, declarations, availability, and approvals.

### Literature and argument

- Use critiques before extracted papers; use extracted sections before PDFs.
- Carry the Matichuk/Ahmadov warning that tuning emissions can absorb meteorology, photolysis, and deposition errors.
- Carry the Neemann/Tran warning that on/off experiments, nudging labels, PBL diagnostics, and chemistry-grid mismatches can hide confounding.
- Use `notes/literature-synthesis-register.md` to carry the four synthesis collections' shared challenge to any claim that meteorology is uniquely dominant.
- Use the downstream CAMx failure set to motivate retention and ventilation diagnostics, while treating its related institutional reports, unresolved run identities, and mixed 2013/2019 episodes as context rather than independent proof.

### Figures and package

- Freeze the nine allowlisted main figures after print, accessibility, hash, and
  permission review.
- Decide whether any separate supplement survives; v3's review-layout Appendix B
  is not a submission supplement.
- Build and inspect the allowlisted package in an independent clean environment.

## Selected final-draft scope

- **Primary:** GFS versus NAM driving analysis under both two-way (X6 minus X5) and one-way (X10 minus X3) default-terrain configurations.
- **Secondary:** within-source one-way-versus-two-way feedback (X10 minus X6 and X3 minus X5) plus the paired forcing-by-feedback interaction.
- **Promoted figure spine:** locator, bounded AQS/MODIS episode context, observed
  temperature evolution, common-pipeline effects, common-AGL retention/ventilation,
  line-free bulk theta, heat deficit, and two Horsepool supplied-state profiles.
- **Maximal-v3 reserve:** terrain, radiation, and X8 panels remain diagnostic/review
  material and do not enter `main.tex`.
- **Optional expansion:** new controlled terrain, radiation, PBL, snow, nudging,
  attribution, or longer-window work appears only in the optional register.
- **Still excluded as sensitivity results:** the confounded X7/X0/X8 resolution ladder and heterogeneous nudging lineage.

No additional WRF integration is needed to audit the broader existing matrix.
Use the completed outputs for targeted analysis and figure selection first.
The held bulk-theta regeneration and current diagnostic checks are complete.
No additional WRF integration is required to begin or complete the author prose pass.

The current ordered queue is `tasks/final-draft-100.md`.
The readiness evidence is `notes/final-draft-readiness-2026-07-15.md`; selective
source-mining order remains in `notes/resource-map.md`.
