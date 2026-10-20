"""Refresh packaging hashes after review. Author: Juan Pablo Traverso Gianini.

Copyright 2026 Juan Pablo Traverso Gianini. SPDX-License-Identifier: Apache-2.0
"""
from verify_repository import ROOT, files, digest

manifest = ROOT/'manifest_sha256.txt'
manifest.write_text(''.join(
    f'{digest(p)}  {p.relative_to(ROOT).as_posix()}\n'
    for p in files() if p != manifest
), encoding='utf-8')
print('Repository manifest refreshed; run verify_repository.py next.')
