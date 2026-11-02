from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from itertools import product,combinations
import json
A=Path(__file__).resolve().parents[1]/'02_validation/AUDIT'
def dump(name,obj):(A/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')

cases=0
for signs in product((-1,1),repeat=6):
 a,ap,b,bp,c,cp=signs
 for t in map(F,(-2,-1,0,1,2)):
  lhs=(1+t*a*b*c)*(1+t*a*bp*cp)*(1+t*ap*b*cp)*(1+t*ap*bp*c)
  rhs=1+t**4+(t+t**3)*(a*b*c+a*bp*cp+ap*b*cp+ap*bp*c)+2*t*t*(a*ap*b*bp+a*ap*c*cp+b*bp*c*cp)
  assert lhs==rhs;cases+=1
# Each side is a polynomial of degree at most four; five exact points certify equality.
def target(m,theta,t):
 sign=[(-1,-1),(-1,1),(1,-1),(1,1)]*(m//4)
 def p(r,c,s):return (1+theta*sign[r][0]*sign[c][0]*sign[s][0])*(1+t*sign[r][1]*sign[c][1]*sign[s][1])/m
 pairs=list((a,b) for a in range(m) for b in range(m) if a!=b)
 return sum((p(r,c,s)*p(r,cp,sp)*p(rp,c,sp)*p(rp,cp,s) for (r,rp),(c,cp),(s,sp) in product(pairs,repeat=3)),F(0))/4
ncheck=0
for theta,t in product(map(F,(-2,-1,0,1,2)),repeat=2):
 m=4;a=(1+theta**4)*(1+t**4);b=(1+theta**2)**2*(1+t**2)**2;c=(1+6*theta**2+theta**4)*(1+6*t**2+t**4)
 assert target(m,theta,t)==(a*(m*m-3*m)+3*b-c/m)/4;ncheck+=1
for m in (4,8):
 for theta,t in ((F(1,2),F(0)),(F(1,2),F(1,2))):
  val=target(m,theta,t);lead=(1+theta**4)*(1+t**4)*m*m/4
  assert 0<=lead-val<=3*((1+theta)*(1+t))**4*m/4
# Hinge: edge sets in both modes, including equal or distinct third labels.
edge=lambda x,y:tuple(sorted((x,y)))
tri=lambda x,y,z:{edge(x,y),edge(x,z),edge(y,z)}
J={edge(*x) for x in [('u','y'),('x','v'),('x','y'),('x','a'),('x','b'),('y','a'),('y','b')]}
for a,b in [('a','b'),('b','a')]:
 ts=[tri('u','y',a),tri('x','v',a),tri('x','y',b)];assert len(set.union(*ts))==9 and sum(map(len,ts))==9;assert set.union(*ts)==J|{edge('u',a),edge('v',a)}
# Sharp rooted count in the Fano packing on seven vertices.
fano=[frozenset((x,y,x^y)) for x in range(1,8) for y in range(x+1,8)];fano=list(set(fano));assert len(fano)==7
pasch=[]
for ts in combinations(fano,4):
 counts=Counter(v for t in ts for v in t)
 if len(counts)==6 and set(counts.values())=={2}:pasch.append(ts)
assert len(pasch)==7 and all(sum(q in s for s in pasch)==4 for q in fano)
for d in range(6):
 for D in range(6):
  def k(d,D):return 1 if not d else (2*D+1)*k(d-1,D*(2*D+1))
  assert k(d,D)<=(2*D+1)**(2**d-1)
dump('check_written_identities.json',{'status':'PASS_FINITE_EXACT_REGRESSIONS','sign_expansion_exact_cases':cases,'polynomial_certificate':'degree at most four in theta; five distinct exact values for every sign assignment','two_scale_exact_targets':ncheck,'two_scale_scope':'exhaustive four coarse/fine sign types at m=4; exact finite check, not universal substitute','diagonal_bounds_checked':4,'hinge_modes':2,'fano_pasch_count':7,'fano_rooted_count':4,'grouping_recurrence_cases':36,'lean_build_executed':False})
print('PASS exact finite regressions')
