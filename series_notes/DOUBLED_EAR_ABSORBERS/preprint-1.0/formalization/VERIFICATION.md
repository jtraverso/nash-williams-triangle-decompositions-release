# Formal proof supplement · Preprint 1.0

**Internal verification, 26 November 2026 · PASS** for the eight statements named in the note. For the subdivided claw, Lean verifies the six-edge core, its minimum and its obstruction. Section 4 of the manuscript gives the proof for every positive number of copies.

| Check | Evidence |
|---|---|
| Public source | The tag `doubled-ears-lean-v1.0` resolves to [the commit cited in Appendix A](https://github.com/jtraverso/typed-triangle-absorption/tree/c7bae66dfd66370138d2f1a6ecc51d3aa29ea8e4). Its parent is the registered Paper II source revision. |
| Complete archive | All 1,588 file paths in the ZIP match the pinned Git tree. Each uncompressed file was compared to its Git blob identifier. The archive includes 1,522 files with extension `.lean`. Lake resolves external dependencies from the included manifest. The [checksum](Doubled_ears_LEAN_SOURCE_v1.0.zip.sha256) identifies the downloadable ZIP. |
| Build | Ran `lake build +DoubledEarsChallenge +DoubledEarsSolution` on the pinned checkout with its installed dependencies. Both explicit targets compiled. The statement module has eight intentional placeholders. The solution entry point imports the proofs. |
| Axioms | Ran `lake env lean` on the [eight queries](endpoint-axioms.lean) importing only the solution. For each endpoint the [output](endpoint-axioms.txt) lists exactly `propext`, `Classical.choice` and `Quot.sound`. |
| Comparison | [Recorded run](comparator-replay.txt) of `lake comparator --inadvisably-no-sandbox --config comparator.windows.json` on Windows. The [local configuration](comparator.windows.json) differs from the pinned configuration only in disabling Nanoda. The default Lean kernel accepted the solution. Independent kernel verification and Palomar certification for this note lie outside this record. |
| Manuscript and translation | The English and Spanish manuscripts retain the previously released text through the scope paragraph in Appendix A. The following two paragraphs now link directly to the public proof sources and supplement. The bilingual regressions checked 54 aligned blocks, 228 mathematical spans, the three finite witnesses and both charge parameters. |
| Typesetting and navigation | Regenerated all four PDFs from their English or Spanish Markdown through the series template and two XeLaTeX passes. Reviewed the six pages of each manuscript and two pages of each supplement. The root README and bilingual series home page link readers to the manuscript, supplement and proof sources. |
