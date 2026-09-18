# AI guide

Private MDPI *Air* manuscript: WRF meteorology for the 2 February 2013 Uinta Basin episode.
Cold start: `hostname -f`, `README.md`, then one task route below.
Current phase and next steps: `ROADMAP.md`; current evidence/revision state: `notes/peer-review-round1-return.md`.

## Routes

| Task | Read |
|---|---|
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
`main.tex` is the audited submission target. `drafts/jrl_manuscript.tex` is the superseded author draft;
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
- Keep manuscripts single-file, sparse, British English, one sentence per source line. Preserve official names, identifiers, bibliographic titles and direct quotations verbatim.
- Never edit `Definitions/` or hand-edit `paperpile.bib`. John supplies one complete Paperpile replacement; `trang_ref` is not Tran et al. (2018).
- After analysis/manuscript changes run `make final-draft-check`, `make submission-check`, and inspect PDFs; refresh the delivery folder with `make package`.
- Production uses only dual-promoted, allowlisted figures. Keep original evidence and transfer inputs; no synthetic output may be promoted.
- Use `jrl/<topic>` PRs into protected `main`; preserve unrelated dirt. Commit one verified concern at a time with John's identity and `Co-Authored-By: Codex <noreply@openai.com>`.
