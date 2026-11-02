"""Verify the header-only revision against unchanged historical build receipts.

Copyright (c) 2026 Juan Pablo Traverso Gianini.
SPDX-License-Identifier: Apache-2.0
Run from an extracted archive root, or pass its directory/ZIP as an argument.
This script never invokes Lean/Lake or rewrites evidence.
"""
from pathlib import Path
import base64
import hashlib
import json
import sys
import zipfile


def verify(read):
    sha = lambda b: hashlib.sha256(b).hexdigest()
    record = json.loads(read("attribution/source_changes.json"))
    receipts = {}
    changes = 0
    for row in record["files"]:
        current = read(row["path"])
        assert sha(current) == row["after_sha256"], row["path"]
        prefix = base64.b64decode(row["after_prefix"])
        assert current.startswith(prefix)
        body = current[len(prefix):]
        assert sha(body) == row["body_sha256"]
        prior = base64.b64decode(row["before_prefix"]) + body
        assert sha(prior) == row["before_sha256"]
        head = current.lstrip(b"\xef\xbb\xbf").split(b"-/", 1)[0]
        assert b"Copyright (c) 2026 Juan Pablo Traverso Gianini." in head
        assert b"Authors: Juan Pablo Traverso Gianini" in head
        assert b"Apache 2.0" in head
        module = row["path"].removeprefix("source/").removesuffix(".lean").replace("/", ".")
        receipt = json.loads(read(f"evidence/receipts/{module}.json"))
        assert receipt["exit_code"] == 0
        assert receipt["source_sha256"] == sha(prior)
        receipts[module] = receipt
        changes += current != prior
    links = 0
    for receipt in receipts.values():
        for module, expected in receipt["imports"].items():
            assert receipts[module]["object_sha256"] == expected
            links += 1
    for line in read("SHA256SUMS.txt").decode().splitlines():
        expected, name = line.split("  ", 1)
        assert sha(read(name)) == expected, name
    assert len(receipts) == 1510 and changes == 1411
    return dict(status="PASS_HEADER_ONLY_REVISION", modules=len(receipts),
                corrected_headers=changes, unchanged_headers=len(receipts)-changes,
                historical_receipts_checked=len(receipts), import_hash_links=links,
                lean_build_executed=False,
                scope="Current body bytes reconstruct the original compiled sources. "
                      "Historical receipts are unchanged; no new compilation is asserted.")


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    if target.is_file():
        with zipfile.ZipFile(target) as z:
            prefix = z.namelist()[0].split("/")[0] + "/"
            result = verify(lambda name: z.read(prefix + name))
    else:
        result = verify(lambda name: (target / name).read_bytes())
    print(json.dumps(result, indent=2))
