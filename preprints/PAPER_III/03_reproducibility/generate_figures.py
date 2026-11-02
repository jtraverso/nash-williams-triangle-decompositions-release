"""Vector figures at manuscript scale; identical geometry in both languages."""
from pathlib import Path
import math,json,itertools
import pymupdf as fitz
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'01_manuscript/figures'
NAVY=(.13,.28,.39);TEAL=(.10,.42,.38);ORANGE=(.68,.32,.12);GRAY=(.36,.40,.43)
FONT='C:/Windows/Fonts/segoeui.ttf';BOLD='C:/Windows/Fonts/segoeuib.ttf'
def text(p,r,s,size=14,color=NAVY,bold=False,align=0):
    f='bold' if bold else 'body';p.insert_font(fontname=f,fontfile=BOLD if bold else FONT)
    assert p.insert_textbox(fitz.Rect(r),s,fontname=f,fontsize=size,color=color,align=align)>=0,s
def line(p,a,b,color=GRAY,dash=None,width=1.3):p.draw_line(a,b,color=color,width=width,dashes=(dash+' 0' if dash else None))
def arrow(p,a,b,color=GRAY,dash=None):
    line(p,a,b,color,dash);dx,dy=b[0]-a[0],b[1]-a[1];r=math.hypot(dx,dy);dx/=r;dy/=r
    p.draw_polyline([b,(b[0]-7*dx+3*dy,b[1]-7*dy-3*dx),(b[0]-7*dx-3*dy,b[1]-7*dy+3*dx),b],color=color,fill=color)
def box(p,r,title,body,color=NAVY):
    p.draw_rect(fitz.Rect(r),color=color,fill=(.975,.982,.985),width=1)
    text(p,(r[0]+9,r[1]+7,r[2]-9,r[1]+32),title,15,color,True)
    text(p,(r[0]+9,r[1]+35,r[2]-9,r[3]-4),body,13,color=GRAY)
def save(d,name):
    p=d[0];d.save(OUT/(name+'.pdf'));p.get_pixmap(matrix=fitz.Matrix(2,2)).save(OUT/(name+'.png'))
    (OUT/(name+'.svg')).write_text(p.get_svg_image(),encoding='utf-8');d.close()
for lang in ('en','es'):
    en=lang=='en';d=fitz.open();p=d.new_page(width=650,height=430)
    box(p,(8,8,193,104),'Original graph' if en else 'Grafo original','H1–H4\nExact fractional seed' if en else 'H1–H4\nSemilla fraccionaria exacta')
    box(p,(233,8,418,104),'Preparation' if en else 'Preparación','Core and vertex windows\nPhysical certificates' if en else 'Núcleo y ventanas\nCertificados físicos')
    box(p,(458,8,643,104),'Reserve R' if en else 'Reserva R','Chosen before residual M\nHas its own decomposition' if en else 'Se elige antes del residuo M\nTiene descomposición propia',TEAL)
    arrow(p,(197,55),(229,55));arrow(p,(422,55),(454,55),TEAL)
    box(p,(8,166,193,270),'Correction bank' if en else 'Banco de correcciones','Pieces prepared before\nthe corresponding demand\nBounded vertex load' if en else 'Piezas preparadas antes\nde la demanda local\nCarga por vértice acotada',ORANGE)
    box(p,(233,166,418,270),'Covering round' if en else 'Ronda de cobertura','Pack and correct\nProtect the reserve\nAccount for auxiliary edges' if en else 'Empaquetar y corregir\nProteger la reserva\nContabilizar aristas auxiliares')
    box(p,(458,166,643,270),'Actual child' if en else 'Hijo efectivo','Surviving edges\nExact child seed\nPhysical certificate' if en else 'Aristas supervivientes\nSemilla exacta del hijo\nCertificado físico')
    arrow(p,(197,216),(229,216),ORANGE);arrow(p,(422,216),(454,216))
    # Preparation-to-round and preparation-to-bank dependencies.
    arrow(p,(325,108),(325,162));line(p,(245,108),(100,135));arrow(p,(100,135),(100,162),ORANGE)
    # R is protected; this path is kept separate from the child and iteration arrows.
    line(p,(550,108),(550,131),TEAL);arrow(p,(550,131),(390,162),TEAL)
    # Explicit return arrow for the smaller-window iteration.
    line(p,(550,274),(550,299));line(p,(550,299),(325,299));arrow(p,(325,299),(325,274))
    text(p,(235,306,641,331),'Repeat on a smaller window' if en else 'Repetir en una ventana menor',13,GRAY,align=1)
    # Terminal residual and reserve meet at completion; the diagram does not claim inclusions.
    arrow(p,(640,275),(640,340),TEAL,'[4 3]')
    box(p,(8,344,643,424),'Terminal absorption' if en else 'Absorción terminal',
        'Decompose R with the admissible residual M; join the covered prefix.' if en else 'Descomponer R con el residuo admisible M; unir al prefijo cubierto.',TEAL)
    save(d,'architecture_'+lang)

def edge(a,b):return tuple(sorted((a,b)))
J={edge(*x) for x in ['uy','xv','xy','xa','xb','ya','yb']}
Wa={edge(*x) for x in ['ua','va']};Wb={edge(*x) for x in ['ub','vb']}
modes=[[('u','y','a'),('x','v','a'),('x','y','b')],[('u','y','b'),('x','v','b'),('x','y','a')]]
for tris,wedge in zip(modes,(Wa,Wb)):
    edges=[edge(a,b) for t in tris for a,b in itertools.combinations(t,2)]
    assert len(edges)==len(set(edges))==9 and set(edges)==J|wedge
assert J.isdisjoint(Wa|Wb|{edge('u','v')}) and len(J)==7
# Both legal cases for the labels of the two apices.
for b_label in (2,3):
    labels={'u':0,'x':0,'v':1,'y':1,'a':2,'b':b_label}
    for mode in modes:
        assert all(len({labels[v] for v in t})==3 for t in mode)
for lang in ('en','es'):
    en=lang=='en';d=fitz.open();p=d.new_page(width=650,height=290)
    for i,cx in enumerate((108,325,542)):
        text(p,(cx-100,4,cx+100,31),('Auxiliary J' if en else 'Auxiliar J') if i==0 else ('Mode a' if en else 'Modo a') if i==1 else ('Mode b' if en else 'Modo b'),16,NAVY,True,1)
        # No vertex lies on the interior of a nonincident edge.
        pts={n:(cx+78*math.cos(math.radians(150-60*k)),132+78*math.sin(math.radians(150-60*k))) for k,n in enumerate(['u','v','a','x','y','b'])}
        if i==0:
            for a,b in J:line(p,pts[a],pts[b],GRAY,width=1.8)
        else:
            for j,t in enumerate(modes[i-1]):
                for a,b in itertools.combinations(t,2):line(p,pts[a],pts[b],(NAVY,TEAL,ORANGE)[j],(None,'[5 2]','[1.5 2]')[j],1.9)
        for n,(x,y) in pts.items():
            p.draw_circle((x,y),3.5,color=NAVY,fill=(1,1,1),width=1)
            dx=(x-cx)/78;dy=(y-132)/78
            text(p,(x+12*dx-7,y+12*dy-10,x+12*dx+15,y+12*dy+15),n,15,NAVY,True)
        if i==0:
            text(p,(8,235,208,281),'7 edges; root uv omitted.' if en else '7 aristas; se omite la raíz uv.',13,GRAY,align=1)
        else:
            for j,t in enumerate(modes[i-1]):text(p,(cx-95,231+j*18,cx+95,256+j*18),''.join(t),13,(NAVY,TEAL,ORANGE)[j],True,1)
    save(d,'hinge_'+lang)
(BASE/'02_validation/figure_checks.json').write_text(json.dumps({'hinge_auxiliary_edges':7,'vertices':6,'edges_per_mode':9,'exact_edge_partitions':True,'root_avoidance':True,'rainbow_same_or_distinct_apex_labels':True,'bilingual_geometry':'same generator coordinates','round_diagram':'not incorporated: redundant with section 6 and Appendix D'},indent=2),encoding='utf-8')
print('Bilingual vector figures generated; hinge partitions checked.')

# Exact profile curve; explicit dash phase required by the PDF setdash operator.
for lang in ('en','es'):
    en=lang=='en';d=fitz.open();p=d.new_page(width=600,height=280)
    x0=74;y0=235;w=450;h=180
    X=lambda t:x0+w*t;Y=lambda k:y0-h*(k-.25)/(.55-.25)
    for value,label in [(17/64,'17/64'),(51/128,'51/128'),(17/32,'17/32')]:
        yy=Y(value);line(p,(x0,yy),(x0+w,yy),(.86,.86,.86),'[3 3]')
        text(p,(2,yy-8,67,yy+12),label,11,align=2)
    line(p,(x0,40),(x0,y0));line(p,(x0,y0),(x0+w+10,y0))
    pts=[(X(i/200),Y(17/64*(1+(i/200)**4))) for i in range(201)]
    p.draw_polyline(pts,color=NAVY,width=2)
    for t,k in [(0,17/64),(2**(-.25),51/128)]:p.draw_circle((X(t),Y(k)),3,color=NAVY,fill=NAVY)
    p.draw_circle((X(1),Y(17/32)),3.5,color=NAVY,fill=(1,1,1),width=1.5)
    text(p,(30,3,570,28),'Fixed coarse profile: 75% / 25%' if en else 'Perfil por bloques fijo: 75% / 25%',14,align=1)
    text(p,(90,35,380,59),'kappa(1/2, t) = 17(1 + t^4)/64',12,align=1)
    text(p,(X(0)-12,241,X(0)+15,263),'0',11,align=1)
    text(p,(X(2**(-.25))-40,241,X(2**(-.25))+40,263),'2^(-1/4)',11,align=1)
    text(p,(X(1)-10,241,X(1)+10,263),'1',11,align=1)
    text(p,(550,231,580,260),'t',12,align=1)
    save(d,'profile_'+lang)
(OUT/'README.md').write_text('''# Figures for preprint 1.0

All six vector PDFs are generated by 03_reproducibility/generate_figures.py.
Each language uses the same geometry. Architecture arrows express dependencies.
The hinge edge partitions are checked by the generator. The profile curve is
kappa(1/2,t)=17(1+t^4)/64, with t=1 excluded; its block proportions are targets,
not exact proportions in a finite square. PDF dash patterns include their phase.
''',encoding='utf-8')

