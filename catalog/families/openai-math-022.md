---
id: openai-math-022
record_type: family
title: Prime-coordinate concentration and orbit-averaged mass accounting
source_family: '022'
source_collection: openai/math
batch_id: B017
subject: Number theory
source_paper_ids:
- P-000139
instrument_ids:
- MI-000238
- MI-000239
headline: For every fixed real shift gamma, the source claims almost-everywhere infinitely many solutions
  of ||qx-gamma||<psi(q) whenever sum phi(q)psi(q)/q diverges. The numerator is unrestricted; this is
  the weak inhomogeneous Duffin-Schaeffer statement.
central_instrument: A nearly diagonal prime-exponent kernel forces a common concentration index and tensorizes.
  Fractional matching preserves a cell cap and converts dependent translation updates into an exact variance
  budget.
novelty_assessment: The common-pivot argument is explicitly adapted from Green-Walker and Hauke-Treuer-Vazquez-Walker.
  The extracted orbit and cap bookkeeping is a candidate reusable interface. The long inhomogeneous approximation
  construction was not audited.
formalization_summary: No family-specific Lean scope document was listed in the pinned inventory. No Lean
  proof was certified.
statement_faithfulness: Kernel inflation applies only off the diagonal. Translation colors need not be
  independent. The energy identity uses the entire transported class family; an arbitrary single class
  need not gain energy.
dependencies: Convolution estimates, Holder inequalities, prime-coordinate tensorization, fractional matching,
  finite-group orbit averaging and capped quadratic energy.
antecedents: Green-Walker, Extremal problems for GCDs, Lemma 2.1; Hauke-Treuer-Vazquez-Walker, Proving
  the Duffin-Schaeffer conjecture without GCD graphs, Lemma 3.2.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Prime-coordinate concentration and orbit-averaged mass accounting

## Source manuscript and claim

[The Weak Inhomogeneous Duffin–Schaeffer Conjecture](../papers/P-000139.md), by OpenAI, September 25, 2026.

For every fixed real shift gamma, the source claims almost-everywhere infinitely many solutions of ||qx-gamma||<psi(q) whenever sum phi(q)psi(q)/q diverges. The numerator is unrestricted; this is the weak inhomogeneous Duffin-Schaeffer statement.

## Extracted instruments

- [MI-000238: Prime-exponent concentration gives a summable gcd tensor kernel](../instruments/MI-000238.md)
- [MI-000239: Dependent matched updates preserve caps and charge variance through finite orbits](../instruments/MI-000239.md)

## Dependencies and antecedents

Convolution estimates, Holder inequalities, prime-coordinate tensorization, fractional matching, finite-group orbit averaging and capped quadratic energy.

Green-Walker, Extremal problems for GCDs, Lemma 2.1; Hauke-Treuer-Vazquez-Walker, Proving the Duffin-Schaeffer conjecture without GCD graphs, Lemma 3.2. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete one-coordinate and tensor proofs, the sparse matching update, clipping calculation and variance-budget proof. The partition construction, arithmetic comparisons, first-join estimates and full-measure transfer were not audited.

No family-specific Lean scope document was listed in the pinned inventory. No Lean proof was certified.

Kernel inflation applies only off the diagonal. Translation colors need not be independent. The energy identity uses the entire transported class family; an arbitrary single class need not gain energy.

[Batch record](../../batches/B017/README.md)
