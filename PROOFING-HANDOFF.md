# Proofing restart — 6 October 2026

Start here:
```sh
cd /uufs/chpc.utah.edu/common/home/u0737349/worktrees/air-proofs-round1
git status --short --branch
```
Read `AGENTS.md` and `proof-package/intake.json`, then only the source/PDF and evidence needed for the immediate query.

## Resume this chat — terse proof Q&A

John wants a concise back-and-forth through [the proof query catalogue](notes/proof-query-catalogue.md), using the chat to clarify points and brainstorm wording.
Take the query he raises, explain the decision briefly, recommend wording, and apply agreed edits to the working TeX.
Ask only for missing author facts or material choices; do not turn brainstorming into an unrequested full proof pass.
Record explicit author decisions separately from suggestions and technical implementation.

**Worktree:** `/uufs/chpc.utah.edu/common/home/u0737349/worktrees/air-proofs-round1`; **branch:** `jrl/proofs-round1`.
**Only editable draft:** [proof-package/working/air-4472509-done.tex](proof-package/working/air-4472509-done.tex).
John previously edited the received copy accidentally; recovery commit `19d2452` preserves his edits in the working copy and restores the received bundle, and `331b971` records its receipt.
Recheck live status; preserve any newer author edits and resolve source passages by text because line numbers shift.

**Current checkpoint: MDPI05a applied; MDPI06 deferred after John reported no current overlap. Next: MDPI07 production notice, then MDPI08a/b Figure 2 checks. Revisit MDPI06 after MDPI05b/MDPI08c layout changes.**
John’s 6 October instruction is to apply agreed changes, confirm each completed batch in chat, commit with John as author and `Co-Authored-By: Codex <noreply@openai.com>`, and push each commit promptly to `jrl/proofs-round1`. Keep changes minimal and match his writing conventions.
Keep the concise author-led discussion pattern; ask only for missing facts or material choices, and do not repeatedly seek permission for the agreed scope.
Always name the catalogue code when identifying the current or next topic. MDPI05a is applied: John approved moving the station-audit table to the start of Appendix A, retaining its Methods callout; it is now A1. John reports no current Figure 1 overlap; defer MDPI06’s final check until after layout shuffling. Next: MDPI07 production notice, then MDPI08a/b (Figure 2 overlap and marker meanings). MDPI09 is the separate appendix-citation-format query.
The working TeX now states WPS **4.6.0** and cites `Powers2017WRF`, DOI [10.1175/BAMS-D-15-00308.1](https://doi.org/10.1175/BAMS-D-15-00308.1).
John supplied the run-use confirmation; live checks corroborated the WPS README, exact `v4.6.0` tag, official remote and HEAD `335c76a111f84503e8b963abaf273ea8053645bb` at `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_build/WPS`.
The embedded reference is correctly inserted at first citation (reference 31 in this batch); all 47 bibliography entries pass the first-citation-order check. Existing entries needed no reordering.
The working proof built under `texlive/20260330` to 18 pages; pages 5 and 17 were inspected. Publisher query comments and received source hash are preserved; known duplicate Table A5 labels and template warnings remain.
WPS correction commit: `597b0f71b4cb8d2aaa3976e10f2ea21e436877f3`; see the MDPI04b batch in the catalogue for full evidence.
John wants formal in-text software citations with verified DOI-bearing bibliography entries where available and no manuscript footnotes.
The second batch moved all existing retrieval/analysis/plotting citations into Methods, retaining thanks and publisher query comments; the 47 entries and compiled citation numbers now follow the changed first-citation order.
Herbie’s submitted DOI `10.5281/zenodo.4567540` was restored after matching it to developer citation guidance. Polars now cites software DOI `10.5281/zenodo.7697217` (all versions); SynopticPy retains a formal repository reference because no verified DOI was supplied by its citation guidance.
The second build remains 18 pages; pages 5, 6, 15, 17 and 18 were inspected. Software correction commit: `54a7ffd2feb028b67546a8f37ac3208f659f4011`; evidence is recorded under MDPI18 in the catalogue.
Recover actual retrieval/analysis/plotting versions separately; general software DOIs and software-paper versions do not identify the installed releases. MDPI18 remains open for those versions and AI scope; MDPI22’s DOI correction is applied, pending final proof review.
The working source contains no `\footnote{` or `\footnotetext{` calls; retain table `\footnotesize` typography.

The terrain description is now in Methods subsection 2.2, before Table 1. GMTED2010 is expanded as Global Multi-resolution Terrain Elevation Data 2010 and cites Danielson–Gesch (2011), DOI [10.3133/ofr20111073](https://doi.org/10.3133/ofr20111073).
Direct study records confirm default GMTED2010 at 30 arc seconds and the coarse NCAR-distributed WPS GMTED2010 product at 5 arc minutes. The fine source is USGS NED/3DEP 1-arc-second DEMs resampled to custom 3-arc-second WPS terrain; it is not a GMTED2010 product.
Formal NCAR product and USGS collection bibliography entries are added; the USGS catalogue explicitly has no registered DOI for the collection. The `[what?]` placeholder is removed.
The [terrain evidence receipt](proof-package/terrain-source-evidence-20261006.json) records exact archived controls, geogrid selections, July source manifest/build evidence, hashes and limits. The newer `ub-wx` terrain rebuild is a different experiment.
The terrain batch builds to 18 pages; pages 4, 5, 6, 17 and 18 were inspected. All 49 references and compiled citation numbers match first-citation order; original entries, publisher comments and received source are preserved.
The coarse WPS product is a derivative: native USGS GMTED2010 resolutions are 7.5/15/30 arc seconds. Do not claim an undocumented NCAR aggregation method or a new terrain result.
Terrain correction commit: `757a102d1f61b29d11c6e1a26974a9032f63bdc4`; see the MDPI04b terrain batch in the catalogue for evidence. Its remaining scope is the other actual software versions and final response/audit.
John asked about figure organisation order. Recommendation: complete affected prose first (this terrain batch is now done), repair logical first-citation order next (MDPI05a), inspect/refine captions, then finalise figure/table placement (MDPI05b/MDPI08c). The premature Methods callouts to Figures 3 and 6 are now removed, retaining their existing Results callouts. First figure citations are verified as 1–9; the 18-page build and pages 3, 6, 7 and 9 pass affected-page checks. The subsequent table batch resolves appendix citation order; final placement remains open under MDPI05b/MDPI08c.
Figure citation correction commit: `73edb040452d2ae71f8ce787fe6b8a5efba33f3c`; pushed to `origin/jrl/proofs-round1`.
The station table is now A1; unchanged labels automatically give first table citations 1, A1–A6. The table batch builds to 19 pages; pages 5, 8, 10, 12–16 and 19 were inspected. Table data, publisher comments, 49 bibliography entries and received source are preserved. The duplicate heat-deficit label now belongs to A6 and remains open.
John confirmed there is no supplementary material. No such references occur in the working source/PDF or root/delivery manuscripts; preserve the official cited NOAA team name containing “Supplemental” and historical files.
Table correction commit: `4a57a764698ca18119e8beb38bead549ae1b61d7`; pushed to `origin/jrl/proofs-round1`.

For agreed TeX changes, build the working source and inspect affected PDF pages; keep query quotations and Paperpile/template files intact.
The recovery build produced 18 pages; pages 1–5 were inspected, while known duplicate Table A5 labels and unresolved draft placeholders remain.
Commit verified concerns with John's identity and the Codex trailer; push each commit as authorised; root integration, merging and submission need their own authorisation.

## Current editing checkpoint — 6 October 2026

**Edit only [proof-package/working/air-4472509-done.tex](proof-package/working/air-4472509-done.tex).**
John's saved edits were recovered from the received TeX into this working file; the received TeX has been restored to its checksum-verified intake baseline.
Close the received-source editor tab without saving it again, and open the working file.
[proof-package/README.md](proof-package/README.md) and the corrected working README give the same editing path and actual build command.
The source includes John's title, email and emphasis decisions, added ORCID macros and in-progress WPS/terrain placeholders.
See the query catalogue's recovery checkpoint and [recovery receipt](proof-package/edit-recovery-20261006.json) for checks and the backup location.
This migration does not resolve the WPS version/citation or terrain-source provenance.

## Setup state — historical 5 October snapshot

- Branch `jrl/proofs-round1`; created from live-verified GitHub `main` at `5ce57e6`. Setup commits are authorised for push to this branch; verify the live tip after publishing.
- Baseline commit `92b14d2`: all 33 received files copied and committed unchanged, plus intake receipt; byte-for-byte comparison passed.
- Received source/PDF: `proof-package/air-4472509-english/air-4472509-done.{tex,pdf}`; PDF is 18 pages.
- Source has 22 `%MDPI:` comment occurrences (several contain multiple requests) and one `%EE:` title-change note; no corrections or confirmations have been made.
- Source embeds its bibliography. The inherited README's `main.tex`/`main.bbl` instructions are stale.
- Editable source: [proof-package/working/air-4472509-done.tex](proof-package/working/air-4472509-done.tex). The complete working copy was created with all 33 files byte-identical; [creation receipt](proof-package/working-copy.json) records initial hashes.
- The [walkthrough and query catalogue](notes/proof-query-catalogue.md) is the single issue/status register, with a batch plan and all original detailed queries.
- Setup has not corrected proof text or confirmed author facts. No new compilation, full visual proof audit, pruning, merge or journal submission has been performed.

## Next work

1. The [proof query catalogue](notes/proof-query-catalogue.md) now records all 22 `%MDPI:` comments and the `%EE:` title note, with exact quotations, source/PDF locators, proposed responses and outstanding evidence/author facts. The recovery checkpoint now records John’s title, email and emphasis decisions; continue the remaining open work from that register. It also records unassigned highlights and the duplicate Table A5 label.
2. Edit/compile only the existing `proof-package/working/air-4472509-done.tex`; preserve editorial queries and the received baseline. Follow the walkthrough batch plan, committing each verified issue or small related group promptly with documented checks and Codex co-authorship.
3. Verify software versions against the actual analysis provenance; do not insert versions from today's environment. Confirm personal details and editorial acceptance from John/saved decisions.
4. Build `air-4472509-done.tex` in the working directory and inspect all pages against the supplied PDF. Resolve scientific wording against the claim ledger and exact artefacts only.
5. When integration is requested, update root `main.tex`/package deliberately, run required Make checks, inspect PDFs, then use a PR into protected `main`.

## Git and other checkout

- Original checkout remains `/uufs/chpc.utah.edu/common/home/u0737349/gits/latex-jrl-mjd-mdpiair-2026` on `jrl/peer-review-round1`; its uploaded `proof-package/` and `notes/print-review-checklist-2026-09-16.md` remain untracked. Do not remove them during cleanup.
- Local `main` is still `f0c945b`; GitHub `main` was `5ce57e6`. Recheck live remote tips before promotion/pruning.
- PR #8 squash commit `309e532` has the same file tree as `jrl/peer-review-round1` at `5129714`; ancestry reports alone therefore overstate unmerged work. Do not merge every old branch.
- Pruning candidates already reachable from verified `origin/main`: local `jrl/chpc-figure-inventory`, `jrl/consolidate-study-truth`; remote `jrl/paperpile-refresh-20260918`, `prep-final-latex`. Archive other tips before deletion; two old finishing branches have linked worktrees, and the July figure-review tip needs its own check.
- Review decisions/replies live outside Git at `~/reviews/lawson-ozone-wrf-mdpiair-2026/` on the writing host. Earlier roadmap approval statements are not proof acceptance.
