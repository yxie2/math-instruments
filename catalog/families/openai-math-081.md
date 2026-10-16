---
id: openai-math-081
record_type: family
title: Moving-measure compactness and charging overlapping flat seeds
source_family: 081
source_collection: openai/math
batch_id: B023
subject: Real and complex analysis
source_paper_ids:
- P-000163
instrument_ids:
- MI-000288
- MI-000289
headline: For d>=4 and 2<=n<=d-2, the source claims that n-Ahlfors-David regular measures with uniformly
  L2-bounded positive hard Riesz truncations have quantitative big pieces of Lipschitz images, uniformly
  at every admissible center and radius.
central_instrument: Fractional cell variance recovers first and second moments on moving measures without
  evaluating a limit representative on the moving support. A finite seed-charging lemma turns separated
  failures along nested chains into a Carleson mass bound even when seeds overlap.
novelty_assessment: Varying-space strong convergence and Carleson charging have established antecedents.
  The source provides concrete flat-limit partitions and a finite overlap-tolerant counting formulation.
  This is not certification of the Riesz rectifiability theorem or exhaustive novelty.
formalization_summary: Read all definitions and the quantitative target in RieszQuantitative.lean. The
  constants are uniform over measures with fixed dimensions, AD constant and hard-truncation bound, including
  unbounded support. Variation and principal-value consequences are not selected targets. These are inspected
  target statements with sorry placeholders; no Lean solution was built or kernel-checked.
statement_faithfulness: Compactness requires positive full-plane limiting density, local L2 and fractional-energy
  bounds, common upper/lower growth and expanding admissible diameter. Weak first-moment convergence alone
  is insufficient. Seed charges are chosen for every eligible ordered pair before integrating over points.
dependencies: Exact variance identity, finite partitions of continuity sets, support convergence from
  lower growth, diagonal subsequences, polarization and nested-partition counting.
antecedents: Rellich compactness and strong convergence over varying Hilbert spaces, including Kuwae-Shioya;
  classical Carleson packing and stopping-time charging.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Moving-measure compactness and charging overlapping flat seeds

## Source manuscript and claim

[Riesz transforms and uniform rectifiability in higher codimension](../papers/P-000163.md), by OpenAI, September 24, 2026.

For d>=4 and 2<=n<=d-2, the source claims that n-Ahlfors-David regular measures with uniformly L2-bounded positive hard Riesz truncations have quantitative big pieces of Lipschitz images, uniformly at every admissible center and radius.

## Extracted instruments

- [MI-000288: Fractional cell variance preserves second moments on moving measures](../instruments/MI-000288.md)
- [MI-000289: Charge overlapping descendant seeds through disjoint generation intervals](../instruments/MI-000289.md)

## Dependencies and antecedents

Exact variance identity, finite partitions of continuity sets, support convergence from lower growth, diagonal subsequences, polarization and nested-partition counting.

Rellich compactness and strong convergence over varying Hilbert spaces, including Kuwae-Shioya; classical Carleson packing and stopping-time charging. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete moving-measure compactness proof and finite seed-charging lemma. The local Riesz energy bound, flat-limit rigidity and excess-propagation theorems supplying their hypotheses were not audited.

Read all definitions and the quantitative target in RieszQuantitative.lean. The constants are uniform over measures with fixed dimensions, AD constant and hard-truncation bound, including unbounded support. Variation and principal-value consequences are not selected targets. These are inspected target statements with sorry placeholders; no Lean solution was built or kernel-checked.

Compactness requires positive full-plane limiting density, local L2 and fractional-energy bounds, common upper/lower growth and expanding admissible diameter. Weak first-moment convergence alone is insufficient. Seed charges are chosen for every eligible ordered pair before integrating over points.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/081.md) · [Batch record](../../batches/B023/README.md)
