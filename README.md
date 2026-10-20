# Triangle decompositions — Nash–Williams and typed absorption

**Juan Pablo Traverso Gianini · Preprint 1.0 · First public edition in preparation**

This series connects a formal proof of the Nash–Williams triangle-decomposition
theorem with the typed absorption results supplying its decomposition inputs.
The mathematical manuscripts and the formalization companions are separate
documents, each in English and Spanish.

La serie conecta una prueba formal del teorema de descomposición en triángulos
de Nash–Williams con los resultados de absorción por tipos que proporcionan
sus entradas de descomposición. Cada artículo tiene un complemento de
formalización independiente, en inglés y español.

**Private release preparation.** Paper I's selected documents and freeze are
staged here. Paper II's final package is pending. No public release, website
deployment or Zenodo deposit has been made from this repository.

**Preparación privada.** Paper I está incorporado con su freeze seleccionado.
La entrega final de Paper II está pendiente. La publicación será conjunta.

## The mathematical route / Recorrido matemático

| Work | Role | Package |
|---|---|---|
| I — Formalizing the Nash–Williams theorem in Lean | Follows Delcourt–Postle's case division and supplies the replacement constructions and interfaces described in the manuscript. | [Documents and frozen sources](preprints/PAPER_I/README.md) |
| II — Robust absorption for typed triangles | Develops decomposition inputs for prescribed triangle types, including the semidense case and finite family constructions. | [Final delivery pending](preprints/PAPER_II/README.md) |

The contribution and attribution of each result are stated in the manuscripts.
Paper I's clean-build record covers its selected dependency closure; it does
not certify a complete clean build of the separate Paper II development.

El registro de compilación de Paper I cubre su cierre de dependencias
seleccionado; no certifica una compilación limpia de todo Paper II.

## Read / Leer

- [Bilingual website](index.html) and [paper index](preprints/README.md).
- [Publication index](PUBLICATION_INDEX.json): version, status and selected artifacts.
- [Citation guide](CITATION.md): metadata without a fabricated DOI or publication date.
- [Licences](LICENSE.md): software and documents have distinct scopes.

## Reproducibility and integrity / Reproducibilidad e integridad

Each paper follows the structure used by the Erdős-series Paper IV:

| Directory | Contents |
|---|---|
| `01_manuscript` | Mathematical article, EN/ES, Markdown, TeX and PDF |
| `02_validation` | Audit scope, reports and validation evidence |
| `03_reproducibility` | Instructions and scripts |
| `04_integrity` | Hashes and selected artifact bindings |
| `05_formalization` | Separate formalization companion and source-freeze guide |

[Repository checks](publication/AUDIT.md) verify the staged files, archive
manifest, links and release hold. They do not rerun Lean or substitute for
the recorded mathematical, bibliographic or kernel checks.

## Release preparation / Preparación del lanzamiento

- [Release checklist](publication/RELEASE_CHECKLIST.md).
- [Cloudflare Pages setup](WEB_PUBLICATION.md). The build is held until the
  release conditions are satisfied; no Cloudflare project is connected.
- [Zenodo plan](publication/zenodo/README.md): individual final PDFs, not a
  repository-sized archive.
- [Selected-file provenance](publication/INTAKE.json).

This repository will carry the first public edition only. Earlier manuscripts,
source freezes and review backups stay in the private research repository;
they are not copied into a `superseded` directory here.
