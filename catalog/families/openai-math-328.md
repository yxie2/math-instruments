---
id: openai-math-328
record_type: family
title: Adaptive convex return and weighted witnesses in nonlinear trees
source_family: '328'
source_collection: openai/math
batch_id: B009
subject: Functional analysis
source_paper_ids:
- P-000107
instrument_ids:
- MI-000170
- MI-000171
headline: The source claims the fixed point property for every real reflexive Banach space in its given
  norm, without normal structure or weak continuity of the map.
central_instrument: A compact semigroup supplies an anchor permitting successive choices with history-dependent
  accuracy. Weighted telescoping then extracts one vector detected along a whole path, without a lower
  bound on branch weights.
novelty_assessment: Resolvents, weak-to-norm convex approximation, compact-semigroup idempotents and weighted
  averaging are classical. The source-specific packages are the adaptive return construction and its use
  in a nonlinear switching tree. The full fixed-point claim and priority are not independently certified.
formalization_summary: ReflexiveFixedPoints.lean states the original-norm fixed point assertion for a
  complete real normed space whose canonical bidual map is onto. Zero and nonseparable spaces are included.
  The commuting-family consequence is not separately asserted there. The family scope and Comparator declarations
  were compared. No Lean solution was built or kernel-checked; the auxiliary cards are not separate Comparator
  targets.
statement_faithfulness: The selected anchor construction uses a weakly compact convex domain; metrizability
  is needed for the sequential selection proof. The final tree contradiction additionally needs weak compactness
  of the whole unit ball of the closed span of K-K. Weak compactness of K alone does not supply that.
dependencies: Nonexpansive resolvents; pointwise weak compactness; separation on finite products; Ellis
  idempotents; adaptive weak approximation; consecutive leaf blocks; nonnegative weighted deficits; finite
  branching and weak compactness for the infinite limit.
antecedents: Goebel-Karlovitz provide the diametral reduction, Bruck studied convex semigroups of nonexpansive
  maps, and Ellis supplies the idempotent lemma. The weighted witness extraction is an elementary averaging
  argument once the difficult tree data exist.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Adaptive convex return and weighted witnesses in nonlinear trees

## Source manuscript and claim

[Fixed Points of Nonexpansive Maps in Reflexive Banach Spaces](../papers/P-000107.md), by OpenAI, September 24, 2026.

The source claims the fixed point property for every real reflexive Banach space in its given norm, without normal structure or weak continuity of the map.

## Extracted instruments

- [MI-000170: A compact semigroup anchor permits convex return after adaptive tail choices](../instruments/MI-000170.md)
- [MI-000171: Weighted telescoping finds a common witness without minimum branch weights](../instruments/MI-000171.md)

## Dependencies and antecedents

Nonexpansive resolvents; pointwise weak compactness; separation on finite products; Ellis idempotents; adaptive weak approximation; consecutive leaf blocks; nonnegative weighted deficits; finite branching and weak compactness for the infinite limit.

Goebel-Karlovitz provide the diametral reduction, Bruck studied convex semigroups of nonexpansive maps, and Ellis supplies the idempotent lemma. The weighted witness extraction is an elementary averaging argument once the difficult tree data exist. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the resolvent, semigroup, anchor and adaptive-selection proofs and the entire finite switching argument. The construction of compact predicted-output families and the full infinite tree were not audited; their hypotheses are kept explicit.

ReflexiveFixedPoints.lean states the original-norm fixed point assertion for a complete real normed space whose canonical bidual map is onto. Zero and nonseparable spaces are included. The commuting-family consequence is not separately asserted there. The family scope and Comparator declarations were compared. No Lean solution was built or kernel-checked; the auxiliary cards are not separate Comparator targets.

The selected anchor construction uses a weakly compact convex domain; metrizability is needed for the sequential selection proof. The final tree contradiction additionally needs weak compactness of the whole unit ball of the closed span of K-K. Weak compactness of K alone does not supply that.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/328.md) · [Batch record](../../batches/B009/README.md)
