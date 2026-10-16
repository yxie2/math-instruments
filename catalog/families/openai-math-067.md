---
id: openai-math-067
record_type: family
title: Rational-curve involutions and mixed exact/modular kernel certificates
source_family: '067'
source_collection: openai/math
batch_id: B033
subject: Algebraic and complex geometry
source_paper_ids:
- P-000206
instrument_ids:
- MI-000374
- MI-000375
headline: The source claims the Campana-Peternell conjecture in dimension six.
central_instrument: Fiber integration for a smooth P1-fibration becomes an involution and twisted product
  rule. A lifted polynomial constraint is certified by combining a modular upper bound on kernel dimension
  with exact rational witnesses.
novelty_assessment: Leray-Hirsch, GRR, divided differences and exact/modular linear algebra are established
  tools. This is extraction of useful certificate structure, not independent certification of the large
  source calculation or classification.
formalization_summary: No formalization scope document is listed for this family in the pinned release
  inventory. No Lean build was performed.
statement_faithfulness: Cohomology identities use rational coefficients. The P1-fibration need not be
  a projectivized vector bundle. Modular ranks only bound rational ranks below; exact witness identities
  remain essential.
dependencies: Leray-Hirsch, relative Grothendieck-Riemann-Roch, rational cohomology, multiset coordinates,
  Gaussian elimination and modular reduction at invertible denominators.
antecedents: Classical fiber integration and exact linear-algebra certificates. No first-priority claim.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Rational-curve involutions and mixed exact/modular kernel certificates

## Source manuscript and claim

[The Campana–Peternell conjecture in dimension six](../papers/P-000206.md), by OpenAI, September 25, 2026.

The source claims the Campana-Peternell conjecture in dimension six.

## Extracted instruments

- [MI-000374: Express P1 fiber integration as an involution and a divided-difference rule](../instruments/MI-000374.md)
- [MI-000375: Certify a lifted polynomial consequence with modular rank and rational witnesses](../instruments/MI-000375.md)

## Dependencies and antecedents

Leray-Hirsch, relative Grothendieck-Riemann-Roch, rational cohomology, multiset coordinates, Gaussian elimination and modular reduction at invertible denominators.

Classical fiber integration and exact linear-algebra certificates. No first-priority claim. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full P1-involution proof, arithmetic-certificate argument and certificate appendix description. The source 8280 by 6820 matrix and reported ranks were not recomputed; geometric input equations and final recognition were not audited.

No formalization scope document is listed for this family in the pinned release inventory. No Lean build was performed.

Cohomology identities use rational coefficients. The P1-fibration need not be a projectivized vector bundle. Modular ranks only bound rational ranks below; exact witness identities remain essential.

[Batch record](../../batches/B033/README.md)
