---
id: openai-math-371
record_type: family
title: A recurrence flux disk and stable graphs with neutral directions
source_family: '371'
source_collection: openai/math
batch_id: B043
subject: Partial differential equations
source_paper_ids:
- P-000246
instrument_ids:
- MI-000454
- MI-000455
headline: The source claims stable self-similar blowup for arbitrarily large odd-power defocusing NLS
  on the twelve-torus.
central_instrument: A quadratic flux of Laguerre tails yields a disk constraint. Backward summation controls
  noncontracting finite-dimensional modes, including a neutral mode, in a weighted stable graph.
novelty_assessment: These are source-specific recurrence and stable-graph interfaces built from classical
  flux and Lyapunov-Perron methods. No novelty or PDE theorem certification.
formalization_summary: Read the scope document and selected DefocusingNLS definitions and theorem targets.
  Targets and a Sobolev-product membership obligation contain sorry. Quantifier is arbitrarily large odd
  powers, not every sufficiently large odd power. No Lean build.
statement_faithfulness: The flux cone needs actual rapidly decaying, nonzero tails. The graph needs uniform
  contraction estimates and summable forcing; a neutral mode is handled by future summation.
dependencies: Laguerre expansions, a purely imaginary recurrence parameter, telescoping flux, weighted
  sequence contraction and summable tails.
antecedents: Classical Laguerre identities, discrete flux methods and Lyapunov-Perron stable manifolds.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# A recurrence flux disk and stable graphs with neutral directions

## Source manuscript and claim

[Stable self-similar blowup for a supercritical defocusing Schrödinger equation on the torus](../papers/P-000246.md), by OpenAI, September 24, 2026.

The source claims stable self-similar blowup for arbitrarily large odd-power defocusing NLS on the twelve-torus.

## Extracted instruments

- [MI-000454: Convert a Laguerre-tail recurrence into a strict disk constraint](../instruments/MI-000454.md)
- [MI-000455: Build a stable graph by summing neutral and expanding modes backward](../instruments/MI-000455.md)

## Dependencies and antecedents

Laguerre expansions, a purely imaginary recurrence parameter, telescoping flux, weighted sequence contraction and summable tails.

Classical Laguerre identities, discrete flux methods and Lyapunov-Perron stable manifolds. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete selected Laguerre recurrence, cone, nonlinear step and graph proofs. The free special-function asymptotics, spectral exclusion certificates and full PDE construction were not audited.

Read the scope document and selected DefocusingNLS definitions and theorem targets. Targets and a Sobolev-product membership obligation contain sorry. Quantifier is arbitrarily large odd powers, not every sufficiently large odd power. No Lean build.

The flux cone needs actual rapidly decaying, nonzero tails. The graph needs uniform contraction estimates and summable forcing; a neutral mode is handled by future summation.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/371.md) · [Batch record](../../batches/B043/README.md)
