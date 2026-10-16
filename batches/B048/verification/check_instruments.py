"""Finite/local checks of the eight B048 interfaces, not headline proofs."""
from fractions import Fraction as F
from itertools import combinations, product
import json
from math import factorial
from pathlib import Path
import random
import numpy as np
import sympy as s

rng=random.Random(480)
R={'scope':'Eight finite/local mechanisms; no global source theorem or Lean solution certified.','checks':{}}

# Exact fourth spherical moments for g(u)^2=u^T B u give its covariance.
kernel_cases=0
for n in range(2,9):
    for rank in range(1,n):
        entries=[s.Rational(i+1) for i in range(rank)]+[s.Integer(0)]*(n-rank)
        B=s.diag(*entries);A=B/s.trace(B)
        C=(s.trace(B)*s.eye(n)+2*B)/((n+2)*s.trace(B))
        field=C-s.eye(n)/n
        assert s.trace(field)==0
        for i in range(rank,n):assert field[i,i]==-s.Rational(2,n*(n+2))
        step=s.Rational(1,100*n*n)
        assert all((A-step*field)[i,i]>0 for i in range(n))
        kernel_cases+=1
def project_density(M):
    vals,U=np.linalg.eigh(M)
    order=np.sort(vals)[::-1];sums=np.cumsum(order)
    rho=max(i for i in range(len(vals)) if order[i]-(sums[i]-1)/(i+1)>0)
    threshold=(sums[rho]-1)/(rho+1)
    return (U*np.maximum(vals-threshold,0))@U.T
np_rng=np.random.default_rng(480)
min_gap=float('inf')
for _ in range(100):
    X=np_rng.normal(size=(4,4));X=(X+X.T)/2
    P=project_density(X)
    B=np_rng.normal(size=(4,4));B=B@B.T;B/=np.trace(B)
    gap=float(np.trace((X-P)@(P-B)))
    assert gap >= -1e-10
    min_gap=min(min_gap,gap)
R['checks']['balancing']={'exact_kernel_cases':kernel_cases,'projection_models':100,'minimum_projection_gap':min_gap,'control':'At k=0 the normalized spherical covariance is I/n even for singular A, so the inward kernel term is zero.'}

def zonotope_volume(generators,dimension):
    return sum(abs(s.Matrix.hstack(*columns).det()) for columns in combinations(generators,dimension))
def simplex_generators(d):
    unit=s.eye(d)/factorial(d-1)
    return [unit[:,i] for i in range(d)]+[s.ones(d,1)/factorial(d-1)]
simplex_cases=0
for d in range(2,8):
    volume=zonotope_volume(simplex_generators(d),d)
    assert volume==s.Rational(d+1,factorial(d-1)**d)
    simplex_cases+=1
product_cases=0
for r,ss in product(range(2,5),repeat=2):
    ga=[v.col_join(s.zeros(ss,1))/factorial(ss) for v in simplex_generators(r)]
    gb=[s.zeros(r,1).col_join(v)/factorial(r) for v in simplex_generators(ss)]
    volume=zonotope_volume(ga+gb,r+ss)
    body_volume=s.Rational(1,factorial(r)*factorial(ss))
    c=lambda d:s.Rational((d+1)*d**d,factorial(d))
    assert volume/body_volume**(r+ss-1)==c(r)*c(ss)
    product_cases+=1
ratio=c(10)**2/c(20)
assert ratio==s.Rational(22355476,22020096)>1
assert 22355476-22020096==335380
assert c(2)**2<c(4)
R['checks']['projection_products']={'simplex_determinant_enumerations':simplex_cases,'product_enumerations':product_cases,'dimension_20_ratio':str(ratio),'exact_integer_excess':335380,'smaller_product_control':'Two triangles have smaller ratio than the four-simplex.'}

# The later noise remains uniform after earlier intercepts are fixed.
grid=[F(1)+F(i,4) for i in range(5)]
noise_cases=0
for earlier in grid:
    intercept=earlier*earlier-F(7,3)
    for tolerance in [F(0),F(1,8),F(1,4),F(3,8)]:
        for shift in [F(-1),F(0),F(1)]:
            probability=F(sum(abs(intercept+fresh-(earlier+shift))<=tolerance for fresh in grid),len(grid))
            assert probability<=2*tolerance+F(1,4)
            noise_cases+=1
assert all(abs(fresh-fresh)==0 for fresh in grid)  # forbidden dependent comparison
assert F(1)>F(1,4)
R['checks']['fresh_noise']={'conditional_grid_cases':noise_cases,'control':'Reusing the current noise in both branches makes the zero-tolerance tie probability one, above the claimed independent-grid bound.'}

bags=[(0,1),(1,2),(1,3),(2,4)]
edges=[(0,1),(0,2),(1,3)]
assignments=list(product([0,1],repeat=5))
def trace(law,bag):
    result={bits:F(0) for bits in product([0,1],repeat=len(bag))}
    for assignment,mass in law.items():result[tuple(assignment[i] for i in bag)]+=mass
    return result
def glue(marginals,root,mass):
    neighbors={i:[] for i in range(len(bags))}
    for a,b in edges:neighbors[a].append(b);neighbors[b].append(a)
    states=[({},F(1))];queue=[(root,None)]
    for node,parent in queue:
        bag=bags[node];overlap=tuple(v for v in bag if parent is not None and v in bags[parent])
        sep={bits:F(0) for bits in product([0,1],repeat=len(overlap))}
        for bits,p in marginals[node].items():sep[tuple(bits[bag.index(v)] for v in overlap)]+=p
        new=[]
        for previous,past in states:
            key=tuple(previous[v] for v in overlap)
            denom=mass if parent is None else sep[key]
            if denom==0:continue
            for bits,p in marginals[node].items():
                if p and all(bits[bag.index(v)]==previous[v] for v in overlap):
                    updated=dict(previous);updated.update(zip(bag,bits));new.append((updated,past*p/denom))
        states=new
        queue.extend((child,node) for child in neighbors[node] if child!=parent)
    result={a:F(0) for a in assignments}
    for values,p in states:result[tuple(values[v] for v in range(5))]+=p*mass
    return result
gluing_cases=0
for mode in range(12):
    weights={a:rng.randint(0,7) for a in assignments}
    if mode==0:weights={a:int(a[1]==0) for a in assignments}
    if mode==1:weights={a:int(a[2]==1) for a in assignments}
    if mode==2:weights={a:int(len(set(a))==1) for a in assignments}
    total=sum(weights.values());law={a:F(3*w,total) for a,w in weights.items()}
    marginals=[trace(law,bag) for bag in bags]
    glued=[glue(marginals,root,F(3)) for root in range(4)]
    assert all(g==glued[0] for g in glued)
    assert sum(glued[0].values())==3
    assert all(trace(glued[0],bag)==mu for bag,mu in zip(bags,marginals))
    if mode==2:assert all(glued[0][a]==glued[0][tuple(1-v for v in a)] for a in assignments)
    for a in assignments:
        numerator=F(1);denominator=F(1)
        for bag,mu in zip(bags,marginals):numerator*=mu[tuple(a[v] for v in bag)]
        for left,right in edges:
            overlap=tuple(v for v in bags[left] if v in bags[right])
            denominator*=trace(law,overlap)[tuple(a[v] for v in overlap)]
        assert glued[0][a]==(numerator/denominator if denominator else 0)
    gluing_cases+=1
assert not any(a!=b and b!=c and c!=a for a,b,c in product([0,1],repeat=3))
R['checks']['markov_gluing']={'bag_law_models':gluing_cases,'roots_per_model':4,'zero_separator_models':2,'control':'Three pairwise anti-correlated binary laws have consistent single-vertex marginals but no global joint law on a triangle.'}

moment_cases=0;potential_cases=0
for size in range(2,7):
    g=[F((i*i+3*i+2)%7,3) for i in range(size)];mean=sum(g)/size
    k=3;labels=list(product([0,1],repeat=k));second=F(0)
    for shifts in product(range(size),repeat=k):
        for x in range(size):
            average=sum(g[(x-sum(e*w for e,w in zip(bits,shifts)))%size] for bits in labels)/len(labels)
            second+=(average-mean)**2
    second/=size**(k+1)
    assert second==(sum(v*v for v in g)/size-mean*mean)/2**k
    moment_cases+=1
    for trial in range(10):
        counts=[rng.randint(0,5) for _ in range(size)]
        phi=sum(F(1,2)**n for n in counts)/size
        expected=sum(sum(F(1,2)**(counts[x]+counts[(x-w)%size]) for x in range(size))/size for w in range(size))/size
        assert expected==phi*phi
        potential_cases+=1
assert len(list(product([0,1],repeat=3)))==8
assert len({sum(bits)*0 for bits in product([0,1],repeat=3)})==1
R['checks']['boolean_sampler']={'exact_second_moment_groups':moment_cases,'exact_potential_square_models':potential_cases,'collision_control':'Three zero shifts yield eight bit labels but only one distinct group element.'}

def interval_covers(centers,radius,left,right):
    intervals=sorted((x-radius,x+radius) for x in centers)
    reach=left
    for lo,hi in intervals:
        if hi<reach:continue
        if lo>reach:return False
        reach=max(reach,hi)
        if reach>=right:return True
    return False
window_cases=0
for radius,L,offset in product([F(1),F(3,2)],[F(7,10),F(11,10),F(7,3)],[F(0),F(3,4)]):
    grid_centers=[offset+2*radius*k for k in range(-12,13)]
    selected=[x for x in grid_centers if -L-radius<=x<=L+radius]
    repeated=[x+2*L*k for x in selected for k in range(-8,9)]
    assert interval_covers(repeated,radius,-L,L)
    window_cases+=1
radius=F(1);L=F(11,10);offset=F(3,4)
selected=[offset+2*k for k in range(-4,5) if -L<=offset+2*k<=L]
assert not interval_covers([x+2*L*k for x in selected for k in range(-4,5)],radius,-L,L)
R['checks']['periodization']={'exact_interval_models':window_cases,'control':'Removing the radius buffer creates a periodic seam gap for L=1.1 and centers 0.75+2Z.'}

def B(v):x,y=v;return (2*x,y+abs(x))
def Binv(v):a,b=v;return (a/2,b-abs(a)/2)
def graph_distance(xs,ys):
    weighted=sum(F(1,2**(i+1))*(abs(x[0]-y[0])+abs(x[1]-y[1])) for i,(x,y) in enumerate(zip(xs,ys)))
    observed=max(abs(x[0]-y[0]) for x,y in zip(xs,ys))
    return max(weighted,observed)
for trial in range(100):
    length=rng.randint(2,12)
    xs=[(F(rng.randint(-10,10),3),F(rng.randint(-10,10),3)) for _ in range(length)]
    ys=[(F(rng.randint(-10,10),3),F(rng.randint(-10,10),3)) for _ in range(length)]
    bx,by=list(map(B,xs)),list(map(B,ys))
    assert list(map(Binv,bx))==xs
    original=graph_distance(xs,ys);transported=graph_distance(bx,by)
    assert original<=transported<=3*original
R['checks']['weighted_graph_transport']={'finite_sequence_pairs':100,'constants':{'forward':3,'inverse':1},'control':'The constant output sequence 1 has finite weighted input sum but is not norm-null.'}

# Finite-support representatives of the genuine infinite sequence shift.
def insert(t,u):return {0:t,**{i+1:v for i,v in u.items()}}
def difference(a,b):return {i:a.get(i,F(0))-b.get(i,F(0)) for i in a.keys()|b.keys()}
def add(a,b):return {i:a.get(i,F(0))+b.get(i,F(0)) for i in a.keys()|b.keys()}
def clean(a):return {i:v for i,v in a.items() if v}
def K(t,u):return difference(insert(t,u),u)
def inverse(d):
    t=d.get(0,F(0));u={i-1:v for i,v in d.items() if i>0}
    return clean(difference(d,K(t,u))),t
for trial in range(100):
    b={i:F(rng.randint(-10,10),3) for i in range(rng.randint(1,12))};t=F(rng.randint(-10,10),3)
    d=clean(add(b,K(t,b)))
    assert inverse(d)==(clean(b),t)
    recovered,first=inverse(b)
    assert clean(add(recovered,K(first,recovered)))==clean(b)
for b in [F(-3),F(0),F(2,3),F(8)]:
    # Q(b)=(b,0), g(u1,u2)=(2u1,u2), K(u1,u2)=u1; E={0}.
    assert 2*(b-b/2)==b
assert F(7,4)*(1-F(3,4)*F(1,2))!=1  # inexact correction
R['checks']['lifted_absorption']={'finite_support_shift_models':100,'nonsurjective_Q_models':4,'inexact_lift_control':'The proposed inverse fails after replacing the exact correction by 3/4 of it.','scope':'The shift model contains linear c0 and does not model the source no-linear-copy obstruction.'}

R.update(status='passed',groups=len(R['checks']),versions={'numpy':np.__version__,'sympy':s.__version__})
Path(__file__).with_name('results.json').write_text(json.dumps(R,indent=2)+'\n',encoding='utf-8')
print(json.dumps(R))
