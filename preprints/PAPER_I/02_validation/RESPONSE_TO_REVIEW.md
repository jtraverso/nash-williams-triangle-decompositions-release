# Response to the review of Paper I

Preprint 1.0, 20 October 2026. Review baseline: `9248386699b10dbc9aae9a32f9d9862c73c71ec2`.

The following corrections concern exposition, attribution, publication metadata and the description of formal evidence. The displayed mathematical formulas, code blocks, theorem statements and selected frozen Lean archive are preserved.

| Item | Resolution |
|---|---|
| B1 | The manuscript, companion and navigation use the series repository, immutable archive links and DOI 10.5281/zenodo.23428173. Documents carry CC BY 4.0; the source archive retains Apache-2.0 and dependency notices. Actual release is an operational step, separate from this document audit. |
| B2 | README, CHANGELOG and BibTeX were rewritten as UTF-8 and scanned with all current documents for corrupted characters. |
| B3 | Added Nash-Williams (1970), Barber–Kühn–Lo–Osthus (2016), Delcourt–Postle refined absorption and Keevash Designs II. Sections 1, 3.2 and 4 distinguish inherited frameworks from the protected reserve and explicit bounded certificates. |
| N1 | The companion states that the excluded historical name is absent and that its exclusion alone is vacuous. The dependency audit also checks actual required and forbidden dependencies. The canonical assembly is identified explicitly. |
| N2 | The companion distinguishes historical source commentary from mathematical conclusions and points to Paper II Section 7.1. The frozen source is unchanged; comment corrections in the separately ported Palomar tree are recorded in that tree. |
| N3 | Appendix A gives the quantitative implication from closeness to extremality, with the choices of gamma and the order threshold written out. This explains an implication already implemented in the proof. |
| N4 | The application explicitly requires b/2 at most sigma_0. |
| N5 | Both uses of the extremality definition cite Delcourt–Postle Definition 12.2. |
| N6 | Optional tightening of valid constants was not adopted; the existing mathematical constants are preserved. |
| N7 | Updated DOI links and the complete reference for the unpublished manuscript; cited the published Hales and Edmonds–Koutsoukou-Argyraki–Paulson articles and arXiv v3 where applicable. |
| N8 | Fixed Windows paths in historical scripts remain documented. These scripts are not represented as platform-independent reproduction commands. |
| N9 | Added the full namespace NashWilliams18.IsExtremal and retained the documented sigma_0 convention. |

## Evidence

The audit checks the source-to-TeX-to-PDF hashes, three successful typesetting passes, bilingual mathematics and identifiers, references, UTF-8, local links, previous-artifact preservation, and the selected archive's internal hashes. The visual review covers every rendered page and enlarged inspection of changed passages. No new Lean build is used as evidence for this editorial revision.

The selected archive is `PAPER_I_LEAN_20261020_ALIGNED_v3.zip`, SHA-256 `bfa42bd57e6d9c2ac918bbf6fe2c2ba7c01894d1d8387d92e81b090020a6aaff`.
