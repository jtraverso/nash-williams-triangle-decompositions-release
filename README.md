# Triangle decompositions — Nash–Williams and typed absorption

**Juan Pablo Traverso Gianini · Preprint 1.0 · 20 October 2026**

This series connects a formal proof of the Nash–Williams triangle-decomposition theorem with the typed absorption results supplying its decomposition inputs. The mathematical articles present the arguments; their separate companions describe the frozen sources, checked declarations and reproducibility evidence.

La serie conecta una prueba formal del teorema de Nash–Williams con los resultados de absorción por tipos utilizados en sus casos extremales. Los artículos y sus complementos de formalización están disponibles en inglés y español.

| Paper | Mathematical role | Documents and DOI |
|---|---|---|
| I — Formalizing the Nash–Williams theorem in Lean | Delcourt–Postle's case division, explicit replacement constructions and the formal theorem. | [Article and companion](preprints/PAPER_I/README.md) · [10.5281/zenodo.23428173](https://doi.org/10.5281/zenodo.23428173) |
| II — Robust absorption for typed triangles | Typed decomposition inputs, the semidense case, finite family constructions and terminal absorption. | [Article and companion](preprints/PAPER_II/README.md) · [10.5281/zenodo.23502224](https://doi.org/10.5281/zenodo.23502224) |

## Palomar registry / Registro Palomar

The Lean formalizations of both papers have been submitted to [Palomar](https://palomar-registry.org), a registry of Lean-verified results that rebuilds the sources, checks the stated theorems against a Mathlib-only challenge file and replays the proofs in independent kernels.

| Paper | Palomar | Lean source |
|---|---|---|
| I — Nash–Williams | **Registered** as [PALOMAR-2026-10-21-000009](https://palomar-registry.org/entry.html?id=PALOMAR-2026-10-21-000009&version=1) (version 1, 21 October 2026) · [archived copy](https://github.com/PalomarArchive/jtraverso--nash-williams-lean--252fc7828395/tree/palomar/PALOMAR-2026-10-21-000009-v1/2603197abdbf0a600ec663f6f046f70fbd209d4a) | [jtraverso/nash-williams-lean @ 2603197](https://github.com/jtraverso/nash-williams-lean/tree/2603197abdbf0a600ec663f6f046f70fbd209d4a) |
| II — Typed absorption | **Submitted** on 23 October 2026; mechanical verification and editorial review in progress | [jtraverso/typed-triangle-absorption @ 673c6d4](https://github.com/jtraverso/typed-triangle-absorption/tree/673c6d4) (version 1.1) |

Paper II version 1.1 rewrites proof scripts in 279 modules of the computer-assisted finite census to shorten the build. Statements, definitions and the challenge file are unchanged, and the mechanical preflight passed. An earlier submission of the 1.0 sources exceeded the verifier's time limit.

*En español:* las formalizaciones en Lean de ambos artículos se enviaron a [Palomar](https://palomar-registry.org), un registro de resultados verificados en Lean. Palomar recompila las fuentes, compara los teoremas enunciados con un archivo de desafío que solo usa Mathlib y repite las pruebas en núcleos independientes. El Artículo I está **registrado** (PALOMAR-2026-10-21-000009). El Artículo II se **envió** el 23 de octubre de 2026 y su verificación y revisión editorial están en curso. La versión 1.1 del Artículo II reescribe las pruebas de 279 módulos del censo finito asistido por computadora para acortar la compilación, sin cambiar enunciados, definiciones ni el archivo de desafío. El preflight mecánico pasó. Un envío anterior de las fuentes 1.0 superó el límite de tiempo del verificador.

## PDF downloads / Descargar PDF

| Document | English | Español |
|---|---|---|
| **Paper I — Nash–Williams** | [Paper I PDF (EN)](preprints/PAPER_I/01_manuscript/PAPER_I_preprint_v1.0_en.pdf) | [Paper I PDF (ES)](preprints/PAPER_I/01_manuscript/PAPER_I_preprint_v1.0_es.pdf) |
| **Paper II — Typed absorption** | [Paper II PDF (EN)](preprints/PAPER_II/01_manuscript/PAPER_II_preprint_v1.0_en.pdf) | [Paper II PDF (ES)](preprints/PAPER_II/01_manuscript/PAPER_II_preprint_v1.0_es.pdf) |
| Paper I formalization companion | [Companion I PDF (EN)](preprints/PAPER_I/05_formalization/FORMALIZATION_COMPANION_preprint_v1.0_en.pdf) | [Companion I PDF (ES)](preprints/PAPER_I/05_formalization/FORMALIZATION_COMPANION_preprint_v1.0_es.pdf) |
| Paper II formalization companion | [Companion II PDF (EN)](preprints/PAPER_II/05_formalization/FORMALIZATION_COMPANION_preprint_v1.0_en.pdf) | [Companion II PDF (ES)](preprints/PAPER_II/05_formalization/FORMALIZATION_COMPANION_preprint_v1.0_es.pdf) |

## Read and cite / Leer y citar

- [Bilingual website](index.html) and [paper index](preprints/README.md).
- [Citation guide](CITATION.md) and [publication index](PUBLICATION_INDEX.json).
- [aiXiv records / Registros en aiXiv](publication/aixiv/README.md).
- [Selected source archives](archives/README.md), with licences, hashes and original build evidence.

## Reproducibility / Reproducibilidad

| Directory in each paper | Contents |
|---|---|
| `01_manuscript` | Mathematical article, EN/ES, PDF, TeX and Markdown |
| `02_validation` | Review responses and validation evidence |
| `03_reproducibility` | Reproduction instructions and source-scope notes |
| `04_integrity` | File hashes |
| `05_formalization` | Separate formalization companion, EN/ES |

Each companion identifies its own checked dependency closure and distinguishes historical compilation, source-preserving packaging revisions and final axiom queries. Neither paper's build is used as evidence for the whole other development.

Cada complemento distingue su clausura comprobada, los registros de compilación, las revisiones de empaquetado y las consultas de axiomas. Los registros no se presentan como reproducción independiente.

Manuscripts and companions use **CC BY 4.0**. Original source and packaging materials use **Apache-2.0**, with third-party notices preserved; see [licences](LICENSE.md).

[Repository audit](publication/AUDIT.md) · [Website configuration](WEB_PUBLICATION.md) · [Publication operations](publication/RELEASE_CHECKLIST.md).

## arXiv endorsement

I am preparing to submit this preprint series to arXiv (math.CO) and, as a first-time submitter, I
need an endorsement. If you are an arXiv author eligible to endorse in math.CO, have looked at
these papers, and found that they add value and are appropriate for the category, you can endorse
me at https://arxiv.org/auth/endorse?x=N8V4R6 (endorsement code `N8V4R6`). An endorsement only confirms that the work is suitable for
the subject area; it is not a review or an approval of its results. Thank you.

*En español:* preparo el envío de esta serie de preprints a arXiv (math.CO) y, como es mi primer
envío, necesito un endorsement. Si eres autor de arXiv habilitado para dar endorsement en math.CO,
revisaste estos trabajos y te parece que aportan y son adecuados para la categoría, puedes dármelo
en https://arxiv.org/auth/endorse?x=N8V4R6 (código `N8V4R6`). El endorsement solo confirma que el trabajo es adecuado para el área;
no es una revisión ni una aprobación de sus resultados. ¡Gracias!
