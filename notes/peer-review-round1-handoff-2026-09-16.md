# First-round peer-review revision handoff

## Authority and scope

- Reviewer-source truth: `/home/johnrobertlawson/reviews/lawson-ozone-wrf-mdpiair-2026/_peer-review/comments.md`.
- Author decisions: `/home/johnrobertlawson/reviews/lawson-ozone-wrf-mdpiair-2026/peer-review-decisions.md`.
- Response draft: `/home/johnrobertlawson/reviews/lawson-ozone-wrf-mdpiair-2026/response-to-reviewers.md`.
- Manuscript base: audited root `main.tex` on `jrl/peer-review-round1`, branched from `bf38e91a2cc1f5e007cdf37c9613ee1afa16fdff`.
- Selective donor only: `/home/johnrobertlawson/reviews/lawson-ozone-wrf-mdpiair-2026/version_1p5/main.tex`.

Do not replace root `main.tex` wholesale with 1p5. Do not resurrect the former separate supplement. Preserve failed scientific gates as failed.

## Agreed revision

- Keep the result to one 2 February 2013 case and the 1400--1800 UTC retained window.
- Describe `S50:500` as a potential-temperature endpoint difference in kelvin.
- Describe `U50:500` as the magnitude of the layer-mean horizontal wind vector, with no transport or ventilation interpretation.
- Add the scalar-speed and vector/scalar alignment check from existing output.
- Add station identities, coordinates, elevations, cell separations, and default-terrain offsets.
- Keep the X0--X4 terrain figure in the main text as a descriptive, support-dependent response with no ranking or mechanism.
- Use verified peer-reviewed sources and narrowly qualified agency-report lineage.
- Integrate only the appendix material needed by the main argument; submit no separate supplement.

## CHPC-only return

The Akamai host has no `/uufs` mount. Submit `verification/slurm/run_peer_review_layer_sensitivity.slurm` from a clean checkout pinned to the revision commit. It reads the four accepted archived runs and calculates the 50--500, 50--250, and 100--500 m layers at 10, 25, and 50 m increments. It runs no WRF simulation and writes a repo-shaped return bundle in scratch.

Import only the returned pair summaries and metadata after checking hashes, the pinned commit, complete station/hour coverage, and metric definitions. Record the imported paths in `notes/peer-review-round1-return.md`; then update the manuscript and response only if the layer result changes or materially qualifies the primary interpretation.

## Stop rules

- Do not infer a cause for Seep Ridge without verified exposure or quality-control evidence.
- Do not treat the horizontal station network as free-air validation.
- Do not infer initial-versus-lateral forcing, basin export, chemistry response, inversion depth, persistence, or product superiority.
- Leave externally dependent response items visibly `PENDING` until verified.
