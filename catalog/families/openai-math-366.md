---
id: openai-math-366
record_type: family
title: Project compact jumps before comparing translated singular sets
source_family: '366'
source_collection: openai/math
batch_id: B027
subject: Partial differential equations
source_paper_ids:
- P-000179
instrument_ids:
- MI-000320
- MI-000321
headline: The source claims the full interior arc, crack-tip and triple-junction description of reduced
  planar Mumford-Shah absolute minimizers, with locally finitely many global crack components.
central_instrument: An L2 gradient projection isolates a divergence-free field supported in curl on a
  compact crack. Translation makes its interaction harmonic; minimality and arbitrary amplitude variations
  then force exact cancellation.
novelty_assessment: Hilbert-space Hodge projection, exterior harmonic expansion and the minimum principle
  are classical. The source combines them in a compact translation argument; no global regularity or historical
  novelty certification is claimed.
formalization_summary: No family-specific scope document or Comparator target is listed. No Lean artifact
  was built or kernel-checked.
statement_faithfulness: The compact jump field is a gradient density off a zero-area set, not necessarily
  a distributional gradient on the whole plane. Linear energy growth is retained when passing from compact
  comparisons to infinite-plane interactions.
dependencies: L2 orthogonal projection, local Poincare inequalities, exterior Fourier expansion, compact
  variational comparisons and the strong minimum principle.
antecedents: Classical Helmholtz-Hodge decomposition, finite-energy harmonic functions and harmonic minimum
  principles.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Project compact jumps before comparing translated singular sets

## Source manuscript and claim

[Interior regularity of planar Mumford–Shah minimizers](../papers/P-000179.md), by OpenAI, None.

The source claims the full interior arc, crack-tip and triple-junction description of reduced planar Mumford-Shah absolute minimizers, with locally finitely many global crack components.

## Extracted instruments

- [MI-000320: Project a compact jump field to a decaying divergence-free field](../instruments/MI-000320.md)
- [MI-000321: Use harmonic translation and amplitude variation to force an interaction to vanish](../instruments/MI-000321.md)

## Dependencies and antecedents

L2 orthogonal projection, local Poincare inequalities, exterior Fourier expansion, compact variational comparisons and the strong minimum principle.

Classical Helmholtz-Hodge decomposition, finite-energy harmonic functions and harmonic minimum principles. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the compact-projection, translated-comparison and harmonic-interaction proofs completely, plus the main theorem and endpoint gradient corollary. Subsequent component-removal and full geometric classification arguments were not audited.

No family-specific scope document or Comparator target is listed. No Lean artifact was built or kernel-checked.

The compact jump field is a gradient density off a zero-area set, not necessarily a distributional gradient on the whole plane. Linear energy growth is retained when passing from compact comparisons to infinite-plane interactions.

[Batch record](../../batches/B027/README.md)
