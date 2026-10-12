# Final proof-return review route — 11 October 2026

Current branch: `jrl/proofs-round1`; proof correction commit `c521764`. Fifty current-proof rows in the [reply table](PROOFER-REPLY-TABLE.md) are checked; PUB01 is a post-submission task. John has approved the visual layout and all 23 [journal-facing replies](PROOFER-RETURN-REPLIES.md). Final approval of the assembled return and journal submission remain open.

Use the [working PDF](proof-package/working/air-4472509-done.pdf) for printed appearance, the [working TeX](proof-package/working/air-4472509-done.tex) for source comments, the [reply table](PROOFER-REPLY-TABLE.md) for exact old/new TeX and PDF locators, and the [catalogue](notes/proof-query-catalogue.md) only when an exact publisher quotation or evidence detail is needed. The [received proof](proof-package/air-4472509-english/air-4472509-done.tex) is immutable.

| # | Microtask | Look at | Status / decision |
| ---: | --- | --- | --- |
| 1 | Confirm the review version and original preservation. | [Handoff](PROOFING-HANDOFF.md), [working TeX](proof-package/working/air-4472509-done.tex), received source; correction commit `c521764`. | Source hash `1a9b07be…ce74c3`; received 33-file bundle unchanged. |
| 2 | Check title, author order, affiliations, four ORCIDs and emails. | PDF p. 1; reply-table EE01, MDPI01–02. | Author-confirmed; review the printed first page. |
| 3 | Check the italic research-question emphasis. | PDF p. 2; MDPI03. | Author requested retention. |
| 4 | Check the observation-provider/instrument limitation and WRF/WPS/terrain versions and sources. | PDF pp. 3–6; MDPI04a/b, JRL01, JRL03; approved MDPI04 reply. | Scoped wording approved; verify no blanket absence claim. |
| 5 | Check software versions/citations and AI-use disclosure. | PDF pp. 5–6, 16; MDPI18, JRL02; Methods and back matter in working TeX. | Author-confirmed model names/CLI use; no per-session snapshot claim. |
| 6 | Check first-citation order and placement: Figures 1–9; Tables 1, A1–A6; Section 3.4 above Figure 4; production-size notice. | PDF pp. 3–15; MDPI05a/b, MDPI07, MDPI08c, JRL08. | Source/auxiliary checks passed; John approved final flow and layout. |
| 7 | Check Figures 1–3 for overlap, Figure 2 marker key and NASA institution wording. | PDF pp. 3–4, 7; MDPI06, MDPI08a/b, MDPI11, JRL04. | Earlier author visual approval recorded. |
| 8 | Check Figures 4–9: panel descriptions, interquartile/night/sensitivity shading, dashed features and resized label legibility. | PDF pp. 8–12; MDPI12–16, JRL05a–e. | John confirmed final readability on 11 October. |
| 9 | Check equation typography and appendix-table citation format. | PDF pp. 5–8; MDPI09–10. | Source changes and author format decision recorded. |
| 10 | Check Table 1 and A1–A6: width, rows, labels, rounded A1 coordinates and retained A5 rules. | PDF pp. 5, 13–15; MDPI17, JRL06a–c, JRL07. | A1 approved earlier; remaining tables approved 11 October. |
| 11 | Check Data Availability, Acknowledgements, Conflicts of Interest and AI statement; confirm no manuscript footnotes or retired-supplement references. | PDF p. 16; JRL09–10, PUB01. | Current wording says repository release follows proof submission. |
| 12 | Check conference dates/locations, NCAR/USGS publisher locations, Herbie DOI and McKinney highlight. | PDF pp. 17–18; MDPI19–22, HL01; 49 embedded bibliography entries. | Source identities and author decisions recorded. |
| 13 | Read the 23 copy-ready replies; use the catalogue for any exact quotation. | [Journal replies](PROOFER-RETURN-REPLIES.md) and [51-row table](PROOFER-REPLY-TABLE.md). | All wording approved 11 October; final assembled-return approval pending. |
| 14 | Inspect the actual upload ZIP: corrected TeX/PDF, template files and eleven figures; no editor swap or auxiliary log files. | [Return ZIP](dist/air-4472509-proof-return-20261011.zip). | 26 entries; integrity and isolated 18-page build passed; SHA-256 `0473c9da…bdded`. |
| 15 | Give final approval, upload the ZIP and replies through MDPI, then retain the submission receipt. | ZIP plus journal replies; MDPI portal. | **Open; nothing submitted by Codex.** |
| 16 | After confirmed proof submission, select/prepare public provenance, release the repository, verify public access and reconcile availability wording. Integrate the proof into root manuscript/package through its separate gate. | PUB01 in [handoff](PROOFING-HANDOFF.md); root `main.tex` and `submission-package/`. | **Later; do not release before submission.** |

The TeX changes on 11 October affect `% JRL:` comments only. The final PDF remains 18 pages with extracted text identical to the prior version. The local return ZIP is ignored by Git and must be transferred separately from the pushed source/reply documents.
