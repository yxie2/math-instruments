---
id: openai-math-203
record_type: family
title: Integral volume control and principal-unit restriction
source_family: '203'
source_collection: openai/math
batch_id: B056
subject: Algebra
source_paper_ids:
- P-000319
- P-000320
instrument_ids:
- MI-000550
- MI-000551
headline: The manuscripts claim Donovan finiteness over algebraic closures of prime fields and over their
  Witt vector rings.
central_instrument: Bounded integral exterior coordinates control row-space projections even when chosen
  bases grow. Principal-unit unique divisibility makes restriction to a Sylow subgroup injective on that
  part of second cohomology.
novelty_assessment: Cauchy-Binet, integral Plucker coordinates, Hensel lifting and restriction-corestriction
  are classical. Eisele explicitly uses the relevant prime-to-p principal-unit divisibility. The source
  global block-theoretic finiteness arguments are not certified.
formalization_summary: Only the selected manuscript arguments are reviewed. No scope document or Comparator
  is listed for this family in the pinned inventory. No Lean solution was built.
statement_faithfulness: Projection control concerns the subspace and its coordinate restrictions, not
  bounded entries of every chosen integral basis. The cohomology kernel is finite for each finite quotient
  group; no uniform bound over arbitrary groups is asserted.
dependencies: Gram determinants, exterior powers, coordinate singular values, complete local orders, Teichmuller
  units, Hensel lifting and finite-group cohomology.
antecedents: Cauchy-Binet and integral exterior-coordinate finiteness; Eisele Lemma 4.4 for unit-group
  cohomology over complete discrete valuation rings.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Integral volume control and principal-unit restriction

## Source manuscripts and claim

- [Donovan's Conjecture over Algebraically Closed Fields](../papers/P-000319.md): selected passages extracted.
- [Integral Donovan Finiteness over Witt Vectors](../papers/P-000320.md): selected passages extracted.

The manuscripts claim Donovan finiteness over algebraic closures of prime fields and over their Witt vector rings.

## Extracted instruments

- [MI-000550: Bound coordinate inversion by integral exterior volume](../instruments/MI-000550.md)
- [MI-000551: Separate principal units before restricting cohomology to a Sylow subgroup](../instruments/MI-000551.md)

## Dependencies and antecedents

Gram determinants, exterior powers, coordinate singular values, complete local orders, Teichmuller units, Hensel lifting and finite-group cohomology.

Cauchy-Binet and integral exterior-coordinate finiteness; Eisele Lemma 4.4 for unit-group cohomology over complete discrete valuation rings.

## Review and formalization scope

Read the complete row-projection argument and the center-unit and restriction lemmas, including the finite Teichmuller contribution. The later descent, normal-subgroup reductions and full Donovan conclusions remain unaudited.

Only the selected manuscript arguments are reviewed. No scope document or Comparator is listed for this family in the pinned inventory. No Lean solution was built.

Projection control concerns the subspace and its coordinate restrictions, not bounded entries of every chosen integral basis. The cohomology kernel is finite for each finite quotient group; no uniform bound over arbitrary groups is asserted.

[Batch record](../../batches/B056/README.md)
