"""Check the translated invariants and reconstruct the finite witnesses from the manuscript."""
from pathlib import Path
from collections import Counter
from itertools import combinations, combinations_with_replacement
import re, json, hashlib
ROOT=Path(__file__).resolve().parents[1]
en,es=[next(ROOT.glob('*_'+lang+'.md')).read_text(encoding='utf-8') for lang in ('en','es')]
a,b=en.split('\n\n'),es.split('\n\n')
assert len(a)==len(b)
patterns=(r'\$\$[\s\S]*?\$\$|\$[^\n$]*\$',r'\x60[^\x60]+\x60',r'https?://[^\s>)]+',r'\d+')
for x,y in zip(a,b):
    for pat in patterns:
        assert re.findall(pat,x)==re.findall(pat,y),(pat,x[:80])
assert en.count('## ')==es.count('## ')
def edges(triangles,labels):
    counts=Counter()
    for t in triangles:
        assert len(set(t))==3 and len({labels[v] for v in t})==2
        counts.update(combinations(sorted(t),2))
    assert set(counts.values())=={1}
    return set(counts)
def witness(rows, labels, aux, size):
    pos,neg,src=[],[],set()
    for (u,v,c,x,y,a,b) in rows:
        pos.extend([(u,v,a),(u,b,x),(v,b,y)])
        neg.extend([(u,v,c),(b,x,y)])
        src.update(tuple(sorted((i,j))) for i in (u,v) for j in (a,b))
    A=edges(neg,labels)
    assert len(A)==size and not A & src and edges(pos+aux,labels)==A|src
def getrows(text):
    return [list(map(int,re.findall(r'\d+',r))) for r in text.splitlines()[2:]]
for i,block in enumerate((a[27],a[38])):
    rows=getrows(block)
    if i==0:
        labels=[1,0,0,1,0,1,0,0,1,0,0,1,0]
        ears=[(10,7),(11,8),(12,9)]
        aux=[(4,5,6)]
    else:
        labels=[0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,0,1,1,1,1,1,1,0]
        ears=list(zip(range(18,24),range(12,18)))
        aux=[(7,9,11),(8,9,10)]
    data=[]
    for line,(intact,split) in zip(rows,ears):
        uv,c,x,y,*earlabels=line
        if earlabels: assert earlabels==[labels[intact],labels[split]]
        data.append((uv//10,uv%10,c,x,y,intact,split))
    witness(data,labels,aux,[18,36][i])
def triples(text):
    return [tuple(map(int,t)) for t in re.findall(r'\((\d+),(\d+),(\d+)\)',text)]
labels=[0,0,1,0,1,1,1,1,0,0,0,0,1,1]
A=edges(triples(a[31]),labels)
P={(v,e) for i in range(3) for v in (i,i+1) for e in (4+2*i,5+2*i)}
assert len(A)==21 and not A & P and edges(triples(a[33]),labels)==A|P
for s in (1,2):
    weights=[(-8*s-2,-2),(7*s+1,0),(-1,1),(-s,s),(2*s,-2*s)]
    q=dict(zip([(0,0),(0,1),(0,2),(1,2),(2,2)],weights))
    for t in combinations_with_replacement(range(3),3):
        pairs=list(combinations(t,2))
        if (1,1) in pairs: continue
        pos=sum(q[e][0] for e in pairs)
        assert pos<=6*s and (pos==6*s)==(t in [(0,0,1),(0,1,2),(2,2,2)])
        if (0,1) not in pairs:
            neg=sum(q[e][1] for e in pairs)
            assert neg<=0
            if s==2: assert (neg==0)==(t in [(0,0,2),(1,2,2)])
print(json.dumps(dict(status='PASS',aligned_blocks=len(a),math_expressions=len(re.findall(patterns[0],en)),finite_minima_witnesses=[18,21,36],charge_parameters=[1,2]),indent=2))
