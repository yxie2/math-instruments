---
id: openai-math-119
record_type: family
title: Scaled binary curvature and bias-sensitive coordinate reduction
source_family: '119'
source_collection: openai/math
batch_id: B049
subject: Theoretical computer science
source_paper_ids:
- P-000273
- P-000274
instrument_ids:
- MI-000494
- MI-000495
headline: The sources claim sharp binary-information contraction and Hellinger contraction for arbitrary
  Boolean output bias.
central_instrument: A two-moment integral representation controls the scaled curvature of binary entropy
  production. Compression and a four-coordinate rearrangement bound reduce Boolean induction to a restricted
  scalar domain.
novelty_assessment: Compression has an explicit ABCJN antecedent. The scalar estimates and coordinate
  envelope are source mechanisms, with no independent claim of historical priority or certification of
  either global contraction theorem.
formalization_summary: The supplied scope and targets address Courtade-Kumar, sharp soft-channel contraction
  and selected entropy production. They do not supply a separate Hellinger companion target. The scope
  document and all linked Comparator definitions and target statements were read. The selected targets
  contain sorry; no solution or Lean project was built.
statement_faithfulness: Binary entropy L-psi and the Hellinger square-root profile are different functions.
  The curvature variable is remaining entropy h; the coordinate envelope requires an increasing Boolean
  function with at least four active coordinates.
dependencies: One-variable differentiation, positive integral representations, covariance monotonicity,
  Jensen; positive cube noise, concavity and the distribution of four independent signs.
antecedents: Classical binary entropy production; Anantharam-Bogdanov-Chakrabarti-Jayram-Nair Proposition
  2 for monotone compression.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Scaled binary curvature and bias-sensitive coordinate reduction

## Source manuscripts and claim

- [Sharp binary-information contraction on the discrete cube](../papers/P-000273.md): selected passages extracted.
- [Hellinger contraction with arbitrary Boolean output bias](../papers/P-000274.md): selected passages extracted.

The sources claim sharp binary-information contraction and Hellinger contraction for arbitrary Boolean output bias.

## Extracted instruments

- [MI-000494: Control binary entropy-production curvature through two moments](../instruments/MI-000494.md)
- [MI-000495: Compress a Boolean function and choose a bias-controlled small coordinate](../instruments/MI-000495.md)

## Dependencies and antecedents

One-variable differentiation, positive integral representations, covariance monotonicity, Jensen; positive cube noise, concavity and the distribution of four independent signs.

Classical binary entropy production; Anantharam-Bogdanov-Chakrabarti-Jayram-Nair Proposition 2 for monotone compression.

## Review and formalization scope

Read the full scalar convexity and scaled-curvature proofs, and the full compression and small-coordinate proofs in the companion. The dimension inductions, finite scalar certificates and continuation arguments establishing global claims were not certified.

The supplied scope and targets address Courtade-Kumar, sharp soft-channel contraction and selected entropy production. They do not supply a separate Hellinger companion target. The scope document and all linked Comparator definitions and target statements were read. The selected targets contain sorry; no solution or Lean project was built.

Binary entropy L-psi and the Hellinger square-root profile are different functions. The curvature variable is remaining entropy h; the coordinate envelope requires an increasing Boolean function with at least four active coordinates.

[Batch record](../../batches/B049/README.md)
