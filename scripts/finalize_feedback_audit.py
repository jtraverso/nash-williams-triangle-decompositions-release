"""Seal and check the audited document intake without publishing.

Copyright 2026 Juan Pablo Traverso Gianini. SPDX-License-Identifier: Apache-2.0
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def save(path, value):
    path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf8"))


def run(*args):
    result = subprocess.run([sys.executable, *args], cwd=ROOT, text=True,
                            capture_output=True, encoding="utf8")
    return dict(command=["python", *args], exit_code=result.returncode,
                stdout=result.stdout, stderr=result.stderr)


def main():
    # Compiler auxiliaries are generated intermediates, not release artifacts.
    for path in (ROOT / "preprints").rglob("*.aux"):
        assert path.resolve().is_relative_to(ROOT / "preprints")
        path.unlink()
    for name in ("INTAKE.json", "SITE_FILES.json"):
        path = ROOT / "publication" / name
        data = json.loads(path.read_text(encoding="utf8"))
        data["files"] = [row for row in data["files"]
                         if not (row if isinstance(row, str) else row["path"]).endswith(".aux")]
        save(path, data)
    for folder in (ROOT / "preprints").glob("PAPER_*"):
        rows = [dict(path=p.relative_to(ROOT).as_posix(), bytes=p.stat().st_size,
                     sha256=hashlib.sha256(p.read_bytes()).hexdigest())
                for p in sorted(folder.rglob("*"))
                if p.is_file() and p.name != "MANIFEST.json"]
        save(folder / "04_integrity/MANIFEST.json", dict(version="1.0", files=rows))
    sealed = run("scripts/seal_repository.py")
    assert sealed["exit_code"] == 0, sealed
    checked = run("scripts/verify_repository.py")
    assert checked["exit_code"] == 0, checked
    state_path = ROOT / "publication/RELEASE_STATE.json"
    state = json.loads(state_path.read_text(encoding="utf8"))
    assert state["public_release_authorized"] is False
    state["final_joint_audit_pass"] = True
    save(state_path, state)
    assert run("scripts/seal_repository.py")["exit_code"] == 0
    checks = [run("scripts/verify_repository.py"),
              run("scripts/build_site.py", "--preview"),
              run("scripts/build_site.py")]
    assert checks[0]["exit_code"] == checks[1]["exit_code"] == 0, checks
    assert checks[2]["exit_code"] != 0, checks[2]
    assert checks[2]["stderr"].strip() == "RELEASE HELD: public_release_authorized", checks[2]
    save(ROOT / "publication/PREPARATION_CHECKS.json", dict(
        status="PASS_PREPARATION_WITH_RELEASE_HELD",
        source="Both papers and companions, preprint 1.0, audited bilingual DOI intake",
        checks=checks, lean_build_executed=False, uploaded=False,
        note="Check outputs precede this report's final manifest refresh; rerun verify_repository.py for the sealed state."))
    assert run("scripts/seal_repository.py")["exit_code"] == 0
    final = run("scripts/verify_repository.py")
    assert final["exit_code"] == 0, final
    print(final["stdout"])
    print("PASS: preview checked; production publication remains blocked.")


if __name__ == "__main__":
    main()
