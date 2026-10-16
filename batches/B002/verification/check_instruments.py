"""Finite checks of selected B002 identities, not a proof of the source theorems.

Run with Python and NumPy. Results are deterministic for the recorded seed.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import math
import numpy as np

SEED = 20261016
RNG = np.random.default_rng(SEED)


def entropy(matrix):
    values = np.linalg.eigvalsh((matrix + matrix.conj().T) / 2)
    assert values.min() >= -2e-12
    positive = values[values > 1e-15]
    return float(-np.dot(positive, np.log(positive)))


def binary_entropy(p):
    return sum(-v * math.log(v) for v in (p, 1-p) if v > 0)


def determinant_entropy(u):
    assert -2e-14 <= u <= 0.25 + 2e-14
    return binary_entropy((1 + math.sqrt(max(0, 1-4*u))) / 2)


def thermal_checks():
    rational_count = 0
    for a, b, c, d in product(range(1, 6), repeat=4):
        total = a+b+c+d
        alpha, beta, eta, delta = (Fraction(v, total) for v in (a,b,c,d))
        k2 = alpha*delta-beta*eta
        if k2 < 0:
            continue
        u0, u1 = alpha+beta, eta+delta
        u = u0*u1-k2
        assert u == beta*u1+eta*u0 and 0 < u <= Fraction(1,4)
        first = (k2/u1,u/u1,Fraction(0),u1)
        second = (u0,Fraction(0),u/u0,k2/u0)
        w1, w2 = beta*u1/u, eta*u0/u
        assert w1+w2 == 1
        assert tuple(w1*x+w2*y for x,y in zip(first,second)) == (alpha,beta,eta,delta)
        assert first[1]*first[3] == second[2]*second[0] == u
        rational_count += 1
    min_slack = float('inf')
    max_equality_error = 0.0
    for trial in range(320):
        rows, columns = 1+trial%4, 1+(trial//4)%4
        x = RNG.normal(size=(rows,columns))+1j*RNG.normal(size=(rows,columns))
        y = RNG.normal(size=(rows,columns))+1j*RNG.normal(size=(rows,columns))
        x /= np.linalg.norm(x)
        y /= np.linalg.norm(y)
        alpha,beta,eta,delta = RNG.dirichlet(np.ones(4))
        if alpha*delta < beta*eta:
            alpha,beta,eta,delta = beta,alpha,delta,eta
        k2 = max(0,alpha*delta-beta*eta)
        k = math.sqrt(k2)
        u = (alpha+beta)*(eta+delta)-k2
        xx,yy,xy = x@x.conj().T,y@y.conj().T,x@y.conj().T
        t = np.block([[alpha*xx+beta*yy,k*xy],[k*xy.conj().T,eta*xx+delta*yy]])
        bound = (alpha+eta)*entropy(xx)+(beta+delta)*entropy(yy)+determinant_entropy(u)
        slack = entropy(t)-bound
        assert slack >= -2e-11, (trial,slack)
        min_slack = min(min_slack,slack)
        equality = np.kron(np.array([[alpha+beta,k],[k,eta+delta]]),xx)
        error = abs(entropy(equality)-entropy(xx)-determinant_entropy(u))
        assert error < 2e-11
        max_equality_error = max(max_equality_error,error)
    return {'exact_rational_mixtures':rational_count,'complex_gram_examples':320,'minimum_entropy_slack':min_slack,'maximum_equal_input_error':max_equality_error}


def interpolation_checks():
    def f(x): return x/math.sinh(x) if x else 1.0
    def b(x): return x/math.tanh(x) if x else 1.0
    values = [-4,-2,-1,-0.2,0,0.2,1,2,4]
    worst = 0.0
    for x,y in product(values,repeat=2):
        s,t = f(x)**2,f(y)**2
        if abs(x) != abs(y):
            e = (t-s)/(2*(b(x)-b(y)))
        elif x:
            e = s*(b(x)-1)/(b(x)-s)
        else:
            e = 0.5
        assert e > 0
        a = b(x)+b(y)
        phi = (x-y)/(a+2*e)
        direct = sum(f(x)*math.exp(sign*x)*(1-sign*phi)**2/4 + f(y)*math.exp(sign*y)*(1+sign*phi)**2/4 for sign in (-1,1))+e*phi**2
        target = f(x)*f(y)/f(x+y)
        error = abs(direct-target)
        assert error < 5e-12
        worst = max(worst,error)
    return {'scalar_parameter_pairs':len(values)**2,'includes_coincident_opposite_and_zero_parameters':True,'maximum_absolute_error':worst,'not_checked':'Stieltjes representation and infinite-dimensional form comparison'}


def choi(channel, n):
    out=[]
    for i in range(n):
        row=[]
        for j in range(n):
            e=np.zeros((n,n),complex)
            e[i,j]=1
            row.append(channel(e))
        out.append(row)
    return np.block(out)


def completion_checks():
    max_corner_error=0.0
    min_choi_eigenvalue=0.0
    for m in (2,3):
        kraus=[]
        for _ in range(2):
            ks=[]
            for _ in range(3):
                u=RNG.normal(size=m)+1j*RNG.normal(size=m)
                v=RNG.normal(size=m)+1j*RNG.normal(size=m)
                ks.append(np.outer(u,v.conj())/m)
            kraus.append(ks)
        def psi(i,x): return sum(k@x@k.conj().T for k in kraus[i])
        effects=[sum(k.conj().T@k for k in ks) for ks in kraus]
        factors=[1/(1+np.trace(a).real) for a in effects]
        deficits=[np.eye(m)-c*a for c,a in zip(factors,effects)]
        n=2*m+1
        def theta(x):
            out=np.zeros((n,n),complex)
            out[:m,:m]=factors[1]*psi(1,x[m:2*m,m:2*m])
            out[m:2*m,m:2*m]=factors[0]*psi(0,x[:m,:m])
            out[-1,-1]=np.trace(deficits[0]@x[:m,:m])+np.trace(deficits[1]@x[m:2*m,m:2*m])+x[-1,-1]
            return out
        c=choi(theta,n)
        cp_min=float(np.linalg.eigvalsh(c).min())
        ppt=c.reshape(n,n,n,n).transpose(0,3,2,1).reshape(n*n,n*n)
        ppt_min=float(np.linalg.eigvalsh(ppt).min())
        assert min(cp_min,ppt_min)>-2e-11
        min_choi_eigenvalue=min(min_choi_eigenvalue,cp_min,ppt_min)
        assert np.max(np.abs(np.trace(c.reshape(n,n,n,n),axis1=1,axis2=3)-np.eye(n)))<2e-12
        square=choi(lambda x:theta(theta(x)),n)
        indices=[i*n+j for i in range(m) for j in range(m)]
        corner=square[np.ix_(indices,indices)]
        expected=factors[0]*factors[1]*choi(lambda x:psi(1,psi(0,x)),m)
        error=float(np.max(np.abs(corner-expected)))
        assert error<2e-12
        max_corner_error=max(max_corner_error,error)
    return {'input_dimensions':[2,3],'maximum_corner_error':max_corner_error,'minimum_choi_or_partial_transpose_eigenvalue':min_choi_eigenvalue,'scope':'PPT measure-and-prepare examples test the completion identity, not existence of an entangled composite.'}


def sampling_checks():
    checked=0
    for k in range(2,6):
        states=list(product((0,1),repeat=k))
        for _ in range(20):
            masses=[int(x) for x in RNG.integers(1,20,size=len(states))]
            total=sum(masses)
            probabilities=[Fraction(x,total) for x in masses]
            q,q0,eps=Fraction(3,4),Fraction(1,4),Fraction(1,2)
            ph=sum(p for z,p in zip(states,probabilities) if sum(z)>=math.ceil(q*k))
            # Select the least integer ell by exact rational comparison.
            ell=0
            while (q0/q)**ell > eps*ph/4:
                ell+=1
            threshold=ph*q**ell/2
            found=False
            for mask in range(1<<k):
                indices=[i for i in range(k) if (mask>>i)&1]
                if len(indices)>ell: continue
                pc=sum(p for z,p in zip(states,probabilities) if all(z[i] for i in indices))
                bad=sum(p for z,p in zip(states,probabilities) if all(z[i] for i in indices) and sum(z)<q0*k)
                if pc>=threshold and bad<=eps*pc:
                    found=True
                    break
            assert found
            checked+=1
    assert Fraction(1,32)+Fraction(1,8)+Fraction(1,512)==Fraction(81,512)<Fraction(1,4)
    return {'exact_rational_joint_distributions':checked,'indicator_counts':[2,3,4,5],'support_budget_arithmetic':'81/512 < 1/4','scope':'Finite sampling-lemma instances and constant arithmetic, not the quantum conditioning theorem.'}


def main():
    results={'seed':SEED,'numpy_version':np.__version__,'scope':'Finite algebraic and numerical checks only; not proof verification, a novelty audit, or a Lean build.','thermal_decomposition':thermal_checks(),'four_weight_minimization':interpolation_checks(),'channel_completion':completion_checks(),'tested_set_sampling':sampling_checks(),'passed':True}
    path=Path(__file__).with_name('results.json')
    path.write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(results,indent=2))


if __name__=='__main__':
    main()
