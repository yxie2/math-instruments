---
id: openai-math-008
record_type: family
title: Ihara depth and saturated integral generator spans
source_family: 008
source_collection: openai/math
batch_id: B042
subject: Number theory
source_paper_ids:
- P-000241
instrument_ids:
- MI-000444
- MI-000445
headline: The source claims the Deligne-Drinfeld conjecture for the rational Grothendieck-Teichmuller
  Lie algebra.
central_instrument: The Ihara bracket adds ordinary y-depth. Independent reductions of integral vectors
  ensure a saturated rational span over the localized integers.
novelty_assessment: Both selected mechanisms are elementary classical algebra. The full dimension squeeze
  and generator construction rely on separate unaudited inputs.
formalization_summary: Read selected DeligneDrinfeld.lean sections defining the equation space, Ihara
  bracket, grading, completions and main statement. The main target contains sorry. The tangent Lie implementation
  was not audited. No Lean build.
statement_faithfulness: Ordinary y-depth is different from the source later B-count filtration. Independence
  modulo two is required for saturation; rational independence alone does not suffice.
dependencies: Free associative expansions, derivations, localized integer lattices and reduction modulo
  a prime.
antecedents: Classical depth filtration and unit-minor lattice saturation.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Ihara depth and saturated integral generator spans

## Source manuscript and claim

[The Deligne-Drinfeld conjecture](../papers/P-000241.md), by OpenAI, September 23, 2026.

The source claims the Deligne-Drinfeld conjecture for the rational Grothendieck-Teichmuller Lie algebra.

## Extracted instruments

- [MI-000444: Track ordinary depth additively through the Ihara bracket](../instruments/MI-000444.md)
- [MI-000445: Certify saturation of a rational span from independent prime reductions](../instruments/MI-000445.md)

## Dependencies and antecedents

Free associative expansions, derivations, localized integer lattices and reduction modulo a prime.

Classical depth filtration and unit-minor lattice saturation. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read both selected proofs and their Ihara convention. Holonomy, deletion representations, characteristic-two image bounds and the final dimension squeeze were not audited.

Read selected DeligneDrinfeld.lean sections defining the equation space, Ihara bracket, grading, completions and main statement. The main target contains sorry. The tangent Lie implementation was not audited. No Lean build.

Ordinary y-depth is different from the source later B-count filtration. Independence modulo two is required for saturation; rational independence alone does not suffice.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/008.md) · [Batch record](../../batches/B042/README.md)
