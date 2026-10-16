---
id: openai-math-247
record_type: family
title: Faithful Steinberg strips and nil-ideal matrix periodicity
source_family: '247'
source_collection: openai/math
batch_id: B059
subject: Group theory
source_paper_ids:
- P-000343
- P-000344
instrument_ids:
- MI-000574
- MI-000575
headline: The sources claim an infinite finitely presented residually finite 2-group and an infinite finitely
  presented periodic group built from a finitely presented matrix-nil algebra.
central_instrument: Disjoint-coordinate strips are read faithfully by elementary matrices, allowing stable
  kernel centrality. Matrix-nil ideals permit finite geometric inverses and elementwise periodicity after
  reduction to F2.
novelty_assessment: The Steinberg-strip/centrality argument is classical and appears in Weibel. Nilpotent
  geometric inversion and characteristic-two powering are also classical. The difficult algebra construction
  and fixed-rank kernel detection are not certified.
formalization_summary: PeriodicGroup defines the Steinberg presentation and asserts an infinite finitely
  presented periodic Steinberg group in rank 12 over an F2-algebra, together with an abstract Burnside
  witness. It does not state residual finiteness, a 2-group conclusion or the nil-algebra theorem, despite
  the broader inventory family title. The scope document and all linked Comparators were read in full.
  Their headline targets have sorry proof bodies; some supporting definitions contain explicit proofs.
  No separate solution or Lean project was built.
statement_faithfulness: Faithfulness is asserted for the strip subgroup, not the full Steinberg matrix
  map. Matrix periodicity assumes every matrix over the ideal is nilpotent; nilpotence of individual ideal
  elements alone is insufficient. No common exponent or 2-primary order conclusion follows.
dependencies: Steinberg relations, disjoint root supports, noncommutative matrix multiplication, matrix-nil
  ideals and finite quotient orders.
antecedents: Weibel, The K-book, Chapter III, Definitions 5.1-5.2 and Theorem 5.2.1; elementary geometric
  series and Frobenius powering of one matrix.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Faithful Steinberg strips and nil-ideal matrix periodicity

## Source manuscripts and claim

- [An infinite finitely presented residually finite 2-group](../papers/P-000343.md): selected passages extracted.
- [An infinite finitely presented periodic group](../papers/P-000344.md): selected passages extracted.

The sources claim an infinite finitely presented residually finite 2-group and an infinite finitely presented periodic group built from a finitely presented matrix-nil algebra.

## Extracted instruments

- [MI-000574: Use faithful disjoint strips to justify stable group identities](../instruments/MI-000574.md)
- [MI-000575: Lift inverses and elementwise finite orders through a matrix-nil ideal](../instruments/MI-000575.md)

## Dependencies and antecedents

Steinberg relations, disjoint root supports, noncommutative matrix multiplication, matrix-nil ideals and finite quotient orders.

Weibel, The K-book, Chapter III, Definitions 5.1-5.2 and Theorem 5.2.1; elementary geometric series and Frobenius powering of one matrix.

## Review and formalization scope

Read the full Steinberg strips section in the residual-finiteness manuscript and the entire matrix-periodicity proof in its companion. The finite algebra presentation, cancellation hierarchy, fixed-rank stability and residual detection are not audited.

PeriodicGroup defines the Steinberg presentation and asserts an infinite finitely presented periodic Steinberg group in rank 12 over an F2-algebra, together with an abstract Burnside witness. It does not state residual finiteness, a 2-group conclusion or the nil-algebra theorem, despite the broader inventory family title. The scope document and all linked Comparators were read in full. Their headline targets have sorry proof bodies; some supporting definitions contain explicit proofs. No separate solution or Lean project was built.

Faithfulness is asserted for the strip subgroup, not the full Steinberg matrix map. Matrix periodicity assumes every matrix over the ideal is nilpotent; nilpotence of individual ideal elements alone is insufficient. No common exponent or 2-primary order conclusion follows.

[Batch record](../../batches/B059/README.md)
