---
id: openai-math-132
record_type: family
title: Gated tournament predicates and joint sensitivity profiles
source_family: '132'
source_collection: openai/math
batch_id: B011
subject: Theoretical computer science
source_paper_ids:
- P-000117
instrument_ids:
- MI-000192
- MI-000193
headline: The source claims total Boolean functions with block sensitivity divided by sensitivity squared
  arbitrarily large, and a stronger fixed superquadratic exponent separation.
central_instrument: A labeled tournament bounds clauses that are one repair away from acceptance. Tracking
  simultaneous changes of two nested predicates prevents a large gate degree from being charged to ordinary
  sensitivity at every recursive level.
novelty_assessment: Tournament-gated clauses adapt Meiburg’s spectral-sensitivity construction, and the
  label existence argument is an elementary union bound. The selected candidate refinement is the ordinary
  joint-profile recursion, not the underlying tournament architecture.
formalization_summary: SensitivitySeparation.lean contains the quantitative existence statement bs(f)/s(f)^2>=2^d/[4(d+2)^2]
  for every integer d>=1. The scope document additionally mentions a fixed exponent greater than two,
  but that is not a separate statement in this Comparator file. Scope documents and Comparator statements
  were compared. No Lean solution was built or kernel-checked, and the extracted auxiliary results are
  not separately certified Comparator targets.
statement_faithfulness: Ordinary sensitivity is a maximum vertex degree; spectral sensitivity is an adjacency
  operator norm and cannot be substituted. Nesting is in predicate index, not monotonicity in raw input
  bits. All profiles concern the same raw bit flip.
dependencies: Regular tournaments; independently sampled edge labels; nested total predicates on disjoint
  child blocks; target and gate clauses; fixed candidate lists at rejecting inputs; one- and two-predicate
  sensitivity profiles.
antecedents: Meiburg supplies the gated-tournament architecture for spectral sensitivity. Classical sensitivity
  examples and the degree/sensitivity theory motivate the question; the source directly analyzes ordinary
  sensitivity rather than infer it from a spectral lower bound.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Gated tournament predicates and joint sensitivity profiles

## Source manuscript and claim

[A superquadratic separation between sensitivity and block sensitivity](../papers/P-000117.md), by OpenAI, September 25, 2026.

The source claims total Boolean functions with block sensitivity divided by sensitivity squared arbitrarily large, and a stronger fixed superquadratic exponent separation.

## Extracted instruments

- [MI-000192: A forbidden label pattern bounds the clauses one bit away from acceptance](../instruments/MI-000192.md)
- [MI-000193: Joint sensitivity profiles control recursive gates while block witnesses multiply](../instruments/MI-000193.md)

## Dependencies and antecedents

Regular tournaments; independently sampled edge labels; nested total predicates on disjoint child blocks; target and gate clauses; fixed candidate lists at rejecting inputs; one- and two-predicate sensitivity profiles.

Meiburg supplies the gated-tournament architecture for spectral sensitivity. Classical sensitivity examples and the degree/sensitivity theory motivate the question; the source directly analyzes ordinary sensitivity rather than infer it from a spectral lower bound. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the labeled tournament, base predicates, disjoint block witnesses and complete recurrence proofs. The final parameter optimization and fixed-exponent sequence were not audited.

SensitivitySeparation.lean contains the quantitative existence statement bs(f)/s(f)^2>=2^d/[4(d+2)^2] for every integer d>=1. The scope document additionally mentions a fixed exponent greater than two, but that is not a separate statement in this Comparator file. Scope documents and Comparator statements were compared. No Lean solution was built or kernel-checked, and the extracted auxiliary results are not separately certified Comparator targets.

Ordinary sensitivity is a maximum vertex degree; spectral sensitivity is an adjacency operator norm and cannot be substituted. Nesting is in predicate index, not monotonicity in raw input bits. All profiles concern the same raw bit flip.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/132.md) · [Batch record](../../batches/B011/README.md)
