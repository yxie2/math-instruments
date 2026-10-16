---
id: openai-math-085
record_type: family
title: Exact cancellation and birth-aware paths on positive refinements
source_family: 085
source_collection: openai/math
batch_id: B023
subject: Real and complex analysis
source_paper_ids:
- P-000165
instrument_ids:
- MI-000292
- MI-000293
headline: The source claims a global L1 weak-gradient bound for the centered disk maximal operator on
  every real W1,1 function in the plane, with local W1,1 regularity of its output, together with an intermediate
  signed finite-band estimate.
central_instrument: Proportional removal realizes scalar cancellation as exact signed-measure identities
  on a refinement graph. A separate positive particle measure fills increasing vector-mass capacities
  and records birth times so every node has exactly the intended occupancy.
novelty_assessment: Proportional cancellation, refinement telescoping and flow-with-birth constructions
  are elementary established ideas. The source combines them with explicit shared-descendant and pre-birth-history
  accounting. The analytic disk estimates and endpoint theorem remain unaudited.
formalization_summary: Read SignedFiniteBand.lean and DiskMaximal.lean, including all positive real disk
  radii, finiteness almost everywhere, local integrability, weak-gradient definitions and the global gradient
  bound. The signed finite band includes both endpoints and the single-radius case. The BV extension is
  outside these targets. These are inspected target statements with sorry placeholders; no Lean solution
  was built or kernel-checked.
statement_faithfulness: The scalar cancellation identity and the positive vector-path measure are different
  objects. Shared descendants are allowed. Zero signed mass can have nonzero cancellation defect, and
  paths born below a zero-mass ancestor retain a history without occupying that ancestor before birth.
dependencies: Nonnegative column-normalized refinement matrices, positive and negative measures, triangle
  defects, finite path unfolding, proportional transport and birth-level filtering.
antecedents: Classical positive/negative decomposition of signed measures, telescoping variation budgets
  and finite network flow decompositions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Exact cancellation and birth-aware paths on positive refinements

## Source manuscript and claim

[An Endpoint Gradient Bound for the Centered Disk Maximal Operator](../papers/P-000165.md), by OpenAI, September 26, 2026.

The source claims a global L1 weak-gradient bound for the centered disk maximal operator on every real W1,1 function in the plane, with local W1,1 regularity of its output, together with an intermediate signed finite-band estimate.

## Extracted instruments

- [MI-000292: Proportional cancellation gives exact reconstruction on a refinement graph](../instruments/MI-000292.md)
- [MI-000293: Fill refinement capacities with particles that retain their birth levels](../instruments/MI-000293.md)

## Dependencies and antecedents

Nonnegative column-normalized refinement matrices, positive and negative measures, triangle defects, finite path unfolding, proportional transport and birth-level filtering.

Classical positive/negative decomposition of signed measures, telescoping variation budgets and finite network flow decompositions. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the entire equal-mass removal, exact scalar pairing and finite-particle proofs. The local disk bounds, direction-label packing, signed-envelope assembly and Sobolev extension were not audited.

Read SignedFiniteBand.lean and DiskMaximal.lean, including all positive real disk radii, finiteness almost everywhere, local integrability, weak-gradient definitions and the global gradient bound. The signed finite band includes both endpoints and the single-radius case. The BV extension is outside these targets. These are inspected target statements with sorry placeholders; no Lean solution was built or kernel-checked.

The scalar cancellation identity and the positive vector-path measure are different objects. Shared descendants are allowed. Zero signed mass can have nonzero cancellation defect, and paths born below a zero-mass ancestor retain a history without occupying that ancestor before birth.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/085.md) · [Batch record](../../batches/B023/README.md)
