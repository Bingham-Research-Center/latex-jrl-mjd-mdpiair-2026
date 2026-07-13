# AI guide

Private MDPI *Air* repo for WRF meteorology during the 2 February 2013 Uinta
Basin winter-ozone episode.
Cold start: run `hostname -f`, read `README.md` and `ROADMAP.md`, then one route.

## Routes

| Task | Read |
|---|---|
| Hybrid gates (active) | `rewrite/HYBRID-ARCHITECTURE-HANDOFF.md`, then Architecture C in `rewrite/RESULTS-ARCHITECTURE-DECISION-PACKET.md` |
| Plan | `tasks/microtasks.md` |
| Claims | `notes/claim-evidence-ledger.md`, `notes/narrative-and-hypotheses.md` |
| Runs | `verification/provenance/run-inventory.csv`, `verification/provenance/comparison-inventory.csv` |
| Figures | `verification/figures/archive-inventory.md`, `verification/figures/manifest.csv`, `figures/MANIFEST.md` |
| Rewrite after gates | `rewrite/README.md`, `rewrite/blueprint.md`, `_manuscript_test.tex` |
| Literature | `notes/resource-map.md`, `notes/literature-synthesis-register.md` |
| Production | `main.tex`, `paperpile.bib`, `Makefile` |
| CHPC | `rewrite/CHPC-CODEX-PROMPT.md` |

Open one route only. Avoid broad trees, raw PDFs, bulk images, legacy checklists,
candidate figures, and `Definitions/` unless required.

## Contract

- John selected Architecture C (hybrid) on 13 July 2026. C1/C2 are anchors;
  C3--C6 and supplement C2 are gated. Do not reopen the choice or edit manuscripts
  before the gate review.
- Authority: run/comparison inventories for design, archive inventory for existence,
  manifests for admission, ledger plus exact artifacts for claims. Separate
  controlled, heterogeneous, and literature context.
- X6/X10/X5/X3 are the confirmed floor, not the scope. X0--X10 also contain gated
  terrain, radiation, PBL/surface-layer, and fine-terrain-feedback questions;
  X7/X8 and legacy runs remain context.
- Every number needs matched runs, domain, stations, window, inputs, and command;
  record facts before prose.
- `main.tex` is the audited baseline; `_manuscript_test.tex` is experimental. Only
  dual-promoted figures may enter either; synthetic output is temporary.
- `trang_ref` is not Tran et al. (2018). Not demonstrated: chemistry, inventories,
  basin export, inversion depth, multi-day persistence.

## Operations

- Akamai/Linode = writing/Git/LaTeX; CHPC = WRF/data/figures and may lack
  `~/reviews`. If `wrf-full-figures` is unreadable, mark style provisional.
- Manuscripts: single-file, sparse, American English, one sentence per source line.
  Never edit `Definitions/`; replace `paperpile.bib` only by complete export.
- After analysis changes: `make check`, `make rewrite-check`, `make smoke`, and PDF
  inspection. `make submission` packages only `main.tex`.
- Use `jrl/<topic>` PRs into protected `main`. Commit one verified concern at a time,
  push substantial batches, and use John's identity plus
  `Co-Authored-By: Codex <noreply@openai.com>`.
