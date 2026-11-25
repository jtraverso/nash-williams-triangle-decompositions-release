"""Build both manuscripts from Markdown using the series layout. Requires Pandoc and XeLaTeX."""
from pathlib import Path
import os
import shutil
import subprocess
import tempfile

root = Path(__file__).resolve().parent
os.chdir(root)
for lang, babel, locale in [('en','english','en-GB'), ('es','spanish','es-CL')]:
    stem = 'Doubled_ears_preprint_v1.0_' + lang
    md = Path(stem + '.md')
    lines = md.read_text(encoding='utf-8').splitlines()
    header = Path('series-template.tex.in').read_text(encoding='utf-8')
    values = dict(TITLE=lines[0][2:], AUTHOR=lines[2].strip(), AFFILIATION=lines[3].strip(),
                  ORCID=lines[4].split()[-1], LANG=babel, LOCALE=locale)
    for key, value in values.items():
        header = header.replace('@@'+key+'@@',value)
    body = subprocess.check_output(['pandoc','-f','markdown','-t','latex','--wrap=none'],
                                   input='\n'.join(lines[6:]), encoding='utf-8')
    body = body.replace(r'\subsection{2.',r'\clearpage\subsection{2.')
    for word in ('Appendix A.', 'Apéndice A.'):
        body = body.replace(r'\subsection{'+word,r'\clearpage\subsection{'+word)
    body = body.replace(r'\begin{figure}',r'\par\noindent\begin{minipage}{\linewidth}\makeatletter\def\@captype{figure}\makeatother').replace(r'\end{figure}',r'\end{minipage}\par')
    for width in ('0.29','0.45','0.26'):
        body = body.replace(r'\real{0.3333}',r'\real{'+width+'}',1)
    tex = Path(stem + '.tex')
    tex.write_text(header + r'\maketitle' + '\n' + body + '\n' + r'\end{document}' + '\n', encoding='utf-8')
    with tempfile.TemporaryDirectory() as tmp:
        for _ in range(2):
            proc = subprocess.run(['xelatex','-interaction=batchmode','-halt-on-error','-output-directory='+tmp,tex.name])
            log = (Path(tmp)/(stem+'.log')).read_text(encoding='utf-8',errors='replace')
            if proc.returncode:
                raise RuntimeError(log[-3000:])
        problems = [l for l in log.splitlines() if 'Overfull' in l or 'Missing character:' in l or 'undefined references' in l]
        if problems:
            raise RuntimeError(problems)
        shutil.copyfile(Path(tmp)/(stem+'.pdf'),stem+'.pdf')
