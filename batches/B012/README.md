# B012: Graph pruning, planar states, folding and infinite-matroid descent

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000196: An augmented matching cover charges rectangular conflict pruning to corner sets](../../catalog/instruments/MI-000196.md) | 173 |
| [MI-000197: Transitive blowups amplify integer subset deficits with bounded block error](../../catalog/instruments/MI-000197.md) | 173 |
| [MI-000198: Planar face imbalance certifies two disjoint incidence states](../../catalog/instruments/MI-000198.md) | 180 |
| [MI-000199: A state bijection fixes directed-cycle boundary weight at three](../../catalog/instruments/MI-000199.md) | 180 |
| [MI-000200: A reciprocal-logarithm potential pays for overlapping recursive pieces](../../catalog/instruments/MI-000200.md) | 181 |
| [MI-000201: Random pair folding makes a simple quotient with a linear collision budget](../../catalog/instruments/MI-000201.md) | 181 |
| [MI-000202: Self-duality converts a mixed packing-covering witness into a full independent cover](../../catalog/instruments/MI-000202.md) | 185 |
| [MI-000203: A local ultrafilter rank interface excludes independent covers on a double ray](../../catalog/instruments/MI-000203.md) | 185 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B012.json).

Selection covers eight mechanisms from four graph and infinite-matroid manuscripts: rank-charged pruning, transitive blowups, disjoint planar states, a matched disk identity, an overlap potential, pair folding, self-dual covering reduction and conditional ordinal descent. The selected source proofs were read, with the preceding local-matroid construction explicitly retained as an unverified input. Five Comparator declarations were compared with their scope documents. Primary antecedents were retrieved for generic matrix rank, second-neighborhood subset reduction, triangulation states, sparse-cut cycle decomposition and infinite-matroid duality. The Ford-Fulkerson attribution follows the source; its publisher page was not retrievable. Targeted searches were not exhaustive priority audits.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups of finite checks. They cover 4,396 augmented pruning graphs, 110,788 blowup subsets, every incidence cut in three even bipyramids, 624 state edge selections, 2,000 split-size triples and 12 full split trees, 12,180 pairing models, 324 self-dual mixed witnesses and 500 finite rank chains. The graph and matroid enumerations use integer or rational arithmetic; the overlap potential uses floating logarithms.

Run `python batches/B012/verification/check_instruments.py` from the repository root; only the Python standard library is required. The run used Python 3.13. The blowup computation checks the unconditional inequality, not the existence of a hypothetical strict-deficit graph. The double-ray computation checks finite orientation and rank bookkeeping, not an infinite matroid or ultrafilter construction.

The complete second-neighborhood contradiction, Hamiltonian construction, graph cycle-decomposition induction and infinite local-matroid construction were not audited. No Lean solution was built, and these checks do not certify the source headline theorems or historical novelty.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
