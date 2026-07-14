# AI guide

Private MDPI *Air* repo for WRF meteorology during the 2 February 2013 Uinta
Basin winter-ozone episode.
Cold start: run `hostname -f`, read `README.md` and `ROADMAP.md`, then one route.

## Routes

| Task | Read |
|---|---|
| Codex v3 integration (active) | `notes/manuscript-v3-integration-plan.md`, then `_manuscript_v3.tex` |
| PDF harvest across hosts | `notes/literature/PDF-HARVEST-WORKFLOW.md` |
| Literature closure record | `WISHLIST-FOR-AKAMAI.md`, then its named `notes/` routes |
| Hybrid gate record | `rewrite/HYBRID-GATE-REVIEW.md`, then `rewrite/HYBRID-ARCHITECTURE-HANDOFF.md` |
| Plan | `tasks/microtasks.md` |
| Claims | `notes/claim-evidence-ledger.md`, `notes/narrative-and-hypotheses.md` |
| Runs | `verification/provenance/run-inventory.csv`, `verification/provenance/comparison-inventory.csv` |
| Figures | `verification/figures/archive-inventory.md`, `verification/figures/manifest.csv`, `figures/MANIFEST.md` |
| Maximal-draft lineage | `notes/manuscript-v3-rationale.md`, then `_manuscript_v3.tex` |
| Rewrite | `rewrite/README.md`, `rewrite/blueprint.md`, `_manuscript_test.tex` |
| Literature | `notes/resource-map.md`, `notes/literature-synthesis-register.md` |
| Production | `main.tex`, `Makefile`; `paperpile.bib` only after John's small export |
| CHPC | `rewrite/CHPC-CODEX-PROMPT.md` |

Open one route only. Avoid broad trees, raw PDFs, bulk images, legacy checklists,
candidate figures, and `Definitions/` unless required.

## Contract

- John selected Architecture C (hybrid) on 13 July 2026, and all five evidence
  gates have been executed. Preserve failed gates as failed and do not promote
  gated material without new evidence; see `rewrite/HYBRID-GATE-REVIEW.md`.
- Authority: run/comparison inventories for design, archive inventory for existence,
  manifests for admission, ledger plus exact artifacts for claims. Separate
  controlled, heterogeneous, and literature context.
- X6/X10/X5/X3 are the confirmed floor, not the scope. X0--X10 also contain gated
  terrain, radiation, PBL/surface-layer, and fine-terrain-feedback questions;
  X7/X8 and legacy runs remain context.
- Every number needs matched runs, domain, stations, window, inputs, and command;
  record facts before prose.
- `main.tex` is the audited baseline; `_manuscript_test.tex` is experimental.
  `_manuscript_v3.tex` was drafted by Claude on CHPC as an over-inclusive working
  revision; Codex is its Akamai caretaker and must audit it independently rather
  than treat AI prose as authority or silently promote it.
- John will supply a small curated Paperpile export later. It is low priority and
  does not block citation-independent editing; never hand-edit it or invent keys.
- Only dual-promoted figures may enter an audited or submission manuscript;
  v3 may inventory gated candidates but cannot promote them. Synthetic output is
  temporary.
- `trang_ref` is not Tran et al. (2018). Not demonstrated: chemistry, inventories,
  basin export, inversion depth, multi-day persistence.

## Operations

- Akamai/Linode = writing/Git/LaTeX; CHPC = WRF/data/figures and may lack
  `~/reviews`. If `wrf-full-figures` is unreadable, mark style provisional.
- Manuscripts: single-file, sparse, American English, one sentence per source line.
  Never edit `Definitions/`; replace `paperpile.bib` only with John's complete small
  export.
- After analysis changes: `make check`, `make rewrite-check`, `make smoke`, and PDF
  inspection. After v3 changes also run `make v3-check`; `make submission` packages
  only `main.tex`.
- Use `jrl/<topic>` PRs into protected `main`. Commit one verified concern at a time,
  push substantial batches, and use John's identity plus
  `Co-Authored-By: Codex <noreply@openai.com>`.
