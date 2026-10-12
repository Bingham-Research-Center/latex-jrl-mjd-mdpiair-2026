# Final proof-return review route — 11 October 2026

Current branch: `jrl/proofs-round1`; John’s independent author-pass commit `be959eb` follows `b262a24`. He reports that the proof was submitted to MDPI. The new local PDF/ZIP reflect later TeX edits and need his visual check. PUB01 public release remains open; Codex will not submit to MDPI.

Use the [working PDF](proof-package/working/air-4472509-done.pdf) for printed appearance, the [working TeX](proof-package/working/air-4472509-done.tex) for source comments, the [reply table](PROOFER-REPLY-TABLE.md) for exact old/new TeX and PDF locators, and the [catalogue](notes/proof-query-catalogue.md) only when an exact publisher quotation or evidence detail is needed. The [received proof](proof-package/air-4472509-english/air-4472509-done.tex) is immutable.

| # | Microtask | Look at | Status / decision |
| ---: | --- | --- | --- |
| 1 | Confirm the review version and original preservation. | [Handoff](PROOFING-HANDOFF.md), [working TeX](proof-package/working/air-4472509-done.tex), received source; author-pass commit `be959eb`. | Source hash `3dec02cd…b55e`; received 33-file bundle unchanged. |
| 2 | Check title, author order, affiliations, four ORCIDs and emails. | PDF p. 1; reply-table EE01, MDPI01–02. | Author-confirmed; review the printed first page. |
| 3 | Check the italic research-question emphasis. | PDF p. 2; MDPI03. | Author requested retention. |
| 4 | Check the observation-provider/instrument limitation and WRF/WPS/terrain versions and sources. | PDF pp. 3–6; MDPI04a/b, JRL01, JRL03; approved MDPI04 reply. | Scoped wording approved; verify no blanket absence claim. |
| 5 | Check software versions/citations and AI-use disclosure. | PDF pp. 5–6, 16; MDPI18, JRL02; Methods and back matter in working TeX. | Author-confirmed model names/CLI use; no per-session snapshot claim. |
| 6 | Check first-citation order and placement: Figures 1–9; Tables 1, A1–A6; Section 3.4 above Figure 4; production-size notice. | PDF pp. 3–15; MDPI05a/b, MDPI07, MDPI08c, JRL08. | Source/auxiliary checks passed; the earlier PDF had author approval. Check the new PDF. |
| 7 | Check Figures 1–3 for overlap, Figure 2 marker key and NASA institution wording. | PDF pp. 3–4, 7; MDPI06, MDPI08a/b, MDPI11, JRL04. | Earlier author visual approval recorded. |
| 8 | Check Figures 4–9: panel descriptions, interquartile/night/sensitivity shading, dashed features and resized label legibility. | PDF pp. 8–12; MDPI12–16, JRL05a–e. | John confirmed the earlier PDF; check this new PDF. |
| 9 | Check equation typography and appendix-table citation format. | PDF pp. 5–8; MDPI09–10. | Source changes and author format decision recorded. |
| 10 | Check Table 1 and A1–A6: width, rows, labels, rounded A1 coordinates and retained A5 rules. | PDF pp. 5, 13–15; MDPI17, JRL06a–c, JRL07. | Tables were approved in the earlier PDF; check this new PDF. |
| 11 | Check Data Availability, Acknowledgements, Conflicts of Interest and AI statement; confirm no manuscript footnotes or retired-supplement references. | PDF p. 16; JRL09–10, PUB01. | Repository is public; anonymous API and proof-source access verified. |
| 12 | Check conference dates/locations, NCAR/USGS publisher locations, Herbie DOI and McKinney highlight. | PDF pp. 17–18; MDPI19–22, HL01; 49 embedded bibliography entries. | Source identities and author decisions recorded. |
| 13 | Read the 23 copy-ready replies; use the catalogue for any exact quotation. | [Journal replies](PROOFER-RETURN-REPLIES.md) and [51-row table](PROOFER-REPLY-TABLE.md). | The MDPI18 reply was revised for John’s Gemini clarification; check the current reply document. |
| 14 | Inspect the new local review ZIP: corrected TeX/PDF, template files and eleven figures; no editor swap or auxiliary log files. | [Return ZIP](dist/air-4472509-proof-return-author-pass-20261011.zip). | 26 entries; integrity and isolated 18-page build passed; SHA-256 `4ec90525…0d72b`. |
| 15 | Check the post-submission PDF and ZIP; retain the MDPI receipt. | Local PDF/ZIP and journal replies. | **John reports proof submitted; Codex will not submit anything.** |
| 16 | Release the repository with selected provenance, verify public access and reconcile availability wording. Integrate the proof into root manuscript/package through its separate gate. | PUB01 in [handoff](PROOFING-HANDOFF.md); root `main.tex` and `submission-package/`. | **Done: public and anonymously readable; default `main` integration remains separate.** |

John’s later TeX tone pass changed printed prose. The new PDF remains 18 pages, but the earlier visual approval does not cover it. The local return ZIP is ignored by Git and must be transferred separately from the pushed source/reply documents.

## Author-pass wording to check

John chose to keep his terse wording after the review proposals. These checks are for his final read of the new PDF; no change was made to these passages:

| PDF page / TeX line | Check |
| --- | --- |
| 5 / 236 | The bulk endpoint difference is described as a tool to locate an inversion top, though the registered evidence does not establish inversion depth. |
| 6 / 291 | “Without failing a pre-processing quality-control check” exceeds the recorded provider result of no returned QC flags. |
| 13 / 513 | “representsa” is a printed typo. |
| 15 / 643 | “Percentage of sign across hull” heads values 0.64–0.93, which are fractions. |
