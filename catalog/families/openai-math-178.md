---
id: openai-math-178
record_type: family
title: Discounted conditional expectations and partial-pairing matrix identities
source_family: '178'
source_collection: openai/math
batch_id: B015
subject: Combinatorics
source_paper_ids:
- P-000134
instrument_ids:
- MI-000228
- MI-000229
headline: The source claims deterministic polynomial-time construction of simple connected nonbipartite
  d-regular Ramanujan graphs for every fixed d>=3 and all sufficiently large even sizes.
central_instrument: Separate expectation discounts allow one transition to control many nonnegative statistics.
  A partial stub pairing admits exact low-rank matrix updates, a weighted nonbacktracking recurrence and
  finite-population cancellation.
novelty_assessment: Conditional expectations, pessimistic estimators, Ihara-Bass identities and Woodbury
  updates are established. The selected partial-pairing formulas and discount bookkeeping are reusable
  interfaces; the full exact spectral repair is not certified.
formalization_summary: No family-specific Lean scope document was listed in the pinned inventory. No Lean
  statement or proof was certified for these extracted tools.
statement_faithfulness: Statistics are controlled through a weighted discounted total, not by separately
  minimizing each one. Pair-update formulas require more than two unresolved stubs. Formal power-series
  identities are not automatically convergent near a spectral edge.
dependencies: Finite averaging, positive-part Taylor estimates, centered stub incidence, nonbacktracking
  recurrences, Woodbury inversion and finite-population averaging.
antecedents: Raghavan and Wigderson-Xiao for conditional expectations and composed estimators; Foata-Zeilberger
  for the Ihara-Bass matrix polynomial; the source credits Henderson-Searle for the inverse update.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Discounted conditional expectations and partial-pairing matrix identities

## Source manuscript and claim

[Deterministic nonbipartite Ramanujan graphs in every fixed degree](../papers/P-000134.md), by OpenAI, September 23, 2026.

The source claims deterministic polynomial-time construction of simple connected nonbipartite d-regular Ramanujan graphs for every fixed d>=3 and all sufficiently large even sizes.

## Extracted instruments

- [MI-000228: Account-specific expectation discounts let one deterministic choice control many statistics](../instruments/MI-000228.md)
- [MI-000229: Partial stub pairings have exact low-rank resolvent updates and centered pair cancellation](../instruments/MI-000229.md)

## Dependencies and antecedents

Finite averaging, positive-part Taylor estimates, centered stub incidence, nonbacktracking recurrences, Woodbury inversion and finite-population averaging.

Raghavan and Wigderson-Xiao for conditional expectations and composed estimators; Foata-Zeilberger for the Ihara-Bass matrix polynomial; the source credits Henderson-Searle for the inverse update. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the discounted-account and scalar-excess proofs and the full path/exposure lemma with its centered-pair identity. The multistage spectral estimates and final exact repair were not audited.

No family-specific Lean scope document was listed in the pinned inventory. No Lean statement or proof was certified for these extracted tools.

Statistics are controlled through a weighted discounted total, not by separately minimizing each one. Pair-update formulas require more than two unresolved stubs. Formal power-series identities are not automatically convergent near a spectral edge.

[Batch record](../../batches/B015/README.md)
