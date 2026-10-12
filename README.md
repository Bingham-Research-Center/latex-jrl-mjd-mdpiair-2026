# WRF Cold-Pool Sensitivities Relevant to Winter-Ozone Modelling in the Uinta Basin

MDPI **Air** manuscript and evidence repository by John R. Lawson, Michael J. Davies, Loknath Dhar and Seth N. Lyman.
The study evaluates meteorology during the 2 February 2013 episode; it contains no chemistry calculation.

## Current proof

The current proof source is [the working TeX](proof-package/working/air-4472509-done.tex) on `jrl/proofs-round1`; the immutable publisher proof is under `proof-package/air-4472509-english/`.
John reports that he returned the proof to MDPI. His later independent tone pass is checkpointed at `be959eb`, and the corresponding local PDF/ZIP are for his final check; generated artifacts are ignored by Git.
The first-round revision of `main.tex` and its evidence checkpoint live on `jrl/peer-review-round1`; this proof branch and default `main` have not yet been integrated.
The [proof handoff](PROOFING-HANDOFF.md) gives the current source, reply and release route. The separate supplement is retired.

## Find the evidence

| Need | Source |
|---|---|
| Current journal proof | [working TeX](proof-package/working/air-4472509-done.tex) |
| Author decisions/reply draft | `~/reviews/lawson-ozone-wrf-mdpiair-2026/peer-review-decisions.md` and `response-to-reviewers.md` |
| Claims and limits | [claim ledger](notes/claim-evidence-ledger.md) |
| Exact runs and contrasts | [run inventory](verification/provenance/run-inventory.csv), [comparison inventory](verification/provenance/comparison-inventory.csv) |
| Derived data | [data manifest](verification/data/manifest.csv) |
| Figure provenance and admission | [verification manifest](verification/figures/manifest.csv), [promoted figures](figures/MANIFEST.md) |
| Archive existence | [figure archive inventory](verification/figures/archive-inventory.md) |
| Literature and bibliography | [resource map](notes/resource-map.md), [source crosswalk](notes/literature-synthesis-register.md), [Paperpile checklist](notes/literature/paperpile-export-list.md) |
| CHPC work | [bounded dispatch guide](rewrite/CHPC-CODEX-PROMPT.md) |
| Historical drafts and frozen gates | [rewrite history](rewrite/README.md), [review milestones](drafts/README.md) |

Architecture C and its failed gates remain frozen.
The four-run X6/X10/X5/X3 matrix is the primary result; other admitted diagnostics retain their individual scope limits.
The layer-sensitivity calculations use existing outputs and do not establish native-resolution sensitivity, basin transport or independent vertical validation.

## Build and review

```bash
make final-draft-check
make submission-check
make package
```

The first target builds/checks the main manuscript and historical test/v3 sources, runs the `brc-tools` smoke checks and checks the manuscript contract.
The second independently compiles the allowlisted source package; the third refreshes the tracked, self-contained `submission-package/` folder.
Inspect the PDFs after changes. Routine root PDFs remain ignored; dated review milestones live in `drafts/`.
The official MDPI template uses pdfLaTeX and BibTeX with `Definitions/mdpi.bst`; never edit `Definitions/`.
If Ghostscript is absent, the independent check uses the existing cached logo conversion; the source ZIP remains source-clean.

`review-references.bib` supplies verified methods, data, software and textbook additions pending Paperpile consolidation; both bibliography files are included in the checks and package.
`paperpile.bib` remains Paperpile-owned. Replace it wholesale with John's complete export; follow the current checklist rather than the obsolete five-paper seed count.
The earlier root source ZIP is `dist/mdpi-air-submission.zip`; it excludes reviews, notes, verification scripts and Git metadata.
The root package is historical on this proof branch; the current proof return is documented in [the handoff](PROOFING-HANDOFF.md).

## Hosts and Git

Akamai/Linode owns writing, Git, LaTeX and selective literature work; CHPC owns WRF/data work.
Label-only figure rerenders from committed summaries can run on the writing host.
`../brc-tools` owns reusable analysis; sibling WRF repositories do not override this paper's inventories or immutable control packets.
The legacy manuscript repository is a read-only donor.

Use `jrl/<topic>` branches and PRs into protected `main`, with narrow verified commits and the required Codex co-author trailer.
Preserve unrelated dirt and the untracked CHPC transfer archives.
