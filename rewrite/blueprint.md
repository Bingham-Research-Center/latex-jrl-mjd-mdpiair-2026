# Evidence-led blueprint for the blank-slate rewrite

## Decision in one page

### Research question

Across four otherwise matched short WRF integrations, how does the meteorological state relevant to cold-pool retention and dilution respond to the driving-data product, and is that response reproduced under both one-way and two-way nest feedback?

### Defensible answer

Over the fixed 14--18 UTC d02 station-column sample, the GFS-driven members are warmer at the surface, less stable from 50 to 500 m AGL, and faster in a fixed-layer transport-wind metric than the matched NAM-driven members.
The stability and transport-wind differences keep the same sign in all five hours under both feedback modes.
Within-product feedback responses are much smaller for these metrics.

### Scientific meaning

The four simulations deliver materially different lower-layer meteorological states to a possible downstream chemistry model.
The experiment tests the adequacy of that input state; it does not calculate dilution, basin export, residence time, or ozone.

### Claims that remain out of bounds

- GFS is generally inferior to NAM.
- The difference is caused by initialization alone.
- The simulated 50--500 m layer has a verified observed inversion counterpart.
- The five-hour separation proves cold-pool persistence or breakup.
- Meteorology dominates emissions, deposition, photolysis, or mechanism uncertainty.
- One-way and two-way feedback are generally equivalent.
- Any archived resolution, nudging, terrain, or PBL sequence belongs in the core result without its own gate.

## Experiment and evidence spine

| Role | Stable IDs | Contrast | What is held common | What remains bundled |
|---|---|---|---|---|
| Primary replication 1 | X6 minus X5; CMP01 | GFS minus NAM under two-way feedback | WRF version, domains, levels, physics, terrain class, initialization time, valid window, output cadence, FDDA off | Product grids, analysis systems, vertical inputs, assimilated observations, initial state, and boundary evolution |
| Primary replication 2 | X10 minus X3; CMP02 | GFS minus NAM under one-way feedback | Same controls as CMP01 | Same product-level bundle |
| Secondary bound 1 | X10 minus X6; CMP03 | one-way minus two-way within GFS | Product family and metgrid inputs | Feedback response for one product and five-hour regime |
| Secondary bound 2 | X3 minus X5; CMP04 | one-way minus two-way within NAM | Product family and configuration apart from feedback | Feedback response for one product and five-hour regime |
| Interaction | CMP05 | GFS feedback response minus NAM feedback response | paired station, hour, domain, and window | deterministic source-conditioned interaction |

The exact archive paths and hashes live in `verification/provenance/run-inventory.csv`.
The experiment is deterministic and unreplicated; no population inference follows from the four integrations.

## Claim-to-artifact map

| Manuscript use | Ledger row | Verified artifact | Exact wording limit |
|---|---|---|---|
| Four-run factorial identity | C02 | run and comparison inventories | Call the factor a driving-data product, not one isolated atmospheric variable. |
| Observed event context | C23 | `figures/obs_temp_timeseries_feb0102.pdf`; observation cache hash in the manifests | Four stations show a recurring floor-to-bench surface pattern consistent with cold-pool conditions; they do not measure inversion depth or volume. |
| Station-column terrain match | C24 | `verification/data/retention_station_timeseries.csv` | Median model-minus-station elevation is -2.0 m, range -32.4 to +14.3 m; this does not establish representativeness. |
| Surface temperature response | C04, C25 | `verification/data/surface_skill_pair_summary.csv` | GFS-minus-NAM paired T2-bias contrasts are +1.79 degrees C under two-way and +1.76 degrees C under one-way feedback. |
| Common-AGL response | C17, C25 | `verification/data/retention_pair_summary.csv`; promoted retention figure | GFS-minus-NAM stability is -3.63/-3.65 K and transport wind +0.79/+0.99 m s-1 for two-way/one-way feedback; all five hourly medians retain sign. |
| Feedback bound | C18, C25 | pair and interaction summary CSVs | GFS one-minus-two is -0.066 K and +0.104 m s-1; NAM is +0.002 K and +0.006 m s-1; interaction is -0.103 K and +0.097 m s-1. |
| PBLH interpretation | C20 | retention summaries and figure | Native PBLH does not reproduce the product separation and remains scheme dependent. |
| Chemistry guardrail | C11, C21 | exact passages in the five current journal sources | Meteorological fidelity is necessary for attribution, not uniquely dominant. |
| Evidence limits | manuscript audit | `notes/manuscript-audit-2026-07-13.md` | Five hours, fixed columns, no independent vertical profile, no chemistry, and no formal sample. |

## What the literature critiques change

The critiques are routing and design inputs, not citable sources.
The paper must cite the underlying publication after checking its passage.

| Underlying study | Practice worth retaining | Failure mode to avoid here | Role in the rewrite |
|---|---|---|---|
| Ahmadov et al. (2015) | Coupled process tests and candid model limitations | Inventory calibration and meteorological ventilation can be degenerate; single-receptor results should not become basin-wide rankings | Establish that emissions and meteorology cannot be apportioned by concentration agreement alone. |
| Neemann et al. (2015) | Multi-platform cold-pool evaluation and explicit failure reporting | A process-off microphysics case is a bound; the validated meteorological grid must match the grid supplied to chemistry | Motivate evaluation of the actual d02 layer and cautious case-specific wording. |
| Matichuk et al. (2017) | Basin-wide, instrument-aware evaluation and honest contradictory outcomes | Concentration-tuned emissions can absorb mixing, photolysis, and deposition error; improved temperature profiles need not improve ozone | Support the rule that meteorological adequacy precedes but does not settle chemical attribution. |
| Tran et al. (2018) | Held-out surface verification and mechanism-first diagnosis of FDDA behavior | “Nudging” is a compound treatment; analysis bias, vertical gates, assimilated sites, and circular wind statistics must be exposed | Justify exact configuration disclosure and keep heterogeneous nudged runs out of the factorial. |
| Later report syntheses | Time-resolved failure to accumulate a confined quantity is more revealing than an episode mean | Related report slices and unresolved runs are not independent validation | Motivate retention and ventilation diagnostics only; no report claim enters prose before metadata and passage checks. |
| External cold-pool synthesis | Common-AGL and time-resolved stability/wind diagnostics are portable design choices | Effect sizes and basin behavior are not portable across cases | Method context only unless an underlying source survives citation freeze. |

## Narrative architecture

| Section move | Job | Evidence or citation route | Stop condition |
|---|---|---|---|
| Introduction 1 | Define the air-quality consequence of a shallow mixing volume | Ahmadov, Neemann, Davies | Do not imply that the present simulations contain chemistry. |
| Introduction 2 | Show why concentration agreement cannot apportion meteorology, emissions, deposition, and mechanism | Ahmadov and Matichuk critiques, then source passages | Do not rank error sources. |
| Introduction 3 | Show why configuration labels and surface scores are insufficient | Neemann and Tran critiques, then source passages | Do not transfer their sensitivity magnitudes. |
| Introduction 4 | State the missing controlled question | CMP01--CMP05 and C14 | Keep it at product response plus feedback replication. |
| Methods 1 | Put the factorial and estimands before configuration detail | C02, inventories | Expose the product bundle and deterministic scope. |
| Methods 2 | Define the common sample and observation limits | C03, C23, C24 | Keep the surface network separate from vertical validation. |
| Methods 3 | Define common-AGL stability and transport wind | retention analysis record | Do not rename transport wind as ventilation rate or export. |
| Results 1 | Establish case context | promoted observation figure | No inversion-depth claim. |
| Results 2 | Lead with the replicated common-AGL product response | C17 and promoted retention figure | Report both feedback modes and hourly sign counts. |
| Results 3 | Use surface response and feedback effects as corroboration and bound | C04, C18, C20, effect table | Do not let aggregate skill replace layer behavior. |
| Discussion 1 | Interpret a product-level response, not a universal product ranking | C17, inventories | Initial versus boundary contribution stays unresolved. |
| Discussion 2 | Translate to a chemistry-input-state consequence | C11, C13, C14 | No ozone effect size or dominant-error claim. |
| Discussion 3 | Make limitations determine the next tests | manuscript audit | Longer run, vertical observations, and boundary attribution precede coupled attribution. |
| Conclusion | Answer only the two research questions | C17, C18 | Retain the five-hour and four-simulation nouns. |

## Figure decisions

| Slot | Artifact | Decision | Why |
|---|---|---|---|
| Figure 1 | `figures/obs_temp_timeseries_feb0102.pdf` | Include | Efficiently establishes multi-day surface context while its caption can state the spatial-profile limitation. |
| Figure 2 | `figures/wrf_retention_ventilation_d02_14to18.pdf` | Include as the main result | Directly shows both factors, the common-AGL metrics, time evolution, station spread, and the scheme-dependent PBLH companion. |
| Current bulk-theta panel | `figures/wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf` | Hold from the test manuscript | It shows only the two-way pair, uses horizontally separated sites, and the promoted PDF still needs the corrected “8 K literature reference” annotation. |
| L04 effect-size panel | summary CSVs already tracked | Best next local figure | It can summarize all five estimands without new WRF output; promote only after a manuscript-specific script, provenance row, and visual review. |
| L10 domain/station locator | current candidate | Conditional Methods figure | Add only if readers cannot understand why d02 is the common domain or how the fixed sites are distributed. |
| Common-AGL GFS-minus-NAM sections | CHPC archive | Reviewer reserve or supplement | They can test whether the response is shallow and basin confined, but need a matched-time selection and manifest promotion. |
| Heat-deficit map/time series | CHPC product plus exploratory narrative | Hypothesis-generating only | The “fails to maintain” reframe requires a reproducible basin definition, post-spin-up trajectory check, and ledger row before prose. |
| Resolution, nudging, PBL, and terrain families | heterogeneous or gated archive sets | Exclude from core figures | They answer different or not-yet-controlled questions. |

This two-figure core is intentionally smaller than the current three-figure baseline.
The effect table carries the factorial magnitude; a new figure must add a distinct decision, not duplicate it.

## Gates

### Must close before coauthor circulation

1. Record Synoptic provider citation, access route, API QC flags, station ownership, sensor metadata, completeness rule, uncertainty treatment, and license.
2. Add WRF, GFS, and NAM citations plus map projection, domain dimensions and centers, time step, boundary interval, static-geography versions, and snow initialization from as-run evidence.
3. Verify every literature statement against the underlying paper passage and complete the Paperpile export for sources that survive.
4. Decide whether the two-site bulk-theta panel returns after CHPC regeneration.
5. Obtain author, CRediT, funding, acknowledgment, conflict, and data-release decisions.

### Needed for a stronger mechanism paper, but not to write this bounded draft

1. Extend the matched factorial through a provenance-checked multi-day period.
2. Add an independent in-basin sounding, tethersonde, profiler, or validated remote-sensing profile.
3. Separate initial-state from lateral-boundary contributions.
4. Validate and productize any heat-deficit maintenance result.
5. Cross selected meteorology with emissions and mechanisms in a separate coupled factorial.

### Prohibited shortcuts

- Do not treat a critique, synthesis, meeting note, repeated number, or polished image as independent evidence.
- Do not infer run identity from a filename.
- Do not add a non-promoted figure to `main.tex`.
- Do not convert descriptive block ranges into confidence intervals or significance.
- Do not describe `trang_ref` as the literal Tran et al. (2018) run.
- Do not let a missing citation become an invented key.

## Rewrite acceptance test

The experimental manuscript is ready to replace the baseline only when a skeptical reader can answer, from the paper alone:

1. exactly which four runs were compared and what each contrast changes;
2. why the common domain, stations, and five-hour window were chosen;
3. what the stability and transport-wind metrics do and do not measure;
4. which result replicated across feedback modes;
5. how large the feedback response was relative to the product response;
6. why this matters to chemistry without constituting a chemistry result;
7. which observations and timescales remain absent;
8. which next experiment would distinguish the leading unresolved explanations.
