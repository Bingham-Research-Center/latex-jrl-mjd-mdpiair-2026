# `wrf-nudge-ozone-air2026` donor disposition

This records what was preserved, absorbed, or deliberately left out from donor commit
`caf5c69` before the repository is deprecated. Nothing was deleted from the donor in
this batch.

| Donor material | Disposition in this manuscript repo | Reason |
|---|---|---|
| `EXPERIMENT-FIGURE-INVENTORY.md` | Migrated and authority-scoped as `verification/figures/archive-inventory.md`. | Figure coverage belongs with the paper; run and narrative truth remain in their own inventories. |
| `cases/pelican2013*.toml` | Migrated byte-for-byte to `verification/config/figures/`. | Paper-specific declarative figure choices; hashes preserved. |
| `slurm/pelican_figures.slurm` | Migrated to `verification/slurm/` and repointed here. | Paper-specific wrapper; reusable engine remains in `brc-tools`. |
| `experiments/pelican2013-pbl-scheme-justification.md` | Migrated and corrected as `verification/docs/pelican2013-pbl-scheme-justification.md`. | Unique methods reasoning, with the unsupported "small below 700 m" conclusion removed. |
| `experiments/pelican2013-tran-physics-bridge.md` | Migrated as `verification/docs/pelican2013-tran-physics-bridge.md`. | Unique matched-treatment and Slurm/review evidence; explicitly reviewer reserve. |
| `literature/tran-2018-fdda/critique.md` | Migrated to `notes/literature/tran-2018-fdda/critique.md`. | Unique critical reading; clearly labeled non-citable. |
| `literature/tran-2018-fdda/wrf-data-paper-contradictions.md` | Migrated as `verification/provenance/tran-2018-paper-archive-reconciliation.md`. | Paper-to-archive reconciliation is manuscript provenance. |
| `literature/tran-2018-fdda/_paper.md` | Not copied; retained in donor history until placed in the review workspace. | Long publication extraction is source material, not manuscript-repo evidence. |
| `experiments/pelican-333m-one-way-feedback.md` | Absorbed by CMP01--CMP05, C02/C17/C18, the X10 provenance record, and the factorial figure note. | A wholesale copy would duplicate current confirmed truth. |
| `experiments/pelican2013-cold-pool-figures.md` | Absorbed by the run/comparison inventories, archive catalogue, and `notes/figure-strategy.md`. | Its useful figure types, RAOB caveats, terrain caveats, and findings now have narrower authorities. |
| `experiments/README.md` | Superseded by `comparison-inventory.csv` and the claim ledger. | The old idea/status register is broader and less exact than the manuscript matrix. |
| `docs/CURRENT.md`, `docs/DECISIONS.md`, `docs/EXTERNAL-PATHS.md`, `docs/MANUSCRIPT-HANDOFF.md` | Facts reconciled into README, ROADMAP, resource map, inventories, and evidence notes; no duplicate copies. | They are coordination layers now owned by this repo. |
| `docs/visualization-products.md` | Superseded by `verification/config/figures/`, the local archive inventory, and `brc-tools` engine docs. | Requirements have become executable configuration and a figure strategy. |
| `observations/README.md` | Superseded by `verification/data/manifest.csv`, station selection, and retained analysis provenance. | Its "immediate need" is already completed. |
| `verification/fiss-concept.md` | Not migrated; preserve in donor history or move later to a `brc-tools` design issue. | Future generalized metric, not needed for tonight's manuscript. |
| Root `README.md`, `AGENTS.md`, `.gitignore`, `literature/README.md`, and archived scaffold notes | Do not migrate. | Router, ignore, and historical scaffolding have current equivalents or remain recoverable in donor Git history. |

Before deprecation, Batch 6 must update surviving sibling pointers, confirm the donor
contains no uncommitted work, add a clear archived/read-only pointer, and preserve a tag
or commit reference to the pre-deprecation state.
