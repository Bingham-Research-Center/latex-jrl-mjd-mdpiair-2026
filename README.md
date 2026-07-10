# Evaluation of WRF Meteorology for a Uinta Basin Winter Ozone Episode

Working repository for a single-file MDPI **Air** manuscript led by John R. Lawson, with Michael J. Davies, Loknath Dhar, and Seth N. Lyman.
The study evaluates WRF meteorology for the 2 February 2013 Uinta Basin cold-air pool as a prerequisite for later coupled winter-ozone chemistry experiments.

## Start here

- Manuscript: [`main.tex`](main.tex)
- Scientific framing and candidate hypotheses: [`notes/narrative-and-hypotheses.md`](notes/narrative-and-hypotheses.md)
- Claim status and provenance: [`notes/claim-evidence-ledger.md`](notes/claim-evidence-ledger.md)
- Hosts, data inventory, and figure workflow: [`notes/hosts-data-and-figures.md`](notes/hosts-data-and-figures.md)
- Verification pipeline and inherited diagnostics: [`verification/README.md`](verification/README.md)
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
