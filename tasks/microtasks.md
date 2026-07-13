# Active microtasks and recovered legacy checklist

This is the granular execution queue beneath `ROADMAP.md`.
Tasks are deliberately small; completing one should change a named artifact or settle a named decision.

Status vocabulary: **next**, **blocked**, **later**, **done**, and **retired**.
Do not mark a scientific task done because prose exists; mark it done only when its evidence gate is met.

## Current tranche: expanded-results decision packet before more prose

- [ ] **DES-04 · next** — Build the freshness-aware CMP01--CMP13 candidate-result ledger specified in `rewrite/RESULTS-EXPANSION-HANDOFF.md`.
- [ ] **FIG-13 · next** — Reconcile stale X9, terrain-label, and cross-case-count statements against `verification/figures/archive-inventory.md` without equating rendering with analysis or promotion.
- [ ] **NAR-07 · next** — Present broad-configuration, maintenance/mechanism, and hybrid paper architectures with main/supplement/reserve figures and one reader decision per figure.
- [ ] **ANA-16 · next after architecture choice** — Validate the productized heat-deficit post-spin-up trajectory, basin/crest definition, masks, units, and sensitivity before adding a ledger claim.
- [ ] **ANA-17 · next after architecture choice** — Analyse CMP09--CMP11 with terrain/elevation-aware diagnostics after resolving the X4 path-lineage gate.
- [ ] **ANA-18 · next after architecture choice** — Analyse CMP07 radiation fields locally and CMP08 on common AGL coordinates with scheme-aware flux/PBLH/TKE treatment.
- [ ] **MAN-14 · blocked by DES-04/NAR-07** — Restructure `_manuscript_test.tex` only after John chooses the expanded evidence/figure architecture.

- [ ] **INV-01 · next** — Locate the out-of-band July 9 provenance archive and verify SHA-256 `b616ec6b4ff70f3a36048904d5cad7a99a2563ba4a19fd79198fbf923332a958`.
- [x] **INV-02 · done** — Mapped the three JRL touchstone header fingerprints to exact durable archive basenames.
- [x] **INV-03 · done** — Added canonical inventory rows for GFS and NAM under both one-way and two-way feedback.
- [x] **INV-04 · done** — Attached exact as-run namelist hashes to the touchstone rows.
- [x] **INV-05 · done** — Recorded version, initialization, valid times, cadence, grid, levels, physics, forcing, and feedback.
- [x] **INV-06 · done** — Proved that the default-terrain NAM one-/two-way pair differs only in feedback.
- [ ] **INV-07 · later/context** — Fingerprint `REF_long`; it is excluded from the frozen result matrix and must never be called Tran-2018 NON.
- [ ] **INV-08 · later/context** — Mark assimilated stations before any nudging comparison; no nudged run enters the frozen result matrix.
- [x] **DES-01 · done** — Froze X6/X10/X5/X3 as a forcing-by-feedback factorial with forcing contrasts, within-source feedback contrasts, and a paired interaction.
- [x] **DES-02 · done** — Froze d02, the reporting-station sample, 14--18 UTC, and a two-hour spin-up exclusion.
- [x] **DES-03 · done** — Defined 50--500 m AGL stability and transport wind and stated the five-hour persistence limit.
- [x] **ANA-01 · done for promoted core** — Re-reduced X3/X5/X6/X10 from exact raw archive paths.
- [x] **ANA-02 · done for promoted core** — Recomputed matched surface and vertical summaries.
- [x] **ANA-03 · done for descriptive scope** — Added two-hour circular block sensitivity intervals while explicitly declining formal five-sample inference.
- [x] **MAN-01--03 · done for first draft** — Drafted Methods and Results from the frozen claims and promoted three-figure spine; coauthor/scientific review is next.
- [ ] **MAN-11 · next** — Close the visible methods placeholders for observation provider/QC/licensing, domain geometry/static inputs, and forcing-product citations before coauthor circulation.
- [x] **MAN-12 · done for experimental rewrite** — Built `_manuscript_test.tex` and `rewrite/blueprint.md` from the audited claims, critique lessons, two-figure core, and explicit stop conditions without replacing `main.tex`.
- [ ] **MAN-13 · next** — Integrate CHPC evidence into the expanded-result ledger, close selected gates, obtain scientific/coauthor review, and decide which experimental structure replaces the audited baseline.
- [ ] **COA-01 · next** — Ask Michael for the code/input/command/meaning mapping for each Teams plot still under consideration.
- [ ] **COA-02 · next** — Send the short Trang/Michael run-identity question list only after the machine inventory narrows it.

## Full backlog by workstream

### Provenance and data

- [ ] **INV-09 · next** — Copy stable run IDs into `verification/figures/manifest.csv` for every retained candidate with known inputs.
- [ ] **INV-10 · next** — Mark candidates with unknown inputs as `provisional` or `rejected`; never infer provenance from filenames.
- [ ] **INV-11 · later** — Resolve the exact Tran-2018 NON/ONU/ANU/OAN production directories.
- [ ] **INV-12 · later** — Resolve whether the January `WRF_anlnudge` output is published OAN or a later revision.
- [x] **INV-13 · done for the current archive** — Inventoried controlled PBL/surface-layer, slope/shading, and terrain pairs in X0--X10; no clean local vertical-grid, snow, microphysics, cloud, or stochastic pair is established.
- [ ] **INV-14 · later** — Record the d03 interior station set separately from the d02 common evaluation set.
- [ ] **INV-15 · next** — Fix legacy issue 3 by making the January observation-pull command reproducible with explicit dates/output and six authoritative stations.
- [ ] **INV-16 · later** — Decide the public archive/repository for minimal processed data, namelists, commands, and code.
- [ ] **INV-17 · next** — Record the Synoptic API QC parameters, station/sensor metadata, archive license, and public-access route used for the February cache.

### Analysis and verification

- [ ] **ANA-04 · blocked** — Describe the observed 2 February cold pool using provenance-checked temperature, potential-temperature, and inversion diagnostics.
- [x] **ANA-05 · done** — Tested the GFS-versus-NAM surface, common-AGL stability, and transport-wind differences on the frozen sample.
- [x] **ANA-06 · done** — Bounded both within-source feedback responses and their paired forcing-by-feedback interaction on the frozen sample.
- [ ] **ANA-07 · later** — Separate initialization from lateral-boundary and forecast-evolution effects only if the first draft or reviewers require another experiment.
- [ ] **ANA-08 · blocked** — Quantify d02/d03 representativeness without treating missing bench stations as model skill.
- [ ] **ANA-09 · later** — Stratify errors by station elevation and variable; avoid basin means that cancel opposing biases.
- [ ] **ANA-10 · later** — Apply circular statistics to wind direction and state when calm winds make direction uninformative.
- [ ] **ANA-11 · later** — If nudging enters Results, evaluate only at held-out stations or label the dependence explicitly.
- [ ] **ANA-12 · later** — Test sensitivity to the two-hour spin-up decision.
- [ ] **ANA-13 · later** — Compare a no-signal/null period only if the experiment and data can be made genuinely comparable.
- [ ] **ANA-14 · later** — Build a reviewer-reserve table of null, contradictory, and secondary results.
- [x] **ANA-15 · done** — Paired aggregate surface scores with common-AGL stability, transport wind, and PBLH over the matched window.

### Literature and narrative

- [ ] **LIT-01 · next** — Convert the completed Matichuk critique into a claim/evidence/caveat row set for the introduction and discussion.
- [ ] **LIT-02 · next** — Build a compact comparison table for Ahmadov, Neemann, Matichuk, Tran, UBAQR-2019/2020, OSIP-2021, Ramboll-2023, the top-down inventory report, and the Rocky Mountain Power report: case, model, meteorological lever, chemistry lever, observations, and principal confounds.
- [ ] **LIT-03 · later** — Verify every manuscript citation against the extracted paper passage or source PDF.
- [ ] **LIT-04 · later** — Decide whether report literature belongs in the main article, supplement, or reviewer reserve.
- [ ] **LIT-05 · next** — Use `notes/literature-synthesis-register.md` to select which report sources genuinely survive narrative freeze.
- [ ] **LIT-06 · blocked by LIT-05** — Add the selected report sources to Paperpile and replace the register's citation placeholders through a complete export.
- [x] **NAR-01 · done for minimum scaffold** — Established the driving-state response as the strongest confirmed anchor; broader narrative selection is reopened in NAR-07.
- [x] **NAR-02 · done for minimum scaffold** — Bounded the source-conditioned feedback response and rejected resolution/nudging as sensitivity results; controlled terrain/radiation/PBL candidates are reopened.
- [x] **NAR-03 · done** — Preserved the chemistry caveat: meteorology is necessary but not shown to be uniquely dominant.
- [ ] **NAR-04 · later** — Write the air-chemistry bridge in terms of dilution volume, cold-pool retention/ventilation, stability, transport, photolysis, and deposition interfaces.
- [ ] **NAR-05 · later** — Decide whether the SIP-era and January runs add useful context or merely distract from controlled touchstones.
- [ ] **NAR-06 · blocked by LIT-05 and DES-01** — Decide whether the downstream CAMx failure lineage is the Introduction's motivating problem or Discussion context after its report sources and the defensible experiment matrix are known.

### Figures

- [x] **FIG-01 · done** — Regenerated and verified the observation panels from real data.
- [x] **FIG-02 · done** — Regenerated real WRF-versus-observation overlays with no synthetic inputs.
- [ ] **FIG-03 · blocked by ANA-07** — Generate initialization/evolution diagnostics that can distinguish inherited from developed error.
- [ ] **FIG-04 · blocked by ANA-08** — Generate a domain/station-coverage orientation figure.
- [ ] **FIG-05 · later** — Select cross-section and time-height panels only after the primary narrative is frozen.
- [ ] **FIG-06 · later** — Select upper-air panels only if they explain a surface/cold-pool result.
- [x] **FIG-07 · done for the factorial** — The named skill was unavailable, so the documented maintained equivalent ran through the `brc-tools` engine at `89883ceb`, the study TOML, and Slurm; X10 has 63 PNGs and exact-config convergence `13896871` skipped all 730 tasks as current.
- [ ] **FIG-08 · later** — Check print dimensions, fonts, units, color accessibility, captions, and raster resolution.
- [x] **FIG-09 · done for first-draft spine** — Promoted the observed evolution, bulk theta contrast, and common-AGL retention/ventilation PDFs and completed both manifests.
- [ ] **FIG-10 · later** — Retain reproducible supplementary/reviewer-reserve diagnostics outside `figures/`.
- [ ] **FIG-11 · next** — Regenerate the promoted bulk-theta figure on CHPC with the plotted 8 K line labeled as a literature reference rather than a physical “CAP threshold,” then update both manifests and hashes.
- [ ] **FIG-12 · later/conditional** — Build the no-new-WRF L04 factorial effect-size panel only if an expanded architecture gives it a distinct decision beyond Table 2; register and promote it before manuscript use.

### Manuscript and submission

- [x] **MAN-01 · done for first draft** — Drafted the touchstone configuration from canonical inventory rows.
- [x] **MAN-02 · done for first draft** — Drafted observations, sample, domain, window, diagnostic, and dependence treatment.
- [x] **MAN-03 · done for first draft** — Drafted the driving-state result and bounded feedback null from promoted evidence.
- [x] **MAN-04 · done for review draft** — Drafted Discussion around the chosen hypotheses, limitations, and air-chemistry interfaces; scientific and coauthor review remains.
- [x] **MAN-05 · done for review draft** — Drafted concise Conclusions that answer the promoted questions within the five-hour scope.
- [x] **MAN-06 · done for review draft** — Drafted an evidence-gated abstract after reconciling Results and Conclusions.
- [ ] **MAN-07 · next** — Have all authors review author order, names, ORCIDs, affiliations, and corresponding-author details.
- [ ] **MAN-08 · next** — Agree CRediT roles, funding, acknowledgments, conflicts, and data-availability language.
- [ ] **MAN-09 · later** — Replace `paperpile.bib` with the complete manuscript-specific Paperpile export.
- [ ] **MAN-10 · later** — Run an unused/missing citation audit after the export stabilizes.
- [x] **MAN-12 · done for experimental rewrite** — Created the isolated blank-slate manuscript, evidence/argument blueprint, build target, and figure-selection rationale.
- [ ] **MAN-13 · next** — Reconcile the selected expanded architecture with CHPC-only facts and coauthor review before merging selected prose into `main.tex`.
- [ ] **PUB-01 · later** — Obtain Michael's provenance/diagnostic review and Loknath/Seth's chemistry-framing review.
- [ ] **PUB-02 · later** — Build and inspect a dated coauthor-review PDF.
- [ ] **PUB-03 · later** — Compile the allowlisted ZIP in an independent environment with pdfLaTeX, BibTeX, and Ghostscript.
- [ ] **PUB-04 · later** — Confirm the ZIP contains every referenced figure/supplement and none of the working-repo material.
- [ ] **PUB-05 · later** — Submit to MDPI Air only after every required front/back-matter item and author approval is complete.

## Disposition of the original 50 tasks

The original checklist is recoverable with `git show 52d027b:FIRST-50-MICROTASKS.md`.
This mapping prevents useful work from disappearing while refusing unsafe premises.

| Old | Disposition | Current destination |
|---:|---|---|
| 1 | done | The aim is in `main.tex`; refine only after narrative freeze. |
| 2 | done for review draft | `MAN-06`; the abstract now uses only verified Results and exposes remaining limits. |
| 3 | active | `NAR-03`, plus Loknath/Seth review. |
| 4 | active | `LIT-03`. |
| 5 | blocked | `INV-05` and `MAN-01`; recovered candidate configs are not run identities. |
| 6 | blocked | `INV-05--06`; confirm grid and feedback from as-run evidence. |
| 7 | blocked | `INV-05`; do not inherit “75 levels” from folder names alone. |
| 8 | blocked | `INV-05` and `MAN-01`. |
| 9 | blocked | `INV-05`; forcing resolution/cycle needs provenance. |
| 10 | later | `MAN-09`; add the NAM source through Paperpile if cited. |
| 11 | active | `DES-02` and `ANA-12`. |
| 12 | retired as written | `INV-07`; `REF_long` must not be called the Tran-2018 reference run. |
| 13 | blocked | `DES-02` and `MAN-02`; freeze the actual common sample first. |
| 14 | provisional | `ANA-08`; d02 coverage rationale still needs inventory confirmation. |
| 15 | drafted | Final AI disclosure review remains part of coauthor review. |
| 16 | blocked | `ANA-02--03`; old draft numbers are not manuscript evidence. |
| 17 | blocked | `ANA-06`. |
| 18 | blocked | `ANA-02--03`; threshold and magnitude need source/uncertainty checks. |
| 19 | blocked | `FIG-06`; upper-air values enter only if narratively explanatory. |
| 20 | retired as written | `INV-07` and `NAR-05`; comparator identity and window were heterogeneous. |
| 21 | blocked | `ANA-04`. |
| 22 | later | `NAR-05`; required if the heterogeneous comparator survives. |
| 23 | decision | `ANA-08`; d03 can be an interior sensitivity, not the common evaluation. |
| 24 | blocked | `ANA-02--03`, then a manuscript table. |
| 25 | later | `ANA-07` and `NAR-04`; mechanism claims require diagnostics. |
| 26 | retired as blind copy | `FIG-01` followed by promotion gates. |
| 27 | retired as blind copy | `FIG-02`; the inherited overlays were synthetic-contaminated and removed. |
| 28 | retired as blind copy | `FIG-05`. |
| 29 | retired as blind copy | `FIG-06`. |
| 30 | retired as blind copy | `INV-07`, `NAR-05`, and `FIG-05`. |
| 31 | retired | Figures are added only after promotion; no commented template blocks remain. |
| 32 | later | `FIG-08--09` and Results drafting. |
| 33 | replaced | `figures/MANIFEST.md` and `verification/figures/manifest.csv`. |
| 34 | done for review draft | `MAN-04`; the Discussion is drafted with provisional interpretation explicit. |
| 35 | bounded in review draft | `NAR-04` and `MAN-04`; the draft avoids “limiting constraint” and confines the claim to the tested metrics. |
| 36 | done for review draft | `MAN-05`; Conclusions answer the verified short-window questions. |
| 37 | done for review draft | Limitations form the spine of `MAN-04`. |
| 38 | done for review draft | `MAN-06`; the abstract reports verified contrasts and explicit exclusions. |
| 39 | drafted | Revisit keywords after narrative freeze. |
| 40 | active | `MAN-08`. |
| 41 | active | `INV-16` and `MAN-08`. |
| 42 | active | `MAN-08`; the `L?D` placeholder is gone. |
| 43 | active | `MAN-08`; the joke placeholder was removed. |
| 44 | partially done | `MAN-07` requires author confirmation. |
| 45 | later | `LIT-03--04`; old tech-report entries are not automatically retained. |
| 46 | done | External BibTeX/Paperpile path is established as `paperpile.bib`. |
| 47 | later | `MAN-09`. |
| 48 | later | `MAN-10`. |
| 49 | partially done | A clean local pdfLaTeX/BibTeX build passed; Overleaf/independent-package confirmation remains `PUB-03`. |
| 50 | retired | The old first-draft PR path is superseded by protected `main` and `jrl/*` PRs here. |
