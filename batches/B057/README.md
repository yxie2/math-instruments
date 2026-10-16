# B057: Lattice insertions, trace reductions and algebraic detectors

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000554: Compress invariant cosets with three-cycle differences](../../catalog/instruments/MI-000554.md) | 206 |
| [MI-000555: Insert lattice witnesses while preserving old operations and fences](../../catalog/instruments/MI-000555.md) | 206 |
| [MI-000556: Repair an idempotent in an exponential weight while preserving every class trace](../../catalog/instruments/MI-000556.md) | 207 |
| [MI-000557: Cancel lift dependence in a Pfaffian deletion cocycle](../../catalog/instruments/MI-000557.md) | 207 |
| [MI-000558: Test mixed commuting squares before asserting a block projection is a functor](../../catalog/instruments/MI-000558.md) | 209 |
| [MI-000559: Combine an Artin-Schreier residue barrier with a distinguished uniformizer norm](../../catalog/instruments/MI-000559.md) | 209 |
| [MI-000560: Amplify a highest-weight multiplicity through leading-exponent sumsets](../../catalog/instruments/MI-000560.md) | 210 |
| [MI-000561: Cancel directional derivatives using a positive weight difference](../../catalog/instruments/MI-000561.md) | 210 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B057.json) records hashes, exact labels and manuscript coverage.

Eight instruments from four families and all eight associated manuscripts. Complete selected arguments were read, with direct primary comparisons to Blackadar, Mochizuki version 8, Matolcsi-Ruzsa, Ikenmeyer and Aldaz-Render. All three available scope documents and all four linked Comparators were read in full.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups: nonabelian coordinate compression, private lattice insertion, weighted idempotent repair, Pfaffian descent, mixed-square naturality, residue and norm data, sumset amplification and differential injectivity.

The strict-functor obstruction is checked against the cited earlier definitions and does not by itself refute the intended vanishing theorem. No higher K-theory class is computed. The actual formal targets are narrower than some scope descriptions: the Bass targets concern finite-support group rings, and the Foulkes target contains only the a>=2 quadratic range with its defining map formula. No Lean solution was built and no source headline theorem is certified. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
