# Citation and prose revision — 18 September 2026

Implemented John's six requested changes in `main.tex`.
The former Table 2 and Section 2.4 are removed; Section 2.3 now introduces the experiment groups in four sentences, with secondary pairs identified alongside their results.
Table 1 lists only the nine analysed configurations, omitting the unused X7/X8 design context.
The numerical appendix, scientific criteria and figure inputs are unchanged.
Repeated qualifications and numerical recitations have been consolidated; essential scope limits, failed tests, observation qualifications and principal effect sizes remain.

All seven footnotes have become bibliography citations, including the model/physics references, heat-deficit papers, observation and imagery services, sounding index and retrieval software.
The manuscript contract now rejects footnote commands and resolves citations against both bibliography files.
Website references print `(URL, accessed 18 September 2026)`; this is the documentation check date, not a replacement for archived data-retrieval timestamps.
The data citations identify the actual GFS grid 004 and NAM grid 218 zero-hour analyses and the AQS/MODIS subsets used.

## Five textbooks and two discretionary placements

| Source | Placement and support | Verification |
|---|---|---|
| Whiteman (2000), *Mountain Meteorology: Fundamentals and Applications* | **Author-review flag 1:** Introduction, mountain thermal contrasts and slope-flow background. This is contextual, not evidence of a simulated drainage mechanism. | [Oxford University Press](https://academic.oup.com/book/40903); DOI `10.1093/oso/9780195132717.001.0001`; [author's book page](https://home.chpc.utah.edu/~whiteman/homepage/book.html). |
| Wallace and Hobbs (2006), *Atmospheric Science: An Introductory Survey*, 2nd ed. | Surface potential temperature, dry static stability, and the hydrostatic conversion of column mass to pressure coordinates in the heat-deficit equation. | [Publisher contents](https://shop.elsevier.com/books/atmospheric-science/wallace/978-0-12-732951-2), Sections 3.2, 3.4 and 3.6; ISBN `9780127329512`. |
| Stull (1988), *An Introduction to Boundary Layer Meteorology* | Dry stability and the limits of a finite-layer endpoint difference; the wind bars are explicitly height means. | [Publisher contents](https://link.springer.com/book/10.1007/978-94-009-3027-8), stability and stable-boundary-layer chapters; DOI `10.1007/978-94-009-3027-8`. |
| Liou (2002), *An Introduction to Atmospheric Radiation*, 2nd ed. | Spectral absorption/scattering background for qualitative satellite interpretation. NASA's separate layer citation supplies the actual 7-2-1 colour interpretation. | [Publisher contents](https://shop.elsevier.com/books/an-introduction-to-atmospheric-radiation/liou/978-0-12-451451-5), solar absorption/scattering and remote-sensing chapters; ISBN `9780124514515`. |
| Wilks (2019), *Statistical Methods in the Atmospheric Sciences*, 4th ed. | **Author-review flag 2:** temporal-dependence background beside the descriptive block calculation. The citation does not validate five observations as an inferential sample. | [Publisher contents](https://shop.elsevier.com/books/statistical-methods-in-the-atmospheric-sciences/wilks/978-0-12-815823-4), inference and time-series chapters; ISBN `9780128158234`. |

These are included in the manuscript, not merely proposed.
The flags are kept here rather than printed in the article.
Publisher metadata and contents were checked; no uninspected textbook passage or page number is quoted.
The exact heat-deficit method remains attributed to [Whiteman et al. (1999), Section 6](https://home.chpc.utah.edu/~whiteman/homepage/articles/Whiteman1999J%20Appl%20Meteorol.pdf) and [Adler et al. (2023), Section 3.3](https://gmd.copernicus.org/articles/16/597/2023/).
The hydrostatic coordinate change and positive clipping are now explicit; the calculation itself is unchanged.

## Other source checks

- Model and schemes: the existing WRF technical-note identity and the [official WRF physics register](https://www2.mmm.ucar.edu/wrf/users/physics/phys_references.html) verify Skamarock, Thompson, Iacono, Jiménez, Tewari, Hong and Janjić. The [Tewari paper](https://www2.mmm.ucar.edu/wrf/users/physics/phys_refs/LAND_SURFACE/noah.pdf) identifies contribution 14.2A. The Version 4 technical note is a model reference, not a claimed DOI for release 4.8.0.
- Forcing and terrain: [NCEI GFS](https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast), [NCEI NAM](https://www.ncei.noaa.gov/products/weather-climate-models/north-american-mesoscale), and [USGS GMTED2010](https://pubs.usgs.gov/publication/ofr20111073). Exact forcing identities come from `verification/provenance/run-inventory.csv`; the GMTED citation identifies the source family, not a new terrain-grid evaluation.
- Observations and imagery: [Synoptic Time Series](https://docs.synopticdata.com/services/time-series), [EPA AirData](https://aqs.epa.gov/aqsweb/airdata/download_files.html), [NASA's layer documentation](https://github.com/nasa-gibs/worldview-options-eosdis/blob/master/common/config/metadata/modis/CorrectedReflectance.md), and the [Utah UBOS index](https://www.inscc.utah.edu/~u0198116/ubos/obs.html). Existing local provenance governs the actual samples and the provisional sounding timestamp. The raw sounding filename is retained in its reference; no new sounding analysis or raw-data retrieval was performed.
- Retrieval software: [Herbie's author-recommended citation](https://github.com/blaylockbk/Herbie#citation--acknowledgment) confirms the all-version DOI `10.5281/zenodo.4567540`. [SynopticPy's author-recommended citation](https://github.com/blaylockbk/SynopticPy#how-to-cite-and-acknowledge) uses its repository URL. The former footnote's `10.5281/zenodo.4567546` could not be verified and is not carried forward. A [verified 2025.9.0 record](https://zenodo.org/records/17066811) exists, but its version is not asserted as the study's retrieval environment. No Synoptic service DOI was verified; the provider receives a service citation and acknowledgement.
- Scientific Python: actual imports in the registered retention, heat-deficit, observation and plotting scripts justify citations for [NumPy](https://numpy.org/citing-numpy/), [SciPy](https://scipy.org/citing-scipy/), [pandas](https://pandas.pydata.org/about/citing.html), [Polars](https://docs.pola.rs/), [xarray](https://research.google/pubs/xarray-n-d-labeled-arrays-and-datasets-in-python/) and [Matplotlib](https://matplotlib.org/stable/project/citing.html). Software-paper citations identify the projects without inventing version pins.
- Tran (2018): [EPA HERO's bibliographic record](https://hero.epa.gov/reference/4439772/) supplies the full title, five authors, volume 177, pages 75–92 and DOI `10.1016/j.atmosenv.2018.01.012`; the publisher endpoint was inaccessible in this check. No new scientific claim is drawn from this metadata check.

## Bibliography ownership and migration

`paperpile.bib` remains byte-identical to the supplied 14-record export: SHA-256 `e3fb5486d195c1c6ba426dd515f92cb441ff71b0223dc63a9de888cdacf9d919`.
`review-references.bib` contains the verified additions and five complete replacement identities needed for a readable bibliography.
Only one identity for each work is cited in the compiled article:

| Uncited export key | Active verified key | Correction |
|---|---|---|
| `WhitemanUnknown-cy` | `Whiteman1999` | Year, journal, volume, pages and DOI. |
| `Skamarock2019-dk` | `Skamarock2019` | Institution and report number. |
| `Hong2006-wp` | `Hong2006` | Removes the DOI mistakenly exported as an arXiv `eprint`. |
| `Adler2023-zp` | `Adler2023` | Adds DOI. |
| `Tran2018-cx` | `Tran2018FDDA` | Full title, author list, volume, pages and DOI. |

The historical test/v3 source files keep their supplied keys and were not edited in this pass.
The auxiliary bibliography also defines the ordinary `jan`, `aug` and `dec` BibTeX strings omitted by the MDPI style, without changing the export.
John can consolidate these records through the next complete Paperpile export; actual exported keys must then be reconciled without retaining duplicate identities.
Final response locators must be checked against the shortened article before reply approval.

Validation and final hashes are recorded in `verification/provenance/citation-tightening-20260918.json` after the final rebuild and package inspection.
