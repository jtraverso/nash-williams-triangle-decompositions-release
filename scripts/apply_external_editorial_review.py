"""Apply the author's pre-release editorial corrections, without changing Lean.

Copyright 2026 Juan Pablo Traverso Gianini. SPDX-License-Identifier: Apache-2.0
Run once, against the reviewed preprint 1.0 snapshot.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def replace(path, pairs):
    text = path.read_text(encoding="utf8")
    for old, new in pairs:
        assert old in text, (path.name, old)
        text = text.replace(old, new)
    path.write_bytes(text.encode())


def main():
    paper = ROOT / "preprints/PAPER_II"
    for lang in ("en", "es"):
        p = paper / f"01_manuscript/PAPER_II_preprint_v1.0_{lang}.md"
        if lang == "en":
            pairs = [
                ("Private immutable source reference supplied with this version.",
                 "The companion identifies the immutable source archive and its SHA-256 hash."),
                ("This appendix supplies the constructions used in C.5a and G.2–G.4.",
                 "This appendix supplies the auxiliary constructions used in C.5a, G.2 and G.4; the cover-down reduction is given separately in G.3."),
                ("We first recall the ordinary refiner in the form used here.",
                 "We first recall the ordinary refiner in the form used here. Throughout B.3, $n$ is the ambient order, whereas H.6 first uses the local order $N=|W|$. Its concluding rescaling gives the ambient-parameter formulation below; in particular, $M=2^h$ in (B.3.2)."),
            ]
        else:
            pairs = [
                ("Esta versión incluye la referencia inmutable de las fuentes a las fuentes.",
                 "El complemento identifica el archivo inmutable de las fuentes y su huella SHA-256."),
                ("graphs y completion", "graphs and completion"),
                ("packing y covering", "packing and covering"),
                ("graphs y hypergraphs", "graphs and hypergraphs"),
                ("Integer y fractional", "Integer and fractional"),
                ("Probability y Computing", "Probability and Computing"),
                ("Probability and Computing (2017).", "Probability and Computing 26 (2017), 911–943."),
            ]
        replace(p, pairs)
        companion = paper / f"05_formalization/FORMALIZATION_COMPANION_preprint_v1.0_{lang}.md"
        pairs = [
            ("3,028" if lang == "en" else "3.028", "3,029" if lang == "en" else "3.029"),
            ("Memory limits were raised for some large modules;" if lang == "en" else
             "Se ampliaron los límites de memoria para algunos módulos grandes;",
             "All 517 modules compiled in the final invocation used the raised memory limit;" if lang == "en" else
             "Los 517 módulos compilados en la última invocación usaron el límite de memoria ampliado;"),
            ("- **G.4**: `BlowupB/StructuralF3General/RefinerF0/RobustSlots.lean`; `exists_robust`.",
             "- **G.4/H.5, C.5a**: `TypedRefinerF0/RobustSlots.lean`; `exists_robust`.\n"
             "- **B.3/G.4/H.6**: `UniversalRefiner/Main.lean`; `exists_universal_refiner`."),
        ]
        replace(companion, pairs)
    es = paper / "01_manuscript/PAPER_II_preprint_v1.0_es.md"
    t = es.read_text(encoding="utf8")
    # Translation of the same editorial clarification; leave all displayed mathematics intact.
    old = next(l for l in t.splitlines() if l.startswith("Este apéndice") and "G.2–G.4" in l)
    first = old.split(". ", 1)[0] + "."
    t = t.replace(first, "Este apéndice proporciona las construcciones auxiliares utilizadas en C.5a, G.2 y G.4; la reducción de cobertura se presenta por separado en G.3. En las cadenas, «conector» traduce wire; «enlace» designa el grafo asociado a una etiqueta raíz.")
    t = t.replace("B.3–B.4, C.5a y G.2–G.4 |", "B.3–B.4, C.5a, G.2 y G.4 |")
    pos = t.index("### B.3.")
    end = t.index("### B.4.", pos)
    section = t[pos:end]
    start = section.index("\n\n") + 2
    section = section[:start] + (
        "En B.3, $n$ es el orden del grafo ambiente, mientras que H.6 utiliza primero el orden local $N=|W|$. "
        "El reescalado al final de H.6 da la formulación con parámetros ambientales que sigue; en particular, $M=2^h$ en (B.3.2).\n\n"
    ) + section[start:]
    t = t[:pos] + section + t[end:]
    # In the chain constructions, wire means connector; root links retain 'enlace'.
    for title, stop in (("### H.1.", "### H.2."), ("### H.6.", "### H.7.")):
        a, b = t.index(title), t.index(stop)
        section = t[a:b].replace("enlaces", "conectores").replace("enlace", "conector")
        section = section.replace("camino de conector", "camino del conector").replace("ciclo de conector", "ciclo del conector")
        t = t[:a] + section + t[b:]
    es.write_bytes(t.encode())
    en = paper / "01_manuscript/PAPER_II_preprint_v1.0_en.md"
    en.write_bytes(en.read_text(encoding="utf8").replace(
        "B.3–B.4, C.5a and G.2–G.4 |", "B.3–B.4, C.5a, G.2 and G.4 |").encode())
    summary = paper / "02_validation/REVIEW_SUMMARY.md"
    summary.write_bytes(summary.read_text(encoding="utf8").replace("3,028", "3,029").encode())
    p = ROOT / "preprints/PAPER_I/01_manuscript/PAPER_I_preprint_v1.0_es.md"
    replace(p, [(
        "Una $\\mathcal F$-descomposición utiliza solamente triángulos de esos tipos. Consideramos",
        "Una $\\mathcal F$-descomposición utiliza solamente triángulos de esos tipos. El marco general de retículos para descomposiciones con datos de etiquetas prescritos se debe a Keevash [19]. Paper II [1, Sección 2.3] distingue ese marco de las hipótesis tipadas explícitas utilizadas aquí. Consideramos"
    )])
    old_name = "PAPER_II_LEAN_20261020_ALIGNED_v4.sha256"
    new_name = "PAPER_II_LEAN_20261020_ALIGNED_v4.zip.sha256"
    (ROOT / "archives" / old_name).rename(ROOT / "archives" / new_name)
    for path in (ROOT / "archives").glob("*.sha256"):
        path.write_bytes(path.read_bytes().replace(b"\r\n", b"\n"))
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(x in path.parts for x in (".git", "_preview", "__pycache__")):
            continue
        if path.suffix not in (".md", ".json", ".html", ".py", ".yml", ".txt"):
            continue
        if path == Path(__file__):
            continue
        text = path.read_text(encoding="utf8")
        updated = text.replace(old_name, new_name)
        if updated != text:
            path.write_bytes(updated.encode())


if __name__ == "__main__":
    main()
