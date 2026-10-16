---
id: openai-math-137
record_type: family
title: Homogeneous lookup and top-coefficient extraction in small space
source_family: '137'
source_collection: openai/math
batch_id: B024
subject: Theoretical computer science
source_paper_ids:
- P-000168
instrument_ids:
- MI-000298
- MI-000299
headline: The source claims soft-O(T^(2/5)) bits to determine the halting outcome of a fixed one-writable-tape
  machine run for a supplied cap T, with fixed read-only heads and a uniform polylog-space initial-symbol
  access procedure.
central_instrument: Homogenize every Boolean lookup block, including constants, then extract its top coefficient
  by finite-field interpolation without factorial division.
novelty_assessment: Multilinear extensions, homogenization and Lagrange interpolation are classical. The
  extraction preserves the precise conventions needed by the source recursive evaluator; it does not certify
  the machine-simulation theorem.
formalization_summary: Read the scope and full OneTapeSpace.lean Comparator. The model includes unit head
  moves, cap-independent initial data, numerical coordinates of magnitude at most T, uncharged read-only
  input and no running-time bound. The selected target concerns outcome, not materializing the final tape.
  These are inspected target statements with sorry placeholders; no Lean solution was built or kernel-checked.
statement_faithfulness: Lookup tables are total Boolean functions. A constant-one Boolean function becomes
  a power of the augmentation coordinate, not the literal field constant. Interpolation requires degree
  strictly below field cardinality, not below characteristic.
dependencies: Homogeneous Boolean basis, finite-field arithmetic, Lagrange interpolation, enumeration
  with reused counters and field accumulators.
antecedents: Classical multilinear extension, projective homogenization and Lagrange leading-coefficient
  formulas; the source connects these with space-efficient tree evaluation.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Homogeneous lookup and top-coefficient extraction in small space

## Source manuscript and claim

[Simulating One-Tape Time in Two-Fifths-Power Space](../papers/P-000168.md), by OpenAI, September 25, 2026.

The source claims soft-O(T^(2/5)) bits to determine the halting outcome of a fixed one-writable-tape machine run for a supplied cap T, with fixed read-only heads and a uniform polylog-space initial-symbol access procedure.

## Extracted instruments

- [MI-000298: Homogenize every lookup block, including the constant table](../instruments/MI-000298.md)
- [MI-000299: Extract the homogeneous term after translation without dividing by factorials](../instruments/MI-000299.md)

## Dependencies and antecedents

Homogeneous Boolean basis, finite-field arithmetic, Lagrange interpolation, enumeration with reused counters and field accumulators.

Classical multilinear extension, projective homogenization and Lagrange leading-coefficient formulas; the source connects these with space-efficient tree evaluation. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the field setup, homogeneous lookup proof and top-coefficient proof. The weighted evaluator, block hierarchy and complete space recurrence were not audited.

Read the scope and full OneTapeSpace.lean Comparator. The model includes unit head moves, cap-independent initial data, numerical coordinates of magnitude at most T, uncharged read-only input and no running-time bound. The selected target concerns outcome, not materializing the final tape. These are inspected target statements with sorry placeholders; no Lean solution was built or kernel-checked.

Lookup tables are total Boolean functions. A constant-one Boolean function becomes a power of the augmentation coordinate, not the literal field constant. Interpolation requires degree strictly below field cardinality, not below characteristic.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/137.md) · [Batch record](../../batches/B024/README.md)
