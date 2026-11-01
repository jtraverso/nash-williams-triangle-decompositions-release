"""Build all four v1.0 PDFs from delivered semantic sources, using Paper II layout."""
from pathlib import Path
import os,re,subprocess,shutil,json,hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'preprints/PAPER_III';MAN=BASE/'01_manuscript';QA=BASE/'02_validation'
PANDOC=Path('C:/Users/jtraverso/.cache/nw-typesetting/pandoc/pandoc-3.12.1/pandoc.exe')
TECTONIC=Path('C:/Users/jtraverso/.cache/nw-typesetting/tectonic/tectonic.exe')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def codebreak(m):
    s=m[1]
    if re.fullmatch('[0-9a-f]{40,64}',s): s=r'\allowbreak{}'.join(s[i:i+16] for i in range(0,len(s),16))
    else:
        s=re.sub(r'(?<=[a-z])(?=[A-Z])',r'\\allowbreak{}',s)
        s=s.replace('.',r'.\allowbreak{}').replace(r'\_',r'\_\allowbreak{}').replace('/',r'/\allowbreak{}')
    return r'\texttt{'+s+'}'
records={}
for source in sorted(list(MAN.glob('PAPER_III_preprint*.md'))+list((BASE/'05_formalization').glob('PAPER_III_Lean_freeze*.md'))):
    lang=source.stem[-2:];en=lang=='en';out=QA/'typeset'/source.stem;out.mkdir(parents=True,exist_ok=True)
    source_hash=sha(source)
    text=source.read_text(encoding='utf-8');title=re.search(r"^title: '(.*)'$",text,re.M)[1]
    body='\n\n'.join(text.split('\n\n')[3:])
    run=subprocess.run([str(PANDOC),'--from=markdown+tex_math_dollars+raw_tex','--to=latex','--wrap=none','--syntax-highlighting=none'],input=body,capture_output=True,text=True,encoding='utf-8',check=True)
    bt=re.sub(r'\\def\\LTcaptype\{none\}[^\n]*\n','',run.stdout)
    bt=re.sub(r'\\texttt\{([^{}]*)\}',codebreak,bt).replace('\n\n\\[','\n\\[')
    if 'preprint' in source.name:
        bt=bt.replace(r'\begin{longtable}',r'\Needspace{18\baselineskip}\begin{longtable}',1)
        bt=re.sub(r'(\\subsection\{(?:Appendix|Apéndice) C\.)',r'\\Needspace{16\\baselineskip}\1',bt)
        # Keep the rooted-Pasch injection argument with its closing inequality.
        lead='Fix two distinct vertices' if en else 'Fijemos dos vértices distintos'
        assert bt.count(lead)==1
        bt=bt.replace(lead,r'\Needspace{25\baselineskip}'+lead)
    bt=bt.replace(r'\begin{verbatim}',r'\begingroup\scriptsize\begin{verbatim}').replace(r'\end{verbatim}',r'\end{verbatim}\endgroup')
    # Reserve room for statement starts. Long statements may break at paragraph boundaries.
    bt=re.sub(r'(\\textbf\{(?:Theorem|Teorema|Proposition|Proposición|Corollary|Corolario) [^}]+\})',r'\\Needspace{7\\baselineskip}\1',bt)
    ref=BASE/f'03_reproducibility/layout/series_{lang}.tex'
    pre=ref.read_text(encoding='utf-8').split(r'\hypersetup')[0]
    pre+=r'\usepackage{graphicx,float}'+'\n'
    author='Independent researcher, Santiago, Chile' if en else 'Investigador independiente, Santiago, Chile'
    front=r'\hypersetup{pdftitle={'+title+r'},pdfauthor={Juan Pablo Traverso Gianini},pdflang={'+('en-US' if en else 'es-ES')+r'},colorlinks=true,linkcolor=blue,urlcolor=blue,citecolor=blue}'+'\n'
    front+=r'\title{'+title+'}\n'+r'\author{Juan Pablo Traverso Gianini\\'+'\n'+r'\small '+author+r'\\'+'\n'+r'\small \href{mailto:jtraverso@gmail.com}{jtraverso@gmail.com}\\'+'\n'+r'\small ORCID: 0009-0003-6068-4096}'+'\n'+r'\date{}\begin{document}\raggedbottom\maketitle'+'\n'
    bib=re.search(r'\\subsection\{(?:References|Referencias)\}[^\n]*\n',bt)
    if bib:bt=bt[:bib.start()]+'\n\\clearpage\n'+bt[bib.start():bib.end()]+'\n\\begingroup\\small\\raggedright\\setlength{\\parskip}{3pt}\n'+bt[bib.end():]+'\n\\endgroup\n'
    if 'Lean_freeze' in source.name:bt=r'\small\setlength{\parskip}{3pt}'+'\n'+bt
    tex=source.with_suffix('.tex');tex.write_text(pre+front+bt+'\n\\end{document}\n',encoding='utf-8',newline='\n')
    font=out/'fonts.conf';font.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>C:/Windows/Fonts</dir><cachedir prefix="xdg">fontconfig</cachedir></fontconfig>',encoding='utf-8')
    env=dict(os.environ,FONTCONFIG_FILE=str(font),TECTONIC_CACHE_DIR=str(ROOT/'tools/editorial-typesetting-runtime/cache'))
    for n in range(1,4):
        r=subprocess.run([str(TECTONIC),'--only-cached','--keep-logs','--keep-intermediates','--outdir',str(out),str(tex)],cwd=MAN,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace')
        log=r.stdout+r.stderr;(out/f'pass{n}.txt').write_text(log,encoding='utf-8')
        print(source.stem,'pass',n,'exit',r.returncode,flush=True)
        if r.returncode:raise RuntimeError(log[-6000:])
    assert sha(source)==source_hash,'Markdown changed during composition: '+source.name
    built=out/source.with_suffix('.pdf').name;assert built.exists() and built.stat().st_mtime>=tex.stat().st_mtime
    assert re.search(r'Writing[^\n]*'+re.escape(built.name),log)
    pdf=source.with_suffix('.pdf');shutil.copyfile(built,pdf);assert sha(pdf)==sha(built)
    ll=(out/tex.with_suffix('.log').name).read_text(encoding='utf-8',errors='replace')
    issues=[x for x in ll.splitlines() if any(t in x for t in ('Overfull','Missing character:','undefined references','LaTeX Error'))]
    records[source.stem]={'md_sha256':sha(source),'tex_sha256':sha(tex),'pdf_sha256':sha(pdf),'reference_sha256':sha(ref),'passes':3,'layout_issues':issues,'delivered_matches_compiler_output':True}
    print('Issues:',issues,flush=True)
(QA/'artifact_build.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
