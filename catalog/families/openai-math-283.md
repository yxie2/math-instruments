---
id: openai-math-283
record_type: family
title: Feedback fields and row-sparse near-isometry encoders
source_family: '283'
source_collection: openai/math
batch_id: B016
subject: Mathematical physics
source_paper_ids:
- P-000137
instrument_ids:
- MI-000234
- MI-000235
headline: The source claims a uniform polynomial-size finite-gate circuit using a target-dependent Boolean
  oracle to approximate any n-qubit unitary in diamond norm by a constant error. The oracle is existential;
  efficient classical construction of its truth table is not asserted.
central_instrument: Unitary feedback gives field maps with telescoping Gram bounds; power-sum phases restrict
  Fourier row support. A programmable-slot encoder then amplifies a row-sparse near-isometry uniformly
  over all singular directions.
novelty_assessment: Unitary transfer functions, Newton identities, multiplexed state preparation and singular-value
  amplification are established. The selected combination of phase coding, Gram bounds and the precise
  slot-model encoder is a candidate reusable interface, without a priority certification.
formalization_summary: No family-specific Lean scope document was listed in the pinned inventory. No Lean
  proof was certified for these extracted tools.
statement_faithfulness: The contraction norm bound for the internal block is an input. A programmable
  slot may contain an arbitrary label-controlled table of two-by-two unitary matrices, so slot count is
  not an ordinary gate count or entry-oracle complexity.
dependencies: Unitary block identities, finite Fourier orthogonality, geometric tails, Newton identities,
  table-controlled state preparation and orthogonal singular-vector planes.
antecedents: Fritzsche-Katsnelson-Kirstein gives the unitary transfer-function framework; Gilyen-Su-Low-Wiebe
  gives state-preparation block encodings and singular-value transformation.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Feedback fields and row-sparse near-isometry encoders

## Source manuscript and claim

[Polynomial-Time Unitary Synthesis from a Boolean Oracle](../papers/P-000137.md), by OpenAI, October 5, 2026.

The source claims a uniform polynomial-size finite-gate circuit using a target-dependent Boolean oracle to approximate any n-qubit unitary in diamond norm by a constant error. The oracle is existential; efficient classical construction of its truth table is not asserted.

## Extracted instruments

- [MI-000234: Feedback fields combine telescoping Gram bounds with power-sum Fourier sparsity](../instruments/MI-000234.md)
- [MI-000235: Row-sparse near-isometries have a uniform programmable-slot encoder](../instruments/MI-000235.md)

## Dependencies and antecedents

Unitary block identities, finite Fourier orthogonality, geometric tails, Newton identities, table-controlled state preparation and orthogonal singular-vector planes.

Fritzsche-Katsnelson-Kirstein gives the unitary transfer-function framework; Gilyen-Su-Low-Wiebe gives state-preparation block encodings and singular-value transformation. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete feedback-field proofs, programmable-slot definition and state-preparation argument, and generic row-sparse encoder proof. The dimension-contraction construction, recursion and finite-gate oracle compilation were not audited.

No family-specific Lean scope document was listed in the pinned inventory. No Lean proof was certified for these extracted tools.

The contraction norm bound for the internal block is an input. A programmable slot may contain an arbitrary label-controlled table of two-by-two unitary matrices, so slot count is not an ordinary gate count or entry-oracle complexity.

[Batch record](../../batches/B016/README.md)
