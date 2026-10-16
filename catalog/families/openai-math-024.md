---
id: openai-math-024
record_type: family
title: Exceptional-fiber counts and uniform phase limits from a common comparison
source_family: '024'
source_collection: openai/math
batch_id: B017
subject: Number theory
source_paper_ids:
- P-000141
instrument_ids:
- MI-000242
- MI-000243
headline: The source claims an explicit asymptotic equivalent for the number V(x) of distinct totients,
  constructed from finite arithmetic approximants, and regular variation V(cx)/V(x)->c for every c>0,
  together with least-preimage interval counts.
central_instrument: A collision count controls exceptional values and their entire preimages. A comparison
  quantity independent of the truncation index forces uniform convergence of phase-dependent coefficients
  without continuity.
novelty_assessment: Finite-map collision inequalities and uniform Cauchy arguments are elementary established
  principles. Their reusable value here is the simultaneous preimage accounting and exact-phase subsequence
  requirement. The totient asymptotic itself was not certified.
formalization_summary: The scope document and both TotientAsymptotic.lean and TotientCompanionZero.lean
  were read. Targets include uniform coefficient limits, the asymptotic formula, regular variation, positive
  companion cases and the exact zero alternative. These are Comparator targets, not certified proof builds.
  No Lean solution was built or kernel-checked, and the auxiliary cards are not all separate formalization
  targets.
statement_faithfulness: Few exceptional values need not mean few exceptional representations. Exact phase
  recurrence replaces continuity; merely dense phase visits do not suffice. Regular variation is a separate
  source argument, not a consequence of arbitrary discontinuous phase coefficients.
dependencies: Finite fibers and pair collisions, a common normalized comparison, exact phase subsequences
  and uniform Cauchy convergence.
antecedents: The source uses Ford's totient structure estimates as separate inputs. The selected finite-map
  and convergence arguments are elementary; no novel general counting or convergence theorem is claimed.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Exceptional-fiber counts and uniform phase limits from a common comparison

## Source manuscript and claim

[An asymptotic formula for the number of totients](../papers/P-000141.md), by OpenAI, September 25, 2026.

The source claims an explicit asymptotic equivalent for the number V(x) of distinct totients, constructed from finite arithmetic approximants, and regular variation V(cx)/V(x)->c for every c>0, together with least-preimage interval counts.

## Extracted instruments

- [MI-000242: Collision counts control exceptional fibers as well as exceptional values](../instruments/MI-000242.md)
- [MI-000243: A common comparison forces uniform phase limits without phase continuity](../instruments/MI-000243.md)

## Dependencies and antecedents

Finite fibers and pair collisions, a common normalized comparison, exact phase subsequences and uniform Cauchy convergence.

The source uses Ford's totient structure estimates as separate inputs. The selected finite-map and convergence arguments are elementary; no novel general counting or convergence theorem is claimed. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the finite-map proof, the finite-coefficient approximation statement and its proof, and the common-comparison convergence proof. The prime-prefix coverage, collision estimates, witness-volume formula and least-preimage arithmetic were not audited.

The scope document and both TotientAsymptotic.lean and TotientCompanionZero.lean were read. Targets include uniform coefficient limits, the asymptotic formula, regular variation, positive companion cases and the exact zero alternative. These are Comparator targets, not certified proof builds. No Lean solution was built or kernel-checked, and the auxiliary cards are not all separate formalization targets.

Few exceptional values need not mean few exceptional representations. Exact phase recurrence replaces continuity; merely dense phase visits do not suffice. Regular variation is a separate source argument, not a consequence of arbitrary discontinuous phase coefficients.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/024.md) · [Batch record](../../batches/B017/README.md)
