# CHPC follow-up: first-round review

The layer calculation is complete; this replaces the earlier launch instructions.
Finish the four checks below using existing files, then return one short report.
No new WRF integration or repeat of job 15610800 is needed.

## Existing result

- Repository: `Bingham-Research-Center/latex-jrl-mjd-mdpiair-2026`; writing branch: `jrl/peer-review-round1`.
- Analysis source: `658bd005e20401f9ad8c8e88c5c2b506bb60e1a8`.
- CHPC worktree: `/uufs/chpc.utah.edu/common/home/u0737349/gits/mdpi-air-review-layers-658bd00`.
- Job: `15610800`, reported `COMPLETED`, exit `0:0`.
- Output root: `/scratch/general/vast/u0737349/latex_jrl_review_layers/15610800`.
- Akamai verified all 19 internal checksums, the pinned source, four accepted runs, d02, 11 station columns, five hours (2 February 2013, 1400--1800 UTC), and baseline reproduction.
- All nine layer/increment combinations preserve the hourly GFS--NAM ordering; the magnitude depends on layer bounds.

## Only the remaining CHPC checks

1. **Original archive hash.** Run `sha256sum` on the original transferred `latex_jrl_review_layers_15610800_handoff.tar.gz`; report its absolute path and command output.
   The Akamai copy hashes to `19e83bc0eb5fc533577394fe1cc839a00b6df774bfafeb50165d4ded84836363`.
   Compare the original bytes, not a newly packed archive; report any mismatch or missing source copy.
2. **Diagnostic inspection.** Under the output root, inspect `raw/{50-500,50-250,100-500}_step-{10,25,50}/wrf_retention_ventilation_d02_14to18.{pdf,png}` for all nine combinations.
   Check layer labels, axes, missing curves and consistency with the adjacent CSVs/metadata.
   Return one pass/issue row per combination with inspected paths; these images were absent from the transfer bundle.
3. **Independent profiles.** Make one bounded search of accessible CHPC observation holdings for in-basin measured vertical profiles covering 2 February 2013, 1400--1800 UTC.
   Record locations searched and, for candidates, instrument, site/coordinates, timestamps, vertical coverage, variables and QC.
   Distinguish a matching profile from out-of-window context; a documented negative search is an acceptable result.
4. **Seep Ridge metadata.** Check accessible observation/provider records for USU04 (39.7539 N, 109.5460 W; reported elevation 1933 m), especially sensor/exposure history, time convention and QC for 31 January--3 February 2013.
   The registered X3 cell separation is 132.7 m and terrain offset is +2.9 m; those alone do not identify a mechanism.
   Return source-backed metadata or a documented negative search.

Do not equate inaccessible data with absent observations.
Keep failed scientific gates closed; these checks do not establish inversion depth, basin export, chemistry or persistence.
Preserve the pinned worktree and original outputs; record defects before proposing any recalculation.

## Return one document

Write `peer-review-round1-chpc-closure-15610800.md` in a separate scratch follow-up directory.
Include the archive hash, nine inspection rows, both observation-search outcomes, and exact commands/paths or source links.
For each item use `verified`, `issue`, `not found in searched locations`, or `unavailable`, as applicable.
Attach only newly recovered small evidence files, with SHA-256 hashes; no bulk WRF files or duplicate copy of the existing return bundle.

Akamai then imports the existing nine CSVs, nine metadata JSONs, run manifest and provenance receipt; updates the layer-bound qualification in `main.tex`; reconciles response items R3-C001/C015/C016/C018; and runs the manuscript/package checks.
Missing independent observations remain stated limitations unless new evidence is recovered.
John retains final review of response wording.
The local receipt is [peer-review-round1-return.md](peer-review-round1-return.md).
