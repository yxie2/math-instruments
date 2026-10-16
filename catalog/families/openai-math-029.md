---
id: openai-math-029
record_type: family
title: Kummer splitting tests and conditional simultaneous primitive roots
source_family: 029
source_collection: openai/math
batch_id: B065
subject: Number theory
source_paper_ids:
- P-000397
- P-000398
instrument_ids:
- MI-000628
- MI-000629
headline: The sources address Artin primitive roots and a conditional simultaneous-prime-base lower bound.
central_instrument: A finite congruence detects splitting in a Kummer field. A reservoir of primes with
  structured p-1 survives deletion of index obstructions under explicit counting inputs.
novelty_assessment: The extracted arguments use classical ingredients. The particular source interfaces
  are recorded without certifying a new headline theorem or earliest priority.
formalization_summary: No Lean scope document or linked Comparator is supplied for this family in the
  pinned inventory. No formal solution was built.
statement_faithfulness: The splitting test excludes primes dividing a q. The simultaneous conclusion remains
  conditional on the reservoir and the uniform small-factor exceptional-set estimate.
dependencies: Finite-field cyclic groups, Frobenius, quadratic reciprocity, product divisibility and finite
  union bounds.
antecedents: Classical Artin-Hooley reduction; Moree, arXiv:math/0412262, section 4, explicitly states
  the Kummer criterion.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Kummer splitting tests and conditional simultaneous primitive roots

## Source manuscripts and claim

- [Primitive roots for every admissible integer base](../papers/P-000397.md): selected passages extracted.
- [Simultaneous primitive roots: a conditional lower bound for prime bases](../papers/P-000398.md): selected passages extracted.

The sources address Artin primitive roots and a conditional simultaneous-prime-base lower bound.

## Extracted instruments

- [MI-000628: Test Kummer splitting by two finite congruences](../instruments/MI-000628.md)
- [MI-000629: Delete order-index obstructions from a structured prime reservoir](../instruments/MI-000629.md)

## Dependencies and antecedents

Finite-field cyclic groups, Frobenius, quadratic reciprocity, product divisibility and finite union bounds.

Classical Artin-Hooley reduction; Moree, arXiv:math/0412262, section 4, explicitly states the Kummer criterion.

## Review and formalization scope

Read the complete splitting-test proof and conditional reduction, including both exceptional-set estimates. Read pages 6-8 of Moree, including the same splitting criterion on page 8. No unconditional primitive-root theorem or analytic counting input is certified.

No Lean scope document or linked Comparator is supplied for this family in the pinned inventory. No formal solution was built.

The splitting test excludes primes dividing a q. The simultaneous conclusion remains conditional on the reservoir and the uniform small-factor exceptional-set estimate.

[Batch record](../../batches/B065/README.md)
