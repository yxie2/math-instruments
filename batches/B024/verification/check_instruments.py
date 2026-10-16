"""Finite algebra and Gaussian checks, independent of the source global algorithms."""
from fractions import Fraction as F
from itertools import product
from math import comb, exp, factorial, prod
from pathlib import Path
import json
import numpy as np
from scipy.linalg import expm

RNG=np.random.default_rng(24135)
OUT={}

def comps(t,r):
    if r==1:yield (t,);return
    for i in range(t+1):
        for rest in comps(t-i,r-1):yield (i,)+rest
def falling(t,h):return prod(range(t-h+1,t+1)) if h<=t else 0
def polymul(A,B,p):
    C={}
    for a,x in A.items():
        for b,y in B.items():
            c=tuple(i+j for i,j in zip(a,b));C[c]=(C.get(c,0)+x*y)%p
    return {a:x for a,x in C.items() if x}
def operator(Q,a,b,k,m,p):
    source=[v+u for v in comps(a,2) for u in comps(b,2)]
    target=[v+u for v in comps(a-k,2) for u in comps(b+m,2)]
    index={v:i for i,v in enumerate(target)};M=np.zeros((len(target),len(source)),dtype=np.int64)
    for j,x in enumerate(source):
        for q,c in Q.items():
            if sum(q[:2])!=k or sum(q[2:])!=m:continue
            if any(q[i]>x[i] for i in range(2)):continue
            y=(x[0]-q[0],x[1]-q[1],x[2]+q[2],x[3]+q[3])
            value=c*falling(x[0],q[0])*falling(x[1],q[1])
            M[index[y],j]=(M[index[y],j]+value)%p
    return M
def rank(M,p):
    M=M.copy()%p;r=0
    for j in range(M.shape[1]):
        hits=np.flatnonzero(M[r:,j])
        if len(hits)==0:continue
        h=r+int(hits[0]);M[[r,h]]=M[[h,r]];M[r]=M[r]*pow(int(M[r,j]),-1,p)%p
        for i in range(r+1,M.shape[0]):
            if M[i,j]:M[i]=(M[i]-M[i,j]*M[r])%p
        r+=1
        if r==M.shape[0]:break
    return r
def bottlenecks():
    cases=0;terms=0;nonempty=0
    a,b,k,m=6,12,2,2;n=k+m;D=(a+1)*(b+1);alpha=F(a,a+2);beta=F(b,b+2);lam=F(k,n);rho=F(k,m)
    assert beta>=alpha and F(a+2,a+1)**n<=2
    for p in [2,3,101]:
        for degrees in [[1,3],[2,2],[1,1,2]]:
            for _ in range(4):
                factors=[{e:int(RNG.integers(0,p)) for e in comps(d,4)} for d in degrees]
                full={(0,0,0,0):1}
                for f in factors:full=polymul(full,f,p)
                M=operator(full,a,b,k,m,p);accum=np.zeros_like(M);dimension_sum=0
                for assignment in product(*(range(d+1) for d in degrees)):
                    if sum(assignment)!=k:continue
                    positive=[j for j,(i,d) in enumerate(zip(assignment,degrees)) if F(i)>lam*d]
                    I=sum(assignment[j] for j in positive);J=sum(degrees[j]-assignment[j] for j in positive)
                    left={(0,0,0,0):1};right={(0,0,0,0):1}
                    for j,(f,i) in enumerate(zip(factors,assignment)):
                        selected={e:c for e,c in f.items() if sum(e[:2])==i}
                        if j in positive:left=polymul(left,selected,p)
                        else:right=polymul(right,selected,p)
                    A=operator(left,a,b,I,J,p);B=operator(right,a-I,b+J,k-I,m-J,p)
                    term=B@A%p;accum=(accum+term)%p
                    dim=(a-I+1)*(b+J+1);dimension_sum+=dim
                    assert rank(term,p)<=dim
                    discrepancy=sum(abs(F(i)-lam*d) for i,d in zip(assignment,degrees))
                    assert F(I)-rho*J==(1+rho)*discrepancy/2
                    assert dim/D<=2*float(alpha)**float((1+rho)*discrepancy/2)+1e-12
                    terms+=1;nonempty+=bool(positive)
                assert np.array_equal(M,accum) and rank(M,p)<=dimension_sum
                H=[sum(float(alpha)**abs(float(F(i)-lam*d)) for i in range(d+1)) for d in degrees]
                assert rank(M,p)<=2*D*prod(H)+1e-10
                cases+=1
    OUT['product_rank']={'polynomial_models':cases,'bidegree_factorizations':terms,'positive_discrepancy_subsets':nonempty,'fields':[2,3,101],'scope':'Small exact operator matrices and dimensional bottlenecks; no IMM trace lower bound or asymptotic circuit-size certification.'}

def occupation():
    cases=0;lower=0
    for r in range(1,6):
        for t in range(9):
            samples=list(comps(t,r))
            for _ in range(15):
                ds=tuple(map(int,RNG.integers(0,3,r)));H=sum(ds)
                empirical=F(sum(prod(falling(x,d) for x,d in zip(v,ds)) for v in samples),len(samples))
                exact=F(falling(t,H)*prod(factorial(d) for d in ds),prod(range(r,r+H)))
                independent=prod(F(factorial(d))*F(t,r)**d for d in ds)
                assert empirical==exact and exact<=independent
                if t>0 and H<=t/2:
                    assert float(exact)+1e-12>=exp(-H*H/t-H*H/(2*r))*float(independent);lower+=1
                cases+=1
    assert -F(4*3,2*3)>-F(4,2)**2
    OUT['occupation_moments']={'exact_moments':cases,'lower_comparisons':lower,'scope':'Uniform weak-composition factorial moments and geometric comparisons. A negative factorial coefficient reverses the upper comparison.'}

# F_16 = F_2[x]/(x^4+x+1), with addition represented by xor.
def gm(a,b):
    result=0
    while b:
        if b&1:result^=a
        b>>=1;a<<=1
        if a&16:a^=19
    return result
def gp(a,n):
    v=1
    while n:
        if n&1:v=gm(v,a)
        a=gm(a,a);n>>=1
    return v
def gs(values):
    v=0
    for x in values:v^=int(x)
    return v
def gprod(values):
    v=1
    for x in values:v=gm(v,int(x))
    return v
def lookup():
    agreement=0;homogeneity=0;zero_star=0
    for d,arity in [(1,1),(2,1),(3,1),(2,2),(3,2)]:
        bits=list(product(range(2),repeat=d));tuples=list(product(bits,repeat=arity))
        table={u:int(RNG.integers(0,2)) for u in tuples}
        def evaluate(z,constant=False):
            return gs(gprod([1 if constant else table[u]]+[gprod(zj[i] if bit else zj[-1]^zj[i] for i,bit in enumerate(uj)) for uj,zj in zip(u,z)]) for u in tuples)
        for u in tuples:
            assert evaluate([list(x)+[1] for x in u])==table[u];agreement+=1
        for _ in range(60):
            z=[list(map(int,RNG.integers(0,16,d+1))) for j in range(arity)];scalar=int(RNG.integers(0,16));j=int(RNG.integers(0,arity))
            changed=[row.copy() for row in z];changed[j]=[gm(scalar,x) for x in z[j]]
            assert evaluate(changed)==gm(gp(scalar,d),evaluate(z));homogeneity+=1
            assert evaluate(z,True)==gprod(gp(row[-1],d) for row in z)
            z[j][-1]=0;assert evaluate(z,True)==0;zero_star+=1
    OUT['homogeneous_lookup']={'Boolean_agreements':agreement,'block_homogeneity_checks':homogeneity,'zero_augmentation_controls':zero_star,'scope':'Fixed finite-field lookup models; not the space-bounded evaluator or Turing-machine simulation.'}

def top_coefficients():
    for a in range(1,16):assert gm(a,gp(a,14))==1
    cases=0;homogeneous=0
    for L in range(15):
        S=list(map(int,RNG.choice(16,L+1,replace=False)))
        weights={s:gp(gprod(s^u for u in S if u!=s),14) for s in S}
        for _ in range(15):
            c=list(map(int,RNG.integers(0,16,L+1)))
            values={s:gs(gm(a,gp(s,i)) for i,a in enumerate(c)) for s in S}
            assert gs(gm(weights[s],values[s]) for s in S)==c[-1];cases+=1
        monomials=list(comps(L,3));coeff=list(map(int,RNG.integers(0,16,len(monomials))))
        def Q(x):return gs(gm(c,gprod(gp(z,e) for z,e in zip(x,a))) for a,c in zip(monomials,coeff))
        for _ in range(8):
            a=list(map(int,RNG.integers(0,16,3)));v=list(map(int,RNG.integers(0,16,3)))
            assert gs(gm(weights[s],Q([x^gm(s,y) for x,y in zip(a,v)])) for s in S)==Q(v);homogeneous+=1
    # The formal derivative of X^4 is zero in characteristic two, although its top coefficient is one.
    assert 4%2==0
    OUT['top_coefficient']={'univariate_models':cases,'translated_homogeneous_models':homogeneous,'maximum_degree':14,'characteristic':2,'scope':'Exact interpolation beyond the characteristic; not recursive word evaluation or a uniform field-construction space bound.'}

def gaussian_absorption():
    cases=0;maxerror=0.;bad=0.
    for slots in [2,4,7]:
        for _ in range(35):
            d=3;v=RNG.normal(size=slots);D=1.2*np.linalg.norm(v);r=float(RNG.uniform(.2,3));n=r/(2*D)
            C=np.eye(slots)-np.outer(v,v)/(4*D*D);values,U=np.linalg.eigh(C);P=(U*np.sqrt(values))@U.T
            assert np.linalg.norm(P@P.T+np.outer(v,v)/(4*D*D)-np.eye(slots))<1e-11
            A=RNG.normal(size=(4,slots));A-=np.outer(A@v+np.ones(4),v)/(v@v)
            assert np.max(abs(A@v+1))<1e-11
            x=RNG.normal(size=d);delta=RNG.normal(size=d);z=RNG.normal(size=(slots,d))
            q=x+r*A@z;shifted=x+delta+r*A@(z+v[:,None]*delta/r)
            assert np.max(abs(q-shifted))<1e-10
            G=RNG.normal(size=(slots,d));Z=RNG.normal(size=d)
            noisy=x+n*Z+r*A@(P@G);rewritten=x+r*A@(P@G-v[:,None]*Z/(2*D))
            error=np.max(abs(noisy-rewritten));maxerror=max(maxerror,float(error));assert error<1e-10
            unmodified=np.eye(slots)+np.outer(v,v)/(4*D*D);bad=max(bad,float(np.linalg.norm(unmodified-np.eye(slots))))
            cases+=1
    OUT['Gaussian_center_absorption']={'query_models':cases,'maximum_query_discrepancy':maxerror,'unmodified_seed_covariance_error':bad,'scope':'Deterministic physical-query identity and Gaussian covariance, not an adaptive compiler accuracy theorem.'}

def stationary_flow():
    cases=0;wrong=0;anchor=0.
    for d in [2,3,5]:
        for _ in range(12):
            B=RNG.normal(size=(d,d));A=np.eye(d)+B.T@B;K=RNG.normal(size=(d,d));s=float(RNG.uniform(.5,2))
            Z=np.zeros((d,d));J=np.block([[Z,-K.T/s],[K@A/s,Z]])
            covariance=np.block([[np.linalg.inv(A),Z],[Z,np.eye(d)]])
            assert np.linalg.norm(J@covariance+covariance@J.T)<1e-10
            E=expm(J);assert np.linalg.norm(E@covariance@E.T-covariance)<1e-9
            augmented=np.zeros((3*d,3*d));augmented[:2*d,:2*d]=J;augmented[2*d:,:d]=K@A
            integral=expm(augmented)[2*d:,:2*d]
            momentum=np.c_[Z,np.eye(d)];output=s*momentum+integral
            assert np.linalg.norm(output-s*momentum@E)<1e-9
            assert np.linalg.norm(output@covariance@output.T-s*s*np.eye(d))<1e-9
            wrongJ=np.block([[Z,-K/s],[K@A/s,Z]])
            if np.linalg.norm(wrongJ@covariance+covariance@wrongJ.T)>1e-4:wrong+=1
            anchor=max(anchor,float(np.linalg.norm(momentum@E@covariance)))
            cases+=1
    OUT['stationary_mean_flow']={'nonsymmetric_kernel_models':cases,'wrong_transpose_failures':wrong,'maximum_final_momentum_initial_anchor_covariance':anchor,'scope':'Exact linear Gaussian flow via matrix exponentials; not general nonlinear transport-kernel estimates or implementable sampling.'}

def field_coefficients():
    cases=0
    for p in [5,7,11]:
        for h in [0,1,2,3]:
            d=min(3,p-2);exponents=[e for e in product(range(d+1),repeat=h) if sum(e)<=d]
            grid=list(product(range(1,p),repeat=h))
            for _ in range(8):
                coeff={e:int(RNG.integers(0,p)) for e in exponents};beta=exponents[int(RNG.integers(0,len(exponents)))]
                def value(z):return sum(c*prod(pow(x,e,p) for x,e in zip(z,a)) for a,c in coeff.items())%p
                total=sum(value(z)*prod(pow(x,-e,p) for x,e in zip(z,beta)) for z in grid)%p
                extracted=total*pow(pow(p-1,h,p),-1,p)%p
                assert extracted==coeff[beta];cases+=1
    # At degree p-1 the constant and x^(p-1) alias on the multiplicative group.
    p=7;assert sum(pow(x,p-1,p) for x in range(1,p))*pow(p-1,-1,p)%p==1
    OUT['finite_field_coefficient']={'exact_models':cases,'aliasing_control_prime':p,'scope':'Finite multiplicative Fourier identity including no selected variables; does not verify counting-hierarchy closure levels.'}

def sign_from_residues():
    cases=0;maxbits=0;maxerror=F(0)
    lists=[[3,5,7,11,13],[2,3,5,7,11,13,17,19,23],[p for p in range(2,102) if all(p%d for d in range(2,int(p**.5)+1))]]
    def recover(primes,residues):
        Y=max(primes);B=Y.bit_length()+10;scale=1<<B;inverses={p:pow(prod(q%p for q in primes if q!=p)%p,-1,p) for p in primes}
        budget=sum(p.bit_length() for p in primes)+1
        records=[]
        for k in range(budget+1):
            cs={p:pow(2,k,p)*residues[p]*inverses[p]%p for p in primes}
            num=sum(scale*cs[p]//p for p in primes)%scale;w=F(num,scale);records.append((k,w))
            if F(1,8)<=w<=F(7,8):return (1 if w<F(1,2) else -1),records
        return 0,records
    for primes in lists:
        Pi=prod(primes);bound=(Pi-1)//6
        values=set(range(-200,201))|{0,1,-1,bound,-bound}
        for _ in range(80):
            magnitude=int.from_bytes(RNG.bytes((Pi.bit_length()+7)//8),'big')%(bound+1)
            values.update([magnitude,-magnitude])
        for X in values:
            assert 6*abs(X)<Pi
            answer,records=recover(primes,{p:X%p for p in primes})
            assert answer==(1 if X>0 else -1 if X<0 else 0)
            for k,w in records:
                residue=F((2**k*X)%Pi,Pi);difference=abs(w-residue);circular=min(difference,1-difference)
                assert circular<F(1,1024);maxerror=max(maxerror,circular)
            cases+=1;maxbits=max(maxbits,X.bit_length())
        assert recover(primes,{p:(Pi-1)%p for p in primes})[0]==-1
    OUT['residue_sign']={'exact_integer_models':cases,'maximum_integer_bits':maxbits,'maximum_circular_error':float(maxerror),'scope':'Residue-only recovery with a supplied product-size guarantee. The test harness stores the product solely to check results. No counting-hierarchy or prime-budget asymptotic certification.'}

if __name__=='__main__':
    for f in [bottlenecks,occupation,lookup,top_coefficients,gaussian_absorption,stationary_flow,field_coefficients,sign_from_residues]:
        f();print('PASS',f.__name__,flush=True)
    Path(__file__).with_name('results.json').write_text(json.dumps({'batch':'B024','status':'passed','check_groups':OUT,'limitations':'Finite algebra and Gaussian examples do not certify the global complexity, circuit, machine-simulation or sampling claims.'},indent=2)+'\n',encoding='utf-8')
