# First-round peer-review revision return record

## Received and checked on Akamai: 16 September 2026

Job `15610800` returned the complete nine-layer/increment calculation in
`latex_jrl_review_layers_15610800_handoff.tar.gz`.
All 19 internal hashes pass (nine pair-summary CSVs, nine metadata JSONs and the run manifest).
Source `658bd005e20401f9ad8c8e88c5c2b506bb60e1a8`, the four inventoried runs, d02, 11 station columns and all five 1400--1800 UTC hours match; the primary results reproduce to their recorded precision.
The files are still in the archive: validation is complete, local import is pending.

Local archive SHA-256: `19e83bc0eb5fc533577394fe1cc839a00b6df774bfafeb50165d4ded84836363`.
An independently reported CHPC archive hash and inspection of the untransferred diagnostic plots remain outstanding.
The only active CHPC request is [the short follow-up handoff](peer-review-round1-handoff-2026-09-16.md).

## Local work completed on Akamai

- Revised root `main.tex` from the audited source, using 1p5 only as a comparison donor.
- Added `verification/data/station_sampling_audit.csv` for all 11 case-window temperature sites.
- Added `verification/data/reviewer_primary_wind_sensitivity.csv` and provenance for the existing 50--500 m output.
- Updated the retention analyser to summarise layer-mean scalar speed and the vector/scalar alignment ratio.
- Added a CHPC-only wrapper for the alternative-layer and interpolation-step checks.
- Reconciled the terrain figure's manuscript-promotion status.
- Removed the retired separate supplement from the active submission-check and package path.

The primary 50--500 m paired GFS-minus-NAM results are:

| Feedback | Vector magnitude (m s-1) | Scalar speed (m s-1) | Alignment-ratio difference |
| --- | ---: | ---: | ---: |
| Two-way | +0.79 | +0.78 | +0.063 |
| One-way | +0.99 | +1.01 | +0.053 |

The vector and scalar speed differences are positive in all five hours. The alignment-ratio difference is positive in three and negative in two hours for each feedback pair, so cancellation does not create the primary speed ordering and supports no transport claim.

## Remaining work by owner

- **CHPC:** confirm the original archive hash and inspect all nine diagnostic figures.
- **CHPC:** record bounded searches for matching independent vertical profiles and Seep Ridge QC/exposure metadata; the current register contains no suitable evidence, and negative or inaccessible outcomes must remain explicit.
- **Akamai:** import `return/verification/data/reviewer_layer_*_pair_summary.csv` and `return/verification/provenance/reviewer_layer_*_metadata.json` to their matching repository paths; retain `reviewer-layer-run-manifest.tsv` and a receipt binding the source commit, job, commands, input paths, coverage and output hashes.
  Preserve the archive's `submission.txt`, `sacct.txt`, `slurm.out`, `slurm.err` and `return_sha256.txt` with that provenance.
- **Akamai:** qualify the layer-bound dependence in `main.tex` (common-AGL methods and driving-product results), then reconcile R3-C001/C015/C016/C018 in the author-response workspace and run the manuscript/package checks.
- **John:** review final response wording and journal-facing commitments.

The existing return supports the same ordering in all nine configurations: each hourly paired station median has a smaller GFS endpoint difference and larger GFS scalar/vector wind speed.
The endpoint-difference magnitude depends on layer bounds; changing the wind integration increment does not reverse the ordering.

## Response reconciliation contract

Each imported result must retain its source commit, command, input paths, station and hour coverage, output hash, and manuscript locator. Replace a `PENDING` response field only after that evidence is present and the manuscript statement has been checked against it.
