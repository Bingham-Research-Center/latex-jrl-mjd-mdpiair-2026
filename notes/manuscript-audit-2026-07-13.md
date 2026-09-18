# Manuscript evidence and logic audit — 13 July 2026

**Scope note:** this audit establishes what the then-current four-run manuscript could
defend; it is not a finding that X0--X10 contain no additional Results.
Use `rewrite/RESULTS-EXPANSION-HANDOFF.md` for the reopened terrain, radiation,
PBL/surface-layer, fine-terrain-feedback, spatial, vertical, and heat-deficit audit.

## Scope and verdict

This audit checked the draft against the claim ledger, the X6/X10/X5/X3 run and comparison inventories, the promoted-figure manifests, the committed derived summaries, the exact retention-analysis record, the three figure generators, and targeted source passages for the five current bibliography entries.
It did not treat planning prose, candidate figures, review syntheses, or repeated claims as independent evidence.

The defensible paper is narrower than the inherited title suggests.
It is a deterministic five-hour case-study comparison of two driving-data products under two nest-feedback settings, evaluated at fixed d02 station columns.
The strongest result is that the GFS-minus-NAM separation has the same sign in all five hours for 50--500 m AGL stability and fixed-layer transport wind under both feedback modes.
The feedback effects are much smaller on this sample.

## Claims that can survive

| Claim | Evidence | Required wording limit |
|---|---|---|
| GFS is warmer relative to the surface observations than NAM under both feedback modes. | C04; `surface_skill_pair_summary.csv` | Five hourly d02 station medians only. |
| GFS has weaker 50--500 m AGL stability and larger fixed-layer transport wind than NAM under both feedback modes. | C17; `retention_pair_summary.csv`; promoted retention figure | The wind metric is a proxy, not measured basin export or a chemistry-model ventilation coefficient. |
| The within-product feedback response is much smaller than the driving-product contrast. | C18; pair and interaction summaries | This is an effect-size statement for one five-hour d02 sample, not general feedback equivalence. |
| Surface observations show recurring floor-to-bench temperature separation around the event. | C23; promoted observation figure | Spatial context consistent with a cold pool, not an observed inversion depth or basin-volume measurement. |

## High-priority scientific gates

1. **Observation provenance and QC.** The cache has a verified hash and reproducible pull command, but the API QC parameters, provider citation, station/sensor metadata, license, and public-access route are not recorded.
2. **No independent vertical observation.** The paper has no promoted sounding, profiler, or colocated temperature profile with which to validate inversion depth or the 50--500 m modeled layer.
3. **Product-level attribution only.** GFS versus NAM bundles the products' native grids, data-assimilation systems, vertical inputs, initial state, and six-hour lateral-boundary evolution.
The design cannot attribute the response to initialization alone or establish a universal GFS/NAM ranking.
4. **Temporal scope and spin-up choice.** Five post-spin-up hours do not establish persistence, event evolution over multiple days, or robustness to the two-hour exclusion.
5. **No inferential sample.** The WRF runs are deterministic and unreplicated.
The circular block ranges are useful only as a descriptive perturbation of five hourly medians and must not be presented as confidence intervals or significance tests.
6. **Fixed-column representativeness.** The 11 stations are not an area-weighted basin sample.
Nearest-cell terrain mismatch is modest in the default d02 grid (median -2.0 m; range -32.4 to +14.3 m), but that does not resolve exposure, slope, or coverage bias.
7. **No chemistry result.** The promoted evidence contains no ozone, precursor, deposition, photolysis, or chemical-mechanism output.
The Discussion may state implications for the meteorological state supplied to chemistry, not a demonstrated ozone response.

## Figure and code audit

The synthetic smoke suite passed for surface scoring, observation plots, cross-sections, upper-air rotation, and common-AGL retention analysis.
The retention generator correctly checks common grids and complete station/hour coverage, destaggers and rotates winds, interpolates to common AGL coordinates, pairs contrasts before aggregation, and records hashes and commands.

Remaining code and presentation risks are:

- The promoted Figure 2 labels the 8 K line as a “CAP threshold,” while the ledger supports only a literature reference value.
  The two generators now use the guarded label, but the promoted PDF must be regenerated on CHPC and re-hashed before replacement.
- `case_study_2013_obs.py` does not set or record Synoptic QC parameters and intentionally has broken no-argument defaults inherited from a separate January workflow.
- Subhourly observations are averaged within each clock hour without a documented completeness rule or observation-error treatment.
- The layer-mean wind can distinguish the four simulations, but it does not calculate flow through the basin boundary, cold-pool volume, or pollutant residence time.
- The two-hour circular resampling of five values has little inferential content; the full plotted time series, hourly range, and sign count are more transparent.
- The promoted bulk-theta PDF cannot be regenerated on the writing host because the hashed observation cache remains on CHPC scratch.

## Literature and citation audit

The present five-paper bibliography supports a guarded motivation:

- Ahmadov et al. (2015) supports the coupled role of confinement, emissions, snow-enhanced photolysis, and deposition, but its own conclusions are conditioned on meteorological adequacy.
- Neemann et al. (2015) supports case-specific snow/cloud sensitivity and documents important domain and bounding-experiment limits.
- Matichuk et al. (2017) supports emissions, deposition, and meteorological uncertainty; improved temperature profiles did not consistently improve ozone profiles.
- Tran et al. (2018) supports sensitivity to explicitly defined FDDA treatments, not attribution of any local archive run to the published experiment.
- Davies et al. (2025) supports the snow/cold-pool/photolysis motivation while emphasizing sparse and noisy Basin observations.

Before submission, the Paperpile export still needs sources for WRF, the exact GFS and NAM products, Synoptic data, and any statistical or diagnostic method that is not defined completely in the text.
Report syntheses remain routing context until their metadata and exact passages are verified.

## Planning corrections made with this audit

- `ROADMAP.md` no longer calls narrative freeze complete while observation metadata, source checks, and coauthor interpretation remain open.
- C23 and C24 separate the defensible observed surface context from unsupported inversion/basin-volume claims.
- `tasks/microtasks.md` now exposes the observation-provenance gate and the Figure 2 label correction, and no longer marks already drafted Discussion, Conclusions, and Abstract work as blocked or later.
