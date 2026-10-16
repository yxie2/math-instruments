---
id: openai-math-170
record_type: family
title: Occupancy improvements and entropy under arbitrary tuple selection
source_family: '170'
source_collection: openai/math
batch_id: B058
subject: Combinatorics
source_paper_ids:
- P-000337
- P-000338
instrument_ids:
- MI-000568
- MI-000569
headline: The sources claim sharp logarithmic exponents for r(5,t) and for every fixed off-diagonal Ramsey
  parameter s>=6.
central_instrument: Uniform independent-set occupancy gives a logarithmic gain for triangle-free graphs.
  An atom cap protects entropy of a selected subsequence against arbitrary adaptive selection and constant-probability
  restrictions.
novelty_assessment: The occupancy method is classical and credited to Alon. The selected-tuple bound is
  a union-bound/min-entropy argument with a source-specific parameter balance. Neither is evidence for
  the full claimed Ramsey lower bound.
formalization_summary: RamseyFive states eventual lower bounds t^4/log(t)^(3+epsilon), a constant upper
  bound with exponent three and convergence of the logarithmic exponent. SharpLogRamsey has the corresponding
  targets for each fixed s>=6, with a positive upper constant chosen independently of epsilon. Every linked
  Comparator and the scope document were read in full. The headline Comparator proof bodies contain sorry;
  this does not describe the separate solution files. No solution or Lean project was built.
statement_faithfulness: Occupancy permits any real degree bound D>=1. Selected tuples have deterministic
  length, only the two permitted orientations, and a bounded density ratio for the whole stream law; auxiliary
  randomness may depend arbitrarily on the stream.
dependencies: Uniform independent sets, neighborhood conditioning, Jensen inequality, atom bounds, Shannon
  entropy and variational relative entropy.
antecedents: Alon, Independence Numbers of Locally Sparse Graphs and a Ramsey Type Problem; classical
  maximum-atom entropy bounds and exponential variational bounds for KL.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Occupancy improvements and entropy under arbitrary tuple selection

## Source manuscripts and claim

- [The sharp logarithmic exponent of r(5,t)](../papers/P-000337.md): selected passages extracted.
- [Sharp logarithmic exponents for fixed off-diagonal Ramsey numbers](../papers/P-000338.md): selected passages extracted.

The sources claim sharp logarithmic exponents for r(5,t) and for every fixed off-diagonal Ramsey parameter s>=6.

## Extracted instruments

- [MI-000568: Gain a logarithm from uniform independent-set occupancy](../instruments/MI-000568.md)
- [MI-000569: Protect entropy against an arbitrarily biased subsequence selector](../instruments/MI-000569.md)

## Dependencies and antecedents

Uniform independent sets, neighborhood conditioning, Jensen inequality, atom bounds, Shannon entropy and variational relative entropy.

Alon, Independence Numbers of Locally Sparse Graphs and a Ramsey Type Problem; classical maximum-atom entropy bounds and exponential variational bounds for KL.

## Review and formalization scope

Read the complete upper-bound section of the r(5,t) manuscript, selecting its occupancy lemma, and the full selected-tuple entropy and rare-event transfer proofs in the fixed-parameter companion. The geometric construction and recursive compression for lower bounds are not audited.

RamseyFive states eventual lower bounds t^4/log(t)^(3+epsilon), a constant upper bound with exponent three and convergence of the logarithmic exponent. SharpLogRamsey has the corresponding targets for each fixed s>=6, with a positive upper constant chosen independently of epsilon. Every linked Comparator and the scope document were read in full. The headline Comparator proof bodies contain sorry; this does not describe the separate solution files. No solution or Lean project was built.

Occupancy permits any real degree bound D>=1. Selected tuples have deterministic length, only the two permitted orientations, and a bounded density ratio for the whole stream law; auxiliary randomness may depend arbitrarily on the stream.

[Batch record](../../batches/B058/README.md)
