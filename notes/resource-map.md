# Planning and evidence resource map

Use this map to mine selectively.
File presence is not evidence quality, and repeated claims across files are not independent corroboration.

## Source-of-truth hierarchy

This repository decides what supports the paper; sibling repositories and external storage retain the machinery and large artifacts.
When two records disagree, use the authority named below and record the discrepancy rather than silently choosing the more convenient value.

| Question or artifact | Canonical paper-facing record | Technical or external authority | Rule |
|---|---|---|---|
| Manuscript claim and status | `notes/claim-evidence-ledger.md` | Exact cited analysis, figure, table, or literature source | Prose in `main.tex` does not validate itself. |
| Scientific framing and experiment role | `ROADMAP.md` and `notes/narrative-and-hypotheses.md` | Controlled-comparison evidence named in the claim ledger | Separate the frozen result core from context and reviewer reserve. |
| WRF run identity used by the paper | `verification/provenance/run-inventory.csv` | As-run output headers, namelist fingerprints, and durable archive/control packet | Never infer identity from a directory name or candidate namelist. |
| Runnable WRF case or namelist change | Pointer from the run inventory or provenance record | `../brc-wrf/brc-cases/` and the immutable archived control packet | `brc-wrf` owns execution; this repo records the verified paper-facing identity. |
| Manuscript-specific analysis or plot | `verification/scripts/` plus its provenance/manifest row | Raw inputs named by that record | Keep one reproducible command and the source commit or hash. |
| Reusable download, reduction, verification, or plotting behavior | Pointer from this repo | `../brc-tools` code, tests, and documentation | General code changes belong in `brc-tools`, not in a paper-specific wrapper. |
| Raw WRF, NWP, observation, or cache data | Exact path and fingerprint in a provenance or manifest record | CHPC archive/scratch or the named data provider | Do not commit bulk data; tracked CSVs are derived evidence, not raw truth. |
| Candidate or diagnostic image | `verification/figures/manifest.csv` | Generator, inputs, and external archive path recorded in its row | Presence or visual polish alone is not provenance. |
| Figure admitted to the manuscript | `figures/MANIFEST.md` | Matching verified row in `verification/figures/manifest.csv` | Only `promoted` files may enter `main.tex`. |
| Bibliographic identity | Complete Paperpile export in `paperpile.bib` | Publisher record or source publication | Do not invent or hand-maintain replacement BibTeX entries. |
| Literature interpretation or critique | `notes/literature-synthesis-register.md` and the relevant claim-ledger row | Named critique/extract under `~/reviews`, then the underlying publication | Critiques locate risks and passages; cite the underlying source. |
| Paper-specific full-figure configuration and archive catalogue | Temporary pointer to `../wrf-nudge-ozone-air2026` during consolidation | `../brc-tools` figure engine and the external figure archive | Migrate the study TOMLs and compact catalogue here before deprecating the donor repo. |

### Temporary consolidation rule

`../wrf-nudge-ozone-air2026` currently contains a mixture of unique paper-specific assets and duplicated status/routing prose.
Treat it as read-only donor evidence during consolidation: migrate and verify one coherent concern at a time, update every surviving pointer, and preserve its Git history until the final deprecation check passes.

## Highest-value sources

| Resource | What to harvest | Important caution |
|---|---|---|
| `verification/provenance/CHPC-WRF-INVENTORY-RESULTS.md` and the out-of-band `wrf_provenance_20260709T224907Z.tgz` | Archive manifests, eight candidate configs, and 16 local header fingerprints | The tarball is sensitive working evidence and is not committed; reconcile it rather than summarizing filenames. |
| `verification/provenance/WRF-RUN-TO-REPORT-MAP.md` | Run-lineage contradictions and questions | It contains proposals and unresolved joins, not source truth. |
| `verification/data/*.csv` and `verification/figures/candidates/` | Existing score/figure longlist and cheap diagnostic leads | Several comparisons are heterogeneous; four synthetic overlay files were removed. Recompute promoted results. |
| `~/reviews/matichuk-cmaq-ub-2017/critique.md` | Completed critical audit of inventory tuning, WRF/CMAQ albedo decoupling, deposition, and attribution limits | Read before asserting chemistry or inventories are relatively adequate. |
| `~/reviews/{ahmadov-ubwo-2015-acp,neemann-2015-UB-CAP,tran-2018-fdda}/critique.md` | Experiment-design strengths, confounds, and portable checks | Use `_paper.md` only when the critique points to a specific source passage. |
| `notes/literature-synthesis-register.md` | Compact register of all four `~/reviews/synth-*` collections, what each critiques, manuscript uses, and citation gaps | Read this before opening an individual synthesis. |
| `~/reviews/synth-ahmadov+neemann+tran/synthesis.md` | Peer-reviewed 2013 emissions/meteorology/FDDA triad and its missing cross-lever experiments | Shared episode does not make the studies a controlled factorial comparison. |
| `~/reviews/synth-bingham+saprc+tran/synthesis.md` | BRC 2015--2023 configuration lineage, disclosure gaps, version/snow questions, and lost ice-fog fix | Two members are reports and one is a section extract; bibliography entries are still missing. |
| `~/reviews/synth-ubaqr19+ubaqr20+tran/synthesis.md` | Nudging-to-chemistry research arc, chemistry-versus-meteorology tension, and unrun best-met/best-mechanism crossing | Strongly challenges a meteorology-only causal story; platforms and emissions change across the arc. |
| `~/reviews/synth-ramboll+topdown+rmp/synthesis.md` | Downstream CAMx failure modes, precursor-based ventilation diagnosis, regime-bound mechanism sensitivity, and retention diagnostics | The members are related report slices spanning 2013 and 2019; run identities and bibliography entries remain unresolved. |
| `~/reviews/wrf-ozone-studies/_extracts/{ramboll-racm2-2023,topdown-inventory-s9_6-9_7,rmp-2022-sIIIB}-critique.md` | Member-level checks behind the downstream synthesis | Open only the critique needed for a named claim, then verify the exact extracted passage before manuscript use. |
| `~/reviews/wrf-ozone-studies/seth-notes-on-papers.md` | Seth's intended literature order and exact high-value report sections | This is argument scaffolding, not an evidence substitute. |
| `~/gits/ceidwad/notes/wrf-run-publication-lookup.md` | The best current run/work/location/lineage register and human confirmation list | Paths still name the legacy repo and some joins remain tentative. |
| `~/gits/ceidwad/notes/meeting-minutes/michael-mdpi-wrf-june29.md` | Ownership, intended comparisons, and Michael's plot/code handoff | Meeting intent may have been superseded by later provenance findings. |
| `~/gits/ceidwad/notes/braindumps/DISCUSS-MICHAEL-TRANG-DATA.md` | Questions to resolve with Michael/Trang and candidate configuration details | The July 7 correction explicitly overturns the earlier “free-running inversion” interpretation. |
| `~/gits/ceidwad/tasks/doing/T-20260427-02--wrf-2013-ozone-study.md` | Project boundary, ownership, and coordination history | Dates and submission targets are stale; preserve decisions, not urgency language. |
| `~/gits/brc-tools/brc_tools/verify/` | Deterministic scoring and alignment implementation used by the inherited pipeline | It is a verification library, not the canonical WRF figure-style source. |

The `~/reviews` and most `~/gits/ceidwad` paths normally exist only on the Akamai/Linode writing host.
On CHPC, use this repository's inventory contracts and the durable WRF archive instead.

## Legacy repository archaeology

The old to-do material was removed from the working tree in commit `3e21a28` during the barebones reset; it remains in history.

Useful recovery commands:

```bash
git show 52d027b:FIRST-50-MICROTASKS.md
git show 7009711:main.tex
git show 7009711:CLAUDE.md
git log --all -- verification/
```

The 50-item list mainly indexed placeholders in the scaffolded legacy manuscript.
Its safe tasks have been re-expressed in `tasks/microtasks.md`; its draft numbers, blind figure-copy tasks, literal Tran attribution, inline-bibliography decision, and old PR step are explicitly retired or gated there.

The legacy GitHub repository adds another planning layer:

- issue 3 records the broken January baseline reproduction defaults and station/path caveats;
- PR 12 records the touchstone pipeline, claimed first-pass results, spin-up decision, and d02/d03 coverage issue;
- PR 13 records the provenance-recovery intent and warns that candidate namelists were not run identities.

Treat PR prose as a claim index and use the current ledger before reusing a result.

## Lower-cost mining order

1. Read `ROADMAP.md`, then the relevant ledger/task row.
2. Open the critique or provenance summary named by that row.
3. Inspect the exact CSV, script, extracted paper passage, or inventory fingerprint.
4. Open a PDF, raw WRF output, bulk image tree, or full review corpus only when the preceding source leaves a named gap.
5. Record any new fact in the run inventory, figure manifest, or claim ledger before drafting prose.

This order prevents repeated whole-corpus ingestion while keeping every important source reachable.

## Useful resources still to obtain

- John's CHPC inventory export in the canonical CSV schema, including exact run basenames and as-run namelist hashes.
- Michael's mapping from each Teams figure to code, input run, command, and intended interpretation.
- The exact production identities of Tran's NON/ONU/ANU/OAN runs and the SIP `REF_long` configuration.
- A decision on held-out observations for any nudging comparison.
- Coauthor-confirmed CRediT roles, funding, acknowledgments, data-release constraints, and final author metadata.
- A manuscript-specific Paperpile export after the narrative and citation set stabilize.
