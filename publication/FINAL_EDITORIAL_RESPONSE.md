# Final editorial response — preprint 1.0

Baseline: `2e9b44e159b832a9f9bff2b874b7e3a18081c531`. Scope: editorial presentation only; no Lean/Lake build, no change to the frozen archives, no Zenodo publication.

| Observation | Correction | Evidence |
|---|---|---|
| Literal `(19+C_d A_0)m` | Math mode in Paper II EN and ES | Exact source operations and PDF text check |
| Six appendices | Eight appendices (A–H) in Paper II ES | Source and PDF check |
| English text in A.6.1 and E.4.1 | Spanish prose only; mathematical symbols retained | Normalized display comparison |
| Appendix F plain-text mathematics | Typeset variables, relations, maps and bounds in both languages | Identical text after the explicit notation-normalization check |
| Orphaned section 7 heading | Reserve nine text lines before that section | Page-content assertion and visual review |
| Licence placement | Existing CC BY 4.0 notice moved to the first page of both Paper II documents | Eight first-page licence checks |
| Missing space after Theorem D | Corrected in Spanish | Source and PDF check |
| Inactive DOI references | Explicit Markdown autolinks, compiled into PDF link annotations | Every cited DOI URL checked against final PDF annotations |
| Cloudflare project name | Aligned with the replacement repository name | `wrangler.jsonc`; no deployment |

The transformation ledger is `FINAL_EDITORIAL_OPERATIONS.json`. `scripts/audit_final_editorial.py` replays it against the baseline, checks exact source hashes and verifies the resulting PDF properties. `scripts/audit_editorial_review.py` additionally compares protected expressions against the earlier mathematical baseline, verifies bilingual display and DOI parity, inspects typesetting logs, and checks both frozen archives byte for byte. Rendered-page review is recorded separately in each paper's `02_validation/VISUAL_REVIEW.json`.
