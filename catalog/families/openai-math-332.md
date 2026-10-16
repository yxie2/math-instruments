---
id: openai-math-332
record_type: family
title: Nonlinear median smoothing through cuts and stopped martingales
source_family: '332'
source_collection: openai/math
batch_id: B008
subject: Functional analysis
source_paper_ids:
- P-000106
instrument_ids:
- MI-000167
- MI-000168
- MI-000169
headline: The source claims metric Markov cotype two for real ell1 with constant 12 sqrt(21), and consequently
  a universal Lipschitz extension bound from Hilbert space to ell1. Its construction and cost estimate
  in fact require only stationarity of the chain.
central_instrument: An exact cut representation retains a contractive map back to the ambient ell1. A
  cubic flat at binary endpoints converts a quartic Hilbert potential into martingale jump control. Geometric
  stopping produces an expected-median modification with both approximation and one-step costs.
novelty_assessment: Cut metrics, cubic cut smoothing, resolvents and metric Markov cotype are established.
  The quartic martingale estimate and the stopped-median combination are candidate source-specific contributions.
  Their priority and the general theorem are not independently certified by finite examples.
formalization_summary: No family-specific formalization scope document is listed for family 332 in the
  pinned inventory. No Comparator comparison or Lean proof build is claimed.
statement_faithfulness: Metric Markov cotype allows nonlinear choices of new points in the full ambient
  space. It is different from Ball’s linear-average condition and from metric cotype. New points need
  not stay in the subspace spanned by the data. Zero stationary masses are permitted, and reversibility
  can be weakened to stationarity for the displayed construction.
dependencies: Finite weighted upper cuts with ambient reconstruction; the cubic 3r^2-2r^3; a quartic convexity
  remainder; a geometrically killed stationary walk; a resolvent identity; a geometric-to-Cesaro endpoint
  comparison; a separate dual-target Lipschitz extension theorem.
antecedents: Mendel-Naor formulate metric Markov cotype and its ell1 question and supply the extension
  framework and resolvent comparison. Deza-Laurent give the classical cut representation. Cheng-Wang-Xiang
  use the same cubic in metric cotype smoothing, a distinct invariant; this prevents attributing the cubic
  itself as new here.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Nonlinear median smoothing through cuts and stopped martingales

## Source manuscript and claim

[Metric Markov Cotype Two of <i>ℓ</i><sub>1</sub> ](../papers/P-000106.md), by OpenAI, October 5, 2026.

The source claims metric Markov cotype two for real ell1 with constant 12 sqrt(21), and consequently a universal Lipschitz extension bound from Hilbert space to ell1. Its construction and cost estimate in fact require only stationarity of the chain.

## Extracted instruments

- [MI-000167: Finite ell1 cuts retain a contractive affine reconstruction](../instruments/MI-000167.md)
- [MI-000168: A flat cubic converts quartic potential into martingale jump energy](../instruments/MI-000168.md)
- [MI-000169: Expected medians of stopped-walk endpoints control two smoothing costs](../instruments/MI-000169.md)

## Dependencies and antecedents

Finite weighted upper cuts with ambient reconstruction; the cubic 3r^2-2r^3; a quartic convexity remainder; a geometrically killed stationary walk; a resolvent identity; a geometric-to-Cesaro endpoint comparison; a separate dual-target Lipschitz extension theorem.

Mendel-Naor formulate metric Markov cotype and its ell1 question and supply the extension framework and resolvent comparison. Deza-Laurent give the classical cut representation. Cheng-Wang-Xiang use the same cubic in metric cotype smoothing, a distinct invariant; this prevents attributing the cubic itself as new here. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete elementary proof of the source’s cotype bound, its expected-median interpretation and its extension deduction. Retrieved Mendel-Naor’s question, extension statement and resolvent lemma, and Cheng-Wang-Xiang’s cut-smoothing construction. Finite tests audit identities and examples, not universal proof certification.

No family-specific formalization scope document is listed for family 332 in the pinned inventory. No Comparator comparison or Lean proof build is claimed.

Metric Markov cotype allows nonlinear choices of new points in the full ambient space. It is different from Ball’s linear-average condition and from metric cotype. New points need not stay in the subspace spanned by the data. Zero stationary masses are permitted, and reversibility can be weakened to stationarity for the displayed construction.

[Batch record](../../batches/B008/README.md)
