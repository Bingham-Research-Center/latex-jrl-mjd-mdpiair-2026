# Active microtasks and recovered legacy checklist

This is the granular execution queue beneath `ROADMAP.md`.
Tasks are deliberately small; completing one should change a named artifact or settle a named decision.

Status vocabulary: **next**, **blocked**, **later**, **done**, and **retired**.
Do not mark a scientific task done because prose exists; mark it done only when its evidence gate is met.

## Current tranche: draft from the frozen short-window core

- [ ] **INV-01 · next** — Locate the out-of-band July 9 provenance archive and verify SHA-256 `b616ec6b4ff70f3a36048904d5cad7a99a2563ba4a19fd79198fbf923332a958`.
- [x] **INV-02 · done** — Mapped the three JRL touchstone header fingerprints to exact durable archive basenames.
- [x] **INV-03 · done** — Added canonical inventory rows for GFS two-way, NAM two-way, and NAM one-way.
- [x] **INV-04 · done** — Attached exact as-run namelist hashes to the touchstone rows.
- [x] **INV-05 · done** — Recorded version, initialization, valid times, cadence, grid, levels, physics, forcing, and feedback.
- [x] **INV-06 · done** — Proved that the default-terrain NAM one-/two-way pair differs only in feedback.
- [ ] **INV-07 · later/context** — Fingerprint `REF_long`; it is excluded from the frozen result matrix and must never be called Tran-2018 NON.
- [ ] **INV-08 · later/context** — Mark assimilated stations before any nudging comparison; no nudged run enters the frozen result matrix.
- [x] **DES-01 · done** — Froze X6/X5 as primary and X3/X5 as a bounded secondary null, each with a predicted diagnostic and falsifier.
- [x] **DES-02 · done** — Froze d02, the reporting-station sample, 14--18 UTC, and a two-hour spin-up exclusion.
- [x] **DES-03 · done** — Defined 50--500 m AGL stability and transport wind and stated the five-hour persistence limit.
- [x] **ANA-01 · done for promoted core** — Re-reduced X3/X5/X6 from exact raw archive paths.
- [x] **ANA-02 · done for promoted core** — Recomputed matched surface and vertical summaries.
- [x] **ANA-03 · done for descriptive scope** — Added two-hour circular block sensitivity intervals while explicitly declining formal five-sample inference.
- [x] **MAN-01--03 · done for first draft** — Drafted Methods and Results from the frozen claims and promoted three-figure spine; coauthor/scientific review is next.
- [ ] **COA-01 · next** — Ask Michael for the code/input/command/meaning mapping for each Teams plot still under consideration.
- [ ] **COA-02 · next** — Send the short Trang/Michael run-identity question list only after the machine inventory narrows it.

## Full backlog by workstream

### Provenance and data

- [ ] **INV-09 · next** — Copy stable run IDs into `verification/figures/manifest.csv` for every retained candidate with known inputs.
- [ ] **INV-10 · next** — Mark candidates with unknown inputs as `provisional` or `rejected`; never infer provenance from filenames.
- [ ] **INV-11 · later** — Resolve the exact Tran-2018 NON/ONU/ANU/OAN production directories.
- [ ] **INV-12 · later** — Resolve whether the January `WRF_anlnudge` output is published OAN or a later revision.
- [ ] **INV-13 · later** — Inventory any controlled PBL, vertical-grid, terrain, snow, microphysics, radiation, or stochastic pairs.
- [ ] **INV-14 · later** — Record the d03 interior station set separately from the d02 common evaluation set.
- [ ] **INV-15 · next** — Fix legacy issue 3 by making the January observation-pull command reproducible with explicit dates/output and six authoritative stations.
- [ ] **INV-16 · later** — Decide the public archive/repository for minimal processed data, namelists, commands, and code.

### Analysis and verification

- [ ] **ANA-04 · blocked** — Describe the observed 2 February cold pool using provenance-checked temperature, potential-temperature, and inversion diagnostics.
- [x] **ANA-05 · done** — Tested the GFS-versus-NAM surface, common-AGL stability, and transport-wind differences on the frozen sample.
- [x] **ANA-06 · done** — Bounded the one-way-versus-two-way feedback response on the frozen sample.
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
- [x] **NAR-01 · done** — Selected the driving-state response as the primary narrative.
- [x] **NAR-02 · done** — Selected nest feedback as a bounded secondary null and rejected resolution/nudging from first-draft Results.
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
- [ ] **FIG-07 · later** — Apply `wrf-full-figures` on CHPC when available and record the style version/commit.
- [ ] **FIG-08 · later** — Check print dimensions, fonts, units, color accessibility, captions, and raster resolution.
- [x] **FIG-09 · done for first-draft spine** — Promoted the observed evolution, bulk theta contrast, and common-AGL retention/ventilation PDFs and completed both manifests.
- [ ] **FIG-10 · later** — Retain reproducible supplementary/reviewer-reserve diagnostics outside `figures/`.

### Manuscript and submission

- [x] **MAN-01 · done for first draft** — Drafted the touchstone configuration from canonical inventory rows.
- [x] **MAN-02 · done for first draft** — Drafted observations, sample, domain, window, diagnostic, and dependence treatment.
- [x] **MAN-03 · done for first draft** — Drafted the driving-state result and bounded feedback null from promoted evidence.
- [ ] **MAN-04 · blocked by NAR-01** — Draft Discussion around the chosen hypotheses, limitations, and air-chemistry interfaces.
- [ ] **MAN-05 · later** — Draft concise Conclusions that answer promoted questions one-for-one.
- [ ] **MAN-06 · later** — Write the abstract only after Results and Conclusions stabilize.
- [ ] **MAN-07 · next** — Have all authors review author order, names, ORCIDs, affiliations, and corresponding-author details.
- [ ] **MAN-08 · next** — Agree CRediT roles, funding, acknowledgments, conflicts, and data-availability language.
- [ ] **MAN-09 · later** — Replace `paperpile.bib` with the complete manuscript-specific Paperpile export.
- [ ] **MAN-10 · later** — Run an unused/missing citation audit after the export stabilizes.
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
| 2 | blocked | `MAN-06`; principal findings require verified Results. |
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
| 34 | blocked | `MAN-04` after narrative freeze. |
| 35 | blocked | `NAR-04` and `MAN-04`; avoid “limiting constraint” without evidence. |
| 36 | later | `MAN-05`. |
| 37 | later | Limitations are a required spine of `MAN-04`. |
| 38 | later | `MAN-06`; no placeholder abstract is retained. |
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
