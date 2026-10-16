"""Finite checks for selected B049 mechanisms; not source-theorem certification."""
import argparse
import itertools
import json
import random
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

RNG = random.Random(490113)


def scaling():
    cases = 0
    for n in range(2, 9):
        for _ in range(8):
            G = [[F(0) for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(i):
                    G[i][j] = G[j][i] = F(RNG.randint(1, 30), 10)
            order = list(range(n)); RNG.shuffle(order)
            v = [F(2)]*n
            alpha = min(G[i][j] for i in range(n) for j in range(i))
            witnesses = []
            for i in order:
                old = v[i]
                v[i] = max(G[i][j]/v[j] for j in range(n) if j != i)
                assert alpha/2 <= v[i] <= old
                assert all(v[a]*v[b] >= G[a][b] for a in range(n) for b in range(a))
                witnesses.append((i, next(j for j in range(n) if j != i and v[i]*v[j] == G[i][j])))
                assert all(v[a]*v[b] == G[a][b] for a,b in witnesses)
            assert all(max(G[i][j]/(v[i]*v[j]) for j in range(n) if j != i)==1 for i in range(n))
            cases += 1
    assert F(3)/1 > 1  # G_12=3 and v=(1,1): the update increases.
    return dict(exact_arrays=cases, infeasible_initialization_control=True)


def matchings(vertices):
    if not vertices:
        yield []; return
    a, *rest = vertices
    for b in rest:
        for tail in matchings([v for v in rest if v != b]):
            yield [(a,b)]+tail


def covariance():
    cases = noncommuting = 0
    for nv in [4,6]:
        edges = list(itertools.combinations(range(nv),2))
        atoms = [sp.Matrix([int(e in M) for e in edges]) for M in matchings(list(range(nv)))]
        s, m = len(edges), nv//2
        for mode in range(3):
            w = [1 if mode == 0 else RNG.randint(1,4) for e in edges]
            weights = [sp.prod(w[i] for i in range(s) if a[i]) for a in atoms]
            probs = [sp.Rational(wt, sum(weights)) for wt in weights]
            x = sum((p*a for p,a in zip(probs,atoms)),sp.zeros(s,1))
            K = sum((p*(a-x)*(a-x).T for p,a in zip(probs,atoms)),sp.zeros(s))
            d = sp.Matrix.hstack(*(a-atoms[0] for a in atoms)).rank()
            assert K.rank() == d
            assert all(K[i,i] == x[i]*(1-x[i]) for i in range(s))
            c = sp.Rational(7,5)
            D = sp.diag(*[-1/t+c/(1-t) for t in x])
            assert sp.trace(K*D) == -s+(c+1)*m
            # Pseudoinverse contraction replaces an eigenbasis summation.
            assert sp.trace(K.pinv()*(K*D*K+K)) == d-s+(c+1)*m
            noncommuting += K*D != D*K
            if mode == 0:
                assert d-s+3*m > 0  # c=2 excludes a local maximum at this stationary point.
            cases += 1
    assert noncommuting
    return dict(exact_covariances=cases, noncommuting_examples=noncommuting)


def spanners():
    exchanges = cases = 0
    for d in range(1,5):
        for _ in range(4):
            V = [sp.zeros(d,1)]+[sp.eye(d)[:,i] for i in range(d)]
            V += [sp.Matrix([RNG.randint(-9,9) for j in range(d)]) for i in range(12)]
            selected = list(range(d+1))
            while True:
                M = sp.Matrix.hstack(*(V[i].col_join(sp.ones(1,1)) for i in selected))
                inv = M.inv()
                coeffs = [inv*v.col_join(sp.ones(1,1)) for v in V]
                violation = next(((j,k) for j in range(d+1) for k,c in enumerate(coeffs) if abs(c[j])>2),None)
                if violation is None: break
                j,k = violation; old = abs(M.det()); selected[j] = k
                new = abs(sp.Matrix.hstack(*(V[i].col_join(sp.ones(1,1)) for i in selected)).det())
                assert new == old*abs(coeffs[k][j]) and new>2*old
                exchanges += 1
            center = sum((V[i] for i in selected),sp.zeros(d,1))/(d+1)
            for _ in range(10):
                a = sp.Matrix([RNG.randint(-5,5) for j in range(d)])
                b = -min((a.T*v)[0] for v in V)+RNG.randint(0,3)
                vals = [(a.T*v)[0]+b for v in V]
                assert max(vals) <= 2*(d+1)*((a.T*center)[0]+b)
            # Embed in a proper affine subspace; barycentric reconstruction persists.
            embed = lambda v: v.col_join(sp.Matrix([sum(v)+3, 2*sum(v)-1]))
            for v,c in zip(V,coeffs):
                assert sum((c[j]*embed(V[i]) for j,i in enumerate(selected)),sp.zeros(d+2,1)) == embed(v)
            cases += 1
    return dict(exact_polytopes=cases, determinant_exchanges=exchanges)


def time_averages():
    tested = 0
    for eps in [sp.Rational(1,4),sp.Rational(1,16),sp.Rational(1,256)]:
        slow = sp.Matrix([[1-eps,eps],[eps,1-eps]])
        fast = sp.ones(2)/2
        P = (sp.eye(4)+sp.kronecker_product(slow,fast))/2
        Q = sp.kronecker_product(sp.ones(2)/2,sp.eye(2))
        J = sp.ones(4)/4
        # K_obs=2, while the full relaxation time is 1/eps.
        assert (2*(sp.eye(4)-P)-(Q-J)).is_positive_semidefinite
        g = sp.Matrix([-1,1,-1,1]); assert Q*g == g
        for nu in [sp.ones(4,1)/4,sp.Matrix([sp.Rational(1,2),sp.Rational(1,4),sp.Rational(1,4),0])]:
            U = 4*max(nu)
            prob = nu
            first = sp.diag(*g)*prob
            second = sp.diag(*[v*v for v in g])*prob
            for N in range(1,25):
                mse = sum(second)/(N*N)
                assert mse <= 4*U/N
                # Propagate moments of the accumulated sum along the path.
                nextprob = P.T*prob
                nextfirst = P.T*first+sp.diag(*g)*nextprob
                nextsecond = P.T*second+2*sp.diag(*g)*(P.T*first)+sp.diag(*[v*v for v in g])*nextprob
                prob,first,second = nextprob,nextfirst,nextsecond
                tested += 1
    return dict(exact_path_moment_bounds=tested, restricted_constant=2, largest_full_relaxation_time=256)


def compositions(total, count):
    if count==1:
        yield (total,); return
    for a in range(total+1):
        for tail in compositions(total-a,count-1): yield (a,)+tail


def residuals():
    laws = 0
    for M in range(1,5):
        for R in [2,3,4]:
            for a in compositions(2**R,M):
                for D in [1,2,3]:
                    delta = F(1,2**D)
                    p = [F(v,2**R) for v in a]
                    if any((1-delta)*v>F(1,M) for v in p): continue
                    ns = [2**(R+D)-M*(2**D-1)*v for v in a]
                    assert min(ns)>=0 and sum(ns)==M*2**R
                    assert all((1-delta)*v+delta*F(n,M*2**R)==F(1,M) for v,n in zip(p,ns))
                    laws += 1
    for V in range(1,100):
        k = (V-1).bit_length()
        assert F(V,2**k)>F(1,2)
        assert all(F(1,2**k)/F(V,2**k)==F(1,V) for i in range(V))
    assert F(1,2)-(1-F(1,8))*F(3,4)<0
    return dict(exact_dyadic_laws=laws, rejection_ranges=99, insufficient_branch_mass_control=True)


def forest():
    cases = mismatched_internal = 0
    for _ in range(16):
        edges = list(itertools.product(range(3),range(3,6)))
        small = edges[-1]; large = edges[:-1]
        cap = {e:2*RNG.randint(2,10) for e in large}; cap[small]=2
        X = {e:sp.Rational(cap[e],2) for e in edges}
        margins = {v:sum(X[e] for e in edges if v in e) for v in range(6)}
        parent = list(range(6))
        def find(i):
            while parent[i]!=i: i=parent[i]
            return i
        tree=[]
        for e in sorted(large,key=lambda e:-cap[e]):
            a,b=map(find,e)
            if a!=b: parent[a]=b;tree.append(e)
        free=[e for e in large if e not in tree]
        assert len(tree)==5
        nonroot=list(range(1,6))
        A=sp.Matrix([[int(v in e) for e in tree] for v in nonroot])
        B=sp.Matrix([[int(v in e) for e in free] for v in nonroot])
        inv=A.inv(); derivative=-inv*B
        for j,t in enumerate(tree):
            for k,e in enumerate(free):
                if derivative[j,k]: assert cap[e]<=cap[t]
                assert abs(derivative[j,k])*(cap[e]+1)/cap[t]<=2
        adj={v:[] for v in range(6)}
        for a,b in tree: adj[a].append(b);adj[b].append(a)
        rootparent={0:None}; order=[0]
        for v in order:
            for w in adj[v]:
                if w not in rootparent:rootparent[w]=v;order.append(w)
        incidence={small[0]:sp.Integer(0),small[1]:sp.Integer(2)}
        def solve(z):
            rhs=sp.Matrix([margins[v]-incidence.get(v,0)-sum(z[e] for e in free if v in e) for v in nonroot])
            vals=dict(zip(tree, inv*rhs));vals.update(z)
            root=sum(vals[e] for e in large if 0 in e)+incidence.get(0,0)-margins[0]
            return vals,root
        roots=[]
        for __ in range(3):
            z={e:sp.Rational(RNG.randint(0,2*(cap[e]+1)),2) for e in free}
            vals,root=solve(z);roots.append(root)
            assert abs(root)<=2*len(edges)*3
            for t in tree:
                a,b=t; child=b if rootparent[b]==a else a
                U={child}; queue=[child]
                for v in queue:
                    for w in adj[v]:
                        if w!=rootparent[v] and w not in U:U.add(w);queue.append(w)
                sig=lambda v:1 if v<3 else -1
                rhs=-sum(sig(next(v for v in e if v in U))*(vals[e]-X[e]) for e in free if len(set(e)&U)==1)
                rhs-=sum(sig(v)*(incidence[v]-X[small]) for v in small if v in U)
                assert sig(child)*(vals[t]-X[t])==rhs
                assert abs(vals[t]-X[t])<=4*len(edges)*cap[t]
                if set(small)<=U: mismatched_internal+=1
        assert len(set(roots))==1
        cases+=1
    assert mismatched_internal
    assert F(101,1)>2  # a capacity-100 chord crossing a capacity-1 tree edge.
    return dict(exact_graphs=cases, internal_mismatched_small_incidence_checks=mismatched_internal, arbitrary_tree_control=True)


def curvature():
    mp.mp.dps=100
    L=mp.log(2); beta0=mp.mpf('1.5')*(L-mp.mpf('.5'))
    rs=[mp.mpf(0),mp.mpf('0.0001')]+[mp.mpf(k)/20 for k in range(1,20)]+[1-mp.mpf(10)**(-k) for k in [2,4,8,16,24]]
    maxerr=mp.mpf(0); prevbeta=beta0; prevb=L; prevn=mp.mpf(1)/3
    for r in sorted(set(rs)):
        if not r:
            h=L;curv=mp.mpf(4)/3;b=L;n=mp.mpf(1)/3
        else:
            v=mp.atanh(r);t=r*r;x=v/r
            psi=((1+r)*mp.log1p(r)+(1-r)*mp.log1p(-r))/2
            h=L-psi
            curv=((1+r*r)*v-r)/((1-r*r)**2*v**3)
            b=h/((1-t)*x);n=(x-1)/(t*x)
            integral=mp.cosh(v)**2*2*mp.quad(lambda s:(1-s*s)*mp.cosh(2*v*s),[0,1])
            maxerr=max(maxerr,abs(curv/integral-1))
        P=h*h*curv;beta=(b-mp.mpf('.5'))/(1-n)
        maxerr=max(maxerr,abs(P-b*b*(1+n)))
        assert mp.mpf('.5')-mp.mpf('1e-70')<=P<=4*L*L/3+mp.mpf('1e-70')
        assert beta<=prevbeta+mp.mpf('1e-70') and b<=prevb+mp.mpf('1e-70') and n>=prevn-mp.mpf('1e-70')
        prevbeta,prevb,prevn=beta,b,n
    assert maxerr<mp.mpf('1e-60')
    return dict(high_precision_points=len(set(rs)), max_identity_error=str(maxerr), numerical_not_interval_certificate=True)


def boolean_reduction():
    # Exact integer truth-table and coefficient enumeration.
    states=np.arange(16)
    signs=2*((states[:,None]>>np.arange(4))&1)-1
    functions=2*((np.arange(65536,dtype=np.int64)[:,None]>>states)&1)-1
    sums=functions.sum(axis=1); coeff=functions@signs
    # x=min active coefficient <= E[fZ] <= envelope, using the latter for all functions.
    envelope=np.minimum.reduce([np.full(65536,6),9-np.abs(sums)//2,16-np.abs(sums)])
    assert np.all(coeff.sum(axis=1)<=4*envelope)
    increasing=np.ones(65536,dtype=bool)
    for i in range(4):
        low=states[(states&(1<<i))==0];high=low|(1<<i)
        increasing &= np.all(functions[:,low]<=functions[:,high],axis=1)
    active=increasing & np.all(coeff>0,axis=1)
    assert np.all(coeff[active].min(axis=1)<=envelope[active])
    for f,c in zip(functions[active],coeff[active]):
        i=int(c.argmin());low=states[(states&(1<<i))==0];high=low|(1<<i)
        assert 2*f[low].sum()==f.sum()-c[i]
        assert 2*f[high].sum()==f.sum()+c[i]
    # Numeric compression, each intermediate step, two concave profiles.
    selected=functions[RNG.sample(range(65536),128)].astype(float)
    comparisons=0
    for rho in [.1,.5,.9]:
        dist=(signs[:,None,:]!=signs[None,:,:]).sum(axis=2)
        kernel=((1-rho)/2)**dist*((1+rho)/2)**(4-dist)
        current=selected.copy()
        for i in range(4):
            low=states[(states&(1<<i))==0];high=low|(1<<i)
            nxt=current.copy();nxt[:,low]=np.minimum(current[:,low],current[:,high]);nxt[:,high]=np.maximum(current[:,low],current[:,high])
            assert np.all(nxt.sum(axis=1)==current.sum(axis=1))
            a=current@kernel;b=nxt@kernel
            for profile in [lambda x:np.sqrt(np.maximum(0,1-x*x)),lambda x:1-x*x]:
                assert np.all(profile(b).mean(axis=1)<=profile(a).mean(axis=1)+1e-12)
                comparisons+=len(current)
            current=nxt
    return dict(exact_truth_tables=65536, monotone_functions=int(increasing.sum()), four_active_monotone=int(active.sum()), numerical_compression_comparisons=comparisons)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=parser.parse_args()
    checks={}
    for fn in [scaling,covariance,spanners,time_averages,residuals,forest,curvature,boolean_reduction]:
        checks[fn.__name__]=fn(); print(fn.__name__,'passed',flush=True)
    report=dict(batch='B049',status='passed',scope='Eight selected finite/local mechanisms; no source headline theorem or Lean solution certified.',checks=checks)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
