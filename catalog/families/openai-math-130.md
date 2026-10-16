---
id: openai-math-130
record_type: family
title: Borrowed-coordinate replay and finite tensor amplification
source_family: '130'
source_collection: openai/math
batch_id: B050
subject: Theoretical computer science
source_paper_ids:
- P-000281
- P-000282
instrument_ids:
- MI-000502
- MI-000503
headline: The sources claim unrestricted exact Fourier circuits and a uniform all-length power saving
  over n log n.
central_instrument: Two reversible sweeps cancel arbitrary auxiliary contents. Dimension-weighted tensor
  sectors turn a strict finite call saving into a binomial recurrence with sublinear tensor-order exponent.
novelty_assessment: Transparent computation and Kronecker-power amplification have explicit antecedents.
  The selected linear replay and conditional recurrence are checked; no source finite-win existence or
  Fourier breakthrough is certified.
formalization_summary: The targets distinguish subsequential unrestricted complex scalar circuits from
  uniform all-length exact arithmetic programs including scalar preparation. They do not claim bounded
  coefficients, numerical conditioning or bit complexity; the synthesis appendix is excluded. The scope
  document and all linked Comparator definitions and targets were read. Their main target proofs contain
  sorry; no solution or Lean project was built.
statement_faithfulness: Workspace can start arbitrarily but must be disjoint from inputs and targets.
  Tensor amplification is conditional on an actual fixed finite winning word; numerical recurrence parameters
  do not supply one.
dependencies: Linear DAGs with bounded fan-in and fan-out, reversible shears and edge coloring; exact
  tensor/direct-sum identities, scalar gate accounting and concavity.
antecedents: Bennett uncomputation and Buhrman-Cleve-Koucky-Loff-Speelman transparent computation; related
  Kronecker-power circuit work by Alman-Li in a different circuit model.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Borrowed-coordinate replay and finite tensor amplification

## Source manuscripts and claim

- [An explicit power saving for the exact discrete Fourier transform](../papers/P-000281.md): selected passages extracted.
- [Finite tensor savings and exact Fourier circuits](../papers/P-000282.md): selected passages extracted.

The sources claim unrestricted exact Fourier circuits and a uniform all-length power saving over n log n.

## Extracted instruments

- [MI-000502: Replay a linear DAG twice to restore arbitrary borrowed memory](../instruments/MI-000502.md)
- [MI-000503: Amplify a finite tensor saving by weighting sectors by dimension](../instruments/MI-000503.md)

## Dependencies and antecedents

Linear DAGs with bounded fan-in and fan-out, reversible shears and edge coloring; exact tensor/direct-sum identities, scalar gate accounting and concavity.

Bennett uncomputation and Buhrman-Cleve-Koucky-Loff-Speelman transparent computation; related Kronecker-power circuit work by Alman-Li in a different circuit model.

## Review and formalization scope

Read the complete replay proof, finite-win definition and tensor-amplification proof. Also read the Newton factorization for context. The finite-win existence, exact-width compiler and global Fourier algorithms remain unverified.

The targets distinguish subsequential unrestricted complex scalar circuits from uniform all-length exact arithmetic programs including scalar preparation. They do not claim bounded coefficients, numerical conditioning or bit complexity; the synthesis appendix is excluded. The scope document and all linked Comparator definitions and targets were read. Their main target proofs contain sorry; no solution or Lean project was built.

Workspace can start arbitrarily but must be disjoint from inputs and targets. Tensor amplification is conditional on an actual fixed finite winning word; numerical recurrence parameters do not supply one.

[Batch record](../../batches/B050/README.md)
