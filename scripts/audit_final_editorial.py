"""Check the authorized final typographical corrections without Lean or network.

Copyright 2026 Juan Pablo Traverso Gianini. SPDX-License-Identifier: Apache-2.0
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import pymupdf

ROOT = Path(__file__).resolve().parents[1]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def appendix_normalized(text, language):
    title = "Appendix" if language == "en" else "Apéndice"
    text = text[text.index("## " + title + " F."):text.index("## " + title + " G.")]
    substitutions = [
        (r"\subseteq", " subset " if language == "en" else " subconjunto de "),
        (r"\in ", " in " if language == "en" else " en "),
        (r"\cup", " union " if language == "en" else " unión "),
        (r"\ell", "ell"), (r"\mapsto", "->"),
        (r"\operatorname{tail}", "tail"), (r"\operatorname{head}", "head"),
        (r"\mathbb E", "E"), (r"\{", "{"), (r"\}", "}"),
    ]
    for before, after in substitutions:
        text = text.replace(before, after)
    return re.sub(r"\s|\$", "", text)


def main():
    approved = json.loads((ROOT / "publication/FINAL_EDITORIAL_OPERATIONS.json").read_text(encoding="utf8"))
    rows = []
    for record in approved["documents"]:
        path = ROOT / record["path"]
        before = subprocess.check_output(
            ["git", "show", approved["baseline_commit"] + ":" + record["path"]], cwd=ROOT
        ).decode("utf8")
        assert digest(before.encode()) == record["before_sha256"]
        expected = before
        for operation in record["operations"]:
            a, b = operation["before"], operation["after"]
            if operation.get("regex"):
                expected, count = re.subn(a, lambda _: b, expected)
                assert count == operation["count"]
            else:
                assert expected.count(a) == operation["count"]
                expected = expected.replace(a, b)
        current = path.read_text(encoding="utf8")
        assert expected == current, record["path"]
        assert digest(current.encode()) == record["after_sha256"]
        language = path.stem[-2:]
        is_paper_ii = path.name.startswith("PAPER_II_")
        if is_paper_ii:
            assert appendix_normalized(before, language) == appendix_normalized(current, language)
        assert not re.search(r"\$e\$dge|\$e\$very", current)
        with pymupdf.open(path.with_suffix(".pdf")) as pdf:
            uris = {link.get("uri", "") for page in pdf for link in page.get_links()}
            dois = set(re.findall(r"<(https://doi\.org/[^>]+)>", current))
            assert dois and dois <= uris, (record["path"], dois - uris)
            assert "CC BY 4.0" in pdf[0].get_text(), record["path"]
            text = "\n".join(page.get_text() for page in pdf)
            assert "(19+C_d A_0)m" not in text
            if is_paper_ii and language == "es":
                for unwanted in ("seis apéndices", "for every", "pending", "Teorema D.La"):
                    assert unwanted not in text, unwanted
                section = "7. Alcance y obstrucciones"
                pages = [page for page in pdf if section in page.get_text()]
                assert len(pages) == 1
                following = pages[0].get_text().split(section, 1)[1].strip()
                assert len(following.split()) > 10, "Section 7 heading remains orphaned"
            rows.append(dict(path=record["path"], md_sha256=digest(path.read_bytes()),
                             pdf_sha256=digest(path.with_suffix(".pdf").read_bytes()),
                             pages=len(pdf), active_dois=sorted(dois),
                             appendix_F_typography_only=is_paper_ii))
    output = dict(status="PASS_FINAL_EDITORIAL_CHECKS",
                  baseline_commit=approved["baseline_commit"], documents=rows,
                  changes="Exact approved transformations replayed; Appendix F invariant after notation normalization.",
                  lean_build_executed=False, publication_performed=False)
    (ROOT / "publication/FINAL_EDITORIAL_CHECKS.json").write_bytes(
        (json.dumps(output, ensure_ascii=False, indent=2) + "\n").encode())
    print("PASS: eight documents; active DOI links, licences, Spanish corrections and typography-only Appendix F")


if __name__ == "__main__":
    main()
