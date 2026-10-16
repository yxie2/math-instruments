---
id: openai-math-155
record_type: family
title: Affine propagation and prime-cyclic stacking for tiling constraints
source_family: '155'
source_collection: openai/math
batch_id: B036
subject: Combinatorics
source_paper_ids:
- P-000215
instrument_ids:
- MI-000392
- MI-000393
headline: The source claims a translational tile in dimension three with no fully periodic tiling, together
  with minimality of that dimension.
central_instrument: A clean four-by-four square propagates an affine shadow; a full-difference partition
  stacks several common-complement equations into one tile.
novelty_assessment: Both mechanisms have explicit Greenfeld-Tao antecedents. The prime-cyclic implementation
  and its weaker same-color overlap condition are recorded without a new-priority claim.
formalization_summary: Read PeriodicTilingThree.lean, including lattice unique representation, almost-everywhere
  Euclidean tiling and finite-index periodicity definitions. Its dimension-three/minimality target contains
  sorry. No Lean build.
statement_faithfulness: The affine shadow only prescribes cells where the affine form is nonzero modulo
  p. Stacking decodes a projected complement; it does not require every lifted complement to have constant
  height.
dependencies: Finite-field affine interpolation, a clean-square count, independent random coloring, exact-cover
  fiber counts and finite-index projection.
antecedents: Greenfeld-Tao, Undecidability of translational monotilings, Theorem 4.7 and Lemma 4.8; A
  counterexample to the periodic tiling conjecture, Section 3.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Affine propagation and prime-cyclic stacking for tiling constraints

## Source manuscript and claim

[A translational tile with no fully periodic tiling in dimension three](../papers/P-000215.md), by OpenAI, September 23, 2026.

The source claims a translational tile in dimension three with no fully periodic tiling, together with minimality of that dimension.

## Extracted instruments

- [MI-000392: Propagate an affine shadow from a clean four-by-four square](../instruments/MI-000392.md)
- [MI-000393: Stack common tiling equations using a full-difference cyclic partition](../instruments/MI-000393.md)

## Dependencies and antecedents

Finite-field affine interpolation, a clean-square count, independent random coloring, exact-cover fiber counts and finite-index projection.

Greenfeld-Tao, Undecidability of translational monotilings, Theorem 4.7 and Lemma 4.8; A counterexample to the periodic tiling conjecture, Section 3. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full selected affine-shadow proof and stacking section. Higher p-adic structure, absence of all vertical periods, lattice encoding and Euclidean thickening were not audited.

Read PeriodicTilingThree.lean, including lattice unique representation, almost-everywhere Euclidean tiling and finite-index periodicity definitions. Its dimension-three/minimality target contains sorry. No Lean build.

The affine shadow only prescribes cells where the affine form is nonzero modulo p. Stacking decodes a projected complement; it does not require every lifted complement to have constant height.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/155.md) · [Batch record](../../batches/B036/README.md)
