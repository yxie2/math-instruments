---
id: openai-math-301
record_type: family
title: Trace-cone ideal recovery and rank signals preserved by block averaging
source_family: '301'
source_collection: openai/math
batch_id: B034
subject: Operator algebras
source_paper_ids:
- P-000210
instrument_ids:
- MI-000382
- MI-000383
headline: The source claims classification of separable nuclear C*-algebras after Razak-Jacelon and compact-operator
  stabilization by extended trace cones.
central_instrument: Additive idempotents of the extended trace cone recover ideals, and scalar limits
  recover finite and zero ideals. Normalized block averaging retains a spectral lower-rank signal with
  a constant independent of the number of candidates.
novelty_assessment: Ideal recovery and scalar limits are explicit in Elliott-Robert-Santiago. Orthogonal
  block averaging and spectral compression are classical. No new ideal theorem or global classification
  certificate is claimed.
formalization_summary: 'Inspected TraceIdealTransportSupport.lean: the comparison concerns ideal weights,
  additive-idempotent ideal recovery, and transport of finite/zero ideals. Several supporting and target
  proofs contain sorry. Spatial classification and final intertwining are outside this comparison; no
  Lean build was performed.'
statement_faithfulness: Use extended lower-semicontinuous traces, including zero and infinite values.
  Internal matrix traces are unnormalized; only the separate candidate-averaging direction is normalized.
dependencies: Extended traces, positive spectral cuts, Cuntz comparison, orthogonal matrix blocks, finite-part
  reduction and normal monotone convergence.
antecedents: Elliott-Robert-Santiago, The cone of lower semicontinuous traces on a C*-algebra, Sections
  3.1-3.2 and equation (3.4).
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Trace-cone ideal recovery and rank signals preserved by block averaging

## Source manuscript and claim

[The trace cone classifies Razak–Jacelon stabilizations](../papers/P-000210.md), by OpenAI, September 25, 2026.

The source claims classification of separable nuclear C*-algebras after Razak-Jacelon and compact-operator stabilization by extended trace cones.

## Extracted instruments

- [MI-000382: Recover the ideal lattice and trace finiteness ideals from the extended trace cone](../instruments/MI-000382.md)
- [MI-000383: Preserve a lower spectral-rank signal under normalized block averaging](../instruments/MI-000383.md)

## Dependencies and antecedents

Extended traces, positive spectral cuts, Cuntz comparison, orthogonal matrix blocks, finite-part reduction and normal monotone convergence.

Elliott-Robert-Santiago, The cone of lower semicontinuous traces on a C*-algebra, Sections 3.1-3.2 and equation (3.4). The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the ideal-transport, folding and averaged-rank proofs and the fixed lower-data definitions. The approximation models, uniqueness and final classification arguments were not audited.

Inspected TraceIdealTransportSupport.lean: the comparison concerns ideal weights, additive-idempotent ideal recovery, and transport of finite/zero ideals. Several supporting and target proofs contain sorry. Spatial classification and final intertwining are outside this comparison; no Lean build was performed.

Use extended lower-semicontinuous traces, including zero and infinite values. Internal matrix traces are unnormalized; only the separate candidate-averaging direction is normalized.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/301.md) · [Batch record](../../batches/B034/README.md)
