# Small curated Paperpile export checklist

Supporting analysis only; this file is excluded from the MDPI submission package.

Status on 14 July 2026: **deferred / low priority** because John will provide a small
manuscript-specific export after the citation-independent integration batch.

`paperpile.bib` is unchanged.
Do not repair, normalize, or expand the current file; replace it wholesale only with
John's small Paperpile export.

No new BibTeX key is guessed below; Paperpile must generate each new key, which must then be recorded verbatim after the full export.

## Minimum small export

The next export needs the existing five cited papers plus the two verified heat-deficit
sources.
Everything else below is later-only and should be omitted unless the edited manuscript
actually cites it.

### Existing five items whose keys must not change

| Exact title | Required existing key | Identifier |
|---|---|---|
| Uinta Basin snow shadow: Impact of snow-depth variation on winter ozone formation | `Davies2025-wy` | doi:10.3390/air3030022 |
| Simulations of a cold-air pool associated with elevated wintertime ozone in the Uintah Basin, Utah | `Neemann2015-ws` | doi:10.5194/acp-15-135-2015 |
| Understanding high wintertime ozone pollution events in an oil- and natural gas-producing region of the western US | `Ahmadov2015-zm` | *Atmospheric Chemistry and Physics* 15, 411–429 |
| Evaluation of the Community Multiscale Air Quality Model for Simulating Winter Ozone Formation in the Uinta Basin | `Matichuk2017-bq` | doi:10.1002/2017JD027057 |
| Four dimensional data assimilation (FDDA) impacts on WRF performance in simulating inversion layer structure and distributions of CMAQ-simulated winter ozone concentrations in Uintah Basin | `Tran2018-ax` | doi:10.1016/j.atmosenv.2018.01.012 |

### Two verified items to add now

| Exact title | Identifier | Paperpile key after import | Intended use |
|---|---|---|---|
| Wintertime Evolution of the Temperature Inversion in the Colorado Plateau Basin | doi:`10.1175/1520-0450(1999)038<1103:WEOTTI>2.0.CO;2` | **TBC from Paperpile export** | Original basin-volume heat-deficit definition. |
| Evaluation of a Cloudy Cold-Air Pool in the Columbia River Basin in Different Versions of the HRRR Model | doi:10.5194/gmd-16-597-2023 | **TBC from Paperpile export** | Closest published column heat-deficit variant. |

## Later only if retained in manuscript prose

| Exact title | Identifier | Paperpile key after import | Intended use |
|---|---|---|---|
| A Description of the Advanced Research WRF Model Version 4 | doi:10.5065/1dfh-6p97 | **TBC from Paperpile export** | General WRF Version 4 technical reference; not an exact 4.8.0 DOI. |
| The Persistent Cold-Air Pool Study | doi:10.1175/BAMS-D-11-00255.1 | **not currently needed** | The non-equivalent 8 K line has been removed; import only if a distinct contextual sentence survives. |

### Software, data-product, and observation-service items

| Exact item title or corporate title | Stable identifier | Paperpile key after import | Required qualifier |
|---|---|---|---|
| WRF Model Version 4.8.0 | <https://github.com/wrf-model/WRF/releases/tag/v4.8.0> | **TBC from Paperpile export** | Software release, released 8 June 2026; pair with the Version 4 technical note and complete local commit. |
| Global Forecast System Analysis, grid 004 (0.5°) | <https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast> | **TBC from Paperpile export** | Corporate authors NOAA NCEI and NCEP; identify the 2 February 2013 12 and 18 UTC +00 subset, access date, filenames, and SHA-256 values. |
| North American Mesoscale Forecast System Analysis, grid 218 (12 km) | NCEI `gov.noaa.ncdc:C00630`, DSI 6173 | **TBC from Paperpile export** | Corporate authors NOAA NCEI and NCEP; identify exact cycles, access date, filenames, and SHA-256 values. |
| Synoptic Data PBC Mesonet API, Time Series service | <https://docs.synopticdata.com/services/time-series> | **TBC from Paperpile export** | Corporate author Synoptic Data PBC; include access date, acknowledgement, named networks, explicit QC request, and provider-specific reuse status. |

### Retained report items

| Exact title | Verified metadata | Paperpile key after import | Intended use |
|---|---|---|---|
| 2019 Annual Report: Uinta Basin Air Quality Research | Seth Lyman, Marc Mansfield, Huy Tran, Trang Tran, and Makenzie Holmes; BRC_190926A; 26 November 2019 | **TBC from Paperpile export** | Discussion context for the sounding-nudging ladder and held-out Fantasy Canyon check. |
| Uinta Basin Ozone State Implementation Plan Meteorological Modeling: Weather Research and Forecasting (WRF) Model Performance Evaluation | Trang Tran and Huy Tran; report to Utah Division of Air Quality; 2021 | **TBC from Paperpile export** | Discussion context for the configuration ladder and process-level MPE. |
| Assessing Wintertime Ozone Prediction Sensitivity to Photochemical Mechanism | Ramboll US Consulting, Inc., Utah State University Bingham Research Center, and William Stockwell; report 1690022670; February 2023 | **TBC from Paperpile export** | Discussion context for fixed-driver, state-conditional mechanism sensitivity. |
| Top-Down Estimates of Emissions from Oil and Gas Production in the Uinta Basin: Final Project Report | Seth Lyman, John Lin, and Huy Tran; BRC_230711B version 2; 9 May 2024 | **TBC from Paperpile export** | Discussion context for precursor evidence and excessive ventilation in the studied 2019 run. |

## Explicitly excluded after report-source freeze

- *2020 Annual Report: Uinta Basin Air Quality Research* remains support-only because the relevant mechanism comparison is not cleanly crossed with platform, microphysics, and coupling.
- Bingham Research Center Annual Report (2023), §8, remains support-only because its configuration lineage is underdisclosed.
- *Adapting the SAPRC Chemistry Mechanism for Low Temperature Conditions* remains support-only because chemistry development is outside this manuscript's scope.
- *Projecting the Impact of Electrification of the Uinta Basin Oil and Gas Fields on Air Quality* remains support-only because the modeled sensitivities occupy a diagnosed diluted state.

## Small-export procedure

1. Confirm that the existing five records are present and that their exported keys remain exactly as listed.
2. Import Whiteman et al. (1999) and Adler et al. (2023) by DOI and inspect title, author, year, and source fields.
3. Add later-only records only when retained manuscript prose actually requires them.
4. Export this small manuscript collection from Paperpile as BibTeX and replace `paperpile.bib` wholesale.
5. Record the actual generated keys in this file without renaming the existing five.
6. Resolve only the citations that survive the next manuscript edit, then run `make check`, `make rewrite-check`, `make v3-check`, `make smoke`, and PDF inspection.

Until John supplies that export, MAN-09 and bibliography-dependent rewrite gates remain
open at low priority; citation-independent manuscript work continues.
