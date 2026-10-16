# B018: Operator algebra: retained structure in derivations, spectra and entropy

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 9 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000246: A positive triangular metric gives an explicit rectangular derivation implementer](../../catalog/instruments/MI-000246.md) | 288 |
| [MI-000247: Cyclic column factorization upgrades derivation bounds without descending through a kernel](../../catalog/instruments/MI-000247.md) | 288 |
| [MI-000248: Reduced density operators remove arbitrary unitaries from a tensor spectral bound](../../catalog/instruments/MI-000248.md) | 292 |
| [MI-000249: A norm ultraproduct preserves spectral minima with unbounded representation dimensions](../../catalog/instruments/MI-000249.md) | 292 |
| [MI-000250: Finite predecessor families force every irreducible class to be periodic](../../catalog/instruments/MI-000250.md) | 292 |
| [MI-000251: Persistent correlations at proper subspaces force a dense G_delta generation locus](../../catalog/instruments/MI-000251.md) | 296 |
| [MI-000252: Separated spectra encode four self-adjoint generators into two after amplification](../../catalog/instruments/MI-000252.md) | 296 |
| [MI-000253: Retaining one ensemble transfers matrix entropy production to free Fisher information](../../catalog/instruments/MI-000253.md) | 298 |
| [MI-000254: A persistent block event yields a Gaussian-relative entropy deficit](../../catalog/instruments/MI-000254.md) | 298 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B018.json).

This batch extracts nine mechanisms from four operator-algebra families. Selected proofs and six Comparator targets were read. Primary texts of Ozawa, Dickson and Jekel-Pi were retrieved for direct antecedent comparison; other antecedents explicitly credited by the manuscripts are identified as such. The extraction distinguishes established component methods from candidate combinations and does not certify historical novelty or the global source claims.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) give nine check groups: triangular metrics; cyclic columns and nonfaithful lifts; positive square roots and partial traces; varying matrix dimensions; finite representation predecessors; conditional Baire-generation margins; spectral matrix encoding; retained-ensemble entropy production; and structural-event entropy bounds.

- Family 288: rectangular metric identities and cyclic factorization were checked. The finite-factor and global similarity arguments were not audited. A derivation need not annihilate the domain representation kernel.
- Family 292: finite checks cannot realize a nonzero representation with no finite-dimensional subrepresentations. The finite gap checks explicitly subtract invariant Hilbert-Schmidt components. Norm ultraproducts and the nuclear nonembedding theorem are not computationally certified.
- Family 296: the Baire conclusion is conditional on a persistent-correlation perturbation, whose difficult construction was not audited. The elementary four-to-two encoding does not itself solve the generator problem.
- Family 298: the same matrix law is retained throughout the entropy comparison. The matrix/free limiting inputs, free cumulant estimates and limiting tuple construction were not certified. The finite rare-event calculations do not prove the full entropy-separation theorem.

Six Comparator targets were inspected; no Lean solution was built or kernel-checked. The original fixed import edition remains unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
