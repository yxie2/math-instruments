# B024: Finite algebra and conditional sampling mechanisms

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000296: Order positive degree discrepancies first to expose a rank bottleneck](../../catalog/instruments/MI-000296.md) | 135 |
| [MI-000297: Uniform weak compositions are dominated in the nonnegative factorial basis](../../catalog/instruments/MI-000297.md) | 135 |
| [MI-000298: Homogenize every lookup block, including the constant table](../../catalog/instruments/MI-000298.md) | 137 |
| [MI-000299: Extract the homogeneous term after translation without dividing by factorials](../../catalog/instruments/MI-000299.md) | 137 |
| [MI-000300: Absorb Gaussian center noise while preserving physical oracle queries](../../catalog/instruments/MI-000300.md) | 139 |
| [MI-000301: A weighted-divergence kernel gives a stationary flow with an exact mean shift](../../catalog/instruments/MI-000301.md) | 139 |
| [MI-000302: Extract a multivariate coefficient by averaging over nonzero field elements](../../catalog/instruments/MI-000302.md) | 141 |
| [MI-000303: Recover an integer sign from the first escape of a rounded CRT phase](../../catalog/instruments/MI-000303.md) | 141 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B024.json).

Eight instruments are extracted from four complexity and sampling families. Selected proofs were read in full. Primary comparisons include degree-residue lower bounds, skew-symmetric invariant dynamics, Stein kernels and approximate CRT sign determination. Three Comparator targets were inspected. These are targeted comparisons, not novelty or full-proof certification.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) give eight check groups.

- Family 135: 36 exact polynomial models over three characteristics, 108 bidegree factorizations, 675 composition moments and 252 lower comparisons. The IMM trace lower bound and asymptotic circuit argument remain unaudited.
- Family 137: 94 Boolean agreements, 300 block-homogeneity identities, 300 zero-augmentation controls, 225 univariate interpolations and 120 translated homogeneous examples over F_16. No recursive evaluator or machine simulation is implemented.
- Family 139: 105 physical-query translation models and 36 nonsymmetric Gaussian flows. Unmodified seed covariance and omitted transposes fail the intended conclusions. Kernel estimates, the adaptive compiler and oracle lower bound remain unaudited. An ideal stationary flow is not by itself an implementable sampler.
- Family 141: 96 coefficient filters and 1,675 exact residue-only sign tests, up to 125-bit integers. Degree aliasing and a violated modulus-size guarantee give explicit failure controls. The prime budget, counting-hierarchy closure and real-algebraic reductions are not certified by these tests.

The three Comparator files contain inspected target statements; no Lean solution was built. Family 141 has no listed family-specific scope document. The immutable import edition is unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
