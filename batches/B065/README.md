# B065: Arithmetic transfer, sign extensions, annular roots and primitive-root reductions

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000622: Transfer an integer density to squarefree squareclasses](../../catalog/instruments/MI-000622.md) | 006 |
| [MI-000623: Upgrade truncated rank tails to uniform integrability](../../catalog/instruments/MI-000623.md) | 006 |
| [MI-000624: Detect splitting of a sign-action lattice extension modulo two](../../catalog/instruments/MI-000624.md) | 018 |
| [MI-000625: Clear rational denominators using local density and a full lattice](../../catalog/instruments/MI-000625.md) | 018 |
| [MI-000626: Place cyclic monodromy on a single cut of a skeleton cycle](../../catalog/instruments/MI-000626.md) | 019 |
| [MI-000627: Reduce tame roots of annular units to a coordinate root](../../catalog/instruments/MI-000627.md) | 019 |
| [MI-000628: Test Kummer splitting by two finite congruences](../../catalog/instruments/MI-000628.md) | 029 |
| [MI-000629: Delete order-index obstructions from a structured prime reservoir](../../catalog/instruments/MI-000629.md) | 029 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B065.json) records hashes, exact labels and manuscript coverage.

Eight instruments from four families and all eight associated manuscripts. Complete selected proofs and conditional reductions were read. Primary passages in Baker-Payne-Rabinoff and Moree were checked. No family in this batch has a Lean scope document in the pinned inventory.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) cover squareclass inversion, truncated tails, sign-action extensions, denominator clearing, graph monodromy, tame binomial roots, Kummer congruences and conditional reservoir deletion.

Analytic rank tails, local group density, skeleton existence and primitive-root counting estimates remain inputs. The graph checks do not certify etale algebraization. No Goldfeld, Margulis-Platonov, section-conjecture or unconditional primitive-root headline is certified. No Lean solution was built. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
