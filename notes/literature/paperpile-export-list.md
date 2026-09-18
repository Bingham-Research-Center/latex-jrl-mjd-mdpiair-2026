# Complete Paperpile export for the first-round revision

Updated 18 September 2026 after the citation and prose revision.
The unmodified Paperpile export has 14 entries; the main manuscript now resolves 39 references using it together with `review-references.bib`.
The [revision and source-check record](citation-tightening-20260918.md) lists the five textbook additions, data/software references and complete replacement identities.
The historical test/v3 sources retain the supplied export keys.
The former five-paper seed checklist is superseded.
John supplied `paperpile-update.bib` and explicitly authorised filtering it against this checklist on 18 September.
The 2,727-entry export was reduced to 14 matching records and renamed over `paperpile.bib`; exported entry contents were preserved.
Do not hand-edit metadata or invent keys; corrections remain Paperpile-owned.
The [replacement receipt](../../verification/provenance/paperpile-refresh-20260918.json) records the supplied-file and filtered-file SHA-256 hashes, exact retained keys and remaining gaps.
The export date is not embedded in the supplied file; 18 September is the supply/import date.

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
| `Tran2018-cx` | FDDA, scheme-dependent PBL diagnosis and model lineage; verified replacement for `Tran2018-ax` |
| `Tran2021-al` | Verified 2021 OSIP WRF MPE agency-report lineage |

Retain these keys where Paperpile permits it.
If the export uses a different key, verify the exact source identity and update the LaTeX citation, including historical build targets where needed; do not manufacture an alias by editing the export.
The supplied `Tran2018-cx` publisher URL resolves to the [same publication](https://www.sciencedirect.com/science/article/abs/pii/S1352231018300189) as the former `Tran2018-ax` DOI, `10.1016/j.atmosenv.2018.01.012`.
The historical test/v3 sources use the actual exported key.
The main article now uses the complete verified `Tran2018FDDA` record alongside the other replacements below; consolidate the corrected identity in Paperpile.
`trang_ref` remains a separate run identifier and must not be substituted for the publication.

## Records to consolidate into the next export

Import the verified records in `review-references.bib` into the manuscript's Paperpile collection.
They are already cited and included in the compiled article and delivery package; there are no remaining manuscript footnotes.
The addition file includes five textbooks, the missing physics references, exact GFS/NAM and observation/imagery service records, GMTED2010, and the acknowledged software.

Five incomplete or malformed export records have complete counterparts used by the main article: `Whiteman1999`, `Skamarock2019`, `Hong2006`, `Adler2023` and `Tran2018FDDA`.
The [identity mapping](citation-tightening-20260918.md#bibliography-ownership-and-migration) gives their supplied keys and corrections.
Reconcile these within Paperpile before exporting so that each work has one complete record.
Do not import the auxiliary `@string` declarations as publications; they only supply standard month names missing from the MDPI style.

The old SynopticPy DOI could not be verified; the current reference follows the author's repository-URL recommendation.
Use a release DOI only after matching the actual retrieval version.
The website access date is the documentation check date, 18 September 2026, distinct from the archived observation/input retrieval dates.

## Replacement and close-out

1. John consolidates the active records and identity corrections in Paperpile, then exports the complete manuscript collection for wholesale replacement.
2. Record export date and SHA-256; reconcile actual keys and source identities without changing exported entry contents.
3. Reconcile main/test/v3 citation keys and remove superseded auxiliary records only when the complete export replaces them; retain the no-footnotes contract and check duplicate source identities.
4. Run `make final-draft-check`, `make submission-check` and `make package`; inspect the resulting PDF and confirm no undefined citations/references.
5. Resume `peer-review-reply` with the saved decisions and final compiled manuscript; update reply locators and obtain John's final wording approval.

The current PDF uses the verified auxiliary bibliography while retaining the supplied Paperpile export unchanged.
The dated checkpoint PDF remains the earlier snapshot.
