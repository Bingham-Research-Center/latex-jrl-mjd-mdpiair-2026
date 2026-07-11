# Evaluation of WRF Meteorology for a Uinta Basin Winter Ozone Episode

Working repository for a single-file MDPI **Air** manuscript led by John R. Lawson, with Michael J. Davies, Loknath Dhar, and Seth N. Lyman.
The study evaluates WRF meteorology for the 2 February 2013 Uinta Basin cold-air pool as a prerequisite for later coupled winter-ozone chemistry experiments.

## In plain language: where truth lives

This repository is the paper's coordination home.
It records what the manuscript claims, which exact runs and data support those claims, and which figures are eligible for the paper.
It does not duplicate large model output or reusable software.

| If you want to know... | Start here |
|---|---|
| What the paper is trying to say | `ROADMAP.md` and `notes/narrative-and-hypotheses.md` |
| Whether a claim is defensible | `notes/claim-evidence-ledger.md` |
| Which exact WRF run was inspected | `verification/provenance/run-inventory.csv` |
| Which run comparison supports which manuscript story | `verification/provenance/comparison-inventory.csv`, then `notes/narrative-and-hypotheses.md` |
| Which figures support three defensible manuscript stories | `notes/figure-strategy.md` |
| Whether a dataset is raw, derived, current, superseded, or context only | `verification/data/manifest.csv` |
| Which data, script, and output produced a candidate figure | `verification/figures/manifest.csv` |
| Which full-figure sets exist or still need rendering | `verification/figures/archive-inventory.md` |
| Which paper-specific full-figure configuration and Slurm wrapper to use | `verification/config/figures/` and `verification/slurm/pelican_figures.slurm` |
| Which figures may appear in `main.tex` | `figures/MANIFEST.md` |
| Where a paper, critique, dataset, namelist, script, or external artifact belongs | `notes/resource-map.md` |

The sibling repositories keep narrower technical responsibilities:

- `../brc-wrf` owns runnable WRF cases, generated control packets, and execution evidence.
- `../brc-tools` owns reusable download, reduction, verification, and plotting code.
- Large WRF/NWP/observation files and bulk figure sets remain in CHPC archive or scratch storage; this repo records exact paths, hashes, and commands.

`../wrf-nudge-ozone-air2026` is now a read-only deprecation candidate.
Its accepted figure workflow and unique paper-specific experiment and literature notes have been migrated or dispositioned here.
Its raw paper extraction and FISS experiment remain donor history rather than manuscript evidence.
Do not add new manuscript-facing truth there; wait for the final cross-repository pointer audit before archiving it.

## Start here

- Manuscript: [`main.tex`](main.tex)
- Large-scale plan and narrative gates: [`ROADMAP.md`](ROADMAP.md)
- Active granular queue and recovered legacy to-dos: [`tasks/microtasks.md`](tasks/microtasks.md)
- Scientific framing and candidate hypotheses: [`notes/narrative-and-hypotheses.md`](notes/narrative-and-hypotheses.md)
- Defensive figure longlist and three draft narratives: [`notes/figure-strategy.md`](notes/figure-strategy.md)
- Claim status and provenance: [`notes/claim-evidence-ledger.md`](notes/claim-evidence-ledger.md)
- Run-comparison lookup: [`verification/provenance/comparison-inventory.csv`](verification/provenance/comparison-inventory.csv)
- Dataset lineage and status: [`verification/data/manifest.csv`](verification/data/manifest.csv)
- Source-of-truth ownership and selective source-mining map: [`notes/resource-map.md`](notes/resource-map.md)
- Four-collection literature synthesis register: [`notes/literature-synthesis-register.md`](notes/literature-synthesis-register.md)
- Hosts, data inventory, and figure workflow: [`notes/hosts-data-and-figures.md`](notes/hosts-data-and-figures.md)
- External full-figure coverage and gaps: [`verification/figures/archive-inventory.md`](verification/figures/archive-inventory.md)
- Verification pipeline and inherited diagnostics: [`verification/README.md`](verification/README.md)
- Donor-repository disposition audit: [`verification/docs/wrf-nudge-donor-disposition.md`](verification/docs/wrf-nudge-donor-disposition.md)
- Publication-promoted figures only: [`figures/MANIFEST.md`](figures/MANIFEST.md)

Do not load `Definitions/`, all candidate figures, or all of `~/reviews` during a normal cold start.
Open only the source needed for the current claim, experiment, or figure.

## Build

The manuscript uses the official MDPI ACS template dated 23 June 2026 and compiles with **pdfLaTeX + BibTeX**:

```bash
make pdf
make check
```

The supplied archive was `mdpi-template-acs.zip` with SHA-256 `baf827d7d2048a69142232cb422cfb74865adae70bff3eac9f821c6dad823568`.
Its complete `Definitions/` directory is committed without local edits.
Ghostscript is required to convert MDPI's EPS logo during a clean local build; Overleaf and CHPC are acceptable final-build environments.

`paperpile.bib` currently contains a five-paper seed bibliography.
Replace the complete file with a manuscript-specific Paperpile export when the collection is ready; do not hand-edit later exports.

## Repository roles

- `main.tex` contains only manuscript material that is expected to survive.
- `figures/` contains only figures promoted into the paper.
- `drafts/` contains selected dated PDFs for coauthor review.
- `verification/` retains scripts, small derived tables, candidate diagnostics, and provenance inherited from Michael's work.
- `notes/` carries the compact reasoning that must not be mistaken for manuscript evidence.

Routine `main.pdf` builds, bulk observations, WRF output, and raw provenance archives remain local.

## Hosts

- **Akamai/Linode:** writing, Git, local LaTeX, and selective literature work under `~/reviews`.
- **CHPC:** WRF runs and figure generation; archive root `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/`.

Check the host and path availability before acting.

## Git workflow

The private GitHub repository is `Bingham-Research-Center/latex-jrl-mjd-mdpiair-2026`.
The inherited history is retained through the `legacy` remote.
After the foundational direct-to-`main` setup, use `jrl/<topic>` branches and pull requests.
Commits should be logically grouped, have concise subjects and explanatory bodies, and include only contributors who actually participated in the change.

## Submission

`make submission` builds an allowlisted staging tree under `dist/` containing only `main.tex`, `paperpile.bib`, the official `Definitions/`, and any explicitly listed promoted figures.
Review PDFs, agent instructions, notes, verification material, scripts, and Git metadata never enter the MDPI source ZIP.
