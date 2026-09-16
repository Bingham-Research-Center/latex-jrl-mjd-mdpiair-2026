# First-round peer-review revision return record

## Imported on the writing host: 16 September 2026

CHPC job `15610800` and its bounded follow-up are complete.
The latest pulled commit is `3e3b629`, which records the [CHPC closure](peer-review-round1-chpc-closure-15610800.md).
The two files supplied in `mdpiair-handoffs/` are the closure archive and its SHA-256 sidecar, not another analysis run.

| Local archive | Verified SHA-256 | Internal checks |
| --- | --- | --- |
| `latex_jrl_review_layers_15610800_handoff.tar.gz` | `19e83bc0eb5fc533577394fe1cc839a00b6df774bfafeb50165d4ded84836363` | 19/19: nine CSVs, nine metadata JSONs, run manifest |
| `mdpiair-handoffs/peer-review-round1-chpc-closure-15610800.tar.gz` | `b594c63981330228e0e9c489ef181b9cdc648c47ea106e1b7b4d2673981fb4f7` | 12/12: closure report, small evidence and audit scripts |

The original analysis archive also matches the independently reported CHPC hash.
The nine CSVs and metadata JSONs are now imported at their intended `verification/data/` and `verification/provenance/` paths.
DATA40--DATA48 in the data manifest register the results.
The [import receipt](../verification/provenance/reviewer-layer-import-15610800.json) binds source commit `658bd005e20401f9ad8c8e88c5c2b506bb60e1a8`, exact commands, generator/station hashes, inventoried run paths, domain, station and hourly coverage, and imported hashes.
The [original job receipts](../verification/provenance/peer-review-round1-15610800/) preserve `submission.txt`, `sacct.txt`, `slurm.out`, `slurm.err`, `return_sha256.txt`, the closure hash list and the local import audit source.
The archives remain local untracked inputs; raw observations and diagnostic plots are not added to the production package.

Local checks independently verified the four accepted runs, d02, eleven columns, all five hours on 2 February 2013 (1400--1800 UTC), pinned generator identity, and primary-layer reproduction within 1e-9 of the registered values.
Re-running the returned observation-summary script against the extracted provider records produced a byte-identical summary.
The source hourly tables and nine diagnostic images remain on CHPC; their numerical/visual inspection is recorded in the closure report, not represented as a new local inspection.

## Results integrated into the manuscript

Every hourly paired GFS-minus-NAM endpoint difference is negative, and every paired scalar/vector speed difference positive, in all nine configurations.
The table below gives means of five hourly paired-station medians at the primary 25 m wind integration increment; each cell lists two-way / one-way feedback.

| Layer (m AGL) | Endpoint difference (K) | Vector magnitude (m s-1) | Scalar speed (m s-1) |
| --- | ---: | ---: | ---: |
| 50--500 | -3.63 / -3.65 | +0.79 / +0.99 | +0.78 / +1.01 |
| 50--250 | -2.22 / -2.08 | +0.67 / +0.85 | +0.70 / +0.83 |
| 100--500 | -3.38 / -3.42 | +0.77 / +1.02 | +0.79 / +1.02 |

At fixed layer bounds, the largest spread of paired mean wind effects over 10/25/50 m increments is 0.0195264 m s-1.
The ordering survives, but magnitude depends on the layer bounds.
These calculations test integration sampling of the same interpolated winds, not native WRF vertical resolution or an alternative interpolation method.
`main.tex` records this in `sec:v3-common-agl`, `sec:v3-driving-response` and `tab:v3-layer-sensitivity`; claims C38--C40 preserve the scope and observation dispositions.

The primary vector/scalar alignment-ratio differences remain +0.063 / +0.053 and change sign in two of five hours for each pair.
Neither metric measures basin transport or ventilation.

## Observation and figure dispositions

- The bounded accessible-holdings search found no measured in-basin profile within the exact retained window. A provisional Roosevelt sounding begins at 1801:54 UTC and has not undergone scientific QC or matched WRF analysis. Inaccessible holdings are not treated as empty. Vertical validation remains an explicit limitation.
- The fresh Seep Ridge pull supplies provider metadata, UTC timestamps and 17/17 retained-window samples for each of four requested variables with no returned QC flags. It supplies no sensor-position or exposure history and does not reproduce the historical observation-cache processing or establish a mechanism for the distinct trace.
- All nine CHPC diagnostic figures have D1 label overlap/clipping despite passing their numerical checks. They remain unpromoted. Repair requires the existing hourly CSVs on CHPC and separate derivative output; those CSVs were not transferred. No WRF or scientific recalculation is needed, and this repair does not block the numerical table.

## Response reconciliation and validation

R3-C001/C015/C016/C018 now use the imported results in the response and decision register; R1-C004 includes the verified Seep Ridge metadata qualification.
All 45 reviewer IDs and quotations were preserved, along with the author's stances and agreed actions.
The four numerical-analysis dependencies are closed; R3-C016 remains `pending-figure-label-update` because visual review found legacy “transport wind” labels in the existing Figures 4 and 5.
The response workspace is `/home/johnrobertlawson/reviews/lawson-ozone-wrf-mdpiair-2026/`.
Final response wording and journal-facing commitments remain subject to John's review.

`make final-draft-check`, `make submission-check`, ZIP integrity and whitespace checks passed.
The revised [main PDF](../main.pdf) has 20 pages; all pages were inspected in overview and pages 6, 8, 11, 16 and 17 in detail.
The added text and table have no observed clipping or overlap, and the main log has no overfull/underfull boxes or undefined references.
Existing template PDF-string/header warnings remain.
The independently built submission PDF has identical extracted text; the ZIP contains the revised source and only allowlisted production material.
The [integration-check receipt](../verification/provenance/reviewer-layer-integration-checks-20260916.json) records commands, inspection and source/PDF/ZIP/response hashes.

Remaining executable figure work is a label-only rerender of Figures 4 and 5 and, if needed for review, D1 repair in the nine CHPC diagnostics.
Keep the original artefacts, render derivatives separately from existing summaries, inspect them, and update both figure manifests before replacing production files.
No WRF integration, expanded observation window or new scientific claim is authorised by this cleanup.
The original untracked transfer inputs are preserved outside Git.
