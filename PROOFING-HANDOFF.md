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

**Current checkpoint: MDPI05b/MDPI08c source placement corrected by moving unchanged Figure 2 after Figure 1 within the observations subsection. Sizes retained. Next: John’s visual placement/size and MDPI06/MDPI08a/MDPI11/MDPI16a overlap checks. PUB01 planned public release and final proof/return integration remain pending.**
John’s latest workflow instruction: avoid loading PDFs into Codex to save tokens; John will inspect them and report visual issues. Continue source, build-log and auxiliary-file checks; do not use `view_image`, screenshots or PDF rendering unless requested. Record visual review as pending until John reports it. Figure/table size changes need a specific observed problem, not an inferred visual sign-off.
John’s 6 October instruction is to apply agreed changes, confirm each completed batch in chat, commit with John as author and `Co-Authored-By: Codex <noreply@openai.com>`, and push each commit promptly to `jrl/proofs-round1`. Keep changes minimal and match his writing conventions. Author replies use a new standalone `% JRL: ...` line, preserving publisher notes and printed formatting.
Keep the concise author-led discussion pattern; ask only for missing facts or material choices, and do not repeatedly seek permission for the agreed scope.
Always name the catalogue code when identifying the current or next topic. MDPI05a is applied: John approved moving the station-audit table to the start of Appendix A, retaining its Methods callout; it is now A1. John reports no current Figure 1 overlap; defer MDPI06’s final check until after layout shuffling. MDPI07 now has the authorised reply on its own `% JRL:` line beneath the publisher note; the 19-page build and full extracted proof text are unchanged, and page 4 was inspected. MDPI08b now explains the verified marker shapes in one caption sentence and retains the hollow-marker coverage explanation. The 19-page build passes; pages 5 and 6 were inspected, with only page 5’s extracted text changed. John authorised deferring MDPI08a/c; the catalogue records all deferred layout checks. MDPI09 is now confirmed with a standalone `% JRL:` reply. MDPI10 changes only descriptive pressure subscripts/differential typography and adds its reply; the 19-page build, unchanged extracted text and pages 5, 6, 8 and 14 pass checks. MDPI11/MDPI16a are now deferred under John’s instruction to batch straightforward choices. MDPI12–16 panel, shading and dashed-line explanations are verified against immutable plotting records and added; MDPI17 table rules are confirmed. The working proof builds to 19 pages; pages 8–11 and 15 were inspected. All plot assets, table data, 49 bibliography entries and publisher notes are unchanged. The duplicate continued-Table-A6 label is removed and its warning cleared. See the catalogue for exact evidence and checks.
Caption/table correction commit: `10f19a3d6b0d44804d5f8bf160269c577de99e53`; pushed to `origin/jrl/proofs-round1`.
MDPI19–21 and the McKinney highlight are verified against original publisher/conference records and retained; MDPI22 now has the standalone DOI-retention reply. This six-comment confirmation batch changes no printed source or reference metadata; it builds to 19 pages, with reference pages 17–19 inspected. Primary-source links and exact PDF-cover evidence are in the catalogue.
Bibliography confirmation commit: `7f14149aa26328cddea07b463c95af9e9b5425b1`; pushed to `origin/jrl/proofs-round1`.
John explicitly confirmed the bundled MDPI01 details and instructed displaying all four ORCIDs. Added Loknath/Seth’s saved C/D macros to their author names and a standalone author reply; 19-page build and page-1 icon/link checks passed.
Author-detail correction commit: `b9dd679eb99d0fc806f504a7772aa1bb3573846d`; pushed to `origin/jrl/proofs-round1`.
Software-version correction commit: `999278208a89ff41d4e837e12ca08cf4d6c38548`; pushed to `origin/jrl/proofs-round1`. Working proof remains 19 pages; pages 5–7 inspected and only pages 6–7 change in extracted text. All first-citation orders and original tables/assets/bibliography are preserved.
MDPI18 AI/PUB01 correction commit: `787955008e0941db1af7057436991c6675dd7502`; pushed to `origin/jrl/proofs-round1`. The working proof builds to 19 pages; pages 16–19 inspected, with extracted-text changes limited to those pages. All 49 references/compiled numbers and figure/table first-citation orders are unchanged; original publisher comments and received source are preserved. Public release is planned, not yet performed.
MDPI05b/MDPI08c placement batch: moved unchanged Figure 2 after Figure 1 in the observations subsection; widths/captions/assets retained. The 19-page build and source/auxiliary checks pass; Figure 2 is now page 4 and Table 1 page 5. No agent PDF loading/rendering/inspection. John’s compact checklist is under MDPI05b in the catalogue.
MDPI07 reply commit: `120a6ec0ca486bc0be523bec5364f88ec636e9d2`; pushed to `origin/jrl/proofs-round1`. MDPI09 is the separate appendix-citation-format query.
MDPI08b caption correction commit: `b303e7453675d83171bc692b2207a831def17187`; pushed to `origin/jrl/proofs-round1`.
MDPI09/MDPI10 correction commit: `0bd3be2e7957bc9654abcb9a53d68935d56c2d52`; pushed to `origin/jrl/proofs-round1`.
The working TeX now states WPS **4.6.0** and cites `Powers2017WRF`, DOI [10.1175/BAMS-D-15-00308.1](https://doi.org/10.1175/BAMS-D-15-00308.1).
John supplied the run-use confirmation; live checks corroborated the WPS README, exact `v4.6.0` tag, official remote and HEAD `335c76a111f84503e8b963abaf273ea8053645bb` at `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_build/WPS`.
The embedded reference is correctly inserted at first citation (reference 31 in this batch); all 47 bibliography entries pass the first-citation-order check. Existing entries needed no reordering.
The working proof built under `texlive/20260330` to 18 pages; pages 5 and 17 were inspected. Publisher query comments and received source hash are preserved; known duplicate Table A5 labels and template warnings remain.
WPS correction commit: `597b0f71b4cb8d2aaa3976e10f2ea21e436877f3`; see the MDPI04b batch in the catalogue for full evidence.
John wants formal in-text software citations with verified DOI-bearing bibliography entries where available and no manuscript footnotes.
The second batch moved all existing retrieval/analysis/plotting citations into Methods, retaining thanks and publisher query comments; the 47 entries and compiled citation numbers now follow the changed first-citation order.
Herbie’s submitted DOI `10.5281/zenodo.4567540` was restored after matching it to developer citation guidance. Polars now cites software DOI `10.5281/zenodo.7697217` (all versions); SynopticPy retains a formal repository reference because no verified DOI was supplied by its citation guidance.
The second build remains 18 pages; pages 5, 6, 15, 17 and 18 were inspected. Software correction commit: `54a7ffd2feb028b67546a8f37ac3208f659f4011`; evidence is recorded under MDPI18 in the catalogue.
MDPI18 now states the archived analysis versions (NumPy 2.5.0, SciPy 1.18.0, pandas 3.0.3, Polars 1.42.0, xarray 2026.4.0) and Matplotlib 3.11.0, with a separate sentence for the later Figures 4/5 label revisions using 3.10.8. The catalogue pins the exact study receipts/stages. Herbie 2026.3.0/SynopticPy 2026.6.0 are now supplied from the recovered CHPC brc-tools-2026 installation, linked to the registered observation-retrieval executable. The software-version evidence receipt pins local files/hashes/dates and attribution limits. John’s 1 June release fallback was not needed (it would have selected older SynopticPy 2025.9.0). John subsequently supplied Claude Opus 5/Fable 5 and Codex Sol 6/Astra 6; the disclosure now uses the verified vendor names and records CLI use in a custom environment. John clarified Gemini CLI labels as `gemini-3.5-flash` and `gemini-3.1-pro`; the disclosure now gives Gemini 3.5 Flash and 3.1 Pro for brainstorming. Google corroborates the readable model names; the Pro CLI label is not independently mapped to a dated/preview snapshot. No model-history or per-session publication claim is made. GitHub still reports this repository as private; Data Availability now records planned public release of the repository and selected provenance. PUB01 tracks selection, release review and public-access/citation verification. MDPI22’s DOI correction/reply is applied, pending final proof review.
The working source contains no `\footnote{` or `\footnotetext{` calls; retain table `\footnotesize` typography.

The terrain description is now in Methods subsection 2.2, before Table 1. GMTED2010 is expanded as Global Multi-resolution Terrain Elevation Data 2010 and cites Danielson–Gesch (2011), DOI [10.3133/ofr20111073](https://doi.org/10.3133/ofr20111073).
Direct study records confirm default GMTED2010 at 30 arc seconds and the coarse NCAR-distributed WPS GMTED2010 product at 5 arc minutes. The fine source is USGS NED/3DEP 1-arc-second DEMs resampled to custom 3-arc-second WPS terrain; it is not a GMTED2010 product.
Formal NCAR product and USGS collection bibliography entries are added; the USGS catalogue explicitly has no registered DOI for the collection. The `[what?]` placeholder is removed.
The [terrain evidence receipt](proof-package/terrain-source-evidence-20261006.json) records exact archived controls, geogrid selections, July source manifest/build evidence, hashes and limits. The newer `ub-wx` terrain rebuild is a different experiment.
The terrain batch builds to 18 pages; pages 4, 5, 6, 17 and 18 were inspected. All 49 references and compiled citation numbers match first-citation order; original entries, publisher comments and received source are preserved.
The coarse WPS product is a derivative: native USGS GMTED2010 resolutions are 7.5/15/30 arc seconds. Do not claim an undocumented NCAR aggregation method or a new terrain result.
Terrain correction commit: `757a102d1f61b29d11c6e1a26974a9032f63bdc4`; see the MDPI04b terrain batch in the catalogue for evidence. The subsequent MDPI18 batch supplies the other software versions; complete response/final audit remain pending.
John asked about figure organisation order. Recommendation: complete affected prose first (this terrain batch is now done), repair logical first-citation order next (MDPI05a), inspect/refine captions, then finalise figure/table placement (MDPI05b/MDPI08c). The premature Methods callouts to Figures 3 and 6 are now removed, retaining their existing Results callouts. First figure citations are verified as 1–9; the 18-page build and pages 3, 6, 7 and 9 pass affected-page checks. The subsequent table batch resolves appendix citation order; final placement remains open under MDPI05b/MDPI08c.
Figure citation correction commit: `73edb040452d2ae71f8ce787fe6b8a5efba33f3c`; pushed to `origin/jrl/proofs-round1`.
The station table is now A1; unchanged labels automatically give first table citations 1, A1–A6. The table batch builds to 19 pages; pages 5, 8, 10, 12–16 and 19 were inspected. Table data, publisher comments, 49 bibliography entries and received source are preserved. The duplicate heat-deficit label moved to A6; the later MDPI11–17 batch removes only its continued-part definition.
John confirmed there is no supplementary material. No such references occur in the working source/PDF or root/delivery manuscripts; preserve the official cited NOAA team name containing “Supplemental” and historical files.
Table correction commit: `4a57a764698ca18119e8beb38bead549ae1b61d7`; pushed to `origin/jrl/proofs-round1`.

For agreed TeX changes, build the working source and check logs/source/auxiliary records; John now owns affected-page visual inspection. Keep query quotations and Paperpile/template files intact.
The recovery build produced 18 pages; pages 1–5 were inspected, while known duplicate Table A5 labels and unresolved draft placeholders remain.
Commit verified concerns with John's identity and the Codex trailer; push each commit as authorised; root integration, merging and submission need their own authorisation.

## Current editing checkpoint — 6 October 2026

**Edit only [proof-package/working/air-4472509-done.tex](proof-package/working/air-4472509-done.tex).**
John's saved edits were recovered from the received TeX into this working file; the received TeX has been restored to its checksum-verified intake baseline.
Close the received-source editor tab without saving it again, and open the working file.
[proof-package/README.md](proof-package/README.md) and the corrected working README give the same editing path and actual build command.
The source includes John's title, email and emphasis decisions and added ORCID macros; WPS/terrain placeholders have since been resolved, and the catalogue records subsequent corrections.
See the query catalogue's recovery checkpoint and [recovery receipt](proof-package/edit-recovery-20261006.json) for checks and the backup location.
The migration itself did not resolve WPS/terrain provenance; the subsequent verified batches above did.

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

1. The [proof query catalogue](notes/proof-query-catalogue.md) now records all 22 `%MDPI:` comments and the `%EE:` title note, with exact quotations, source/PDF locators, proposed responses and outstanding evidence/author facts. The recovery checkpoint now records John’s title, email and emphasis decisions; continue the remaining open work from that register. It also records the completed AI disclosure and the resolved duplicate continued-table label.
2. Edit/compile only the existing `proof-package/working/air-4472509-done.tex`; preserve editorial queries and the received baseline. Follow the walkthrough batch plan, committing each verified issue or small related group promptly with documented checks and Codex co-authorship.
3. Software versions and personal details are now recorded with evidence/author confirmation. MDPI18 model names/CLI use are supplied; settle the planned publication scope under PUB01; MDPI04a already retains John’s saved limitation reply. Audit its scope and preserve all recorded attribution limits.
4. Build `air-4472509-done.tex` in the working directory; Codex checks source/logs/auxiliary records and John visually inspects the PDFs. Resolve scientific wording against the claim ledger and exact artefacts only.
5. When integration is requested, update root `main.tex`/package deliberately, run required Make checks, inspect PDFs, then use a PR into protected `main`. Worktree/working-source edits do not copy automatically to `main`; the saved proof corrections need this explicit integration after the proof pass is ready, as explained to John on 6 October.

## Git and other checkout

- Original checkout remains `/uufs/chpc.utah.edu/common/home/u0737349/gits/latex-jrl-mjd-mdpiair-2026` on `jrl/peer-review-round1`; its uploaded `proof-package/` and `notes/print-review-checklist-2026-09-16.md` remain untracked. Do not remove them during cleanup.
- Local `main` is still `f0c945b`; GitHub `main` was `5ce57e6`. Recheck live remote tips before promotion/pruning.
- PR #8 squash commit `309e532` has the same file tree as `jrl/peer-review-round1` at `5129714`; ancestry reports alone therefore overstate unmerged work. Do not merge every old branch.
- Pruning candidates already reachable from verified `origin/main`: local `jrl/chpc-figure-inventory`, `jrl/consolidate-study-truth`; remote `jrl/paperpile-refresh-20260918`, `prep-final-latex`. Archive other tips before deletion; two old finishing branches have linked worktrees, and the July figure-review tip needs its own check.
- Review decisions/replies live outside Git at `~/reviews/lawson-ozone-wrf-mdpiair-2026/` on the writing host. Earlier roadmap approval statements are not proof acceptance.
