# Quantum decoding and sharp subset bounds

Status: public preprint with proofs and an exact polynomial certificate for a restricted family.

**Ying Xie — [From Quantum Decoding to Sharp Subset Bounds: A Use Case for Extracted Mathematical Instruments](https://zenodo.org/records/23441704)**. Preprint, October 17, 2026. [DOI: 10.5281/zenodo.23441704](https://doi.org/10.5281/zenodo.23441704).

Can decoding errors on smaller signal alphabets certify the error for a full quantum alphabet? This study follows instruments extracted from partial differential equations and differential geometry into quantum state discrimination. It illustrates the research approach of the [direction paper](https://zenodo.org/records/23319145): identify reusable proof mechanisms, adapt them to a new problem, and develop the additional arguments the application requires.

## Extracted inputs

| Instrument | Source and role in the application |
| --- | --- |
| [MI-000329: Retain trace-free structure to obtain sharp five-dimensional contraction constants](../../catalog/instruments/MI-000329.md) | The constrained cubic spectral calculation in [The critical dimension for one-phase Bernoulli minimizers](../../catalog/papers/P-000183.md), specifically `cert:trace-bounds`, suggests the general-dimensional moment argument used for pure-state pairwise decoding. |
| [MI-000787: Certify scalar and matrix polynomial signs by normalized Bernstein coefficients](../../catalog/instruments/MI-000787.md) | The conversion formula in [Zero-Plane Rigidity for Einstein Four-Manifolds](../../catalog/papers/P-000520.md), specifically `lem:bernstein-conversion`, supplies the certificate mechanism used after reducing a restricted four-signal problem to polynomial inequalities. |

Both source passages are pinned to OpenAI repository revision `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. The paper uses catalogue revision `d1f149b7da001f8b0ca409e47582ab1435094fc0`. The instrument records give exact source locations and hashes.

Constrained spectral optimization and Bernstein positivity have classical antecedents. The application re-proves the required spectral argument and explains the positivity criterion; it does not assume the source manuscripts' headline geometric theorems. The general mixed-state bounds require additional Schur-complement and POVM-moment arguments developed in the application.

## Target and adaptation

For positive signal operators $`A_i=p_i\rho_i`$, write $`T=\sum_i\operatorname{tr}A_i`$. Let $`E`$ be the full-alphabet pretty good measurement (PGM) error and $`E_I`$ the unnormalized PGM error on a subset $`I`$, retaining the original signal weights. The comparison uses

```math
B_{N,k}=\binom{N-2}{k-2}^{-1}\sum_{|I|=k}E_I,
\qquad L_{N,k}=\left(1+\sqrt{1-k/N}\right)^2.
```

This is a pair-counting normalization, not the ordinary mean of conditional subset errors. For equally likely normalized signals, $`B_{N,k}=(N-1)\bar r_k/(k-1)`$, where $`\bar r_k`$ is that conditional mean. The paper credits Lee and Lami for this formulation and the regular-simplex lower-bound example. Its target is a matching upper bound, $`E\le L_{N,k}B_{N,k}`$.

The spectral mechanism helps retain dependencies between Gram-matrix moments that separate estimates would lose. Passing to mixtures then requires retaining matrix blocks: the Schur-complement estimate controls square-root compression defects, and the tight-average proof bounds noncommutativity through POVM moments. The second extracted mechanism turns the remaining two-parameter family calculation into a finite exact sign certificate.

## Results and evidence

The preprint supplies the proofs of the following statements in finite dimension.

- **Pure-state pairwise bound (Theorem 3.1).** For every equally likely pure ensemble with $`N\ge2`$, the coefficient $`L_{N,2}=(1+\sqrt{1-2/N})^2`$ is sharp.
- **Mixed states with a tight average (Theorem 5.1).** If $`\sum_iA_i=cP`$ for $`c>0`$ and the common support projection $`P`$, the sharp bound holds for every $`2\le k\le N`$. Individual states may be mixed, have different ranks, and fail to commute. For normalized signals, the average state is maximally mixed on its support.
- **Mixed-state leave-one bound (Corollaries 4.3 and 4.4).** For $`N\ge3`$, the sharp coefficient $`L_{N,N-1}=(1+1/\sqrt N)^2`$ holds when $`E/T\ge1/N`$, with no additional restrictions on priors, ranks, commutativity or dimension. This includes all equally likely ensembles supported in dimension at most $`N-1`$. Sharpness is for the whole stated class, not asserted separately for every smaller fixed dimension.
- **Nearly full subsets without those assumptions (Theorem 7.1).** For arbitrary positive signal operators and $`N/2<k\le N`$, the coefficient $`(1-\sqrt{(N-k)/k})^{-2}`$ is valid. Together with the simplex example, this determines the unrestricted optimum's leading correction as $`1+2\sqrt\delta+O(\delta)`$ when $`\delta=1-k/N\to0`$. The finite-parameter upper coefficient is generally not sharp.

Appendix A proves the sharp four-to-three coefficient $`9/4`$ for a specified two-orbit family and its orthogonal direct sums. The certificate combines Bernstein subdivision with a local Taylor bound and exact arithmetic in $`\mathbb Q(\sqrt3)`$. It handles a boundary zero that is cubic along one incident edge and quadratic along the other. The manuscript's accompanying verification materials replay the certificate and separately compare the analytic formulas with matrix computations. Numerical agreement alone is not the proof of nonnegativity.

Section 6 gives an explicit noisy four-signal qutrit example. It demonstrates a sharper error certificate under the stated assumptions; it does not establish improved channel capacity, sensing precision or implementation cost. The unrestricted sharp mixed-state subset problem remains open, including the general four-to-three case. The paper's comparison with earlier work does not establish exhaustive historical priority.

## What this use case demonstrates

The cross-domain transfer is a transfer of proof mechanisms: a spectral calculation from a free-boundary problem and a polynomial certificate method from geometry become useful in quantum decoding. The mixed-state results also show where the extracted mechanisms cease to suffice and additional mathematics is needed. The study records these dependencies so that readers can distinguish the reused ingredients, the adaptations, the new arguments and the remaining problem.

## Publication and references

- [Application paper and publication metadata on Zenodo](https://zenodo.org/records/23441704).
- [Download the application PDF](https://zenodo.org/api/records/23441704/files/paper.pdf/content).
- [Direction paper: What the Machine Invented](https://zenodo.org/records/23319145).
- [Bernoulli source manuscript and pinned version](../../catalog/papers/P-000183.md).
- [Einstein four-manifold source manuscript and pinned version](../../catalog/papers/P-000520.md).
- [Catalogue assessment and evidence policy](../../methodology/assessment.md).

The Zenodo paper is authored by Ying Xie and released under CC BY 4.0. Its acknowledgment records the author's guidance, independent verification of the mathematical claims, and responsibility for the final manuscript, as well as GPT-6 assistance with exploratory calculations, proof development, code checks and drafting.
