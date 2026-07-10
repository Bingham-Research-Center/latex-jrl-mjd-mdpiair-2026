# Planning and evidence resource map

Use this map to mine selectively.
File presence is not evidence quality, and repeated claims across files are not independent corroboration.

## Highest-value sources

| Resource | What to harvest | Important caution |
|---|---|---|
| `verification/provenance/CHPC-WRF-INVENTORY-RESULTS.md` and the out-of-band `wrf_provenance_20260709T224907Z.tgz` | Archive manifests, eight candidate configs, and 16 local header fingerprints | The tarball is sensitive working evidence and is not committed; reconcile it rather than summarizing filenames. |
| `verification/provenance/WRF-RUN-TO-REPORT-MAP.md` | Run-lineage contradictions and questions | It contains proposals and unresolved joins, not source truth. |
| `verification/data/*.csv` and `verification/figures/candidates/` | Existing score/figure longlist and cheap diagnostic leads | Several comparisons are heterogeneous; four synthetic overlay files were removed. Recompute promoted results. |
| `~/reviews/matichuk-cmaq-ub-2017/critique.md` | Completed critical audit of inventory tuning, WRF/CMAQ albedo decoupling, deposition, and attribution limits | Read before asserting chemistry or inventories are relatively adequate. |
| `~/reviews/{ahmadov-ubwo-2015-acp,neemann-2015-UB-CAP,tran-2018-fdda}/critique.md` | Experiment-design strengths, confounds, and portable checks | Use `_paper.md` only when the critique points to a specific source passage. |
| `~/reviews/synth-ubaqr19+ubaqr20+tran/synthesis.md` | Cross-study contradictions, chemistry-versus-meteorology ordering, and unrun factorial experiments | Strongly challenges a meteorology-only causal story; some report evidence is itself incomplete. |
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
