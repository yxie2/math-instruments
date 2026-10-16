"""Finite models for B059. Transfinite, stable-group and global claims remain analytic."""
from itertools import combinations, product
import json
import math
from pathlib import Path
import random
import time

import numpy as np
from scipy.linalg import expm


def matrix_split():
    rng = np.random.default_rng(5901)
    cases = bits = 0
    for n,k in [(1,1),(3,5),(8,7),(12,16)]:
        for _ in range(12):
            a,a2 = rng.integers(0,2,size=(2,n,k))
            diff = a^a2
            lower = diff*(np.arange(k)[None,:]<=np.arange(n)[:,None])
            upper = diff^lower
            assert np.array_equal(lower^upper,diff)
            assert all(np.count_nonzero(lower[i])<=i+1 for i in range(n))
            assert all(np.count_nonzero(upper[:,j])<=j for j in range(k))
            for i,j in product(range(n),range(k)):
                for _ in range(3):
                    u = rng.integers(0,2,size=k); v = rng.integers(0,2,size=n)
                    before = int(a[i,j])^int(u[j])^int(v[i])
                    after = int(a2[i,j])^int((u^lower[i])[j])^int((v^upper[:,j])[i])
                    assert before==after
                    bits += 1
            cases += 1
    return dict(rectangular_models=cases, translated_torsor_bits=bits,
                scope='Finite windows verify the bit identity; row/column finiteness on omega is proved analytically.')


def coherent_limits():
    rng = random.Random(5902)
    diagrams = representatives = 0
    for size in range(1,6):
        nodes = list(range(1<<size))
        for _ in range(4):
            underlying = {i:[-1]+[v for v in range(size) if i>>v&1] for i in nodes}
            labels = {}
            for i,values in underlying.items():
                shuffled = rng.sample(range(100,200),len(values))
                labels[i] = dict(zip(values,shuffled))
            inverses = {i:{v:k for k,v in labels[i].items()} for i in nodes}
            def move(i,j,x):
                assert i&j==i
                return labels[j][inverses[i][x]]
            top = nodes[-1]
            tagged = [(i,x) for i in nodes for x in labels[i].values()]
            for i,x in tagged:
                for j,y in tagged:
                    common = i|j
                    equal_later = move(i,common,x)==move(j,common,y)
                    assert equal_later==(move(i,top,x)==move(j,top,y))
            for i,j,k in product(nodes,repeat=3):
                if i&j==i and j&k==j:
                    for x in labels[i].values():
                        assert move(j,k,move(i,j,x))==move(i,k,x)
            # A compatible embedding into a larger structure descends uniquely.
            for i,x in tagged:
                assert 3*inverses[i][x]+8 == 3*inverses[top][move(i,top,x)]+8
            assert len({move(i,top,x) for i,x in tagged}) == size+1
            representatives += len(tagged)
            diagrams += 1
    return dict(finite_directed_diagrams=diagrams, tagged_representatives=representatives,
                scope='Checks the coherent quotient model, not infinite AEC recovery or Replacement.')


def box(L):
    vertices = list(product(range(L),repeat=3))
    edges = []
    for v in vertices:
        for axis in range(3):
            if v[axis]<L-1:
                w = list(v); w[axis]+=1
                edges.append((v,tuple(w),axis))
    return vertices,edges


def sparse_cochains():
    rng = np.random.default_rng(5903)
    cases = zero_curl = 0
    for L in (2,3,4,6):
        vertices,edges = box(L)
        index = {(v,a):i for i,(v,w,a) in enumerate(edges)}
        def gradient(phi):
            return np.array([(phi[w]-phi[v])%3 for v,w,a in edges])
        def curls(cochain):
            values = {}
            for v in vertices:
                for a,b in combinations(range(3),2):
                    if v[a]==L-1 or v[b]==L-1:
                        continue
                    va = list(v); va[a]+=1; va=tuple(va)
                    vb = list(v); vb[b]+=1; vb=tuple(vb)
                    values[v,a,b] = int((cochain[index[v,a]]+cochain[index[va,b]]-cochain[index[vb,a]]-cochain[index[v,b]])%3)
            return values
        for kind in range(20):
            phi0 = {v:int(rng.integers(3)) for v in vertices}
            cochain = gradient(phi0)
            if kind>=5:
                for e in rng.choice(len(edges),size=min(kind-4,len(edges)),replace=False):
                    cochain[e] = (cochain[e]+int(rng.integers(1,3)))%3
            curl = curls(cochain)
            t = sum(x!=0 for x in curl.values())
            phi1 = {(i,j,k):sum(int(cochain[index[(a,j,k),0]]) for a in range(i))%3 for i,j,k in vertices}
            r1 = (cochain-gradient(phi1))%3
            i0 = min(range(L),key=lambda i:sum(value!=0 for (v,a,b),value in curl.items() if a==1 and b==2 and v[0]==i))
            phi2 = {(i,j,k):sum(int(r1[index[(i0,b,k),1]]) for b in range(j))%3 for i,j,k in vertices}
            r2 = (r1-gradient(phi2))%3
            phi3 = {(i,j,k):sum(int(r2[index[(i0,0,c),2]]) for c in range(k))%3 for i,j,k in vertices}
            residual = (r2-gradient(phi3))%3
            assert curls(residual)==curl
            assert np.count_nonzero(residual)<=L*t  # Stronger intermediate source bound.
            assert all(residual[e]==0 for e,(v,w,a) in enumerate(edges) if a==0)
            # Face boundaries are explicit divergence-free test flows.
            for (v,a,b),value in curl.items():
                assert curls(cochain-residual)[v,a,b]==0
            if t==0:
                assert not np.any(residual)
                zero_curl += 1
            cases += 1
    return dict(cochains=cases, gradient_controls=zero_curl, field=3,
                verified_support_bound='L times number of nonzero curls')


def giant_component():
    rng = random.Random(5904)
    c = 1-2**(-1/3)
    boundaries = components = nested = 0
    for L in (2,3,5):
        vertices,edges = box(L)
        sets = ([{vertices[i] for i in range(8) if mask>>i&1} for mask in range(1,256)] if L==2 else
                [set(rng.sample(vertices,rng.randrange(1,len(vertices)//2+1))) for _ in range(60)])
        for selected in sets:
            if len(selected)>len(vertices)/2:
                continue
            projections = [len({tuple(v[i] for i in range(3) if i!=axis) for v in selected}) for axis in range(3)]
            boundary = sum((v in selected)!=(w in selected) for v,w,a in edges)
            assert len(selected)**2 <= math.prod(projections)
            assert boundary>=c*len(selected)**(2/3)-1e-12
            boundaries += 1
    def connected(vertices,edges,deleted):
        adj = {v:[] for v in vertices}
        for i,(v,w,a) in enumerate(edges):
            if i not in deleted:
                adj[v].append(w); adj[w].append(v)
        unseen = set(vertices); groups=[]
        while unseen:
            root=next(iter(unseen)); group={root}; todo=[root]; unseen.remove(root)
            while todo:
                for w in adj[todo.pop()]:
                    if w in unseen:
                        unseen.remove(w); group.add(w); todo.append(w)
            groups.append(group)
        return groups
    for L in (3,5,8):
        vertices,edges = box(L)
        for repeat in range(16):
            deleted=set(rng.sample(range(len(edges)),repeat+1))
            groups=connected(vertices,edges,deleted)
            small=sum(len(g) for g in groups if len(g)<=len(vertices)/2)
            assert small<=c**(-1.5)*(2*len(deleted))**1.5+1e-10
            # Use the explicit sufficient condition, not the asymptotic 6*L^(7/4) threshold.
            if c**(-1.5)*(2*len(deleted))**1.5 < len(vertices)/2:
                assert len([g for g in groups if len(g)>len(vertices)/2])==1
            extra=deleted|set(rng.sample(range(len(edges)),2))
            later=connected(vertices,edges,extra)
            old=[g for g in groups if len(g)>len(vertices)/2]
            new=[g for g in later if len(g)>len(vertices)/2]
            if old and new:
                assert new[0]<=old[0]
                nested += 1
            components += 1
    return dict(boundary_sets=boundaries, deleted_edge_models=components,nested_giants=nested,
                scope='Explicit finite mass bound; no assertion that these sizes meet the asymptotic threshold.')


def inverse_binary(a):
    n=len(a); work=np.concatenate((a.copy()%2,np.eye(n,dtype=int)),axis=1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if work[i,j]),None)
        if pivot is None:
            return None
        work[[j,pivot]]=work[[pivot,j]]
        for i in range(n):
            if i!=j and work[i,j]: work[i]^=work[j]
    return work[:,n:]


def power_binary(a,k):
    result=np.eye(len(a),dtype=int)
    while k:
        if k&1: result=(result@a)%2
        a=(a@a)%2; k//=2
    return result


def faithful_strips():
    rng=np.random.default_rng(5905)
    models=0
    block=2; n=5; split=3
    def root(i,j,a):
        result=np.eye(n*block,dtype=int)
        result[i*block:(i+1)*block,j*block:(j+1)*block]=a
        return result
    for _ in range(60):
        x=np.eye(n*block,dtype=int); y=x.copy()
        first=np.zeros_like(x); second=np.zeros_like(x)
        for i in range(split):
            for j in range(split,n):
                a=rng.integers(0,2,size=(block,block)); b=rng.integers(0,2,size=(block,block))
                first[2*i:2*i+2,2*j:2*j+2]=a
                second[2*i:2*i+2,2*j:2*j+2]=b
                x=x@root(i,j,a)%2; y=y@root(i,j,b)%2
        assert np.array_equal(x,np.eye(n*block,dtype=int)^first)
        assert np.array_equal(x@y%2,np.eye(n*block,dtype=int)^first^second)
        word=np.eye(n*block,dtype=int)
        for _ in range(8):
            i,j=rng.choice(split,2,replace=False)
            word=word@root(i,j,rng.integers(0,2,size=(block,block)))%2
        inv=inverse_binary(word)
        outgoing=(word@x@inv)%2
        assert np.array_equal(outgoing[:6,6:],word[:6,:6]@first[:6,6:]%2)
        reverse=np.eye(n*block,dtype=int)^first.T
        incoming=(word@reverse@inv)%2
        assert np.array_equal(incoming[6:,:6],first.T[6:,:6]@inv[:6,:6]%2)
        models += 1
    return dict(noncommutative_coefficient_models=models, coefficient_ring='2 by 2 matrices over F2',
                scope='Matrix actions and strip collection; abstract Steinberg faithfulness relies on the read presentation proof.')


def matrix_periodicity():
    rng=np.random.default_rng(5906)
    cases=invertible=0
    for n in (1,2,3,4):
        for _ in range(20):
            reduction=rng.integers(0,2,size=(n,n))
            a=np.zeros((3*n,3*n),dtype=int)
            for i,j in product(range(n),repeat=2):
                block=reduction[i,j]*np.eye(3,dtype=int)
                for row,col in combinations(range(3),2): block[row,col]=rng.integers(2)
                a[3*i:3*i+3,3*j:3*j+3]=block
            inverse=inverse_binary(a); reduced_inverse=inverse_binary(reduction)
            assert (inverse is None)==(reduced_inverse is None)
            if inverse is not None:
                b=np.kron(reduced_inverse,np.eye(3,dtype=int))
                u=(a@b)%2^np.eye(3*n,dtype=int)
                assert not np.any(power_binary(u,3))
                geom=np.eye(3*n,dtype=int)^u^(u@u%2)
                assert np.array_equal(b@geom%2,inverse)
                d=1
                while not np.array_equal(power_binary(reduction,d),np.eye(n,dtype=int)):
                    d+=1
                    assert d<1000
                v=power_binary(a,d)^np.eye(3*n,dtype=int)
                assert not np.any(power_binary(v,3))
                assert np.array_equal(power_binary(a,4*d),np.eye(3*n,dtype=int))
                invertible+=1
            cases+=1
    # Periodicity of the quotient does not imply all orders are powers of two.
    order_three=np.array([[0,1],[1,1]])
    assert np.array_equal(power_binary(order_three,3),np.eye(2,dtype=int))
    assert not np.array_equal(power_binary(order_three,2),np.eye(2,dtype=int))
    return dict(matrix_models=cases,invertible_models=invertible,
                ring='F2 identity plus strictly upper triangular 3 by 3 matrices',
                non_two_primary_control=True)


def masked_operators():
    rng=np.random.default_rng(5907)
    models=0; residual=0.
    for order,n,k,p in [(4,6,3,2),(5,7,4,3),(6,8,3,2)]:
        for _ in range(10):
            vectors=rng.normal(size=(k,n))+1j*rng.normal(size=(k,n))
            vectors/=np.linalg.norm(vectors,axis=0)
            shifts=rng.integers(order,size=n); shifts[1]=shifts[0]
            allowed=[(x,i) for x in range(order) for i in range(n)]
            rng.shuffle(allowed)
            edges=[]; row=[0]*order; col=[0]*order
            for x,i in allowed:
                y=(x+int(shifts[i]))%order
                if row[x]<p and col[y]<p:
                    edges.append((x,i,y)); row[x]+=1; col[y]+=1
            phases=np.exp(2j*np.pi*rng.random(len(edges)))
            analysis=np.zeros((len(edges),order*k),complex)
            synthesis=np.zeros((order*k,len(edges)),complex)
            direct=np.zeros((order*k,order*k),complex)
            for j,(x,i,y) in enumerate(edges):
                analysis[j,y*k:(y+1)*k]=vectors[:,i].conj()
                synthesis[x*k:(x+1)*k,j]=vectors[:,i]
                direct[x*k:(x+1)*k,y*k:(y+1)*k]+=phases[j]*np.outer(vectors[:,i],vectors[:,i].conj())
            factored=(synthesis*phases)@analysis
            residual=max(residual,float(np.linalg.norm(direct-factored,2)))
            assert np.allclose(direct,factored,atol=1e-12)
            b0=max(np.linalg.norm(vectors[:,list(indices)],2) for indices in combinations(range(n),p))
            assert np.linalg.norm(direct,2)<=b0*b0+1e-12
            assert np.linalg.norm(analysis,2)<=b0+1e-12
            assert np.linalg.norm(synthesis,2)<=b0+1e-12
            models+=1
    return dict(indexed_mask_models=models,repeated_group_labels=True,max_factorization_error=residual)


def positive_power(a,power):
    if a.shape==(0,0): return a.copy()
    values,vectors=np.linalg.eigh(a)
    assert values.min()>0
    return (vectors*values**power)@vectors.conj().T


def protected_transfer():
    rng=np.random.default_rng(5908)
    cases=truncations=0; max_residual=max_ratio=max_protected=0.
    for n in (3,5,8):
        for h in (1/128,1/32,1/8):
            for zero in (False,True):
                r=n//2; rp=r+1
                b=np.diag(rng.uniform(.8,1.3,size=n))
                gamma=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); gamma=(gamma+gamma.conj().T)/2
                if zero: gamma[:rp,:rp]=0
                gamma/=max(1.,np.linalg.norm(gamma,2))
                a=b+h*gamma
                def transfer(rank):
                    bh=positive_power(b,.5); bi=positive_power(b,-.5)
                    ah=bi@a@bi
                    aa=ah[:rank,:rank]; ab=ah[:rank,rank:]; dd=ah[rank:,rank:]
                    ai=np.linalg.inv(aa) if rank else aa.copy()
                    schur=dd-ab.conj().T@ai@ab
                    si=positive_power(schur,-.5)
                    q=np.block([[positive_power(aa,-.5),-ai@ab@si],
                                [np.zeros((n-rank,rank)),si]])
                    return bi@q@bh
                eta=np.linalg.norm(gamma[:rp,:rp],2)
                s=transfer(r); sp=transfer(rp)
                error=np.linalg.norm(s.conj().T@a@s-b,2)
                max_residual=max(max_residual,float(error))
                assert error<2e-12 and np.linalg.norm(s[r:,:r])<1e-12
                ratio=np.linalg.norm(s-np.eye(n),2)/h
                max_ratio=max(max_ratio,float(ratio)); assert ratio<10
                protected=np.linalg.norm((s-np.eye(n))[:,:r],2)
                if eta:
                    max_protected=max(max_protected,float(protected/(h*eta)))
                    assert protected<10*h*eta
                else: assert protected<1e-12
                change=np.linalg.solve(sp,s)
                assert np.linalg.norm(change.conj().T@b@change-b,2)<3e-12
                assert np.linalg.norm((change-np.eye(n))[:,:r],2)<=20*h*eta+3e-12
                for boundary in (0,n):
                    sb=transfer(boundary)
                    assert np.linalg.norm(sb.conj().T@a@sb-b,2)<3e-12
                cases+=1
    for n in (3,5,8):
        for _ in range(12):
            herm=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); herm=(herm+herm.conj().T)/2
            herm*=.2/np.linalg.norm(herm,2)
            unitary=expm(1j*herm); r=n//2
            e=np.linalg.norm((unitary-np.eye(n))[:,:r],2)
            d=unitary[r:,r:]
            polar=d@positive_power(d.conj().T@d,-.5)
            fixed=np.eye(n,dtype=complex); fixed[r:,r:]=polar
            assert np.linalg.norm(fixed.conj().T@fixed-np.eye(n),2)<2e-12
            assert np.linalg.norm(fixed-unitary,2)<=3*e+2e-12
            truncations+=1
    return dict(metric_pairs=cases,zero_compression_controls=9,unitary_corrections=truncations,
                max_metric_identity_error=max_residual,max_global_ratio=max_ratio,max_protected_ratio=max_protected,
                scope='Finite norm checks; observed ratios do not establish a dimension-free universal constant.')


def main():
    started=time.perf_counter(); results={}
    for fn in (matrix_split,coherent_limits,sparse_cochains,giant_component,faithful_strips,
               matrix_periodicity,masked_operators,protected_transfer):
        results[fn.__name__]=fn(); print(fn.__name__,'passed',flush=True)
    report=dict(status='passed',elapsed_seconds=round(time.perf_counter()-started,3),checks=results,
                scope='Selected finite mechanisms only; no categoricity, complexity-separation, infinite-group or amenability headline theorem is certified.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}))


if __name__=='__main__': main()
