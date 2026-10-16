# B007: Adaptive comparisons, algebraic counts and sieve probabilities

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000154: A small column sample approximates a cut using total squared mass](../../catalog/instruments/MI-000154.md) | 012 |
| [MI-000155: A common degree event transfers single-site tests to adaptive cut norms](../../catalog/instruments/MI-000155.md) | 012 |
| [MI-000156: A weighted affine family has small norm on mean-zero functions](../../catalog/instruments/MI-000156.md) | 013 |
| [MI-000157: Overlap components give an entropy bound for bad block arrangements](../../catalog/instruments/MI-000157.md) | 013 |
| [MI-000158: A monotone rank record controls bad primes chosen adaptively](../../catalog/instruments/MI-000158.md) | 020 |
| [MI-000159: Selected coordinate pairs give a uniform weighted Hilbert coefficient](../../catalog/instruments/MI-000159.md) | 020 |
| [MI-000160: Derivative weights turn harmonic sieve paths into a probability process](../../catalog/instruments/MI-000160.md) | 021 |
| [MI-000161: Random forbidden classes have a second moment stable under measure changes](../../catalog/instruments/MI-000161.md) | 021 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B007.json).

Selection covers four number-theory manuscripts through their reusable auxiliary arguments: adaptive cut sampling, finite-field affine mixing, overlap counting, adaptive prime deletion, weighted Hilbert functions, probability normalization of sieve paths and stable second moments. The selected statements and proofs were read, and all six associated Comparator challenge files were compared with the formalization scope documents. Primary sources were retrieved for cut sampling, bounded differences, group-action mixing, determinant methods and sieve antecedents. Targeted novelty searches support cautious comparisons, not exhaustive priority certification.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups of finite checks: exhaustive small cut samples; conditional product-space means and Lipschitz extensions; affine matrices and Fourier-Mellin identities; complete small block permutations; exact subset-deletion averages; rational extracted-equation examples and Hilbert-series coefficients; finite sieve-path likelihoods; and exact forbidden-class means, pair probabilities and variances. A negative control shows that equal records must preserve adaptive data for the deletion argument to work.

The cards state which formulas are explicit abstractions of the source arguments. They preserve the distinction between conditional and integrated moments, fixed and adaptive tests, fixed-depth and growing-depth limits, and finite likelihood identities versus infinite-path theorems.

The release's Comparator declarations concern the four headline results, not these auxiliary lemmas. No Lean solution was built. This batch does not independently certify the joint Dickman law, inverse Goldbach conclusion, power-free polynomial theorem or improved Jacobsthal bound. Substantial arithmetic, geometric and limiting arguments remain outside the selected review.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
