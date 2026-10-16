---
id: openai-math-329
record_type: family
title: Partition-label compression and polar covering conversion
source_family: '329'
source_collection: openai/math
batch_id: B009
subject: Functional analysis
source_paper_ids:
- P-000108
instrument_ids:
- MI-000172
- MI-000173
headline: The source claims counterexamples to every dimension-free pair of constants in metric-entropy
  duality, with one body a cube and the other full dimensional.
central_instrument: Logarithmic distance profiles tolerate a fixed enlargement of graph balls. Greedy
  pivots can then be encoded by partition labels rather than original centers; a support-function identity
  transfers this compression to a polar cover.
novelty_assessment: Polarity, covering-packing comparisons and convex-hull approximation are classical.
  The partition-label encoding is the selected candidate source-specific mechanism. The finite-field separation
  construction and global counterexample are not independently certified.
formalization_summary: MetricEntropyDuality.lean asserts, for every real a,b>=1, a positive finite dimension
  and symmetric convex body K violating the proposed upper entropy bound, with explicit finite-cover existence
  and ambient translation centers. The additional limiting-ratio statement mentioned in the scope is not
  a separate Comparator declaration. The family scope and Comparator declarations were compared. No Lean
  solution was built or kernel-checked; the auxiliary cards are not separate Comparator targets.
statement_faithfulness: Ordinary covering numbers are distinct from convexified packing. Dimension is
  allowed to grow with the proposed constants. Approximation-list functions need not lie in the column
  hull, so selecting actual coefficient representatives incurs a factor two.
dependencies: Partition graph distances, including disconnected components; common-index averaging; bounded
  greedy pivot lists; logarithmic radius dilation; grouped weight rounding; positive/negative coefficient
  splitting; full-dimensional cube thickening.
antecedents: Artstein-Milman-Szarek prove entropy duality for an ellipsoid, and Artstein-Milman-Szarek-Tomczak-Jaegermann
  prove convexified-packing duality. These results do not assert the unrestricted ordinary-covering comparison
  addressed by the source.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Partition-label compression and polar covering conversion

## Source manuscript and claim

[Counterexamples to the duality conjecture for metric entropy](../papers/P-000108.md), by OpenAI, September 24, 2026.

The source claims counterexamples to every dimension-free pair of constants in metric-entropy duality, with one body a cube and the other full dimensional.

## Extracted instruments

- [MI-000172: Partition labels compress logarithmic distance profiles independently of center count](../instruments/MI-000172.md)
- [MI-000173: A row support function converts column compression into a polar cover](../instruments/MI-000173.md)

## Dependencies and antecedents

Partition graph distances, including disconnected components; common-index averaging; bounded greedy pivot lists; logarithmic radius dilation; grouped weight rounding; positive/negative coefficient splitting; full-dimensional cube thickening.

Artstein-Milman-Szarek prove entropy duality for an ellipsoid, and Artstein-Milman-Szarek-Tomczak-Jaegermann prove convexified-packing duality. These results do not assert the unrestricted ordinary-covering comparison addressed by the source. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the entire partition compression and matrix-to-body proofs. The symmetric finite-field form construction, its simultaneous nonvanishing argument and the final parameter hierarchy were not fully audited.

MetricEntropyDuality.lean asserts, for every real a,b>=1, a positive finite dimension and symmetric convex body K violating the proposed upper entropy bound, with explicit finite-cover existence and ambient translation centers. The additional limiting-ratio statement mentioned in the scope is not a separate Comparator declaration. The family scope and Comparator declarations were compared. No Lean solution was built or kernel-checked; the auxiliary cards are not separate Comparator targets.

Ordinary covering numbers are distinct from convexified packing. Dimension is allowed to grow with the proposed constants. Approximation-list functions need not lie in the column hull, so selecting actual coefficient representatives incurs a factor two.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/329.md) · [Batch record](../../batches/B009/README.md)
