---
id: openai-math-242
record_type: family
title: Complete-witness uniqueness in arithmetic encodings
source_family: '242'
source_collection: openai/math
batch_id: B021
subject: Mathematical logic
source_paper_ids:
- P-000156
instrument_ids:
- MI-000273
- MI-000274
- MI-000275
headline: The source claims a single-fold polynomial representation of every recursively enumerable subset
  of N^n, with uniqueness of the entire natural-number witness tuple, and derives undecidability under
  an at-most-one-solution promise.
central_instrument: Disjoint cases freeze every inactive variable, rational codes normalize inverse witnesses,
  and large-base digit extraction converts binary containment into binomial parity while retaining all
  power-call witnesses.
novelty_assessment: Single-fold closure, normalized coprimality witnesses and binomial digit masking have
  established antecedents. The particular shifted rational code is explicit source bookkeeping. The rank-one
  growth construction, single-fold power graph and machine compiler behind the headline were not audited.
formalization_summary: Read SingleFold.lean evaluation, whole-witness uniqueness and main target for every
  positive input arity. The at-most-one-solution undecidability consequence is not a separate selected
  target. These are target statements with sorry placeholders; no Lean solution was built or kernel-checked.
statement_faithfulness: All auxiliaries, including inactive branches, inequalities, normalization and
  nested calls, count in uniqueness. Binary masking is conditional here on a complete single-fold power
  graph; ordinary exponentiation evaluation is weaker.
dependencies: Disjoint guarded cases, natural slacks, reduced rational fractions, normalized modular inverses,
  Euclidean division, binomial expansion and Lucas parity.
antecedents: Matiyasevich single-fold constructions; Cantone-Cuzziol-Omodeo, On Diophantine Singlefold
  Specifications, Section 2; Julia Robinson large-base coefficient extraction; Jones-Matiyasevich binary
  masking and Lucas congruence.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Complete-witness uniqueness in arithmetic encodings

## Source manuscript and claim

[Single-fold Diophantine representations](../papers/P-000156.md), by OpenAI, September 24, 2026.

The source claims a single-fold polynomial representation of every recursively enumerable subset of N^n, with uniqueness of the entire natural-number witness tuple, and derives undecidability under an at-most-one-solution promise.

## Extracted instruments

- [MI-000273: Freeze inactive branches to preserve complete polynomial-witness uniqueness](../instruments/MI-000273.md)
- [MI-000274: A shifted inverse identity gives one natural-number code for each rational](../instruments/MI-000274.md)
- [MI-000275: Large-base binomial digits test binary containment with unique division witnesses](../instruments/MI-000275.md)

## Dependencies and antecedents

Disjoint guarded cases, natural slacks, reduced rational fractions, normalized modular inverses, Euclidean division, binomial expansion and Lucas parity.

Matiyasevich single-fold constructions; Cantone-Cuzziol-Omodeo, On Diophantine Singlefold Specifications, Section 2; Julia Robinson large-base coefficient extraction; Jones-Matiyasevich binary masking and Lucas congruence. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the closure lemma, rational-code proof and complete binary-containment proof. The elliptic growth, Pell power construction and machine compiler were not audited.

Read SingleFold.lean evaluation, whole-witness uniqueness and main target for every positive input arity. The at-most-one-solution undecidability consequence is not a separate selected target. These are target statements with sorry placeholders; no Lean solution was built or kernel-checked.

All auxiliaries, including inactive branches, inequalities, normalization and nested calls, count in uniqueness. Binary masking is conditional here on a complete single-fold power graph; ordinary exponentiation evaluation is weaker.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/242.md) · [Batch record](../../batches/B021/README.md)
