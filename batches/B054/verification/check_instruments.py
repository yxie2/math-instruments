"""Finite checks for selected B054 arguments, including hypothesis controls."""
from fractions import Fraction as F
from itertools import product, permutations, combinations_with_replacement
from math import factorial, gcd, ceil, log, sqrt, pi
from pathlib import Path
import json
import time

import mpmath as mp
import numpy as np
from scipy.integrate import quad
from scipy.linalg import null_space
from scipy.special import ndtr

mp.mp.dps = 45
RNG = np.random.default_rng(540)


def moments():
    vals = [F(-2), F(1), F(3)]
    weights = [F(1, 2), F(1, 3), F(1, 6)]
    mean = sum(x * w for x, w in zip(vals, weights))
    for k in range(1, 7):
        direct = sum(w * (x - mean) ** k for x, w in zip(vals, weights))
        copied = F(0)
        for inds in product(range(3), repeat=k + 1):
            weight = weights[inds[0]]
            value = F(1)
            for i in inds[1:]:
                weight *= weights[i]
                value *= vals[inds[0]] - vals[i]
            copied += weight * value
        assert copied == direct
    radius, n = 1.4, 128
    vals_b = []
    for k in range(n):
        w = radius * np.exp(2j * pi * k / n)
        z = mp.mpc(1 - w)
        vals_b.append(complex(z * (2 * (mp.zeta(1 + z) - 1) + mp.mpf('.4') * (mp.zeta(3 + z) - 1))))
    coeff = np.fft.fft(vals_b) / n / radius ** np.arange(n)
    errors = [abs(sum(coeff[:h + 1]) - 2) for h in [6, 12, 20]]
    assert errors[-1] < 2e-9 and errors[-1] < errors[0]
    for t in [F(1, 4), F(1), F(3)]:
        for h in range(16):
            partial = sum(t ** j / factorial(j) - (t ** (j - 1) / factorial(j - 1) if j else 0) for j in range(h + 1))
            assert partial == t ** h / factorial(h)
    for h in range(24):
        # A model with mean 2^(-h-1), noise 4^h, and 256^h copies.
        variance_of_average = F(16 ** h, 256 ** h)
        assert variance_of_average == F(1, 16 ** h)
        assert F(256 ** h, 2 ** (h + 1)) == F(128 ** h, 2)
    return dict(copy_moments=6, coefficient_count=21, taylor_error=float(errors[-1]), fixed_parameter_telescopes=48, replication_variances=24, expected_replication_cost='infinite by geometric terms 128^h/2')


def augmentation():
    checks = 0
    max_error = 0.0
    for a in [.3, 1., 2.]:
        def density(z):
            if z <= 0:
                return 0.
            b = np.arccosh(np.exp(z)) / a
            return np.exp(-z + a*a/2) * (ndtr(b-a) - ndtr(-b-a))
        def f(x):
            return np.logaddexp(a*x, -a*x) - log(2)
        normal = lambda x: np.exp(-x*x/2) / sqrt(2*pi)
        for z in [.02, .1, .4, 1., 3., 6.]:
            b = np.arccosh(np.exp(z)) / a
            direct = np.exp(-z) * quad(lambda x: np.cosh(a*x)*normal(x), -b, b, epsabs=2e-13)[0]
            max_error = max(max_error, abs(direct - density(z)))
            assert abs(direct - density(z)) < 1e-11
            checks += 1
        grid = np.linspace(.03, 9, 240)
        logs = np.log([density(z) for z in grid])
        assert np.max(np.diff(logs, n=2)) < 2e-12
        mean = quad(lambda x: f(x)*normal(x), -14, 14, epsabs=1e-11)[0]
        var = quad(lambda x: (f(x)-mean)**2*normal(x), -14, 14, epsabs=1e-11)[0]
        mass_g = quad(density, 0, 100, epsabs=1e-10)[0]
        mean_g = quad(lambda z: z*density(z), 0, 100, epsabs=1e-10)[0]
        var_g = quad(lambda z: (z-mean_g)**2*density(z), 0, 100, epsabs=1e-10)[0]
        assert abs(mass_g-1) < 1e-9 and abs(mean_g-mean-1) < 1e-9 and abs(var_g-var-1) < 1e-8
        for t in [.15, .4, .6]:
            mf = quad(lambda x: np.exp(t*(f(x)-mean))*normal(x), -14, 14, epsabs=1e-10)[0]
            mg = quad(lambda z: np.exp(t*(z-mean_g))*density(z), 0, 150, epsabs=1e-10)[0]
            assert abs(mg-mf*np.exp(-t)/(1-t)) < 1e-8
    return dict(tilted_density_comparisons=checks, max_density_error=max_error, log_concavity_grid_size=240, gaussian_models=3, centered_mgf_comparisons=9)


def ward():
    errors = []
    for n in [2, 3, 5, 8, 13, 20]:
        for eta in [.1, .5, 2.]:
            A = RNG.normal(size=(n,n)) + 1j*RNG.normal(size=(n,n))
            H = (A + A.conj().T)/2
            G = np.linalg.inv(H-(.37+1j*eta)*np.eye(n))
            imG = (G-G.conj().T)/(2j)
            errors.append(np.max(np.abs(G.conj().T@G-imG/eta)))
            assert errors[-1] < 1e-11
            assert abs(np.mean(np.abs(G)**2)-np.trace(imG).real/(n*n*eta)) < 1e-12
    graphs = []
    for n in [4, 5, 7]:
        graphs.append([{(i-1)%n,(i+1)%n} for i in range(n)])
        graphs.append([set(range(n))-{i} for i in range(n)])
    graphs.append([set(range(3,6)) if i<3 else set(range(3)) for i in range(6)])
    for adj in graphs:
        n, degree = len(adj), len(adj[0])
        states = {(i,j):F(1,n*degree) for i in range(n) for j in adj[i]}
        for step in range(6):
            marg = [sum(w for (i,j),w in states.items() if j==v) for v in range(n)]
            assert marg == [F(1,n)]*n
            nxt = {}
            for (i,j),w in states.items():
                for k in adj[j]-{i}:
                    nxt[(j,k)] = nxt.get((j,k),F(0)) + w/(degree-1)
            states=nxt
    for n in range(2,10):
        G = np.eye(n)/(-.5j)
        same = np.mean(abs(np.diag(G))**2)
        independent = np.mean(abs(G)**2)
        assert abs(same-n*independent)<1e-13 and same>independent
    return dict(resolvents=18, max_ward_residual=float(max(errors)), fixed_position_distributions=42, dependent_root_controls=8)


def symmetric_basis(dim, order):
    cols=[]
    for multi in combinations_with_replacement(range(dim), order):
        inds=set(permutations(multi))
        v=np.zeros((dim,)*order)
        for ix in inds:
            v[ix]=1/sqrt(len(inds))
        cols.append(v.ravel())
    return np.stack(cols,axis=1)


def tensor_power(M,j):
    out=np.ones((1,1))
    for _ in range(j):
        out=np.kron(out,M)
    return out


def tensor_gap():
    records=[]
    for d,p,j,colors in [(3,0.,3,1),(3,.5,3,1),(3,.85,3,1),(4,.2,3,1),(4,.75,3,1),(3,.4,4,1),(3,.3,3,2)]:
        Q=null_space(np.ones((1,d)))
        w=np.eye(d)[:,0]
        a=d*(1-p*p)/(d-1)
        basis=symmetric_basis(d*colors,j)
        frame=np.zeros((d,d))
        constraints=[]
        quadratic=np.eye(basis.shape[1])
        gap2=0.
        for i in range(d):
            v=p*w+sqrt(a)*np.r_[0,Q[i]]
            line=np.r_[0,Q[i]]/np.linalg.norm(Q[i])
            P=np.outer(w,w)+np.outer(line,line)
            normal=(w-v)/np.linalg.norm(w-v)
            swap=np.eye(d)-2*np.outer(normal,normal)
            ep=(w+v)/sqrt(2*(1+p)); em=(w-v)/sqrt(2*(1-p))
            s=(ep+em)/sqrt(2); t=(ep-em)/sqrt(2)
            q=sqrt(1-p*p); bs=(q-(d-2)/d)/(2*q)
            assert 0<bs<1
            frame+=bs*np.outer(s,s)+(1-bs)*np.outer(t,t)
            Pc=np.kron(P,np.eye(colors)); Sc=np.kron(swap,np.eye(colors))
            projected=tensor_power(Pc,j)@basis
            constraints.append((tensor_power(Sc,j)-np.eye((d*colors)**j))@projected)
            quadratic-=.5*projected.T@projected
            # The identity order-two tensor is invariant under every orthogonal swap.
            assert np.linalg.norm(Sc@Pc@Sc.T-Pc)<1e-12
            gap2+=.5*np.linalg.norm(Pc)**2
        assert np.linalg.norm(frame-np.eye(d))<1e-12
        assert abs(d*colors-gap2)<1e-12
        N=null_space(np.vstack(constraints),rcond=2e-10)
        if N.shape[1]:
            eigen=np.linalg.eigvalsh(N.T@quadratic@N)
            assert min(eigen)>1e-7
            gap=float(min(eigen))
        else:
            gap=None  # Only the zero tensor satisfies the constraints in this case.
        records.append(dict(d=d,p=p,order=j,colors=colors,constraint_dimension=N.shape[1],smallest_gap=gap))
    return dict(models=records, order_two_zero_gap_controls=len(records))


def posterior_product():
    channels=[]
    for obs in [2,3,4]:
        rows=[]
        for i in range(4):
            vals=[int(x) for x in RNG.integers(0,6,size=obs)]
            vals[i%obs]+=1
            rows.append([F(x,sum(vals)) for x in vals])
        channels.append(rows)
    cases=0
    for A in channels:
        for B in channels:
            for y in range(len(A[0])):
                mu=sum(A[i][y] for i in range(4))/4
                p=[A[i][y]/(4*mu) for i in range(4)]
                for z in range(len(B[0])):
                    nu=sum(B[i][z] for i in range(4))/4
                    q=[B[i][z]/(4*nu) for i in range(4)]
                    weight=4*sum(p[i]*q[i] for i in range(4))
                    direct=sum(A[i][y]*B[i][z] for i in range(4))/4
                    assert mu*nu*weight==direct
                    if direct:
                        assert [A[i][y]*B[i][z]/(4*direct) for i in range(4)] == [4*p[i]*q[i]/weight for i in range(4)]
                    for lam in [F(-1,3),F(0),F(1,4),F(1)]:
                        cp=[F(1,4)+lam*(x-F(1,4)) for x in p]
                        assert all(x>=0 for x in cp) and sum(cp)==1
                        info=4*sum((x-F(1,4))**2 for x in p)
                        info_c=4*sum((x-F(1,4))**2 for x in cp)
                        assert info_c==lam*lam*info
                        tv=sum(abs(x-F(1,4)) for x in p)/2
                        assert tv*tv<=info/4
                    cases+=1
    pure=[tuple(F(int(i==j)) for i in range(4)) for j in range(4)]
    zero_pairs=sum(4*sum(x*y for x,y in zip(p,q))==0 for p in pure for q in pure)
    assert zero_pairs==12
    return dict(observation_pairs=cases, edge_scalings=4*cases, impossible_pure_pairs=zero_pairs)


def flow():
    cases=one_child=0
    for B in range(1,6):
        c=F(1,100); K=c/B**3
        for r in [F(1,4),F(1,2),F(4,5)]:
            delta=K*(1-r*r)/(1+9*K)**3
            for _ in range(24):
                ms=[F(int(x),10) for x in RNG.integers(0,31,size=B)]
                bs=[r*x for x in ms]; S=sum(bs)
                D=max([bs[i]*bs[k]*(bs[i]+bs[k]) for i in range(B) for k in range(i)]+[F(0)])
                assert S**3<=sum(x**3 for x in bs)+B**3*D
                m=min(F(3),S-c*D)
                assert m>=0
                ys=[x+K*x**3 for x in ms]; y=m+K*m**3
                assert y<=r*sum(ys)-K*r*(1-r*r)*sum(x**3 for x in ms)
                assert y<=r*sum(x*(1-delta*x*x) for x in ys)
                cases+=1
                one_child+=int(B==1)
    paths=0
    for model in range(12):
        r=mp.mpf('.7'); depth=4
        children={}; labels={}
        levels=[[()]]
        for h in range(depth):
            nxt=[]
            for v in levels[-1]:
                children[v]=[v+(i,) for i in range(1+int(RNG.integers(3)))]
                nxt+=children[v]
            levels.append(nxt)
        for v in levels[-1]:
            labels[v]=mp.mpf(int(RNG.integers(1,20)))/10
        for h in range(depth-1,-1,-1):
            for v in levels[h]:
                labels[v]=mp.mpf('.8')*sum(r*labels[w]/mp.sqrt(1+labels[w]**2) for w in children[v])
        ell={():mp.mpf(1)}; theta={}
        for level in levels[:-1]:
            for v in level:
                for w in children[v]:
                    ell[w]=ell[v]*mp.mpf('.8')*r/mp.sqrt(1+labels[w]**2)
                    theta[w]=ell[w]*labels[w]
                assert abs(sum(theta[w] for w in children[v])-ell[v]*labels[v])<mp.mpf('1e-40')
        for leaf in levels[-1]:
            pot=sum((r**(-h)*theta[leaf[:h]])**2 for h in range(1,depth+1))
            assert pot<=1- (r**(-depth)*ell[leaf])**2+mp.mpf('1e-40')
            paths+=1
    return dict(rational_renormalizations=cases, one_child_cases=one_child, finite_trees=12, conserved_path_checks=paths, infinite_tree_scope='analytic telescoping, not a finite simulation conclusion')


def refinement():
    # Each old posterior is a rational convex combination of grid vertices.
    grid=[(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)),(F(1,2),F(1,2),F(0))]
    base=[F(1,6),F(1,3),F(1,6),F(1,3)]
    records=[]
    for perm in permutations(range(3)):
        zs=[tuple(z[i] for i in perm) for z in grid]
        p=tuple(sum(base[k]*zs[k][i] for k in range(4)) for i in range(3))
        records.append((p,list(zip(zs,base))))
    rho=F(1,len(records)); nu={}
    for p,spread in records:
        for z,alpha in spread:
            nu[z]=nu.get(z,F(0))+rho*alpha
    assert [sum(rho*p[i] for p,_ in records) for i in range(3)]==[F(1,3)]*3
    old_info=new_info=F(0)
    for y,(p,spread) in enumerate(records):
        old_info+=rho*sum((x-F(1,3))**2 for x in p)
        for i in range(3):
            assert sum(alpha*z[i]/p[i] for z,alpha in spread)==1
            recovered=sum(3*nu[z]*z[i]*(rho*alpha/nu[z]) for z,alpha in spread)
            assert recovered==3*rho*p[i]
    for z,mass in nu.items():
        new_info+=mass*sum((x-F(1,3))**2 for x in z)
    assert new_info>old_info
    # Retain a common orbit fraction; reveal the input on omitted observations.
    retain=F(2,5)
    pure_mass=[sum(rho*(1-retain)*p[i] for p,_ in records) for i in range(3)]
    assert pure_mass==[(1-retain)/3]*3
    for i in range(3):
        reverse=[rho*(1-retain)*p[i]/pure_mass[i] for p,_ in records]
        assert sum(reverse)==1
        for y,(p,_) in enumerate(records):
            assert 3*rho*retain*p[i]+3*pure_mass[i]*reverse[y]==3*rho*p[i]
    completed_info=retain*old_info+sum(pure_mass)*F(2,3)
    assert completed_info>old_info
    # The three labeled pure observations identify I; their single orbit does not.
    labeled_accuracy=F(1); orbit_accuracy=F(1,3)
    assert labeled_accuracy>orbit_accuracy
    return dict(labeled_old_observations=len(records), grid_points=len(nu), reverse_garblings=18, old_quadratic_information=str(old_info), refined_quadratic_information=str(new_info), pure_completion_information=str(completed_info), orbit_label_control=True)


def lattice_minimum():
    ranks={0:0,1:0,2:0}; cases=0
    for A in [np.array([[1,0],[0,7]]),np.array([[2,1],[0,3]]),np.array([[3,2],[1,4]]),np.array([[2,0],[0,2]])]:
        det=int(round(abs(np.linalg.det(A))))
        for T in [F(1,2),F(3,2),F(5,2),F(4),F(8)]:
            T0=2*T
            bound=ceil(np.linalg.norm(np.linalg.inv(A),ord=np.inf)*float(T0))+2
            vectors=[]
            for x,y in product(range(-bound,bound+1),repeat=2):
                if gcd(x,y)!=1:
                    continue
                v=A@np.array([x,y]); squared=int(v@v)
                if squared<=T0*T0:
                    vectors.append(squared)
            candidates=[(F(1),0),(F(det*det)/T**4,2)]
            candidates += [(F(sq)/T**2,1) for sq in vectors if sq<=T*T]
            score,rank=min(candidates)
            ranks[rank]+=1; cases+=1
            assert score<=1
            if rank==0:
                assert det>=T*T and all(sq>=T*T for sq in vectors)
            elif rank==1:
                length_squared=score*T*T
                assert F(det*det)/length_squared>=T*T
            else:
                assert det<=T*T
            # All lower determinants at scale T0 are found inside this exhaustive bound.
            deficits=[0.,2*log(float(T0))-log(det)]
            deficits += [log(float(T0))-.5*log(sq) for sq in vectors]
            Delta=max(deficits)
            assert rank<=Delta/log(2)+1e-12
    assert all(ranks.values())
    return dict(exhaustive_two_dimensional_cases=cases, minimizing_rank_counts=ranks)


def gaussian_fourier():
    comparisons=0; max_error=mp.mpf(0)
    for spacing,scale in [(mp.mpf(3),mp.mpf('.8')),(mp.mpf(16),mp.mpf(3))]:
        # Dual weights exp(-pi(k/(spacing*scale))^2), k in Z.
        width=spacing*scale
        cutoff=int(mp.ceil(12*width))
        ks=range(-cutoff,cutoff+1)
        weights=[mp.exp(-mp.pi*(k/width)**2) for k in ks]
        mass=sum(weights)
        tail=2*mp.exp(-mp.pi*((cutoff+1)/width)**2)/(1-mp.exp(-mp.pi*(2*cutoff+3)/width**2))
        assert tail<mp.mpf('1e-190')
        denom=sum(mp.exp(-mp.pi*(scale*spacing*k)**2) for k in range(-20,21))
        max_shift=mp.mpf('2.4') if spacing==3 else mp.mpf(7)
        first_distance=scale*(21*spacing-max_shift)
        primal_tail=2*mp.exp(-mp.pi*first_distance**2)/(1-mp.exp(-mp.pi*(2*first_distance*scale*spacing+(scale*spacing)**2)))
        assert primal_tail<mp.mpf('1e-190')
        def primal(t):
            return sum(mp.exp(-mp.pi*(scale*(spacing*k-t))**2) for k in range(-20,21))/denom
        for t in [mp.mpf(0),mp.mpf('.3'),mp.mpf(1),mp.mpf('2.4')]:
            dual=sum(w*mp.cos(2*mp.pi*k*t/spacing) for k,w in zip(ks,weights))/mass
            f=primal(t)
            max_error=max(max_error,abs(dual-f))
            assert abs(dual-f)<mp.mpf('1e-40')
            distance=scale*abs(t-spacing*mp.nint(t/spacing))
            assert 0<=f<=1+mp.mpf('1e-40')
            assert f<=mp.sqrt(2)*mp.exp(-mp.pi*distance**2/2)+mp.mpf('1e-40')
            comparisons+=1
    # One-dimensional separated subset sums: coefficients 1,2,4 modulo 16.
    spacing=mp.mpf(16); scale=mp.mpf(3); R=scale/3
    patterns=list(product([0,1],repeat=3))
    sums=[sum(bit*c for bit,c in zip(bits,[1,2,4])) for bits in patterns]
    assert min(scale*min(abs(x-y),16-abs(x-y)) for x in sums for y in sums if x!=y)>2*R
    phase_checks=0
    for p in [mp.mpf('.2'),mp.mpf('.5'),mp.mpf('.7')]:
        probs=[p**sum(bits)*(1-p)**(3-sum(bits)) for bits in patterns]
        b=max(p,1-p)
        phase_free=mp.mpf(0)
        for j,s in enumerate(sums):
            near=sum(probs[i] for i,t in enumerate(sums) if scale*min(abs(t-s),16-abs(t-s))<=R)
            assert near<=b**3+mp.mpf('1e-40')
            phase_free+=probs[j]*sum(probs[i]*primal(mp.mpf(t-s)) for i,t in enumerate(sums))
        assert phase_free<=b**3+mp.sqrt(2)*mp.exp(-mp.pi*R*R/2)
        for phases in [[mp.mpf(0)]*3,[mp.mpf('.13'),mp.mpf('.37'),mp.mpf('.61')]]:
            direct=mp.mpf(0)
            for k,w in zip(ks,weights):
                term=mp.mpf(1)
                for c,s in zip([1,2,4],phases):
                    term*=abs(1-p+p*mp.exp(2j*mp.pi*(c*k/spacing+s)))**2
                direct+=w*term/mass
            expanded=mp.mpc(0)
            for i,xi in enumerate(patterns):
                for j,xj in enumerate(patterns):
                    phase=sum(s*(u-v) for s,u,v in zip(phases,xi,xj))
                    expanded+=probs[i]*probs[j]*mp.exp(2j*mp.pi*phase)*primal(mp.mpf(sums[i]-sums[j]))
            assert abs(direct-expanded)<mp.mpf('1e-39')
            assert direct<=phase_free+mp.mpf('1e-39')
            phase_checks+=1
    return dict(poisson_ratio_comparisons=comparisons, max_ratio_error=str(max_error), dual_tail_bound_less_than='1e-190', bernoulli_phase_comparisons=phase_checks, separated_patterns=len(patterns), numerical_scope='one-dimensional finite truncations with generous Gaussian tail margins')


def main():
    start=time.perf_counter()
    results={}
    for fn in [moments,augmentation,ward,tensor_gap,posterior_product,flow,refinement,lattice_minimum,gaussian_fourier]:
        results[fn.__name__]=fn()
        print(fn.__name__, 'passed', flush=True)
    report=dict(batch='B054',status='passed',elapsed_seconds=round(time.perf_counter()-start,3),checks=results,scope='Selected finite algebraic and numerical models, not certification of the source headline theorems or Lean solutions.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
