# B039: Filtrations, coefficient algebras and cyclic descent

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000416: Recover a Lefschetz filtration from a common lowering operator](../../catalog/instruments/MI-000416.md) | 043 |
| [MI-000417: Detect hard Lefschetz in nonzero tensor factors](../../catalog/instruments/MI-000417.md) | 043 |
| [MI-000418: Prove a cut-polynomial quotient is finite by selecting a nonzero level set](../../catalog/instruments/MI-000418.md) | 044 |
| [MI-000419: Lift a graded special-fiber isomorphism using target flatness](../../catalog/instruments/MI-000419.md) | 044 |
| [MI-000420: Retain extra tensor-category morphisms in a coefficient algebra](../../catalog/instruments/MI-000420.md) | 053 |
| [MI-000421: Detect polynomial tensors by finitely many scalar evaluations without discarding coefficients](../../catalog/instruments/MI-000421.md) | 053 |
| [MI-000422: Detect an exact Jacobian-algebra length by one finite rank condition](../../catalog/instruments/MI-000422.md) | 064 |
| [MI-000423: Remove cyclic base change by a continuous seam correction](../../catalog/instruments/MI-000423.md) | 064 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B039.json).

Eight selected algebraic and topological interfaces with exact labels. Complete selected proofs read; targeted primary comparisons for Lefschetz filtrations, cocircuit ideals and coefficient-algebra reconstruction. Global source headline proofs were not audited.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups: exact Lefschetz strings and tensor ranks, thirty cut ideals, graded-flat lifting controls, coefficient-algebra and interpolation models, truncated Jacobian lengths, and 312 cyclic seam models.

The coefficient-algebra tests are exterior-algebra toys, not Sp representations or Chow computations. The descent tests use linear spaces, not Milnor tubes. None certifies P=W, Hikita, the Chow counterexample or mu-constant topological triviality. These four families have no listed formalization scope. No Lean build. Immutable import edition unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
