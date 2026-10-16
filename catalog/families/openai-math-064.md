---
id: openai-math-064
record_type: family
title: Finite Milnor-number tests and explicit removal of cyclic base change
source_family: '064'
source_collection: openai/math
batch_id: B039
subject: Algebraic and complex geometry
source_paper_ids:
- P-000230
instrument_ids:
- MI-000422
- MI-000423
headline: The source claims topological triviality of mu-constant families of surface singularities.
central_instrument: A truncated Jacobian multiplication matrix detects an exact finite length; a seam-corrected
  transport descends a given tube trivialization through cyclic base change.
novelty_assessment: Finite-length Nakayama and explicit seam correction are standard mechanisms. The selected
  interfaces do not certify the source global singularity theorem or its priority.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build.
statement_faithfulness: The rank test uses truncation by m^(mu+1). Descent requires an existing jointly
  continuous trivialization with continuous inverses on compatible tubes; it does not construct that input.
dependencies: Noetherian local algebra, rank strata and continuous families of fiber automorphisms.
antecedents: Classical finite-length Nakayama and cyclic covering-space gluing.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite Milnor-number tests and explicit removal of cyclic base change

## Source manuscript and claim

[Topological triviality of mu-constant families of surface singularities](../papers/P-000230.md), by OpenAI, September 24, 2026.

The source claims topological triviality of mu-constant families of surface singularities.

## Extracted instruments

- [MI-000422: Detect an exact Jacobian-algebra length by one finite rank condition](../instruments/MI-000422.md)
- [MI-000423: Remove cyclic base change by a continuous seam correction](../instruments/MI-000423.md)

## Dependencies and antecedents

Noetherian local algebra, rank strata and continuous families of fiber automorphisms.

Classical finite-length Nakayama and cyclic covering-space gluing. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete finite-jet length argument and complete base-change removal proof. The preceding geometric construction of a tube trivialization was not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build.

The rank test uses truncation by m^(mu+1). Descent requires an existing jointly continuous trivialization with continuous inverses on compatible tubes; it does not construct that input.

[Batch record](../../batches/B039/README.md)
