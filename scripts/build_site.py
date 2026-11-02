"""Build allowlisted static files; never upload. Author: Juan Pablo Traverso Gianini.

Copyright 2026 Juan Pablo Traverso Gianini. SPDX-License-Identifier: Apache-2.0
"""
from pathlib import Path
import argparse
import json
import shutil
from verify_repository import ROOT, local_links, verify

parser = argparse.ArgumentParser()
parser.add_argument('--preview', action='store_true', help='Local, ignored output only')
args = parser.parse_args()
state = json.loads((ROOT/'publication/RELEASE_STATE.json').read_text())
required = ['public_release_authorized', 'paper_ii_final_received', 'final_joint_audit_pass',
            'public_references_reconciled', 'manuscript_licence_recorded',
            'author_headers_reconciled']
if not args.preview:
    pending = [key for key in required if state[key] is not True]
    if pending:
        raise SystemExit('RELEASE HELD: '+', '.join(pending))
    idx = json.loads((ROOT/'PUBLICATION_INDEX.json').read_text(encoding='utf-8'))
    for paper in idx['papers']:
        assert len(paper['documents']) == 4 and paper['source_archive'], 'Final artifacts missing'
        assert (ROOT/paper['source_archive']).is_file()
        for doc in paper['documents']:
            text = (ROOT/doc['files']['md']).read_text(encoding='utf-8')
            assert 'nash-williams-private-review' not in text, 'Private document references remain'
verify()
selected = json.loads((ROOT/'publication/SITE_FILES.json').read_text())['files']
assert len(selected) == len(set(selected)) and len(selected) <= 20000
target = ROOT/('_preview' if args.preview else 'dist')
assert target.resolve().parent == ROOT and target.name in ('_preview', 'dist')
if target.exists():
    shutil.rmtree(target)
target.mkdir()
for rel in selected:
    source = (ROOT/rel).resolve()
    assert source.is_relative_to(ROOT) and source.is_file()
    assert source.stat().st_size <= 25*1024*1024, rel
    dest = target/rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, dest)
# Link checker expects ROOT as origin; test relative targets against the output itself.
import verify_repository
original = verify_repository.ROOT
try:
    verify_repository.ROOT = target
    links = local_links([target/p for p in selected])
finally:
    verify_repository.ROOT = original
print(json.dumps({'output': target.name, 'files': len(selected), 'local_links': links,
                  'uploaded': False, 'preview': args.preview}))
