"""Render all final pages and contact sheets; human/model review follows separately."""
from pathlib import Path
import hashlib,json,subprocess
import pymupdf as fitz
from PIL import Image,ImageDraw
B=Path(__file__).resolve().parents[1];out=B/'02_validation/page_review';out.mkdir(exist_ok=True)
records=[]
for pdf in sorted(list((B/'01_manuscript').glob('*.pdf'))+list((B/'05_formalization').glob('*.pdf'))):
 d=fitz.open(pdf);folder=out/pdf.stem;folder.mkdir(exist_ok=True);pages=[];contacts=[]
 for i,page in enumerate(d):
  p=folder/f'page_{i+1:02}.png';page.get_pixmap(matrix=fitz.Matrix(1.45,1.45),alpha=False).save(p);pages.append(p)
 for start in range(0,len(pages),6):
  sheet=Image.new('RGB',(1260,1840),'#e6e6e6');draw=ImageDraw.Draw(sheet)
  for k,p in enumerate(pages[start:start+6]):
   im=Image.open(p);im.thumbnail((610,570));x=15+(k%2)*630;y=30+(k//2)*610
   sheet.paste(im,(x+(610-im.width)//2,y));draw.text((x,y-20),f'{pdf.stem}: {start+k+1}',fill='black')
  p=folder/f'contact_{start+1:02}_{min(start+6,len(pages)):02}.jpg';sheet.save(p,quality=85);contacts.append(p.relative_to(B).as_posix())
 # A second PDF renderer checks syntax and complete output without retaining duplicates.
 prefix=folder/'poppler';r=subprocess.run(['pdftoppm','-r','45','-png',str(pdf),str(prefix)],capture_output=True,text=True)
 (folder/'poppler.log').write_text(r.stderr,encoding='utf-8');assert r.returncode==0 and not r.stderr.strip(),(pdf.name,r.stderr)
 assert len(list(folder.glob('poppler-*.png')))==len(d)
 records.append({'pdf':pdf.relative_to(B).as_posix(),'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(d),'contact_sheets':contacts,'rendered_pages':[p.relative_to(B).as_posix() for p in pages],'poppler_status':'PASS'})
(B/'02_validation/AUDIT/RENDER_INDEX.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
print('Rendered',sum(r['pages'] for r in records),'pages in four documents; visual review remains to be recorded.')
