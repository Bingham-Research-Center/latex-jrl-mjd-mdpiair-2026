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

**Resume with MDPI04b: WPS citation/version and terrain provenance**, around working-source lines 196–197, containing `[WRF/WPS ref]` and `[what?]`.
John wants formal software bibliography entries, preferably suitable paper/software DOIs, with citations in the text rather than footnotes or acknowledgements.
Verified citation advice, not accepted TeX edits: Powers et al. (2017), DOI [10.1175/BAMS-D-15-00308.1](https://doi.org/10.1175/BAMS-D-15-00308.1), describes WPS; retain Skamarock (2019) for WRF.
WPS version 4.8.0 in the draft is unverified; recover the actual preprocessing version independently of WRF.
A targeted search of the paper's `verification/provenance/` found no recorded WPS version; its run inventory records WRF 4.8.0 only.
John explicitly reiterated the citation policy in this session: formal in-text references, verified paper/software DOIs where available, and no manuscript footnotes.
Recommend software use/citations/verified versions in Methods; moving citations from Acknowledgements remains advice, not an accepted edit.
The working source has no `\footnote{` or `\footnotetext{` calls; retain table `\footnotesize` typography.
Proposed WPS sentence: “The terrain datasets were ingested using the WRF Preprocessing System (WPS), version [verified version] [Powers et al., 2017].”
Next obtain the archived WPS preprocessing/build version record linked to these runs; the citation itself does not establish the version.
This session updated the handoff and catalogue only; no manuscript correction, build or PDF inspection was performed.
Expand GMTED2010 as Global Multi-resolution Terrain Elevation Data 2010; the existing Danielson–Gesch (2011) reference has DOI [10.3133/ofr20111073](https://doi.org/10.3133/ofr20111073).
The inventory records custom `topo_brc_custom_3s`, default 30-arc-second-class terrain, and coarse `topo_gmted2010_5m`; exact upstream sources and preparation still need evidence.
Native GMTED2010 products are 7.5/15/30 arc seconds, so establish the five-arc-minute derivative's provenance.
Last discussion question: what supplied the custom fine terrain, and did the coarse input come from NCAR or John's own processing? No answer yet.

For agreed TeX changes, build the working source and inspect affected PDF pages; keep query quotations and Paperpile/template files intact.
The recovery build produced 18 pages; pages 1–5 were inspected, while known duplicate Table A5 labels and unresolved draft placeholders remain.
Commit verified concerns with John's identity and the Codex trailer; root integration, pushing and submission need their own authorisation.

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
