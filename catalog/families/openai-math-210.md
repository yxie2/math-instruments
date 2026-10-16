---
id: openai-math-210
record_type: family
title: Multiplicity amplification by sumsets and differential cancellation by weight
source_family: '210'
source_collection: openai/math
batch_id: B057
subject: Algebra
source_paper_ids:
- P-000329
- P-000330
instrument_ids:
- MI-000560
- MI-000561
headline: The sources claim Foulkes comparison for the sixth symmetric power in the full range and uniform
  quadratic stabilization of the canonical Foulkes-Howe map.
central_instrument: Distinct leading exponents turn multiplication into a sumset lower bound for multiplicities.
  A Fischer inner product makes a directional derivative injective on an entire positive-weight bihomogeneous
  space.
novelty_assessment: The sumset inequality is explicitly due to Matolcsi-Ruzsa, and the derivative criterion
  is classical sl2 weight injectivity. The source packages them as usable quantitative certificates; neither
  full Foulkes theorem is certified here.
formalization_summary: The actual FoulkesHowe Comparator states existence, uniqueness and surjectivity
  of the map satisfying its explicit averaged formula for a>=2 and b>=a(a-1). Its target proof contains
  sorry. Unlike the scope description, it has no separate a=1, vanishing-on-products or reverse-embedding
  theorem. It covers sixth powers only for b>=30, not the companion full range b>=6. The scope document
  and every linked Comparator were read in full. No solution or Lean project was built.
statement_faithfulness: Power amplification is conditional on an existing multiplicity lower bound. Derivative
  cancellation requires the strict degree inequality before each individual operator, over characteristic
  zero.
dependencies: Leading monomials, affine dimensions, finite sumsets, half-open simplex counts, highest-weight
  products, Fischer norms and sl2 commutators.
antecedents: Matolcsi-Ruzsa Theorem 1.5; Ikenmeyer Claim 5.1 on weight-shift injectivity; Aldaz-Render
  on the apolar inner product.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Multiplicity amplification by sumsets and differential cancellation by weight

## Source manuscripts and claim

- [Foulkes' conjecture for the sixth symmetric power](../papers/P-000329.md): selected passages extracted.
- [Quadratic stabilization of the canonical Foulkes--Howe map](../papers/P-000330.md): selected passages extracted.

The sources claim Foulkes comparison for the sixth symmetric power in the full range and uniform quadratic stabilization of the canonical Foulkes-Howe map.

## Extracted instruments

- [MI-000560: Amplify a highest-weight multiplicity through leading-exponent sumsets](../instruments/MI-000560.md)
- [MI-000561: Cancel directional derivatives using a positive weight difference](../instruments/MI-000561.md)

## Dependencies and antecedents

Leading monomials, affine dimensions, finite sumsets, half-open simplex counts, highest-weight products, Fischer norms and sl2 commutators.

Matolcsi-Ruzsa Theorem 1.5; Ikenmeyer Claim 5.1 on weight-shift injectivity; Aldaz-Render on the apolar inner product.

## Review and formalization scope

Read the full sumset and power-certificate proofs and the complete differential-injectivity proof, including the canonical-image setup. The large-degree vanishing induction and the extensive sixth-power finite certificate computation are not audited.

The actual FoulkesHowe Comparator states existence, uniqueness and surjectivity of the map satisfying its explicit averaged formula for a>=2 and b>=a(a-1). Its target proof contains sorry. Unlike the scope description, it has no separate a=1, vanishing-on-products or reverse-embedding theorem. It covers sixth powers only for b>=30, not the companion full range b>=6. The scope document and every linked Comparator were read in full. No solution or Lean project was built.

Power amplification is conditional on an existing multiplicity lower bound. Derivative cancellation requires the strict degree inequality before each individual operator, over characteristic zero.

[Batch record](../../batches/B057/README.md)
