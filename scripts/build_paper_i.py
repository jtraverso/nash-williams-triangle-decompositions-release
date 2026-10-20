"""Build only the four Paper I preprint documents. Never invokes Lean or Lake."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT/"preprints/PAPER_I/02_validation/typeset"
TEMPLATE = ROOT/"scripts/series_template.tex"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()


def display(match):
    text=match[1].strip()
    if r"\qquad"+"\n" in text and r"\begin{aligned}" not in text:
        tag=re.search(r"\n(\\tag\{[^}]+\})\s*$",text)
        suffix=""
        if tag:
            suffix="\n"+tag[1];text=text[:tag.start()]
        text="\\begin{gathered}\n"+text.replace("\\qquad\n","\\\\\n")+"\n\\end{gathered}"+suffix
    return "$$\n"+text+"\n$$"


def code(match):
    text=match[1]
    # Long namespace components and SHA-256 strings must remain readable.
    if re.fullmatch(r"[0-9a-f]{40,64}",text):
        text=r"\allowbreak{}".join(text[i:i+8] for i in range(0,len(text),8))
    else:
        text=re.sub(r"(?<=[a-z])(?=[A-Z])",r"\\allowbreak{}",text)
        text=text.replace(".",r".\allowbreak{}").replace(r"\_",r"\_\allowbreak{}")
        text=text.replace("/",r"/\allowbreak{}")
    text=text.replace("≤",r"\ensuremath{\le}").replace("σ",r"\ensuremath{\sigma}")
    return r"\texttt{"+text+"}"


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--pandoc",required=True)
    parser.add_argument("--tectonic",required=True)
    parser.add_argument("--only")
    args=parser.parse_args()
    QA.mkdir(exist_ok=True,parents=True)
    fontconfig=QA/"fonts.conf"
    fontconfig.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>C:/Windows/Fonts</dir><cachedir prefix="xdg">fontconfig</cachedir></fontconfig>',encoding="utf-8")
    env=dict(os.environ,FONTCONFIG_FILE=str(fontconfig))
    record_path=QA/"artifact_build.json"
    records=json.loads(record_path.read_text()) if record_path.exists() else []
    sources=sorted((ROOT/"preprints/PAPER_I").glob("*/*preprint_v1.0_*.md"))
    for source in sources:
        if args.only and args.only not in source.name: continue
        lang=source.stem[-2:];companion="COMPANION" in source.name
        source_hash=sha(source)
        md=source.read_text(encoding="utf-8")
        title=re.search(r"^title: '(.*)'$",md,re.M)[1]
        body=re.sub(r"^---\n.*?\n---\n","",md,count=1,flags=re.S)
        if companion:
            body=body.replace("\\exists N\\in\\mathbb N\\;\\forall G:\\quad\n","\\begin{gathered}\n\\exists N\\in\\mathbb N\\;\\forall G:\\\\\n")
            body=body.replace("\\quad\\Longrightarrow\\quad G\\text{","\\\\\n\\Longrightarrow\\quad G\\text{")
            body=body.replace("decomposition}.\n$$","decomposition}.\n\\end{gathered}\n$$")
            body=body.replace("triángulos}.\n$$","triángulos}.\n\\end{gathered}\n$$")
        else:
            body=re.sub(r"\$\$\n(.*?)\n\$\$",display,body,flags=re.S)
        run=subprocess.run([args.pandoc,"--from=markdown+tex_math_dollars","--to=latex","--wrap=none","--syntax-highlighting=none"],
                           input=body,capture_output=True,text=True,encoding="utf-8",check=True)
        texbody=re.sub(r"\\def\\LTcaptype\{none\}[^\n]*\n","",run.stdout)
        texbody=re.sub(r"\\texttt\{([^{}]*)\}",code,texbody)
        for pattern,n in [(r"(\\subsubsection\{(?:Main theorem|Teorema principal))",12),
                          (r"(\\subsubsection\{(?:Proposition|Proposición) 3\.1)",12),
                          (r"(\\subsubsection\{(?:Proposition|Proposición) 4\.2)",24),
                          (r"(\\subsubsection\{4\.3\.)",9),
                          (r"(\\textbf\{(?:Table|Tabla) 1\.\})",12),
                          (r"(\\subsection\{(?:2|3|4|5)\. )",9)]:
            texbody=re.sub(pattern,lambda m:"\n\\Needspace{"+str(n)+"\\baselineskip}\n"+m[1],texbody)
        bib=re.search(r"\\subsection\{(?:References|Referencias)\}[^\n]*\n",texbody)
        if bib:
            texbody=texbody[:bib.end()]+"\n\\begingroup\\small\\raggedright\n\\setlength{\\parskip}{3pt}\n"+texbody[bib.end():]+"\n\\endgroup\n"
            if companion:
                texbody=texbody[:bib.start()]+"\n\\noindent\\begin{minipage}{\\linewidth}\n"+texbody[bib.start():]+"\n\\end{minipage}\n"
        tex=TEMPLATE.read_text(encoding="utf-8")
        vals={"LANG":"english" if lang=="en" else "spanish",
              "BABEL":"english" if lang=="en" else "spanish,es-noshorthands,es-tabla",
              "TITLE":title,"PDFLANG":"en-US" if lang=="en" else "es-ES",
              "AFFILIATION":"Independent researcher, Santiago, Chile" if lang=="en" else "Investigador independiente, Santiago, Chile",
              "BODY":texbody}
        for k,v in vals.items(): tex=tex.replace("@@"+k+"@@",v)
        assert "@@" not in tex
        texpath=source.with_suffix(".tex");texpath.write_bytes(tex.encode("utf-8"))
        # Three explicit invocations; Tectonic also resolves internal reruns.
        for iteration in range(1,4):
            result=subprocess.run([args.tectonic,"--keep-logs","--keep-intermediates",
                                   "--outdir",str(source.parent),str(texpath)],
                                  cwd=source.parent,capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
            raw=result.stdout+result.stderr
            sanitized=raw.replace(str(ROOT),"<REPO>")
            (QA/(source.stem+f"_pass{iteration}.txt")).write_bytes(sanitized.encode("utf-8"))
            print(source.stem,iteration,result.returncode,flush=True)
            if result.returncode: raise RuntimeError(raw[-6000:])
        pdf=source.with_suffix(".pdf")
        log=source.with_suffix(".log").read_text(encoding="utf-8",errors="replace")
        (QA/(source.stem+"_texlog.txt")).write_bytes(log.replace(str(ROOT),"<REPO>").replace(ROOT.as_posix(),"<REPO>").encode("utf-8"))
        assert pdf.is_file() and pdf.stat().st_mtime>=texpath.stat().st_mtime
        assert re.search(r"Writing[^\n]*"+re.escape(pdf.name),raw)
        issues=[line for line in log.splitlines() if any(w in line for w in
                ("Overfull","Missing character:","undefined references","LaTeX Error"))]
        assert sha(source)==source_hash, "Source changed during typesetting; rerun before accepting output"
        item={"source":source.relative_to(ROOT).as_posix(),"markdown_sha256":sha(source),
              "tex_sha256":sha(texpath),"pdf_sha256":sha(pdf),"template_sha256":sha(TEMPLATE),
              "engine":"Tectonic 0.17.0 (XeTeX)","passes":3,"layout_issues":issues,
              "lean_build_executed":False}
        records=[r for r in records if r["source"]!=item["source"]]+[item]
        record_path.write_bytes((json.dumps(records,indent=2)+"\n").encode("utf-8"))
        print(json.dumps(item),flush=True)
        source.with_suffix(".log").unlink()


if __name__=="__main__":
    main()
