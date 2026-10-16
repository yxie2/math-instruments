# B005: Posterior sampling, spectral approximation and critical comparison

Extraction date: 2026-10-16. This batch adds 3 previously uncatalogued families, 3 source manuscripts and 6 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000142: Finite response bounds extend by limsup to a canonical infinite-volume drift](../../catalog/instruments/MI-000142.md) | 231 |
| [MI-000143: Picard inversion on the full product path space gives a Brownian sampler](../../catalog/instruments/MI-000143.md) | 231 |
| [MI-000144: Weak convergence plus support-edge convergence controls the capped R-transform uniformly](../../catalog/instruments/MI-000144.md) | 234 |
| [MI-000145: Eigenspace symmetry bounds pressure changes caused by spectral multiplicity errors](../../catalog/instruments/MI-000145.md) | 234 |
| [MI-000146: Compatible conditional copies turn innovation uniqueness into measurable recovery](../../catalog/instruments/MI-000146.md) | 236 |
| [MI-000147: Small-field gains and an adaptive path cutoff make a critical Osgood estimate integrable](../../catalog/instruments/MI-000147.md) | 236 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B005.json).

Selection covers infinite-volume posterior sampling, spectral approximation and critical stochastic comparison. Exact source passages and the selected proofs were read. Primary antecedents were retrieved for strongly Rayleigh covariance bounds, Brownian Ising factors, compatible stochastic couplings and invariant spin-glass transforms. Established inputs are credited separately from candidate source-specific formulations; targeted searches do not certify historical priority.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) cover rational weighted-tree and determinantal covariances, finite Picard quadrature, capped-transform approximations and a missing-edge-hypothesis negative control, endpoint eigenspace averaging, conditional-kernel variance, and scalar critical-cutoff estimates. Each group states its limits. No Lean solution was built or kernel-checked.

- Family 231: the forest target is a universal Borel rule on locally finite simple unweighted graphs. The selected review does not establish a coding radius or runtime.
- Family 234: only the two spectral approximation lemmas are selected. The global all-temperature variational formula and cavity argument have not been fully audited.
- Family 236: the Comparator includes the critical threshold and almost-sure equivariance for each fixed automorphism. The manuscript's stronger pointwise spin-map construction is separate. The earlier critical information and weighted path estimates remain inputs to the extracted final comparison.

The common theme is converting local or finite sensitivity estimates into controlled infinite-volume limits, while preserving the hypotheses needed for those limits.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
