# Complete Paperpile export for the first-round revision

Updated 18 September 2026 from the actual `main.tex` citation set.
The current bibliography has 37 entries; the main manuscript cites the nine keys below, all of which resolve.
The historical test/v3 sources use a subset of those nine.
The former five-paper seed checklist is superseded.
Do not hand-edit, prune, normalise or invent keys in `paperpile.bib`; John will supply one complete export.

## Existing cited records to retain

| Current key | Use in this revision |
|---|---|
| `Ahmadov2015-zm` | Uinta winter ozone, emissions sensitivity and attribution limits |
| `Davies2025-wy` | Uinta snow and winter-ozone context |
| `Lyman2015-aq` | Observed inversion/surface-temperature setting |
| `Mansfield2020-kl` | Longer-term Uinta winter-ozone record |
| `Matichuk2017-bq` | Coupled meteorology/chemistry and compensating errors |
| `Neemann2015-ws` | Cold-pool, snow, cloud and grid sensitivity context |
| `Oltmans2014-md` | Upper Green River Basin winter-ozone analogue |
| `Tran2018-ax` | FDDA, scheme-dependent PBL diagnosis and model lineage |
| `Tran2021-al` | Verified 2021 OSIP WRF MPE agency-report lineage |

Retain these keys where Paperpile permits it.
If the export uses a different key, verify the exact source identity and update the LaTeX citation, including historical build targets where needed; do not manufacture an alias by editing the export.
The similarly named `Tran2018-cx` record and `trang_ref` must not be substituted without checking the actual source.

## References currently carried in prose/footnotes

Include the following records when replacing the existing prose/footnote references with formal bibliography citations; verify the export metadata and use its actual keys.

- Whiteman, Bian and Zhong (1999), *Wintertime Evolution of the Temperature Inversion in the Colorado Plateau Basin*: DOI `10.1175/1520-0450(1999)038<1103:WEOTTI>2.0.CO;2`.
- Adler et al. (2023), *Evaluation of a Cloudy Cold-Air Pool in the Columbia River Basin in Different Versions of the HRRR Model*: DOI `10.5194/gmd-16-597-2023`.
- Skamarock et al. (2019), *A Description of the Advanced Research WRF Model Version 4*: DOI `10.5065/1dfh-6p97`; distinguish this technical note from the as-run WRF 4.8.0 release.
- The named physics references already listed in Methods: Thompson et al. (2008), Iacono et al. (2008), Jiménez et al. (2012), Tewari et al. (2004) and Hong et al. (2006).
- Exact forcing products and observation/data services used: GFS/NAM analyses, Synoptic Data PBC Mesonet, EPA AQS AirData and NASA GIBS/MODIS. Use the registered product/version/subset metadata rather than a generic product citation.
- Herbie and SynopticPy, already acknowledged by DOI, if formal software citations are included.

Metadata and source passages are routed through `notes/literature/verified-citations.md`, `notes/literature-synthesis-register.md` and the provenance inventories.
Additional historical reports remain leads unless the final manuscript actually uses them; the September report-source decision permits the existing focused lineage paragraph, not wholesale literature expansion.

## Replacement and close-out

1. John exports the complete manuscript collection once and replaces `paperpile.bib` wholesale.
2. Record export date and SHA-256; reconcile actual keys and source identities without changing exported entry contents.
3. Resolve the existing Methods footnotes using only verified export records, and check main/test/v3 citations and duplicate source identities.
4. Run `make final-draft-check`, `make submission-check` and `make package`; inspect the resulting PDF and confirm no undefined citations/references.
5. Resume `peer-review-reply` with the saved decisions and final compiled manuscript; update reply locators and obtain John's final wording approval.

The 18 September checkpoint deliberately retains the current bibliography unchanged and is available for review before this replacement.
