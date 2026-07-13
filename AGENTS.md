# AI guide

Private working repo for the MDPI *Air* paper on WRF meteorology during the 2 February 2013 Uinta Basin winter-ozone episode.
Run `hostname -f`, read `README.md` and `ROADMAP.md`, then open one route.

## Routes

| Task | Read |
|---|---|
| Plan | `tasks/microtasks.md` |
| Blank-slate rewrite | `rewrite/RESULTS-EXPANSION-HANDOFF.md`, `rewrite/README.md`, `rewrite/blueprint.md`, `_manuscript_test.tex` |
| Claims | `notes/claim-evidence-ledger.md`, `notes/narrative-and-hypotheses.md`, `notes/figure-strategy.md` |
| Runs | `verification/provenance/run-inventory.csv`, `verification/provenance/comparison-inventory.csv`, then one record |
| Figures | `rewrite/RESULTS-EXPANSION-HANDOFF.md`, `verification/figures/archive-inventory.md`, `verification/figures/manifest.csv`, `figures/MANIFEST.md` |
| Literature | `notes/resource-map.md`, `notes/literature-synthesis-register.md`, then one critique or source passage |
| Production | `main.tex`, `paperpile.bib`, `Makefile` |
| CHPC | `rewrite/CHPC-CODEX-PROMPT.md` |

Avoid broad evidence-tree reads, raw PDFs, bulk image trees, legacy checklists, candidate figures, and `Definitions/` unless the task names the need.

## Evidence rules

- Inventories, manifests, the claim ledger, and exact artifacts outrank prose.
- Separate controlled comparisons, heterogeneous context, and literature context.
- X6/X10/X5/X3 are the minimum confirmed factorial, not the paper's scope; X0--X10 also contain gated terrain, radiation, PBL/surface-layer, and fine-terrain-feedback questions.
- Figure existence follows `archive-inventory.md`; comparison meaning follows the comparison inventory; neither makes a figure promoted or a claim confirmed.
- Each number needs matched run, domain, stations, window, inputs, and command; record facts before prose.
- `main.tex` is the audited review baseline; `_manuscript_test.tex` is an experimental rewrite, not submission truth.
- Only `promoted` figures may enter either manuscript; synthetic outputs stay temporary.
- `trang_ref` is never the literal Tran et al. (2018) run.
- Chemistry, inventories, basin export, inversion depth, and multi-day persistence are not demonstrated.

## Hosts, edits, and checks

- Akamai/Linode is for writing, Git, LaTeX, and selective `~/reviews`; CHPC is for WRF/data/figures and may lack `~/reviews`.
- Use `wrf-full-figures` only when readable; otherwise mark styling provisional.
- Keep both manuscripts single-file, sparse, American English, and one sentence per source line.
- Never edit `Definitions/`; replace `paperpile.bib` only as a complete export.
- Run `make check`, `make rewrite-check`, and `make smoke` after analysis changes; inspect changed PDFs.
- `make submission` packages only the production manuscript.

## Git

- Use `jrl/<topic>` branches and PRs into protected `main`.
- Commit one verified concern at a time, push substantial batches, and use John’s identity plus `Co-Authored-By: Codex <noreply@openai.com>`.
