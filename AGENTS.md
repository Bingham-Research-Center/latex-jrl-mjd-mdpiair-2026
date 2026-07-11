# Repository guide

Private working repository for an MDPI **Air** manuscript about WRF meteorology during the 2 February 2013 Uinta Basin winter-ozone episode.

## Cold start

1. Read `README.md`.
2. Read the current phase and exit gate in `ROADMAP.md`.
3. Open one task-specific route below; do not load the whole evidence tree.

| Work | Open | Avoid by default |
|---|---|---|
| Pick or update work | `tasks/microtasks.md` | Legacy checklists without their disposition map. |
| Change scientific framing | `notes/narrative-and-hypotheses.md`, then `notes/claim-evidence-ledger.md` | Draft numbers or inherited conclusions. |
| Verify a run or comparison | `verification/provenance/run-inventory.csv`; for a comparison also open `verification/provenance/comparison-inventory.csv`; then `notes/hosts-data-and-figures.md` and one relevant provenance record | Inferring identity from filenames, folders, or candidate namelists. |
| Generate/promote a figure | `verification/figures/manifest.csv`, `figures/MANIFEST.md` | Copying candidate images directly into `figures/`. |
| Mine literature/history | `notes/resource-map.md`; for cross-paper context use `notes/literature-synthesis-register.md`; then open one named critique, extract, commit, issue, or PR | All of `~/reviews`, raw PDFs, image trees, or the full legacy repo. |
| Edit manuscript/build | `main.tex`, `paperpile.bib`, `Makefile` | `Definitions/` unless debugging the class/template. |

## Evidence contract

- Treat prose, code, tables, figures, papers, and agent notes as claims to reconcile, not mutual validation.
- Separate controlled comparisons, heterogeneous context, and literature yardsticks.
- Require matched run identity, domain, stations, window, source artifacts, and reproducible command before rendering a number.
- Never call `trang_ref` the literal Tran et al. (2018) run.
- Meteorological fidelity is necessary for chemical interpretation; do not claim chemistry or inventories are settled.
- Include only `promoted` files from `figures/MANIFEST.md`; synthetic tests write only to temporary directories.
- Record new facts in the run inventory, figure manifest, or claim ledger before drafting prose.
- The current matched forcing-by-feedback factorial is X6 (GFS two-way), X10
  (GFS one-way), X5 (NAM two-way), and X3 (NAM one-way); resolve their exact
  paths through `verification/provenance/run-inventory.csv`, not this router.

## Hosts

Run `hostname -f` and test paths first.

- Akamai/Linode: writing, Git, local LaTeX, and selective critiques under `~/reviews`.
- CHPC: WRF/data/figure work; archive root `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/`; do not assume `~/reviews` exists.
- Use `wrf-full-figures` only when the skill is installed and readable; otherwise mark styling provisional and use documented `brc-tools` conventions.

## Editing and checks

- Keep `main.tex` single-file, sparse, American English, and one sentence per source line.
- Build with pdfLaTeX + BibTeX via `latexmk -pdf main.tex`; never switch to XeLaTeX or biber.
- Never hand-edit `Definitions/`; refresh it only from an official MDPI archive.
- Replace `paperpile.bib` as a complete Paperpile export; do not hand-edit a later export.
- Routine `main.pdf` is ignored; meaningful review milestones belong under `drafts/`.
- Run `make check`; run `make smoke` for analysis-code changes; inspect the PDF after prose, citation, figure, or layout changes; use `make submission` only for the allowlisted package.

## Git

- Work on `jrl/<topic>` branches and PR into protected `main`.
- Commit one coherent, verified concern at a time and push after each substantial batch.
- Use John’s configured identity plus `Co-Authored-By: Codex <noreply@openai.com>` for Codex-assisted commits.
- Preserve inherited authorship; credit only contributors to the new commit.
