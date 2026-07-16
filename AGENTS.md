# AI guide

Private MDPI *Air* repo for WRF meteorology during the 2 February 2013 Uinta
Basin winter-ozone episode.
Cold start: run `hostname -f`, read `README.md` and `ROADMAP.md`, then take one
route.

## Routes

| Task | Read |
|---|---|
| Final-draft state | `notes/final-draft-readiness-2026-07-15.md`, then `main.tex` |
| John's author draft | `jrl_manuscript.tex`, then `notes/jrl-manuscript-review-2026-07-16.md` |
| Required/optional queue | `tasks/final-draft-100.md` |
| Claims and framing | `notes/claim-evidence-ledger.md`, `notes/narrative-and-hypotheses.md` |
| Runs/comparisons | `verification/provenance/run-inventory.csv`, `verification/provenance/comparison-inventory.csv` |
| Figures | `verification/figures/manifest.csv`, then `figures/MANIFEST.md` |
| Hybrid gate history | `rewrite/HYBRID-GATE-REVIEW.md`, `rewrite/HYBRID-ARCHITECTURE-HANDOFF.md` |
| Maximal v3 lineage | `notes/manuscript-v3-integration-plan.md`, then `_manuscript_v3.tex` |
| X8 review only | `NOTES-CHPC-111m-JUL26.md`, `verification/provenance/x8-deficit-transport-13971080.json` |
| Literature | `notes/resource-map.md`, `notes/literature-synthesis-register.md` |
| PDF harvest | `notes/literature/PDF-HARVEST-WORKFLOW.md` |
| Production | `main.tex`, `Makefile`, `figures/submission-files.txt` |
| CHPC dispatch | `rewrite/CHPC-CODEX-PROMPT.md` |

Open one route only. Avoid broad trees, raw PDFs, bulk images, candidate figures,
legacy checklists, and `Definitions/` unless the selected task requires them.

## Contract

- Architecture C is frozen. All five gates ran; preserve failed gates as failed
  unless new predeclared evidence reopens one.
- Inventories govern design, the archive inventory governs existence, manifests
  govern figure admission, and the ledger plus exact artefacts govern claims.
- `main.tex` is the audited submission starting point. `jrl_manuscript.tex` is
  John's tracked author draft and is not yet the submission target.
  `_manuscript_v3.tex` is the over-inclusive caretaker snapshot;
  `_manuscript_test.tex` is experimental.
- X6/X10/X5/X3 are the confirmed floor. Other X0--X10 results remain gated or
  contextual. X8 deficit transport is within-run process context, not comparative
  or basin-export evidence.
- Every number needs matched runs, domain, stations, window, inputs, and command.
  Separate controlled, heterogeneous, observational, and literature context.
- Only figures promoted in both manifests may enter `main.tex`. Never hand-edit
  `paperpile.bib`; John will replace it with one complete small export.
- `trang_ref` is not Tran et al. (2018). Chemistry, inventories, basin export,
  inversion depth, and multi-day persistence are not demonstrated here.

## Operations

- Akamai/Linode owns writing, Git, and LaTeX; CHPC owns WRF/data/figure work.
  `../brc-tools` owns reusable analysis. No sibling WRF checkout overrides the
  paper inventories or immutable CHPC control packets.
- Keep manuscripts single-file, sparse, in British English, and one sentence per
  source line. Preserve official product names, code identifiers, bibliographic
  titles, and direct quotations verbatim. Never edit `Definitions/`.
- After analysis or manuscript changes run `make final-draft-check`,
  `make submission-check`, and inspect the PDFs. `make submission` packages only
  allowlisted production sources.
- Use `jrl/<topic>` PRs into protected `main`. Commit one verified concern at a
  time with John's identity and `Co-Authored-By: Codex <noreply@openai.com>`.
