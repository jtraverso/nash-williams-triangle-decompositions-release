# Response to the final editorial review

20 October 2026. Both papers retain preprint version 1.0.

This response concerns the review of `cb1ee86`. Its identical-tree replacement after the author/committer identity correction is `230fb9a427f010f90bf2afe103a465d55be9097a`.

| Observation | Resolution | Evidence |
|---|---|---|
| Paper II Spanish references [11], [16], [17], [19] translated words inside English titles | Restored the original English titles. | Bilingual title comparison in `scripts/audit_editorial_review.py`; rendered references. |
| Spanish journal names [12], [20]; missing Montgomery volume/pages | Restored *Combinatorics, Probability and Computing* and `26 (2017), 911–943`. | `publication/MONTGOMERY_REFERENCE_CHECK.json` and rendered bibliography. |
| Paper II reference [8] retained private wording and damaged Spanish | Both languages now identify the immutable source archive and its SHA-256 through the companion. | Current Markdown, TeX and PDF. |
| Paper I Spanish §3.2 omitted attribution | Restored the attribution to Keevash [19] and the comparison in Paper II [1, §2.3]. | Spanish article, page 5. |
| Checksum sidecars used CRLF and inconsistent names | Both are named `*.zip.sha256` and use LF. The verifier enforces names, line endings and hashes; `.gitattributes` preserves LF. | GNU `sha256sum -c` passes for both archives. |
| Memory limit described as applying to some modules | Both companions now state that all 517 modules compiled in the final invocation used the raised limit. | Verified against frozen `evidence/verification.json`. |
| Evidence file count | Corrected to 3,029. | Counted directly inside the unchanged archive. |
| Auxiliary source mapping | Replaced the cited copy of `exists_robust` with `TypedRefinerF0/RobustSlots.lean`; added `UniversalRefiner/Main.lean: exists_universal_refiner`. | Both declarations checked inside the frozen source archive. |
| Appendix H heading overclaimed G.3 | The introduction and correspondence table now identify C.5a, G.2 and G.4; G.3 remains a separate cover-down reduction. | Both manuscript languages. |
| Ambient/local orders | B.3 now explains ambient `n`, local `N = |W|`, the rescaling in H.6 and `M = 2^h`. Existing formulas are unchanged. | Semantic comparison and page renders. |
| Spanish wire/link ambiguity | Chains use “conector”; “enlace” denotes the root-label link graph. The convention is explicit in H. | Spanish Appendix H. |
| Repository presentation | Description and web instructions present both papers and their companions as available. The obsolete “awaiting Paper II” description is removed. | Repository metadata and `WEB_PUBLICATION.md`. |
| Git identity | Author and committer use Juan Pablo Traverso Gianini and the GitHub `jtraverso` noreply address. The five preparation commits were reconstructed with identical trees; current immutable links use the replacement commits. | `publication/GIT_IDENTITY_REVIEW.json`. |
| First public edition | Removed the obsolete sentence about a `superseded` archive from both Paper II companions. All articles and companions identify themselves as preprint 1.0. No previous manuscript edition is packaged; technical source-archive revision identifiers remain unchanged. | `publication/DOCUMENT_VERSION_CHECKS.json`; static editorial audit and regenerated companions. |

## Audit and scope

The internal audit compares all original displayed formulas and inline mathematical content with the reviewed snapshot. It verifies the eight Markdown/TeX/PDF artifact bindings, bibliography corrections, checksum sidecars, frozen evidence counts and auxiliary declaration locations. All pages were inspected on contact sheets; changed and dense pages were also inspected at readable resolution. The visual reports identify the exact PDF hashes and retained images.

Both source ZIPs remain byte-identical. No Lean sources, statements, proofs or build evidence were modified, and this editorial audit did not run Lean or Lake. The separate Palomar build is not substituted for the evidence cited by these documents.

Repository visibility remains private and no Zenodo deposit or production site was published. The public-facing document wording is prepared for release; actual publication remains a separate authorized operation.

Rewriting reachable Git history does not certify removal of old objects from GitHub caches. The identity report concerns the current branch history.

## Reproduction

Run `python -I scripts/audit_editorial_review.py` for the static editorial comparison and `python -I scripts/verify_repository.py` for the sealed package. The visual inspection record is in each paper's `02_validation/VISUAL_REVIEW.json`; this is an internal editorial audit, not a new external mathematical review.

The canonical repository is now `jtraverso/nash-williams-triangle-decompositions-release`, created privately with the corrected GitHub no-reply history. The previous repository was left intact at the author’s request. Manuscript links were updated and all eight PDFs regenerated; the DOI reservations and frozen Lean archive hashes remain unchanged.
