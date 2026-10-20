"""Static release checks. Copyright 2026 Juan Pablo Traverso Gianini.

SPDX-License-Identifier: Apache-2.0
No Lean, Lake, network or publication operations.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {'.git', '__pycache__', '_preview', 'dist', '.wrangler'}


def files():
    return sorted(p for p in ROOT.rglob('*') if p.is_file()
                  and not (set(p.relative_to(ROOT).parts) & IGNORED))


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        self.targets.extend(v for k, v in attrs if k in ('href', 'src') and v)


def local_links(paths):
    count = 0
    for p in paths:
        if p.suffix not in ('.html', '.md'):
            continue
        text = p.read_text(encoding='utf-8')
        if p.suffix == '.html':
            parser = Links()
            parser.feed(text)
            targets = parser.targets
        else:
            targets = re.findall(r'\]\(([^)\s]+)\)', text)
        for target in targets:
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            path = unquote(url.path)
            resolved = ((ROOT / path.lstrip('/')) if path.startswith('/')
                        else p.parent / path).resolve()
            assert resolved.is_relative_to(ROOT), (p, target, 'outside repository')
            assert resolved.exists(), (p, target, 'missing link')
            count += 1
    return count


def verify():
    intake = json.loads((ROOT/'publication/INTAKE.json').read_text())
    for row in intake['files']:
        p = ROOT/row['path']
        assert p.stat().st_size == row['bytes'] and digest(p) == row['sha256'], row['path']
    idx = json.loads((ROOT/'PUBLICATION_INDEX.json').read_text(encoding='utf-8'))
    for paper in idx['papers']:
        for doc in paper['documents']:
            assert set(doc['files']) == {'pdf', 'tex', 'md'}
            assert all((ROOT/p).is_file() for p in doc['files'].values())
    freeze = 'PAPER_I_LEAN_20261020_ALIGNED_v3'
    with zipfile.ZipFile(ROOT/f'archives/{freeze}.zip') as z:
        lines = z.read(freeze+'/SHA256SUMS.txt').decode().splitlines()
        for line in lines:
            expected, name = line.split('  ', 1)
            assert hashlib.sha256(z.read(freeze+'/'+name)).hexdigest() == expected, name
        assert len(lines) == 3240
        from verify_header_revision import verify as verify_headers
        assert verify_headers(lambda name: z.read(freeze+'/'+name))['modules'] == 1070
        assert (ROOT/'LICENSE').read_bytes() == z.read(freeze+'/LICENSE')
        for p in (ROOT/'LICENSES').glob('*.txt'):
            assert p.read_bytes() == z.read(freeze+'/dependencies/licenses/'+p.name)
    manifest = ROOT/'manifest_sha256.txt'
    bound = {}
    for line in manifest.read_text().splitlines():
        expected, name = line.split('  ', 1)
        assert digest(ROOT/name) == expected, name
        bound[name] = expected
    actual = {p.relative_to(ROOT).as_posix() for p in files() if p != manifest}
    assert set(bound) == actual, ('manifest coverage', actual ^ set(bound))
    assert not (ROOT/'superseded').exists()
    selected_archives = {paper['source_archive'] for paper in idx['papers'] if paper['source_archive']}
    assert {p.relative_to(ROOT).as_posix() for p in (ROOT/'archives').glob('*.zip')} == selected_archives
    visual = json.loads((ROOT/'publication/web-qa/checks.json').read_text())
    assert len(visual['rows']) == 6
    for row in visual['rows']:
        html = 'index.html' if row['page'] == '/' else row['page'].lstrip('/')
        assert digest(ROOT/html) == row['html_sha256']
        assert digest(ROOT/'assets/style.css') == row['css_sha256']
        assert digest(ROOT/row['screenshot']) == row['sha256']
    links = local_links(files())
    result = dict(status='PASS_PREPARATION', imported_files=len(intake['files']),
                  archive_hashes=len(lines), repository_hashes=len(bound), local_links=links,
                  scope='Static packaging only; no Lean/Lake, no deployment.')
    print(json.dumps(result, indent=2))
    return result


if __name__ == '__main__':
    verify()
