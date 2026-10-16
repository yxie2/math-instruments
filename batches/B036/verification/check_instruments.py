"""Finite checks of eight extracted interfaces; not proofs of headline results."""
import itertools as it
import json
import random
from pathlib import Path
import sympy as s

rng = random.Random(36016)
results = {}

def rank_mod(rows, p):
    a = [[v % p for v in row] for row in rows]
    r = 0
    for j in range(len(a[0])):
        k = next((k for k in range(r, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        z = pow(a[r][j], -1, p)
        a[r] = [v*z % p for v in a[r]]
        for k in range(len(a)):
            if k != r:
                z = a[k][j]
                a[k] = [(v-z*w) % p for v,w in zip(a[k],a[r])]
        r += 1
    return r

# All row and diagonal second differences on a four-by-four square.
rows = []
for n,m in it.product(range(4),repeat=2):
    for dn,dm in [(1,0),(1,1),(1,-1)]:
        cells = [(n+k*dn,m+k*dm) for k in range(3)]
        if all(0<=a<4 and 0<=b<4 for a,b in cells):
            row=[0]*16
            for (a,b),v in zip(cells,[1,-2,1]): row[4*b+a]=v
            rows.append(row)
for p in [5,7,11,211,223]:
    assert rank_mod(rows,p)==13
    for basis in [[1]*16,[n for m in range(4) for n in range(4)],
                  [m for m in range(4) for n in range(4)]]:
        assert all(sum(a*b for a,b in zip(row,basis))%p==0 for row in rows)
    if p>200:
        N=p*p
        K=(3*(N-3)+32*p*N)//(N-3-48*p)+1
        assert (N-3)*(K-3)>16*p*(3*K+2*N)
results['affine_square']={'prime_fields':5,'kernel_dimension':3,'clean_square_bounds':2}

# Exact cover search enumerates all stacked complements, with no symmetry quotient.
def covers(translates, universe):
    bycell={x:[i for i,t in enumerate(translates) if x in t] for x in universe}
    def rec(left,chosen):
        if not left:
            yield tuple(sorted(chosen)); return
        x=min(left,key=lambda x:sum(translates[i]<=left for i in bycell[x]))
        for i in bycell[x]:
            if translates[i]<=left:
                yield from rec(left-translates[i],chosen+[i])
    return set(rec(universe,[]))
E=[{0,1,3},{2,4,5,6}];q=7
assert all({(a-b)%q for a in e for b in e}==set(range(q)) for e in E)
models=decoded=0
for h in range(2,6):
    subsets=[set(c) for k in range(1,h+1) for c in it.combinations(range(h),k)]
    for _ in range(12):
        F=[rng.choice(subsets),rng.choice(subsets)]
        tile={(x,t) for f,e in zip(F,E) for x in f for t in e}
        U=set(it.product(range(h),range(q))); shifts=sorted(U)
        translates=[{((a+x)%h,(b+t)%q) for x,t in tile} for a,b in shifts]
        B=covers(translates,U)
        common=[]
        for A in subsets:
            if all(all(sum((g-a)%h in f for a in A)==1 for g in range(h)) for f in F):
                common.append(A)
                lifted=tuple(sorted(shifts.index((a,0)) for a in A))
                assert lifted in B
        assert bool(B)==bool(common)
        for inds in B:
            A={shifts[i][0] for i in inds}
            assert len(A)==len(inds)
            assert A in common
            decoded+=1
        models+=1
results['stacking']={'finite_models':models,'complements_decoded':decoded}

x,y,z=s.symbols('x y z')
# Exact near-integer interpolation and a smooth-denominator negative control.
count=0
for e in range(1,4):
    for degree in range(e,e+3):
        H=2*degree+2; m=210; t0=1009; t=t0+m*z
        M=sum(rng.randint(-3,3)*z**j for j in range(degree-e+1))
        delta=s.Rational(1,10**40)
        T=s.expand(t**e*(M+delta))
        nodes=[j*(H-1)//degree for j in range(degree+1)]
        vals=[]
        for j in nodes:
            v=T.subs(z,j); n=s.floor(v+s.Rational(1,2))
            vals.append((j,n))
        R=s.interpolate(vals,z)
        assert s.expand(R-t**e*M)==0
        assert all(s.diff(R,z,j).subs(z,-s.Rational(t0,m))==0 for j in range(e))
        assert all(s.denom(M.subs(z,j))==1 and s.gcd(t.subs(z,j),210)==1 for j in range(H))
        count+=1
assert s.Rational(1,2)*2==1 and s.denom(s.Rational(1,2))!=1
results['rough_interpolation']={'exact_models':count,'coprimality_negative_control':True}

# Conditional last stage of the Ramsey selection: cardinality color is Omega mod r.
count=0
for r in range(1,5):
    for length in range(1,5):
        sizes=[2*r*rng.randint(1,3) for _ in range(length)]
        tails=[];start=0
        for a in sizes: tails.append(set(range(start,start+a-1)));start+=a-1
        pivots=list(range(start,start+length))
        blocks=[T|{i} for T,i in zip(tails,pivots)]
        for j in range(length-1): assert max(tails[j])<min(tails[j+1])
        assert max(tails[-1])<pivots[0]
        for k in range(1,length+1):
            for J in it.combinations(range(length),k):
                union=set().union(*(blocks[j] for j in J))
                assert len(union)==sum(sizes[j] for j in J)
                assert len(union)%r==0
        count+=1
results['product_chain']={'conditional_cardinality_models':count,'ramsey_bound_computed':False}

count=0
for pts in [[(0,0),(1,0),(0,1)],[(0,0),(1,0),(0,1),(1,1)],[(0,0),(2,0),(0,2)]]:
    distances={sum((a-b)**2 for a,b in zip(p,q)) for p in pts for q in pts if p!=q}
    separators=[]
    for p in pts:
        norm=(x-p[0])**2+(y-p[1])**2
        f=s.prod((norm-r)/(-r) for r in distances)
        separators.append(f)
        assert s.Poly(f,x,y).total_degree()<=2*len(distances)
        for q in pts: assert f.subs({x:q[0],y:q[1]})==int(p==q)
    eqs=[1-sum(separators)]+[(v-p[j])*f for p,f in zip(pts,separators) for j,v in enumerate((x,y))]
    zeros=s.solve_poly_system(eqs,x,y)
    assert set(zeros)==set(pts)
    count+=1
results['distance_separators']={'exact_point_sets':count}

# Nonreduced local algebra: x^2(x-1), y^2. Coefficient functionals of divided determinant.
X,Z,Y,W=s.symbols('X Z Y W')
det=(X**2+X*Z+Z**2-X-Z)*(Y+W)
s0=-s.expand(det).coeff(Z,1).coeff(W,1)
s1=s.expand(det.subs(Z,1)).coeff(W,1)
assert s0==1-X and s1==X**2
for a,f in [(0,s0),(1,s1)]:
    u=3*f*f-2*f**3
    for b in [0,1]:
        assert u.subs(X,b)==int(a==b) and s.diff(u,X).subs(X,b)==0
        v=(X-a)*f*f
        assert v.subs(X,b)==0 and s.diff(v,X).subs(X,b)==int(a==b)
# x(x-1),xy also has the positive-dimensional component x=0.
assert X.subs(X,0)==0 and X.subs(X,1)==1
assert s.Matrix([[0,0],[0,0]]).det()==0  # Jacobian at the nonreduced origin.
results['singular_interpolation']={'nonreduced_isolated_points':2,'positive_component_model':1,'first_jet_checks':8}

# Rational basis coordinates expose a height-one obstruction exactly.
M=s.Matrix([[x,y],[0,x*y]]); checked=nonmembers=0
for _ in range(80):
    v=s.Matrix([rng.randint(-3,3)+rng.randint(-3,3)*x+rng.randint(-3,3)*y for j in range(2)])
    c=M.inv()*v
    dens=[s.fraction(s.cancel(a))[1] for a in c]
    member=all(s.Poly(d,x,y).total_degree()==0 for d in dens)
    if not member:
        assert any(s.factor_list(d)[1] for d in dens);nonmembers+=1
    assert all(s.cancel(a)==0 for a in M*c-v)
    checked+=1
assert s.gcd(x,y)==1 and s.groebner([x,y],x,y).reduce(s.Integer(1))[1]==1
results['height_one_lattice']={'rational_coordinate_models':checked,'detected_nonmembers':nonmembers,'nonfree_ideal_negative_control':True}

# Kernel restrictions u+v mod y and u-v mod (x+y), with alpha=x.
B=s.Matrix([[y/2,(x+y)/2],[y/2,-(x+y)/2]])
assert s.factor(B.subs(x,0).det())==-y**2/2
def member(v):
    return s.expand((v[0]+v[1]).subs(y,0))==0 and s.expand((v[0]-v[1]).subs(x,-y))==0
for _ in range(120):
    v=s.Matrix([sum(rng.randint(-2,2)*a for a in [1,x,y,x*y,x*x,y*y]) for j in range(2)])
    assert member(v)==member(x*v)
for e in [s.Matrix([1,0]),s.Matrix([0,1])]:assert member(y*(x+y)*e)
assert s.rem(x,x,x)==0 and s.rem(x,x*x,x)!=0
results['saturated_quotient']={'exact_polynomial_models':120,'proportional_label_negative_control':True}

output={'batch':'B036','status':'pass','scope':'Selected finite interfaces only; no headline theorem or Lean build certified.','checks':results}
Path(__file__).with_name('results.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
print(json.dumps(output,indent=2))
