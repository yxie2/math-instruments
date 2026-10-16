# B067: Height projections, norm descent, Hodge gaps and Cartier curvature

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000638: Transfer a polynomial generalized inverse to canonical height spaces](../../catalog/instruments/MI-000638.md) | 016 |
| [MI-000639: Force a full torsion graph from two polarization multipliers](../../catalog/instruments/MI-000639.md) | 016 |
| [MI-000640: Preserve Iitaka dimension by integral finite pullback of section rings](../../catalog/instruments/MI-000640.md) | 033 |
| [MI-000641: Descend a globally generated power through the finite Stein norm](../../catalog/instruments/MI-000641.md) | 033 |
| [MI-000642: Use harmonic-exact orthogonality to force a Hodge norm growth gap](../../catalog/instruments/MI-000642.md) | 034 |
| [MI-000643: Track geometric component counts through the constant field](../../catalog/instruments/MI-000643.md) | 034 |
| [MI-000644: Detect numerical triviality from one ample intersection for a nef surface class](../../catalog/instruments/MI-000644.md) | 035 |
| [MI-000645: Compute rank-one p-curvature by cyclic orbits of set partitions](../../catalog/instruments/MI-000645.md) | 035 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B067.json) records hashes, exact labels and manuscript coverage.

Eight instruments from four families and eight selected manuscripts. Seventeen companion manuscripts remain explicitly inventory-only. Complete selected source proofs, the one scope document and its Comparator were read. Primary comparisons include Milne Rosati definitions, Stacks norms, and Katz section 5.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) check polynomial inverses, torsion graphs, section norms, hyperplane avoidance, Hodge deficits, constant-field degrees, nef intersection models and rank-one p-curvature.

Finite models do not certify geometric realizations, global period arguments, Zilber-Pink, Iitaka subadditivity, uniform indices or abundance. The explicit Hodge-gap constant has not received an exhaustive novelty review. No Lean solution was built. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
