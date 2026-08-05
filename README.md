# Evaluation of WRF Meteorology for a Uinta Basin Winter Ozone Episode

Working repository for a single-file MDPI **Air** manuscript led by John R. Lawson, with Michael J. Davies, Loknath Dhar, and Seth N. Lyman.
The study evaluates WRF meteorology for the 2 February 2013 Uinta Basin cold-air pool as a prerequisite for later coupled winter-ozone chemistry experiments.

## In plain language: where truth lives

This repository is the paper's coordination home.
It records what the manuscript claims, which exact runs and data support those claims, and which figures are eligible for the paper.
It does not duplicate large model output or reusable software.

| If you want to know... | Start here |
|---|---|
| Whether the repo is ready for a final author draft | `notes/final-draft-readiness-2026-07-15.md` |
| What must happen next, and what is merely optional | `tasks/final-draft-100.md` |
| What the paper is trying to say | `ROADMAP.md` and `notes/narrative-and-hypotheses.md` |
| Which Results architecture was selected and how its gates closed | `rewrite/HYBRID-GATE-REVIEW.md`, then `notes/manuscript-v3-integration-plan.md` |
| How the blank-slate rewrite and expanded Results audit differ from the baseline | `rewrite/RESULTS-EXPANSION-HANDOFF.md`, then `rewrite/README.md` and `rewrite/blueprint.md` |
| Whether a claim is defensible | `notes/claim-evidence-ledger.md` |
| Which exact WRF run was inspected | `verification/provenance/run-inventory.csv` |
| Which run comparison supports which manuscript story | `verification/provenance/comparison-inventory.csv`, then `notes/narrative-and-hypotheses.md` |
| How the selected hybrid Results gates closed | `rewrite/HYBRID-GATE-REVIEW.md`, with the historical specification in `rewrite/HYBRID-ARCHITECTURE-HANDOFF.md` |
| How to harvest a new PDF across Akamai and CHPC | `notes/literature/PDF-HARVEST-WORKFLOW.md` |
| Whether a dataset is raw, derived, current, superseded, or context only | `verification/data/manifest.csv` |
| Which data, script, and output produced a candidate figure | `verification/figures/manifest.csv` |
| Which full-figure sets exist or still need rendering | `verification/figures/archive-inventory.md` |
| Which paper-specific full-figure configuration and Slurm wrapper to use | `verification/config/figures/` and `verification/slurm/pelican_figures.slurm` |
| Which figures may appear in `main.tex` | `figures/MANIFEST.md` |
| Where a paper, critique, dataset, namelist, script, or external artefact belongs | `notes/resource-map.md` |

Other repositories keep narrower technical responsibilities:

- `../brc-tools` owns reusable download, reduction, verification, and plotting code.
- No sibling WRF checkout overrides the run/comparison inventories, WRF headers,
  namelist fingerprints, or immutable CHPC control packets recorded here.
- Large WRF/NWP/observation files and bulk figure sets remain in CHPC archive or scratch storage; this repo records exact paths, hashes, and commands.

`../lawson-davies-air-wrf-2026` is the read-only legacy manuscript donor.
Its accepted material has been migrated or dispositioned here; its raw extraction,
old checklist, and FISS experiment remain donor history rather than evidence.
Do not edit it or add new manuscript-facing truth there.

## Start here

- Final-draft starting point: [`main.tex`](main.tex)
- John's archived author draft: [`jrl_manuscript.tex`](drafts/jrl_manuscript.tex), with
  the dated review in [`notes/jrl-manuscript-review-2026-07-16.md`](notes/jrl-manuscript-review-2026-07-16.md)
- Readiness and branch/repo audit: [`notes/final-draft-readiness-2026-07-15.md`](notes/final-draft-readiness-2026-07-15.md)
- Ordered required and optional register: [`tasks/final-draft-100.md`](tasks/final-draft-100.md)
- Completed Codex caretaker record: [`notes/manuscript-v3-integration-plan.md`](notes/manuscript-v3-integration-plan.md)
- Maximal caretaker snapshot: [`_manuscript_v3.tex`](_manuscript_v3.tex)
- Completed Architecture C gate record: [`rewrite/HYBRID-GATE-REVIEW.md`](rewrite/HYBRID-GATE-REVIEW.md)
- Expanded Results/figure handoff: [`rewrite/RESULTS-EXPANSION-HANDOFF.md`](rewrite/RESULTS-EXPANSION-HANDOFF.md)
- Results architecture decision packet: [`rewrite/RESULTS-ARCHITECTURE-DECISION-PACKET.md`](rewrite/RESULTS-ARCHITECTURE-DECISION-PACKET.md)
- Experimental blank-slate workbench: [`rewrite/README.md`](rewrite/README.md), then [`_manuscript_test.tex`](_manuscript_test.tex)
- Large-scale plan and narrative gates: [`ROADMAP.md`](ROADMAP.md)
- Scientific framing and candidate hypotheses: [`notes/narrative-and-hypotheses.md`](notes/narrative-and-hypotheses.md)
- Figure longlist and the earlier minimum-draft narratives: [`notes/figure-strategy.md`](notes/figure-strategy.md)
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
make final-draft-check
make submission-check
```

The first command builds and checks `main.tex`, `_manuscript_test.tex`, and
`_manuscript_v3.tex`, runs the `brc-tools` smoke check, enforces the manuscript
contract, and checks the diff.
The second command assembles and independently checks the allowlisted submission.

The supplied archive was `mdpi-template-acs.zip` with SHA-256 `baf827d7d2048a69142232cb422cfb74865adae70bff3eac9f821c6dad823568`.
Its complete `Definitions/` directory is committed without local edits.
Ghostscript converts MDPI's EPS logo when available.
The staging-tree check may use the committed cached conversion when Ghostscript is
absent, while the ZIP itself remains source-clean; the independent final build must
record which path it used.

`paperpile.bib` currently contains a five-paper seed bibliography.
John will replace it later with a small curated Paperpile export; this does not block
citation-independent editing, and agents must not hand-edit the current or exported file.

## Repository roles

- `main.tex` is the audited 17-page final-draft starting point and submission target.
- `drafts/jrl_manuscript.tex` is John's archived author draft based on the
  maximal-v3 donor; its accepted material is already integrated into `main.tex`,
  the submission target.
- `_manuscript_v3.tex` is the over-inclusive 26-page caretaker snapshot; its
  diagnostic figures and Appendix B review layout are not submission admissions.
- `_manuscript_test.tex` and `rewrite/` form a temporary evidence-led workbench for the total rewrite; neither is included by `make submission`.
- `figures/` contains only figures promoted into the paper.
- `drafts/` contains selected dated PDFs for coauthor review.
- `verification/` retains scripts, small derived tables, candidate diagnostics, and provenance inherited from Michael's work.
- `notes/` carries the compact reasoning that must not be mistaken for manuscript evidence.

Routine build PDFs, bulk observations, WRF output, and raw
provenance archives remain local.

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
