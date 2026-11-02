"""Audit the external-review corrections against the previous mathematical text.

Copyright 2026 Juan Pablo Traverso Gianini. SPDX-License-Identifier: Apache-2.0
No Lean, Lake, network or publication commands are run.
"""
from pathlib import Path
import argparse
import difflib
import hashlib
import json
import re
import subprocess
import zipfile
import pymupdf
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "230fb9a427f010f90bf2afe103a465d55be9097a"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode())


def displays(text):
    # Two author-approved translations inside Spanish displays; symbols unchanged.
    text = text.replace(r"\hbox{para todo }v.", r"\hbox{for every }v.")
    text = text.replace(r"y\ \mathrm{pendiente}", r"y\ \mathrm{pending}")
    return re.findall(r"\$\$(.*?)\$\$", text, re.S)


def inline(text):
    return re.findall(r"(?<!\\)\$([^$\n]+)(?<!\\)\$", re.sub(r"\$\$.*?\$\$", "", text, flags=re.S))


def audit(render):
    results = []
    for number in ("I", "II"):
        folder = ROOT / "preprints" / f"PAPER_{number}"
        qa = folder / "02_validation"
        builds = {row["source"]: row for row in json.loads((qa / "typeset/artifact_build.json").read_text())}
        rows, changes, rendered = [], [], []
        for md in sorted(folder.glob("*/*preprint_v1.0_*.md")):
            rel = md.relative_to(ROOT).as_posix()
            old = subprocess.check_output(["git", "show", f"{BASELINE}:{rel}"], cwd=ROOT).decode()
            text = md.read_text(encoding="utf8")
            assert displays(old) == displays(text), ("changed display mathematics", rel)
            matcher = difflib.SequenceMatcher(a=inline(old), b=inline(text), autojunk=False)
            edits = [op for op in matcher.get_opcodes() if op[0] != "equal"]
            assert all(op[0] == "insert" for op in edits), ("removed or replaced inline mathematics", rel, edits)
            assert not edits or (number == "II" and "01_manuscript" in rel)
            assert not re.search(r"Private immutable source reference|de las fuentes a las fuentes|Probability y Computing", text)
            assert "superseded" not in text.lower(), rel
            assert not re.search(r"(?i)\bpreprint\s+(?!1\.0\b)\d", text), rel
            record = builds[rel]
            pdf = md.with_suffix(".pdf")
            assert record["markdown_sha256"] == sha(md)
            assert record["tex_sha256"] == sha(md.with_suffix(".tex"))
            assert record["pdf_sha256"] == sha(pdf)
            assert record["layout_issues"] == [], record
            with pymupdf.open(pdf) as doc:
                extracted = "\n".join(p.get_text() for p in doc)
                assert "\ufffd" not in extracted
                assert "Private immutable source reference" not in extracted
                assert "superseded" not in extracted.lower(), rel
                row = dict(source=rel, markdown_sha256=sha(md), pdf_sha256=sha(pdf),
                           display_count=len(displays(text)), pages=len(doc))
                rows.append(row)
                if render:
                    output = qa / "renders" / pdf.stem
                    output.mkdir(parents=True, exist_ok=True)
                    sheets = []
                    for start in range(0, len(doc), 9):
                        sheet = Image.new("RGB", (1800, 2500), "#dddddd")
                        draw = ImageDraw.Draw(sheet)
                        for j in range(start, min(start + 9, len(doc))):
                            pix = doc[j].get_pixmap(matrix=pymupdf.Matrix(1.0, 1.0), alpha=False)
                            im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
                            im.thumbnail((582, 795))
                            col, line = (j-start) % 3, (j-start) // 3
                            sheet.paste(im, (col*600 + (600-im.width)//2, line*833+26))
                            draw.text((col*600+10, line*833+7), f"{number} {pdf.stem[-2:]} p.{j+1}", fill="black")
                        dest = output / f"contact-{start+1:03}.jpg"
                        sheet.save(dest, quality=90)
                        sheets.append(dict(path=dest.relative_to(ROOT).as_posix(), sha256=sha(dest)))
                    rendered.append(dict(pdf=pdf.relative_to(ROOT).as_posix(),
                                         sha256=sha(pdf), pages=len(doc), contact_sheets=sheets))
            changes.append(dict(source=rel, baseline_sha256=hashlib.sha256(old.encode()).hexdigest(),
                                current_sha256=sha(md), display_mathematics_unchanged=True,
                                translation_normalization="Spanish prose in A.6.1 and E.4.1 only",
                                inline_insertions=[inline(text)[op[3]:op[4]] for op in edits],
                                scope="Bibliography, attribution, resource-evidence description, source locators and terminology; existing equations and proof steps retained."))
        for part in ("01_manuscript", "05_formalization"):
            en = next((folder / part).glob("*_en.md")).read_text(encoding="utf8")
            es = next((folder / part).glob("*_es.md")).read_text(encoding="utf8")
            # Translated \text prose was already present in the reviewed baseline;
            # the per-language comparison above requires every display byte unchanged.
            def mathematical_tokens(t):
                return [re.sub(r"\s+", "", re.sub(r"\\text\{[^}]*\}", "", d))
                        for d in displays(t)]
            assert mathematical_tokens(en) == mathematical_tokens(es), (number, part, "display parity")
            doi = lambda t: set(re.findall(r"10\.\d{4,9}/[A-Za-z0-9._/()\-]+", t))
            assert doi(en) == doi(es), (number, part, "DOI parity")
        save(qa / "SEMANTIC_CHANGE_REPORT.json", dict(status="PASS", baseline_commit=BASELINE,
             documents=changes, lean_sources_changed=False, lean_build_executed=False))
        save(qa / "AUDIT_RESULT.json", dict(status="PASS_LOCAL_DOCUMENT_CHECKS",
             documents=rows, total_pages=sum(r["pages"] for r in rows),
             scope="External editorial review corrections; protected-math comparison, bilingual displays and DOI parity, three-pass compilation and log checks. Visual review is recorded separately."))
        if render:
            save(qa / "RENDER_INDEX.json", rendered)
        results += rows
    # Original English titles and journal names must survive Spanish translation.
    folder = ROOT / "preprints/PAPER_II/01_manuscript"
    en, es = [(folder / f"PAPER_II_preprint_v1.0_{lang}.md").read_text(encoding="utf8") for lang in ("en", "es")]
    for number in (11, 12, 16, 17, 19, 20):
        lines = [re.search(rf"^\[{number}\] (.*)$", t, re.M)[1] for t in (en, es)]
        titles = [re.search(r"\*(.*?)\*", t)[1] for t in lines]
        assert titles[0] == titles[1], (number, titles)
    assert "Computing 26 (2017), 911–943." in es
    for path in (ROOT / "archives").glob("*.sha256"):
        raw = path.read_bytes()
        assert b"\r" not in raw
        checksum, name = raw.decode().strip().split("  ", 1)
        assert path.name == name + ".sha256" and sha(path.parent / name) == checksum
    for path in (ROOT / "archives").glob("*.zip"):
        old = subprocess.check_output(["git", "rev-parse", f"{BASELINE}:archives/{path.name}"], cwd=ROOT).decode().strip()
        now = subprocess.check_output(["git", "hash-object", str(path)], cwd=ROOT).decode().strip()
        assert old == now, path.name
    with zipfile.ZipFile(ROOT / "archives/PAPER_II_LEAN_20261020_ALIGNED_v4.zip") as z:
        prefix = "PAPER_II_LEAN_20261020_ALIGNED_v4/"
        evidence_count = sum(n.startswith(prefix + "evidence/") and not n.endswith("/") for n in z.namelist())
        assert evidence_count == 3029
        verification = json.loads(z.read(prefix + "evidence/verification.json"))
        assert len(verification["modules_with_raised_memory_threshold"]) == 517
        for path, decl in (("TypedRefinerF0/RobustSlots.lean", "theorem exists_robust"),
                           ("UniversalRefiner/Main.lean", "theorem exists_universal_refiner")):
            assert decl in z.read(prefix + "source/PartitionedTriangleAbsorption/" + path).decode()
    save(ROOT / "publication/EXTERNAL_REVIEW_CHECKS.json", dict(
        status="PASS_STATIC_EDITORIAL_CHECKS", baseline_commit=BASELINE,
        documents=results, evidence_files=evidence_count,
        final_invocation_raised_memory_modules=517, original_archives_byte_identical=True,
        sha256_sidecars="LF; uniform .zip.sha256; verified hashes",
        bibliographic_titles_and_montgomery_details="PASS",
        lean_build_executed=False, publication_performed=False))
    print("PASS_STATIC_EDITORIAL_CHECKS", len(results), "documents")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--render", action="store_true")
    audit(parser.parse_args().render)
