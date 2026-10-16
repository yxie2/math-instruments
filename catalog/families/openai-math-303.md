---
id: openai-math-303
record_type: family
title: Cutoff transport and finite-stage ideal membership
source_family: '303'
source_collection: openai/math
batch_id: B041
subject: Operator algebras
source_paper_ids:
- P-000235
instrument_ids:
- MI-000432
- MI-000433
headline: The source claims that individual proper infiniteness implies strong pure infiniteness, and
  removes fixed amplification under exactness.
central_instrument: A cutoff permits a common partial-isometry transport that preserves all represented
  matrix norms. Functional calculus turns approximation by an ideal into exact membership of a spectral
  cut.
novelty_assessment: These selected Cuntz-comparison and ideal-cutoff mechanisms are classical. The source
  explicit rectangular and representation bookkeeping is useful without certifying its stronger headline.
formalization_summary: Read the scope and selected target/definition sections of ExactInfiniteness.lean
  and IndividualStrongInfiniteness.lean. The displayed main targets contain sorry. The latter stabilization
  implementation was not audited. No Lean build.
statement_faithfulness: The transporting partial isometry is only in the bidual; its products with the
  cut hereditary algebra lie in the algebra. Finite matrix tests do not model nonzero properly infinite
  elements.
dependencies: Cuntz subequivalence, hereditary subalgebras, rectangular polar decomposition, functional
  calculus and quotient representations.
antecedents: Rordam comparison lemma, as recalled by Antoine-Perera-Thiel; standard ideal/representation
  separation.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Cutoff transport and finite-stage ideal membership

## Source manuscript and claim

[Weak pure infiniteness and O-infinity absorption](../papers/P-000235.md), by OpenAI, None.

The source claims that individual proper infiniteness implies strong pure infiniteness, and removes fixed amplification under exactness.

## Extracted instruments

- [MI-000432: Transport a cut hereditary algebra while preserving every represented matrix norm](../instruments/MI-000432.md)
- [MI-000433: Turn ideal approximation into exact membership after a spectral cutoff](../instruments/MI-000433.md)

## Dependencies and antecedents

Cuntz subequivalence, hereditary subalgebras, rectangular polar decomposition, functional calculus and quotient representations.

Rordam comparison lemma, as recalled by Antoine-Perera-Thiel; standard ideal/representation separation. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete cutoff-transport, exact-cut implementation and ideals/cutoffs proofs. The separation, uniform-gap and pure-infiniteness arguments were not audited.

Read the scope and selected target/definition sections of ExactInfiniteness.lean and IndividualStrongInfiniteness.lean. The displayed main targets contain sorry. The latter stabilization implementation was not audited. No Lean build.

The transporting partial isometry is only in the bidual; its products with the cut hereditary algebra lie in the algebra. Finite matrix tests do not model nonzero properly infinite elements.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/303.md) · [Batch record](../../batches/B041/README.md)
