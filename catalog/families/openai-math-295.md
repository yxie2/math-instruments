---
id: openai-math-295
record_type: family
title: Central cochain correction and continuity through iterated tracial ultrapowers
source_family: '295'
source_collection: openai/math
batch_id: B034
subject: Operator algebras
source_paper_ids:
- P-000208
instrument_ids:
- MI-000378
- MI-000379
headline: The source claims vanishing of bounded Hochschild cohomology in every degree at least two for
  arbitrary complex von Neumann algebras.
central_instrument: An explicit central-cut homotopy corrects mixed inputs with a degree-only norm bound.
  A uniform bounded-ball modulus lets linear maps descend through repeated tracial ultrapowers.
novelty_assessment: Bar-complex contraction and uniform quotient continuity are classical mechanisms.
  The extraction records explicit formulas and hypotheses, without certifying the global cohomology vanishing
  argument.
formalization_summary: Read KadisonRingrose.lean and its ordinary bounded Hochschild differential. Its
  degree-at-least-two target has no separability or type restriction and contains sorry. No Lean build
  was performed.
statement_faithfulness: The cochain output lies in zM for a central projection z; its complementary projection
  annihilates that module. Ultrapower descent needs L2 continuity on each fixed operator-norm ball, not
  merely operator-norm boundedness.
dependencies: Hochschild differential, central projections, multilinearity, uniform continuity on bounded
  balls and tracial ultrapower ideals.
antecedents: Classical chain homotopy and quotient continuity; no first-priority claim.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Central cochain correction and continuity through iterated tracial ultrapowers

## Source manuscript and claim

[Vanishing of higher bounded Hochschild cohomology](../papers/P-000208.md), by OpenAI, September 23, 2026.

The source claims vanishing of bounded Hochschild cohomology in every degree at least two for arbitrary complex von Neumann algebras.

## Extracted instruments

- [MI-000378: Correct mixed central inputs by an explicit bounded Hochschild homotopy](../instruments/MI-000378.md)
- [MI-000379: Transfer a bounded-ball L2 modulus through repeated tracial ultrapowers](../instruments/MI-000379.md)

## Dependencies and antecedents

Hochschild differential, central projections, multilinearity, uniform continuity on bounded balls and tracial ultrapower ideals.

Classical chain homotopy and quotient continuity; no first-priority claim. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full central-cut homotopy and iterated-ultrapower continuity proofs. The random-walk construction, Liouville rigidity and primitive construction were not audited.

Read KadisonRingrose.lean and its ordinary bounded Hochschild differential. Its degree-at-least-two target has no separability or type restriction and contains sorry. No Lean build was performed.

The cochain output lies in zM for a central projection z; its complementary projection annihilates that module. Ultrapower descent needs L2 continuity on each fixed operator-norm ball, not merely operator-norm boundedness.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/295.md) · [Batch record](../../batches/B034/README.md)
