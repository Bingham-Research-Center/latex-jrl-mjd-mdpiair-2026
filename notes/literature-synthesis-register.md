# Literature synthesis register

Supporting analysis only; this file is excluded from the MDPI submission package.

The four synthesis directories under `~/reviews/synth-*` were inspected on 10 July 2026.
They are critiques of linked study sets, not citable publications and not independent evidence.
Use them to locate contradictions, design gaps, and source passages; cite the underlying paper or report after verifying it.

## Register

| Collection | What it combines | What the synthesis is critiquing | Best manuscript use | Citation state |
|---|---|---|---|---|
| `synth-ahmadov+neemann+tran` | Ahmadov et al. (2015), Neemann et al. (2015), and Tran et al. (2018) | Three peer-reviewed studies sharing the 2013 Uinta Basin episode but pulling emissions/chemistry, snow/cloud meteorology, and FDDA levers under different models and baselines | Introduction framing and experiment-design cautions | All three keys already exist in `paperpile.bib`: `Ahmadov2015-zm`, `Neemann2015-ws`, `Tran2018-ax`. |
| `synth-bingham+saprc+tran` | BRC 2023 annual-report section 8, the 2015 low-temperature SAPRC report, and the 2021 Uinta Basin Ozone SIP WRF MPE report | The BRC/USU configuration lineage: incomplete self-citation, missing namelist-level disclosure, WRF-version discontinuities, snow/LSM confounding, and a repeatedly lost ice-fog fix | Methods disclosure standard, archive fingerprinting, and future controlled experiments | Underlying reports are not in the current bibliography; Paperpile placeholders below. |
| `synth-ubaqr19+ubaqr20+tran` | Tran et al. (2018), UBAQR-2019 section 8, and UBAQR-2020 section 5 | The group sequence from surface nudging, to sounding nudging, to chemistry mechanisms; especially uncrossed meteorology/mechanism levers and changing platforms/emissions | Strongest check on a meteorology-only narrative; held-out verification and factorial-design guidance | `Tran2018-ax` exists; both annual-report sections need real Paperpile entries. |
| `synth-ramboll+topdown+rmp` | A 2023 CAMx mechanism-sensitivity report, a top-down inventory report section for a 2019 episode, and a 2022 utility-report section on a failed 2019 CAMx application | Downstream consequences when the meteorological driver vents or dilutes the cold pool; attribution among meteorology, inventory, and mechanism; and overclaims about profile nudging | Motivation for retention/ventilation diagnostics, time-resolved evaluation, and run-level provenance | All three reports need verified metadata and Paperpile entries; the synthesis and extracted critiques are not citable sources. |
| `synth-arthur+foster+lareau` | Lareau et al. (2013), Foster et al. (2017), and Arthur et al. (2022) | External cold-pool diagnostic and sensitivity-design lessons across observational, surface-state, and turbulence/diffusion studies | Context for common-AGL, time-resolved stability and wind diagnostics; never evidence for a Uinta result | No members are in the current Paperpile export; retain as non-manuscript context until a source survives narrative freeze. |

## Source-passage crosswalk

This crosswalk formalizes the critique and synthesis inputs without citing them as evidence.
Every cited passage below is in the underlying publication or report.
The local critique or synthesis is only the route by which the passage was located.

| Input route | Underlying source and exact passage | Ledger link | Citation state and use limit |
|---|---|---|---|
| `matichuk-cmaq-ub-2017/critique.md` | Matichuk et al. (2017), Abstract; §§3--4: improved WRF temperature profiles did not consistently improve ozone profiles, and the authors retain emissions uncertainty. | C11 | `Matichuk2017-bq`; context for the non-unique meteorology guardrail, not a ranking of error sources. |
| `ahmadov-ubwo-2015-acp/critique.md` | Ahmadov et al. (2015), §4.2.3 and §5: inventory/precursor sensitivity experiments and their stated limits. | C11 | `Ahmadov2015-zm`; context for inventory and chemistry uncertainty, not a basin-wide control recommendation. |
| `neemann-2015-UB-CAP/critique.md` | Neemann et al. (2015), Abstract; §§2.2--2.3: snow, albedo, and cloud-microphysics sensitivity treatments for CAP structure and ozone. | C21 | `Neemann2015-ws`; demonstrates interacting levers, not an isolated snow or cloud effect for the present runs. |
| `notes/literature/tran-2018-fdda/critique.md` | Tran et al. (2018), Table 1 and §§2.1--2.3: four FDDA configurations, published surface-temperature statistics, and evaluation design. | C09, C21 | `Tran2018-ax`; retain the published statistic as heterogeneous context and do not identify a local run as the paper run. |
| `synth-ahmadov+neemann+tran/synthesis.md` | Ahmadov et al. (2015), §4.2; Neemann et al. (2015), §§2.2--2.3; Tran et al. (2018), §§2.1--2.2.2. | C11, C21 | Use the three underlying journal sources above; their differing model, chemistry, and intervention designs are not a factorial. |
| `synth-bingham+saprc+tran/synthesis.md` | *Adapting the SAPRC Chemistry Mechanism for Low Temperature Conditions* (2015), §6; *Uinta Basin Ozone SIP Meteorological Modeling---WRF Model Performance Evaluation* (2021), reported configuration sections; Bingham Research Center Annual Report (2023), §8. | C21 | `PAPERPILE-TODO`; methods-disclosure and future-design context only. |
| `synth-ubaqr19+ubaqr20+tran/synthesis.md` | UBAQR 2019 Annual Report, §8; UBAQR 2020 Annual Report, §5; Tran et al. (2018), §§2.1--2.3. | C11, C21 | UBAQR sources remain `PAPERPILE-TODO`; do not infer a general ordering of meteorology and chemistry. |
| `synth-ramboll+topdown+rmp/synthesis.md` | Ramboll (2023), §§1.3 and 3.3; top-down inventory report, §9.7; Rocky Mountain Power (2022), §III.B. | C13, C14 | All reports remain `PAPERPILE-TODO`; related 2013/2019 contexts are not independent tests. |
| `synth-arthur+foster+lareau/synthesis.md` | Lareau et al. (2013), Fig. 3 and §Initial Findings; Foster et al. (2017), §§2.1--2.2 and Table 1; Arthur et al. (2022), Table 1 and Figs. 3--4. | C22 | No current Paperpile keys; external CAP design context only. |
| `wrf-ozone-studies/_extracts/ramboll-racm2-2023-critique.md` | *Assessing Wintertime Ozone Prediction Sensitivity to Photochemical Mechanism* (2023), §§1.3 and 3.3.1. | C13, C14 | `PAPERPILE-TODO`; fixed-driver mechanism context only. |
| `wrf-ozone-studies/_extracts/topdown-inventory-s9_6-9_7-critique.md` | *Top-Down Estimates of Emissions from Oil and Gas Production in the Uinta Basin*, §9.7. | C13 | `PAPERPILE-TODO`; the stated ventilation interpretation is episode- and run-identity-limited. |
| `wrf-ozone-studies/_extracts/rmp-2022-sIIIB-critique.md` | *Projecting the Impact of Electrification of the Uinta Basin Oil and Gas Fields on Air Quality* (2022), §III.B and Figs. 19--21. | C13, C14 | `PAPERPILE-TODO`; retained as a compromised-model-state warning, not validation. |

## 1. Peer-reviewed 2013 modeling triad

Source: `~/reviews/synth-ahmadov+neemann+tran/synthesis.md`.

### Context

The set shares the February 2013 target but is not a controlled factorial experiment.
Ahmadov changes inventory/chemistry in WRF-Chem, Neemann changes snow and cloud treatment, and Tran changes data assimilation in WRF coupled to CMAQ.

### What it critiques

- Ahmadov's inventory inference is conditioned on meteorology being adequate, while Neemann and Tran show large configuration and inversion sensitivities.
- Tran's artificial primary-formaldehyde workaround revisits an emissions/mechanism failure already exposed by Ahmadov, but under a different CTM mechanism and inventory.
- The literature never crosses ice-retention microphysics with observational nudging, so it cannot show whether the two interventions cooperate or conflict.
- All three lean on NAM deficiencies, yet none publishes the direct NAM-versus-sonde profile comparison that would anchor the causal story.
- Cross-paper effect sizes cannot be added because baselines, chemistry, inventories, and verification differ.

### Useful consequences here

- The GFS/NAM touchstones can address part of the missing driving-analysis question if their as-run configurations are reconciled.
- A clean main result should concern matched meteorological comparisons, not adjudicate inventory or formaldehyde causality.
- Snow must be treated as two interfaces: its effect on WRF cold-pool structure and the separate albedo/photolysis treatment seen by a chemistry model.
- Any process-off experiment is a bound, not automatically an estimate of realistic effect size.

## 2. BRC/USU 2015--2023 lineage

Source: `~/reviews/synth-bingham+saprc+tran/synthesis.md`.

### Context

The members are an internal institutional lineage rather than three equivalent papers: a whole 2015 chemistry report, a whole 2021 WRF MPE report, and one section of the 2023 BRC annual report.
The synthesis asks whether later configuration recommendations build coherently on earlier BRC findings.

### What it critiques

- The 2023 physics study does not engage the center's earlier FDDA, version, snow-initialization, and microphysics findings in the inspected section.
- A large Noah warm failure is not isolated from undocumented snow initialization, despite Noah being usable in the earlier documented-snow lineage.
- WRF v3.9 outperforms v4.2 in the 2021 report, while v4.3.3 is later tested without a fixed-physics version bridge.
- The 2015 Thompson ice-retention modification is absent from the later standard-Thompson work, which then re-discovers the warm-cloud/ice-fog failure.
- Multi-kelvin meteorological temperature errors are dismissed or discussed without propagating them through winter chemistry.
- Recommended configurations remain difficult to reproduce because exact namelist options, snow procedures, and nudging coefficients are incompletely archived.

### Useful consequences here

- The Methods inventory must record namelist option numbers, snow initialization, nudging variables/coefficients, version, spin-up, and conversion tools.
- LSM, PBL, microphysics, snow, version, and nudging should not be ranked from unrelated runs.
- Version and snow initialization are candidate controlled threads if John's CHPC inventory exposes suitable pairs.
- Ice fog and valley winds are credible reviewer-reserve/future-work problems, but not automatic main-paper narratives.

## 3. Tran/UBAQR 2018--2020 arc

Source: `~/reviews/synth-ubaqr19+ubaqr20+tran/synthesis.md`.

### Context

This is the closest thing to a longitudinal experiment program: Tran's four FDDA configurations, UBAQR-2019's sounding-nudging ladder, and UBAQR-2020's mechanism comparison share a model lineage and much of the 2013 episode.
They still change WRF versions, CTMs, emissions bases, and evaluation practice between stages.

### What it critiques

- “Nudging” is not one lever: surface temperature/wind nudging and sounding temperature/moisture nudging can change clouds in opposite directions.
- The later sounding study reverses the earlier suggestion to nudge NAM moisture aloft, but both sides rely partly on unpublished comparisons.
- Within the extracted 2020 analysis, changing CB05 to RACM produces a larger ozone response than the earlier meteorological refinement ladder; this does not prove general mechanism dominance because platform/speciation and factorial controls remain incomplete.
- The best reported meteorology and best reported chemistry are never crossed, leaving compensating error unresolved.
- Verification repeatedly uses assimilation-adjacent sites, weakening claims of independent skill.
- Version fingerprints and `OBS_DOMAIN*` contents may help separate paper-era, sounding-nudging, and mechanism-study archive vintages.

### Useful consequences here

- The current paper must retain its “meteorology is necessary, not uniquely dominant” guardrail.
- Any nudging result needs the exact nudged variables, vertical/radius gates, coefficients, and held-out stations.
- The free-forecast touchstones can be useful precisely because their design differs from production nudging, but a fair comparison cannot treat that difference as one isolated lever.
- “Best meteorology × best mechanism” is a future coupled-study experiment, not a claim this meteorology paper can settle.

## 4. Downstream CAMx failure set

Source: `~/reviews/synth-ramboll+topdown+rmp/synthesis.md`.

### Context

The set assembles three BRC/USU-orbit report slices in which WRF meteorology drives CAMx.
The Ramboll mechanism study covers February 2013, whereas the top-down inventory and Rocky Mountain Power sections cover a late-February 2019 episode and may share a platform family.
They are related institutional products, not three independent replications, and the 2019 anchor run cannot yet be reconstructed consistently from the inspected material.

### What it critiques

- The 2019 inventory analysis finds modeled ambient precursors no higher than observations despite strongly elevated inventoried NOx, supporting excessive ventilation over a simple missing-emissions explanation for that episode; the regime and run identity remain unresolved.
- The consistent-platform mechanism study changes chemistry while holding its meteorological driver fixed, but no mechanism recovers observed ozone accumulation and the report attributes much of the miss to meteorology.
- Mechanism and emissions sensitivities measured inside a diluted model state are regime-bound; they do not show what those levers would do inside a realistically trapped cold pool.
- A utility report's claim that tethersonde nudging is required is neither a necessity nor a sufficiency result: non-profile-nudged counterexamples exist, and a later mechanism report still blames meteorology from a lineage that included profile nudging without identifying its exact run.
- Window or episode averages can look tolerable while the model misses day-over-day buildup, inversion retention, or event timing; several inherited printed statistics also fail basic arithmetic checks.
- Figure-level reuse obscures the exact WRF/CAMx run, version, forcing, and nudging state across the 2019 reports.

### Useful consequences here

- The paper has a sharper air-quality question than generic configuration ranking: does each WRF simulation retain the shallow, weakly ventilated layer that a chemistry model would receive?
- Every promoted comparison should include time-resolved stability, inversion-depth, wind, or another defensible retention/ventilation diagnostic alongside aggregate surface scores.
- The frozen five-hour touchstone window can support claims about short-window structure and evolution only; multi-day persistence remains literature motivation unless longer provenance-checked runs enter the experiment matrix.
- Sensitivities from failed or compromised states may be useful as paired differences, but they must be labeled as conditional on that state.
- Before any of these reports enters manuscript prose, verify its full bibliographic metadata and the exact underlying passage; do not cite this synthesis or its critiques.

## Cross-synthesis constraints on this manuscript

Across all four syntheses, the most defensible shared lessons are methodological:

1. Archive and disclose the exact configuration before interpreting its result.
2. Separate run identity, configuration equivalence, storage location, and report lineage.
3. Match domains, stations, windows, and assimilation independence before ranking simulations.
4. Expect interactions among snow, surface schemes, microphysics, nudging, version, and chemistry rather than additive sensitivities.
5. Validate the field, layer depth, ventilation, and grid actually supplied to downstream chemistry.
6. Pair aggregate metrics with time-resolved diagnostics that can expose premature cold-pool breakup or dilution.
7. Treat valley winds and ice fog as persistent weaknesses requiring direct evidence.
8. Treat sensitivities measured in a compromised model state as conditional on that regime.
9. Avoid attributing tuned concentration agreement to one input category.
10. Preserve null and contradictory results because they determine which narrative survives.

The syntheses do not establish a universal ordering of meteorology, emissions, and chemistry errors.
They establish that the ordering changes with configuration and that no reviewed sequence completes the factorial design needed to apportion all three cleanly.

## Candidate experiment ideas exposed by the syntheses

| Experiment | Relevance to this paper | Current status |
|---|---|---|
| GFS versus NAM initial/boundary state with otherwise identical short forecasts | Potential primary result | Touchstones exist; as-run equivalence TBC. |
| One-way versus two-way feedback | Potential secondary result | Pair exists; isolation TBC. |
| Direct driving-analysis versus sonde/profile comparison | Strong diagnostic for inherited error | Data and exact analysis fields TBC. |
| Snow initialization crossed with LSM | Possible later sensitivity | Inventory TBC. |
| Fixed-physics WRF version ladder | Possible later sensitivity | Inventory TBC. |
| Time-resolved inversion-retention and ventilation diagnostic across every promoted pair | Required diagnostic spine | Exact profile fields and observations TBC; the current five-hour window cannot establish multi-day persistence. |
| Ice-retention microphysics crossed with nudging | Future/reviewer reserve | No controlled pair established. |
| Surface-only versus profile temperature/moisture nudging with held-out sites | Future/reviewer reserve | Relevant archived lineage exists; exact production identities TBC. |
| Best meteorology crossed with a competent winter mechanism | Separate coupled-chemistry study | Outside the present paper's scope. |

## Paperpile citation placeholders

Do not add invented BibTeX keys or incomplete hand-written entries.
John will create a manuscript-specific Paperpile export containing the sources that survive narrative freeze.

- **PAPERPILE-TODO:** Uinta Basin Air Quality Research 2019 annual report, section 8 on tethersonde/sounding observation nudging; verify complete title, report authors/editors, institution, year, and stable URL.
- **PAPERPILE-TODO:** Uinta Basin Air Quality Research 2020 annual report, section 5 on meteorology/chemistry coupling and CB05/RACM comparisons; verify complete report metadata and stable URL.
- **PAPERPILE-TODO:** *Uinta Basin Ozone SIP Meteorological Modeling---WRF Model Performance Evaluation* (2021); verify exact author list, commissioning institution, report number, and stable URL.
- **PAPERPILE-TODO:** Bingham Research Center 2023 Annual Report, section 8, “Improvements to Methods for Simulation of Wintertime Inversions”; verify chapter authors and report metadata.
- **PAPERPILE-TODO:** *Adapting the SAPRC Chemistry Mechanism for Low Temperature Conditions* (2015 final report); verify exact authors, funder/recipient, report number, and stable URL.
- **PAPERPILE-TODO:** *Assessing Wintertime Ozone Prediction Sensitivity to Photochemical Mechanism* (2023 final report); verify the complete author list, report number, funder, and stable URL.
- **PAPERPILE-TODO:** *Top-Down Estimates of Emissions from Oil and Gas Production in the Uinta Basin*; verify the complete author list, publication year, institution, report number, and stable URL.
- **PAPERPILE-TODO:** *Projecting the Impact of Electrification of the Uinta Basin Oil and Gas Fields on Air Quality* (2022 final report to Rocky Mountain Power); verify the complete author list, institution, report number, and stable URL.

Until those entries exist, cite only the already verified Ahmadov, Neemann, and Tran journal articles in manuscript prose.
