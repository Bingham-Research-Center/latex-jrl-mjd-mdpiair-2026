# AI guide

MDPI *Air* manuscript: WRF meteorology for the 2 February 2013 Uinta Basin episode. Active phase: proof return.
Start with `hostname -f`, `git status --short --branch`, `git worktree list`, then [PROOFING-HANDOFF.md](PROOFING-HANDOFF.md).

## Active folder and files

Work in `/uufs/chpc.utah.edu/common/home/u0737349/worktrees/air-proofs-round1`, branch `jrl/proofs-round1`.
A worktree is a separate folder on its own branch, sharing Git history with the original checkout. Proof edits reach `main` only through deliberate integration/PR; editing here does not update the other folder’s manuscript.

| Purpose | Path | Rule |
| --- | --- | --- |
| Editable proof | `proof-package/working/air-4472509-done.tex` | Edit/compile here; embedded bibliography is authoritative. |
| Publisher originals | `proof-package/air-4472509-english/` | Preserve all 33 files; baseline `92b14d2`, hashes in `proof-package/intake.json`. |
| Decisions/evidence | `notes/proof-query-catalogue.md` | Master register: 22 MDPI comments plus EE01 and individual subqueries. |
| Final reply/checklist | `PROOFER-REPLY-TABLE.md` | Derived old/new TeX/PDF locators; refresh after source/layout changes. |
| Restart/next action | `PROOFING-HANDOFF.md` | Keep concise and current; identify the next catalogue code. |
| Later integration | `main.tex`, `submission-package/` | Reconcile only when requested; working-source edits do not copy automatically. |

## Proof workflow

- Preserve publisher `%MDPI:`/`%EE:` notes exactly. Add author replies on a new standalone `% JRL: ...` line; do not alter printed text for a comment-only reply.
- Keep changes minimal, British English, one sentence per source line. Preserve official names, identifiers, titles and quotations. No manuscript footnotes or supplementary-material references; retain `\footnotesize`, historical files and the official NOAA team name containing “Supplemental”.
- Saved author decisions govern. Separate author confirmation, verified implementation and outstanding review. Confirm software versions from study records; current installations and software-paper dates do not establish versions used.
- John owns visual PDF review. Do not open/render/screenshot PDFs or images unless requested. Use source, logs, `.aux` and SyncTeX metadata; record readability/page balance as pending until John confirms it.
- After actual TeX changes, build from `proof-package/working` with `latexmk -pdf -interaction=nonstopmode -halt-on-error air-4472509-done.tex` (on CHPC, `module load texlive/20260330`). Check warnings, first-citation order, embedded bibliography numbering, original-note preservation and `git diff --check`. The inherited received README names the wrong source.
- Documentation-only changes need locator/quotation/path/whitespace checks; no routine LaTeX rebuild. Build metadata may be regenerated when required for accurate PDF locators. Working PDF/build outputs remain ignored.
- Sync catalogue, reply table and handoff after each batch. Commit one verified concern or related batch, then push immediately to `jrl/proofs-round1`; John already authorises this pattern.
- Every commit: `John Lawson <john.rob.lawson@googlemail.com>` and `Co-Authored-By: Codex <noreply@openai.com>`. Include query codes, validation and remaining decisions. Status followups may record preceding correction hashes.
- PUB01: John authorises making the repo public after confirmed proof submission. Prepare his selected provenance and verify unauthenticated access when released; timing is already agreed. Until then keep the printed future-release statement accurate.
- Root integration, protected-main PR/merge, final packaging and journal submission remain separate steps. Preserve unrelated dirt, transfer archives and `salvage/`; never prune other worktrees as proof cleanup.

## Read only the needed route

| Task | Read |
| --- | --- |
| Proof/replies | `PROOFING-HANDOFF.md` → `PROOFER-REPLY-TABLE.md` → exact catalogue entry/source |
| Root revision/reviewer decisions | `notes/peer-review-round1-return.md`; `~/reviews/lawson-ozone-wrf-mdpiair-2026/peer-review-decisions.md` → `response-to-reviewers.md` |
| Claims | `notes/claim-evidence-ledger.md` → exact registered artefact |
| Runs/comparisons | `verification/provenance/run-inventory.csv`, `verification/provenance/comparison-inventory.csv` |
| Figures | `verification/figures/manifest.csv` → `figures/MANIFEST.md`; existence: `verification/figures/archive-inventory.md` |
| Literature/bibliography | `notes/resource-map.md`, `notes/literature-synthesis-register.md`, `notes/literature/paperpile-export-list.md` |
| Integration/package | `Makefile`, `figures/submission-files.txt`, `packaging/README-package.md` |
| CHPC/history | `rewrite/CHPC-CODEX-PROMPT.md`; `rewrite/README.md` → `rewrite/HYBRID-GATE-REVIEW.md` |

`README.md`/`ROADMAP.md` describe the earlier revision, not proof-query completion. Superseded drafts and July registers are historical. Avoid broad trees, bulk figures, raw PDFs and `Definitions/` unless the immediate task requires a targeted read.

## Evidence and integration contract

- Architecture C and all five gate outcomes are frozen; failed gates stay failed without new predeclared evidence. X6/X10/X5/X3 are the confirmed floor; other X0–X10 results retain recorded admission/limits. X8 is within-run context, never comparative or basin-export evidence.
- Inventories govern design, archives govern existence, both figure manifests govern admission, and ledger plus exact artefacts govern claims. Every number needs matched runs, domain, stations/footprint, window, inputs and command; distinguish controlled, heterogeneous, observational and literature evidence.
- Chemistry, emissions-inventory adequacy, basin export, inversion depth and multi-day persistence are not demonstrated. Do not separate initial from lateral forcing by wording. Colleague advice remains advisory until author-confirmed.
- Never edit `Definitions/` or hand-edit `paperpile.bib`; John supplies a complete Paperpile replacement. `trang_ref` is not Tran et al. (2018). Cite software/data formally with verified DOIs or URLs and web access dates; preserve original evidence and transfer inputs, with no synthetic output promoted.
- Akamai/Linode owns writing/Git/LaTeX; CHPC owns WRF/data work. Reusable analysis belongs in `../brc-tools`; sibling WRF checkouts do not override paper inventories or immutable CHPC packets. New CHPC dispatch requires a bounded packet and immutable source ref.
- When root integration is requested, reconcile proof edits and bibliography deliberately; run `make final-draft-check`, `make submission-check`, and `make package`. John reviews the PDFs under the current workflow. Production figures must be dual-promoted and allowlisted. Use a `jrl/<topic>` PR into protected `main`.
