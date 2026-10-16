# B019: Algebra: derived structure, formal equations and filtered positions

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000255: Vanishing normalized lengths pass through noninjective directed limits](../../catalog/instruments/MI-000255.md) | 194 |
| [MI-000256: A finite flat product map realizes prescribed cohomological roots over every base ring](../../catalog/instruments/MI-000256.md) | 194 |
| [MI-000257: Twisted central-idempotent selection reads a prescribed extinction time](../../catalog/instruments/MI-000257.md) | 198 |
| [MI-000258: Derived tensor survival appears as separate bar summands in a square-zero extension](../../catalog/instruments/MI-000258.md) | 198 |
| [MI-000259: Two vanishing couplings remove a simple resolvent pole and permit a fixed complement](../../catalog/instruments/MI-000259.md) | 201 |
| [MI-000260: Fixed-root Schur equations are equivalent to a polynomial identity over truncated free coefficients](../../catalog/instruments/MI-000260.md) | 201 |
| [MI-000261: Nested filtration profiles determine the generic intersection exactly](../../catalog/instruments/MI-000261.md) | 204 |
| [MI-000262: A nilpotent centralizer realizes every allowed motion of its kernel filtration](../../catalog/instruments/MI-000262.md) | 204 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B019.json).

This batch selects four algebra families and extracts eight finite or conditional mechanisms. Selected proofs were read in full, with primary comparisons to normalized-length theory, Eisenbud-Schreyer root bundles, Minamoto-Yamaura trivial-extension formulas and Fresse centralizer actions. Three Comparator targets were inspected. Established mechanisms are credited; targeted comparisons do not establish novelty of the source headline theorems.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) give eight check groups: normalized finite root towers and noninjective colimits; Cech cohomology and prescribed roots; twisted character selection; derived bar blocks; annihilated resolvent poles; Schur equations in truncated free algebras; nested-profile matching; and Jordan centralizer lifts.

- Family 194: common annihilators and zero normalized length are retained explicitly. The uniform complex estimate and full Lech theorem were not audited. Its formalization target is only the supporting positive-characteristic complete-domain Dutta comparison.
- Family 198: the nonflat bar example detects higher Tor that ordinary tensors miss. Its base has infinite global dimension, so it tests the bar formula only. The fixed finite-presentation, lifting and simulation inputs to the claimed counterexample were not audited.
- Family 201: both vanishing couplings and distinct central roots are essential. Tests retain noncommutative word order. The division-ring construction and descent to its actual center were not audited.
- Family 204: filtered generic positions and commuting lifts were checked. Separate kernel and dual-kernel surjectivity is not asserted to give arbitrary simultaneous prescribed motions. The saturation theorem and schedule construction were not audited.

Three Comparator targets were inspected; no Lean solution was built or kernel-checked. Two families have no scope document in the pinned inventory. The original fixed import edition remains unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
