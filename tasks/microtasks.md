# Active microtasks and recovered legacy checklist

This is the granular execution queue beneath `ROADMAP.md`.
Tasks are deliberately small; completing one should change a named artifact or settle a named decision.

Status vocabulary: **next**, **blocked**, **later**, **done**, and **retired**.
Do not mark a scientific task done because prose exists; mark it done only when its evidence gate is met.

## Current tranche: inventory before interpretation

- [ ] **INV-01 · next** — Locate the out-of-band July 9 provenance archive and verify SHA-256 `b616ec6b4ff70f3a36048904d5cad7a99a2563ba4a19fd79198fbf923332a958`.
- [ ] **INV-02 · next** — Map the three JRL touchstone header fingerprints to exact durable archive basenames.
- [ ] **INV-03 · next** — Add one canonical inventory row each for GFS two-way, NAM two-way, and NAM one-way.
- [ ] **INV-04 · next** — Attach the exact as-run namelist and SHA-256 to each touchstone row.
- [ ] **INV-05 · next** — Record WRF version, initialization, valid times, output cadence, grid, vertical levels, physics, forcing, and feedback for each touchstone.
- [ ] **INV-06 · next** — Prove that the NAM one-/two-way pair differs only in feedback, or list every confound.
- [ ] **INV-07 · next** — Fingerprint `REF_long` and state its relationship to the OSIP-era report without calling it Tran-2018 NON.
- [ ] **INV-08 · next** — Mark every observation station assimilated by any comparator so verification independence is visible.
- [ ] **DES-01 · blocked by INV-03--08** — Freeze the primary experiment matrix and write one predicted diagnostic plus one falsifier per comparison.
- [ ] **DES-02 · blocked by DES-01** — Freeze the common domain, station sample, 14--18 UTC window, and spin-up exclusion.
- [ ] **ANA-01 · blocked by DES-02** — Re-reduce promoted runs from raw output using recorded commands and hashes.
- [ ] **ANA-02 · blocked by ANA-01** — Recompute per-run deterministic scores and across-run spread.
- [ ] **ANA-03 · blocked by ANA-02** — Add uncertainty appropriate for a five-hour, autocorrelated sample and record its limitations.
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
- [ ] **ANA-05 · blocked** — Test the GFS-versus-NAM surface and lower-tropospheric difference on the frozen sample.
- [ ] **ANA-06 · blocked** — Test the one-way-versus-two-way feedback difference on the frozen sample.
- [ ] **ANA-07 · blocked** — Diagnose whether differences are inherited at initialization or develop during forecast evolution.
- [ ] **ANA-08 · blocked** — Quantify d02/d03 representativeness without treating missing bench stations as model skill.
- [ ] **ANA-09 · later** — Stratify errors by station elevation and variable; avoid basin means that cancel opposing biases.
- [ ] **ANA-10 · later** — Apply circular statistics to wind direction and state when calm winds make direction uninformative.
- [ ] **ANA-11 · later** — If nudging enters Results, evaluate only at held-out stations or label the dependence explicitly.
- [ ] **ANA-12 · later** — Test sensitivity to the two-hour spin-up decision.
- [ ] **ANA-13 · later** — Compare a no-signal/null period only if the experiment and data can be made genuinely comparable.
- [ ] **ANA-14 · later** — Build a reviewer-reserve table of null, contradictory, and secondary results.

### Literature and narrative

- [ ] **LIT-01 · next** — Convert the completed Matichuk critique into a claim/evidence/caveat row set for the introduction and discussion.
- [ ] **LIT-02 · next** — Build a compact comparison table for Ahmadov, Neemann, Matichuk, Tran, UBAQR-2019/2020, and OSIP-2021: case, model, meteorological lever, chemistry lever, observations, and principal confounds.
- [ ] **LIT-03 · later** — Verify every manuscript citation against the extracted paper passage or source PDF.
- [ ] **LIT-04 · later** — Decide whether report literature belongs in the main article, supplement, or reviewer reserve.
- [ ] **NAR-01 · blocked by DES-01** — Select the primary narrative from the roadmap matrix.
- [ ] **NAR-02 · blocked by NAR-01** — Select at most two secondary narratives and explicitly reject unsupported angles.
- [ ] **NAR-03 · next** — Preserve the chemistry caveat: meteorology is necessary but not shown to be uniquely dominant.
- [ ] **NAR-04 · later** — Write the air-chemistry bridge in terms of dilution volume, stability, transport, photolysis, and deposition interfaces.
- [ ] **NAR-05 · later** — Decide whether the SIP-era and January runs add useful context or merely distract from controlled touchstones.

### Figures

- [ ] **FIG-01 · blocked by ANA-01** — Regenerate the observation panels from the frozen dataset into a temporary/candidate directory.
- [ ] **FIG-02 · blocked by ANA-02** — Regenerate real WRF-versus-observation overlays; confirm no synthetic labels or fixtures.
- [ ] **FIG-03 · blocked by ANA-07** — Generate initialization/evolution diagnostics that can distinguish inherited from developed error.
- [ ] **FIG-04 · blocked by ANA-08** — Generate a domain/station-coverage orientation figure.
- [ ] **FIG-05 · later** — Select cross-section and time-height panels only after the primary narrative is frozen.
- [ ] **FIG-06 · later** — Select upper-air panels only if they explain a surface/cold-pool result.
- [ ] **FIG-07 · later** — Apply `wrf-full-figures` on CHPC when available and record the style version/commit.
- [ ] **FIG-08 · later** — Check print dimensions, fonts, units, color accessibility, captions, and raster resolution.
- [ ] **FIG-09 · later** — Promote accepted files to `figures/` and complete both manifests in the same commit.
- [ ] **FIG-10 · later** — Retain reproducible supplementary/reviewer-reserve diagnostics outside `figures/`.

### Manuscript and submission

- [ ] **MAN-01 · blocked by INV-03--06** — Draft the touchstone Methods configuration from canonical inventory rows.
- [ ] **MAN-02 · blocked by DES-02** — Draft observations, QC, station sample, domain, window, and score definitions.
- [ ] **MAN-03 · blocked by ANA-02** — Draft Results one promoted comparison at a time, including null results.
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
