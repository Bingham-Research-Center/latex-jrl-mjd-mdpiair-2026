# AI guide

Private MDPI *Air* manuscript: WRF meteorology for the 2 February 2013 Uinta Basin episode.
Cold start: `hostname -f`, `git status --short --branch`, `git worktree list`, then one task route below.
For the active proofing task, read `PROOFING-HANDOFF.md` first; `README.md`, `ROADMAP.md` and the return record describe the earlier revision, not proof-query completion.

## Active proofing

- Branch: `jrl/proofs-round1`; worktree: `/uufs/chpc.utah.edu/common/home/u0737349/worktrees/air-proofs-round1`.
- Received baseline: commit `92b14d2`, directory `proof-package/air-4472509-english/`; hashes and intake state: `proof-package/intake.json`.
- Preserve every received file unchanged. The complete working copy now exists at `proof-package/working/`; `proof-package/working-copy.json` records all 33 initial file hashes.
- Edit and compile only `proof-package/working/air-4472509-done.tex`. The received source is an immutable reference; supplied PDF: `air-4472509-done.pdf` (18 pages). The received README incorrectly names `main.tex` and `main.bbl`; the source embeds `thebibliography`.
- There are 22 `%MDPI:` comment occurrences plus one `%EE:` title note, some with multiple requests. Catalogue each request before resolving it; preserve quotations and record proposed responses/status separately.
- Keep proof corrections in the working copy until integration is requested. Confirm author facts from saved decisions or John; software versions must come from the recorded analysis environment, not the current shell.
- Compile the working copy with `latexmk -pdf -interaction=nonstopmode -halt-on-error air-4472509-done.tex`; inspect the resulting PDF. Root Make targets do not validate this proof source.
- When integrating into root `main.tex`, run the repository checks and package refresh below. Check embedded references explicitly; BibTeX changes alone do not update them.
- Work only on `jrl/proofs-round1` in the proof worktree. Push setup/correction commits to that branch when authorised; root integration, merging and journal submission are separate actions. Recheck live refs and worktrees before any authorised cleanup.


## Proof layout and commit logic

| Purpose | Path in the proof worktree | Rule |
| --- | --- | --- |
| Editable manuscript to return | `proof-package/working/air-4472509-done.tex` | Apply accepted proof corrections here. |
| Issue walkthrough and exact query register | `notes/proof-query-catalogue.md` | Start with the batch plan; retain EE01/MDPI01–22 quotations and individual subqueries. |
| Received source, PDF and supporting files | `proof-package/air-4472509-english/` | Preserve unchanged, including all original compilation artefacts. |
| Working-copy creation receipt | `proof-package/working-copy.json` | Initial hashes document the copy; they are not hashes of later corrected files. |
| Session restart and host boundaries | `PROOFING-HANDOFF.md` | Keep current state, editable path and next action accurate. |
| Repository manuscript and delivery copy | `main.tex`, `submission-package/` | Update only when integration is requested. |

The walkthrough is the single status register: use its batches to plan work and its individual entries to record decisions.
After each verified issue or small related batch, record the applied change, exact evidence, validation, proposed/final reply, remaining author decision and correction commit hash.
Do not mark proposed replies as accepted or technical implementation as author confirmation.
Commit promptly after validation rather than accumulating a full proof pass.
Every commit in this workflow must use John's identity and `Co-Authored-By: Codex <noreply@openai.com>`, including documentation, copy setup and later corrections.
Commit subjects should identify the concern; bodies should name query IDs, changes, evidence/checks and unresolved decisions.
A follow-up status/documentation commit may record the preceding correction hash; do not claim an unbuilt correction passed PDF inspection.
Track the working TeX and supporting inputs, including cached logo conversions; compilation outputs and the working manuscript PDF stay ignored.
Documentation/copy setup needs quotation, path, checksum and whitespace checks.
Proof corrections need the working-source build and affected-page inspection; root Make checks apply at repository integration.

## Routes

| Task | Read |
|---|---|
| Proofs | `PROOFING-HANDOFF.md` → `notes/proof-query-catalogue.md` → working source and exact evidence for the immediate query |
| Manuscript/revision | `notes/peer-review-round1-return.md` → `main.tex` |
| Reviewer decisions/replies | `~/reviews/lawson-ozone-wrf-mdpiair-2026/peer-review-decisions.md` → `response-to-reviewers.md`; saved author decisions govern |
| Claims | `notes/claim-evidence-ledger.md` → exact registered artefact |
| Runs/comparisons | `verification/provenance/run-inventory.csv`, `verification/provenance/comparison-inventory.csv` |
| Figures | `verification/figures/manifest.csv` → `figures/MANIFEST.md`; archive existence: `verification/figures/archive-inventory.md` |
| Literature/bibliography | `notes/resource-map.md`, `notes/literature-synthesis-register.md`, `notes/literature/paperpile-export-list.md` |
| Build/package | `Makefile`, `figures/submission-files.txt`, `packaging/README-package.md` |
| CHPC dispatch | `rewrite/CHPC-CODEX-PROMPT.md`; new bounded packet and immutable source ref required |
| History/gates | `rewrite/README.md` → `rewrite/HYBRID-GATE-REVIEW.md`; July task register is historical |

Open only the route needed. Avoid broad trees, bulk figures, raw PDFs, legacy checklists and `Definitions/` unless required.
Root `main.tex` is the repository integration target; the active proof source is identified above. `drafts/jrl_manuscript.tex` is the superseded author draft;
`_manuscript_v3.tex` is the over-inclusive caretaker snapshot and `_manuscript_test.tex` is experimental.

## Evidence contract

- Architecture C is frozen; all five gates ran. Failed gates stay failed without new predeclared evidence.
- Inventories govern design, archive records govern existence, both manifests govern figure admission, and the ledger plus exact artefacts govern claims.
- X6/X10/X5/X3 are the confirmed floor. Other X0–X10 results require their recorded admission and limits; X8 is within-run context, never comparative or basin-export evidence.
- Every number needs matched runs, domain, stations/footprint, window, inputs and command. Separate controlled, heterogeneous, observational and literature evidence.
- Chemistry, emissions-inventory adequacy, basin export, inversion depth and multi-day persistence are not demonstrated. Do not separate initial from lateral forcing by wording.
- Preserve reviewer quotations and author decisions. Colleague advice remains advisory unless explicitly confirmed; do not confuse implementation with author approval.

## Operations

- Akamai/Linode owns writing, Git and LaTeX; CHPC owns WRF/data work. Label-only plotting from committed summaries may run locally; reusable analysis belongs in `../brc-tools`.
- No sibling WRF checkout overrides the paper inventories or immutable CHPC packets.
- Keep manuscripts single-file, sparse, British English, one sentence per source line. Preserve official names, identifiers, bibliographic titles and direct quotations verbatim; avoid wholesale reformatting of the proof source.
- Never use manuscript footnotes. Cite references, websites and data sources in the bibliography; give web URLs and access dates, and acknowledge/cite software with verified DOIs or URLs.
- Never edit `Definitions/` or hand-edit `paperpile.bib`. John supplies one complete Paperpile replacement; `trang_ref` is not Tran et al. (2018).
- After changes to the repository analysis/manuscript run `make final-draft-check`, `make submission-check`, and inspect PDFs; refresh the delivery folder with `make package`. Documentation-only handoffs need whitespace/path checks, not LaTeX builds.
- Production uses only dual-promoted, allowlisted figures. Keep original evidence and transfer inputs; no synthetic output may be promoted.
- Use `jrl/<topic>` PRs into protected `main`; preserve unrelated dirt. Commit one verified concern at a time with John's identity and `Co-Authored-By: Codex <noreply@openai.com>`.
