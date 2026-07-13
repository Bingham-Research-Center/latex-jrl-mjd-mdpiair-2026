# AI guide

Private working repo for the MDPI *Air* paper on WRF meteorology during the 2 February 2013 Uinta Basin winter-ozone episode.
Read `README.md`, then `ROADMAP.md`; open only the route for the task.

## Task index

| Task | Read |
|---|---|
| Choose or update work | `tasks/microtasks.md` |
| Framing or figure selection | `notes/narrative-and-hypotheses.md`, `notes/figure-strategy.md`, `notes/claim-evidence-ledger.md` |
| Run/comparison verification | `verification/provenance/run-inventory.csv`, `verification/provenance/comparison-inventory.csv`, `notes/hosts-data-and-figures.md`, then one provenance record |
| Figure generation/promotion | `verification/figures/archive-inventory.md`, `verification/figures/manifest.csv`, `figures/MANIFEST.md` |
| Literature/history | `notes/resource-map.md`, `notes/literature-synthesis-register.md`, then one named source artifact |
| Manuscript/build | `main.tex`, `paperpile.bib`, `Makefile` |

Avoid broad evidence-tree reads, raw PDFs, image trees, legacy checklists, candidate figures, and `Definitions/` unless the task explicitly needs them.

## Key context

- Evidence is not mutually validating: reconcile claims against source artifacts.
- Separate controlled comparisons, heterogeneous context, and literature context.
- A rendered number requires matched run identity, domain, stations, window, source artifacts, and a reproducible command.
- The frozen factorial is X6 (GFS two-way), X10 (GFS one-way), X5 (NAM two-way), and X3 (NAM one-way); resolve paths only through the run inventory.
- Never call `trang_ref` the literal Tran et al. (2018) run. Meteorology is necessary for chemical interpretation; chemistry and inventories are not settled.
- Add facts to the run inventory, figure manifest, or claim ledger before prose. Only `promoted` figures in `figures/MANIFEST.md` may enter `main.tex`; synthetic tests use temporary directories.

## Hosts and edits

- Run `hostname -f` and test paths first. Akamai/Linode is for writing, Git, LaTeX, and selective `~/reviews` work; CHPC is for WRF/data/figures and may not have `~/reviews`.
- Use `wrf-full-figures` only when installed and readable; otherwise mark styling provisional and follow documented `brc-tools` conventions.
- Keep `main.tex` single-file, sparse, American English, and one sentence per source line. Do not hand-edit `Definitions/`; replace `paperpile.bib` only as a complete export.
- Use pdfLaTeX + BibTeX (`latexmk -pdf main.tex`); `make check` routinely, `make smoke` after analysis-code changes, inspect the PDF after prose/citation/figure/layout changes, and use `make submission` only for the allowlisted package.

## Git

- Use `jrl/<topic>` branches and PRs into protected `main`.
- Commit one verified concern at a time, push substantial batches, and use John’s identity plus `Co-Authored-By: Codex <noreply@openai.com>`.
