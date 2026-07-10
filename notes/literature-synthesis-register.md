# Literature synthesis register

Supporting analysis only; this file is excluded from the MDPI submission package.

The three synthesis directories under `~/reviews/synth-*` were inspected on 10 July 2026.
They are critiques of linked study sets, not citable publications and not independent evidence.
Use them to locate contradictions, design gaps, and source passages; cite the underlying paper or report after verifying it.

## Register

| Collection | What it combines | What the synthesis is critiquing | Best manuscript use | Citation state |
|---|---|---|---|---|
| `synth-ahmadov+neemann+tran` | Ahmadov et al. (2015), Neemann et al. (2015), and Tran et al. (2018) | Three peer-reviewed studies sharing the 2013 Uinta Basin episode but pulling emissions/chemistry, snow/cloud meteorology, and FDDA levers under different models and baselines | Introduction framing and experiment-design cautions | All three keys already exist in `paperpile.bib`: `Ahmadov2015-zm`, `Neemann2015-ws`, `Tran2018-ax`. |
| `synth-bingham+saprc+tran` | BRC 2023 annual-report section 8, the 2015 low-temperature SAPRC report, and the 2021 Uinta Basin Ozone SIP WRF MPE report | The BRC/USU configuration lineage: incomplete self-citation, missing namelist-level disclosure, WRF-version discontinuities, snow/LSM confounding, and a repeatedly lost ice-fog fix | Methods disclosure standard, archive fingerprinting, and future controlled experiments | Underlying reports are not in the current bibliography; Paperpile placeholders below. |
| `synth-ubaqr19+ubaqr20+tran` | Tran et al. (2018), UBAQR-2019 section 8, and UBAQR-2020 section 5 | The group sequence from surface nudging, to sounding nudging, to chemistry mechanisms; especially uncrossed meteorology/mechanism levers and changing platforms/emissions | Strongest check on a meteorology-only narrative; held-out verification and factorial-design guidance | `Tran2018-ax` exists; both annual-report sections need real Paperpile entries. |

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

## Cross-synthesis constraints on this manuscript

Across all three syntheses, the most defensible shared lessons are methodological:

1. Archive and disclose the exact configuration before interpreting its result.
2. Separate run identity, configuration equivalence, storage location, and report lineage.
3. Match domains, stations, windows, and assimilation independence before ranking simulations.
4. Expect interactions among snow, surface schemes, microphysics, nudging, version, and chemistry rather than additive sensitivities.
5. Validate the field and grid actually supplied to downstream chemistry.
6. Treat valley winds and ice fog as persistent weaknesses requiring direct evidence.
7. Avoid attributing tuned concentration agreement to one input category.
8. Preserve null and contradictory results because they determine which narrative survives.

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

Until those entries exist, cite only the already verified Ahmadov, Neemann, and Tran journal articles in manuscript prose.
