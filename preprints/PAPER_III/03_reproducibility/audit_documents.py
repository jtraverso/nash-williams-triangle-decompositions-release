"""Portable internal audit for the first-publication document package."""
from pathlib import Path
from collections import Counter
from itertools import combinations,product
from fractions import Fraction as F
import hashlib,json,re,zipfile,subprocess
import pymupdf as fitz
B=Path(__file__).resolve().parents[1];M=B/'01_manuscript';A=B/'02_validation/AUDIT';S=B/'03_reproducibility/lean'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(name,obj):(A/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def math(s):return Counter(re.sub(r'\s+','',re.sub(r'\\text\{[^}]*\}','',x)) for x in re.findall(r'\$\$[\s\S]*?\$\$|(?<!\$)\$(?!\$)[^\n$]+\$',s))
def tagged(s):
 return {re.search(r'\\tag\{([^}]+)\}',x)[1]:x for x in re.findall(r'\$\$[\s\S]*?\$\$',s) if r'\tag{' in x}
protected=json.loads((A/'PROTECTED_ELEMENT_INDEX.json').read_text(encoding='utf-8'));docs=[];parity=[];links=[]
for stem in ('PAPER_III_preprint','PAPER_III_Lean_freeze'):
 ss={l:((B/'05_formalization' if stem=='PAPER_III_Lean_freeze' else M)/f'{stem}_v1.0_{l}.md').read_text(encoding='utf-8') for l in ('en','es')}
 ps={l:re.split(r'\n\s*\n',s) for l,s in ss.items()};assert len(ps['en'])==len(ps['es']),(stem,{l:len(p) for l,p in ps.items()})
 for i,(en,es) in enumerate(zip(ps['en'],ps['es'])):assert math(en)==math(es),(stem,i,math(en)-math(es),math(es)-math(en))
 ids=lambda s:Counter(x.replace('HEIGHT_PROGRAM_es.md','HEIGHT_PROGRAM_en.md') for x in re.findall(r'`([^`\n]+)`',s))
 assert ids(ss['en'])==ids(ss['es']),stem
 for lang,s in ss.items():
  p=(B/'05_formalization' if stem=='PAPER_III_Lean_freeze' else M)/f'{stem}_v1.0_{lang}.md';pdf=fitz.open(p.with_suffix('.pdf'));txt='\n'.join(page.get_text() for page in pdf)
  assert '1.0' in pdf[0].get_text();assert '\ufffd' not in txt
  forbidden=r'v0\.[0-9]|version 0\.[0-9]|versión 0\.[0-9]|private review|revisión privada|freeze.{0,30}pending|freeze.{0,30}pendiente|not assembled|NOT kernel-checked'
  assert not re.search(forbidden,s+'\n'+txt,re.I),p.name
  assert 'MonitorShift' not in s and 'recover_signed_monitor' not in s
  urls={u.rstrip('.') for u in re.findall(r'https?://[^\s)>]+',s)};active={a.get('uri') for page in pdf for a in page.get_links()}
  assert urls<=active,(p.name,urls-active)
  tex=p.with_suffix('.tex').read_text(encoding='utf-8');assert tex.count(r'\documentclass')==tex.count(r'\hypersetup{')==1
  refs=set(re.findall(r'\\ref\{([^}]+)\}',tex));labels=set(re.findall(r'\\label\{([^}]+)\}',tex));assert refs<=labels,(refs-labels)
  assert '??' not in txt
  rec={'path':p.relative_to(B).as_posix(),'md_sha256':sha(p),'tex_sha256':sha(p.with_suffix('.tex')),'pdf_sha256':sha(p.with_suffix('.pdf')),'pages':len(pdf),'status':'PASS'};docs.append(rec)
  links.append({'document':p.name,'urls':sorted(urls),'resolved_figure_references':sorted(refs),'status':'PASS'})
  if stem=='PAPER_III_preprint':
   statements=re.findall(r'^\*\*(?:Theorem|Teorema|Corollary|Corolario|Proposition|Proposición)[^\n]+',s,re.M)
   assert [hashlib.sha256(x.encode()).hexdigest() for x in statements]==protected[lang]['statement_sha256']
   tt=tagged(s);assert list(tt)==protected[lang]['tags'] and len(tt)==72
   for label,display in tt.items():
    if label!='D.5':assert hashlib.sha256(display.encode()).hexdigest()==protected[lang]['display_sha256'][label],(lang,label)
   assert re.findall(r'^#{2,3} (\d[\d.]*|[A-D]\.\d+)',s,re.M)==re.findall(r'^#{2,3} (\d[\d.]*|[A-D]\.\d+)',ss['es' if lang=='en' else 'en'],re.M)
   h='## Acknowledgments' if lang=='en' else '## Agradecimientos';end='## Appendix A.' if lang=='en' else '## Apéndice A.'
   tail=s[s.index(h):].split(end)[0].strip();assert hashlib.sha256(tail.encode()).hexdigest()==protected[lang]['acknowledgment_and_tools_sha256']
 parity.append({'document':stem,'paragraph_pairs':len(ps['en']),'paragraph_math':'PASS','code_identifiers':'PASS'})
build=json.loads((B/'02_validation/artifact_build.json').read_text(encoding='utf-8'))
for rec in docs:
 r=build[Path(rec['path']).stem];assert not r['layout_issues']
 for ext in ('md','tex','pdf'):assert r[ext+'_sha256']==rec[ext+'_sha256']
 assert r['passes']==3 and r['delivered_matches_compiler_output']
# Source/archive integrity and fresh endpoint queries.
source_map=json.loads((S/'source_closure.json').read_text(encoding='utf-8'));assert len(source_map)==1141
for module,v in source_map.items():assert sha(S/v['path'])==v['sha256'],module
for row in (S/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
 h,n=row.split('  ',1);assert sha(S/n)==h,n
archive=B.parents[1]/'archives/PAPER_III_LEAN_SOURCE_v1.0.zip';cert=json.loads((A/'ARCHIVE_CERTIFICATE.json').read_text(encoding='utf-8'));assert sha(archive)==cert['sha256']
with zipfile.ZipFile(archive) as z:
 for n in z.namelist():assert z.read(n)==(S/n).read_bytes(),n
ver=json.loads((S/'audit/VERIFICATION.json').read_text(encoding='utf-8'));assert ver['status']=='PASS' and ver['project_modules']==1141 and len(ver['endpoint_audits'])==6
queries=[]
for r in ver['endpoint_audits']:
 p=S/'audit/logs'/('AUDIT_'+r['audit']+'.log');assert sha(p)==r['log_sha256'];txt=p.read_text(encoding='utf-8');assert 'sorryAx' not in txt
 for declaration,axioms in re.findall(r"'([^']+)' depends on axioms:\s*\[([^]]*)\]",txt):
  ax=sorted(x.strip() for x in axioms.split(','));assert set(ax)<={'propext','Classical.choice','Quot.sound'};queries.append({'declaration':declaration,'axioms':ax,'audit':r['audit']})
 for declaration in re.findall(r"'([^']+)' does not depend on any axioms",txt):
  queries.append({'declaration':declaration,'axioms':[],'audit':r['audit']})
comp=(B/'05_formalization/PAPER_III_Lean_freeze_v1.0_en.md').read_text(encoding='utf-8')
for d in re.findall(r'`(TypedTriangle\.[^`]+)`',comp):assert any(r['declaration']==d for r in queries),d
# File/declaration and import-closure concordance, including the explicit split.
texts={m:(S/v['path']).read_text(encoding='utf-8-sig') for m,v in source_map.items()}
def noncomment(s):
 out=[];i=0;depth=0;string=False
 while i<len(s):
  if depth:
   if s.startswith('/-',i):depth+=1;i+=2
   elif s.startswith('-/',i):depth-=1;i+=2
   else:i+=1
  elif string:
   out.append(s[i])
   if s[i]=='\\' and i+1<len(s):i+=1;out.append(s[i])
   elif s[i]=='"':string=False
   i+=1
  elif s.startswith('/-',i):depth=1;i+=2;out.append(' ')
  elif s.startswith('--',i):
   j=s.find('\n',i);i=len(s) if j<0 else j
  else:
   if s[i]=='"':string=True
   out.append(s[i]);i+=1
 assert depth==0 and not string
 return ''.join(out)
clean={m:noncomment(t) for m,t in texts.items()}
for m,t in clean.items():assert not re.search(r'\b(?:sorry|admit|axiom)\b',t),m
equiv=json.loads((A/'SOURCE_COMMENT_EQUIVALENCE.json').read_text(encoding='utf-8'))
fresh=json.loads((A/'SOURCE_module_results.json').read_text(encoding='utf-8'));changed={v['module']:v for v in equiv['changed']};assert len(changed)==15
old_plan=json.loads((A/'reconstruction-record/plan.json').read_text(encoding='utf-8'))
for m,v in source_map.items():
 if m in changed:
  c=changed[m];assert v['sha256']==c['after_sha256'] and hashlib.sha256(clean[m].encode()).hexdigest()==c['noncomment_text_sha256']
  assert any(r['module']==m and r['source_sha256']==v['sha256'] and r['exit_code']==0 for r in fresh)
 else:assert v['sha256']==old_plan['sources'][m]['sha256'],m
def closure(root):
 seen=set()
 def visit(m):
  if m in seen or m not in texts:return
  seen.add(m)
  for row in re.findall(r'^\s*(?:public\s+)?import\s+([^\r\n]+)',texts[m],re.M):
   for child in row.split():visit(child)
 visit('RequestProject.TypedTriangle.'+root);return seen
roots={r:closure(r) for r in ('MainPaperIII','MainPaperIIIPasch','MainPaperIIITriangleTower')};maps=[]
for filename in set(re.findall(r'`([A-Za-z0-9]+\.lean)`',(M/'PAPER_III_preprint_v1.0_en.md').read_text(encoding='utf-8')+comp)):
 found=[m for m in texts if source_map[m]['path'].endswith('/'+filename)];assert len(found)==1,filename
 m=found[0];maps.append({'file':filename,'module':m,'imported_by':[r for r,cl in roots.items() if m in cl]})
needed={'signed_envelope_sparse_packing':'SignedEnvelopePacking','signed_envelope_sparse_packing_explicit':'ExplicitMonitoredPackingCore','smooth_on_paid_prepared_child':'VortexPaidChildSmooth','exactify_of_smooth':'SmoothExactification','sparse_edge_deletion_host':'SparseEdgeHost','intrinsic_H2_of_physical_reference_and_mode':'G4ReferenceH2Generic','paid_smooth_at_explicit':'ExplicitPaidSmooth','adaptiveOuterRate_spec':'PaschFinalAssemblyParameters','TrackingState.initial':'PaschAdaptiveInitialState','physical_vertex_first_entry_lattice':'VertexFirstEntry','induced_lattice_persistence':'PreparedCoreConstruction'}
for decl,file in needed.items():
 m='RequestProject.TypedTriangle.'+file;assert re.search(r'\b(?:theorem|lemma|def)\s+'+re.escape(decl)+r'\b',texts[m]),(decl,file)
 if file=='ExplicitPaidSmooth':assert m not in roots['MainPaperIII'] and m in roots['MainPaperIIITriangleTower']
maps.append({'declarations':needed,'default_root':'MainPaperIII','target_closure_sizes':{r:len(c) for r,c in roots.items()}})
# Arithmetic program and finite five-partite certificate.
program={l:re.findall(r'```lean\n([\s\S]*?)```',(B/f'03_reproducibility/HEIGHT_PROGRAM_{l}.md').read_text(encoding='utf-8')) for l in ('en','es')}
assert program['en']==program['es'] and len(program['en'])==312
text=(M/'PAPER_III_preprint_v1.0_en.md').read_text(encoding='utf-8');triples=re.findall(r'\\\{(\d_\d,\d_\d,\d_\d)\\\}',text);assert len(triples)==30
edges=[]
for triple in triples:
 vs=triple.split(',');assert len({v[0] for v in vs})==3;edges.extend(tuple(sorted(e)) for e in combinations(vs,2))
assert len(edges)==len(set(edges))==90
# The signed conversion is affine; verify its exact identity and error factor.
for av,wv,bv in product((F(0),F(1,3),F(1)),(F(-1),F(0),F(1)),(F(1,2),F(2))):
 W=wv*bv*av;J0=av/2;J1=(W/bv+2*av)/3
 assert av/3<=J1<=av and 0<=J0<=1 and W==3*bv*J1-4*bv*J0
 assert 3*bv*J1+4*bv*J0<=5*bv*av
# Rerun the exact finite polynomial and graph checks in the companion checker.
reg=subprocess.run(['python',str(B/'03_reproducibility/check_written_identities.py')],capture_output=True,text=True);assert reg.returncode==0,reg.stdout+reg.stderr
for name in ('architecture','hinge','profile'):
 en=fitz.open(M/f'figures/{name}_en.pdf');es=fitz.open(M/f'figures/{name}_es.pdf');assert en[0].rect==es[0].rect
 geom=lambda p:[{k:v for k,v in row.items() if k!='seqno'} for row in p.get_drawings()]
 assert geom(en[0])==geom(es[0]),name
dump('MODULE_MAP_CERTIFICATE.json',{'status':'PASS','entries':maps,'audited_endpoints':queries})
dump('LINK_CERTIFICATE.json',{'status':'PASS','documents':links})
dump('FINAL_EDITORIAL_CHECKS.json',{'status':'PASS_FINAL_EDITORIAL_CHECKS','version':'1.0','documents':docs,'bilingual_parity':parity,'tagged_equations':72,'theorem_statements':'unchanged','display_change':'D.5 hypotheses moved to preceding paragraph; conclusions retained','height_definitions':312,'base_triangles':30,'base_edges':90,'formal_axiom_groups':6,'formal_sources':1141,'new_math_code':False,'prior_version_mentions_in_publication_documents':0})
print('PASS: four PDFs, bilingual mathematics, protected statements, source and query concordance, exact regressions, links and first-publication status.')
