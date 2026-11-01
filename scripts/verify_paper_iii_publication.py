"""Download the published Paper III artifacts without credentials and verify bytes.

Copyright 2026 Juan Pablo Traverso Gianini. SPDX-License-Identifier: Apache-2.0
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,urllib.request,sys
R=Path(__file__).resolve().parents[1]
commit=sys.argv[1]
idx=json.loads((R/'PUBLICATION_INDEX.json').read_text(encoding='utf-8'))
paper=next(p for p in idx['papers'] if p['id']=='PAPER_III')
paths=[d['files']['pdf'] for d in paper['documents']]+[paper['source_archive']]
rows=[]
for path in paths:
    url=f'https://raw.githubusercontent.com/jtraverso/nash-williams-triangle-decompositions-release/{commit}/{path}'
    with urllib.request.urlopen(url,timeout=90) as response:data=response.read()
    actual=hashlib.sha256(data).hexdigest();assert actual==hashlib.sha256((R/path).read_bytes()).hexdigest(),path
    rows.append({'path':path,'url':url,'bytes':len(data),'sha256':actual})
record={'status':'PASS_PUBLIC_GITHUB_DOWNLOADS','checked_utc':datetime.now(timezone.utc).isoformat(),'source_commit':commit,'files':rows,'authenticated':False}
(R/'publication/paper-iii/GITHUB_DOWNLOADS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print('PASS: four public GitHub PDFs and formal source archive match approved bytes.')
