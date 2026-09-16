# First-round peer-review revision return record

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

## Pending external evidence

- CHPC return for 50--250 and 100--500 m layers and 10/25/50 m increments.
- Targeted search for an independent in-basin vertical profile matching the retained hours; none is registered in the current study archive.
- Any additional Seep Ridge quality-control or exposure metadata; the verified cell distance is 133 m and the X3 elevation offset is +2.9 m.
- Final author review of response wording and all journal-facing commitments.

## Response reconciliation contract

Each imported result must retain its source commit, command, input paths, station and hour coverage, output hash, and manuscript locator. Replace a `PENDING` response field only after that evidence is present and the manuscript statement has been checked against it.
