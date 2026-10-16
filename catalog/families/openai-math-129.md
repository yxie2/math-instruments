---
id: openai-math-129
record_type: family
title: Finite-semigroup corners and deterministic configuration tours
source_family: '129'
source_collection: openai/math
batch_id: B050
subject: Theoretical computer science
source_paper_ids:
- P-000279
- P-000280
instrument_ids:
- MI-000500
- MI-000501
headline: The sources claim exponential state lower bounds for two-way complementation and for deterministic
  recognition of one-way liveness languages.
central_instrument: Minimal idempotent preimages lift units, and a relation corner restricts exactly to
  a smaller full relation monoid. Deterministic reachability to a sink is encoded by one contour tour
  of its tree component.
novelty_assessment: Elementary finite-semigroup facts and classical configuration-tree traversal. Their
  uses in the source lower-bound architecture are recorded; the lower bounds are not certified.
formalization_summary: The targets specify growing-alphabet complementation and determinization bounds
  with denominator 127, and a separate one-way liveness bound with denominator 31 and convention-dependent
  quadratic state factor. The scope document and all linked Comparator definitions and targets were read.
  Their main target proofs contain sorry; no solution or Lean project was built.
statement_faithfulness: Minimality is in the idempotent nesting order and finiteness supplies idempotent
  powers. The sink graph has one successor per vertex; nondeterministic transition graphs need not have
  tree components.
dependencies: Finite semigroup powers, idempotent corners and relation composition; partial functions,
  edge counting and cyclic orders at tree vertices.
antecedents: Classical finite semigroup structure; Sipser halting traversal and Lange-McKenzie-Tapp reversible
  simulation, as cited by the source.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite-semigroup corners and deterministic configuration tours

## Source manuscripts and claim

- [An exponential state lower bound for two-way nondeterministic complementation](../papers/P-000279.md): selected passages extracted.
- [An exponential two-way deterministic state lower bound for one-way liveness](../papers/P-000280.md): selected passages extracted.

The sources claim exponential state lower bounds for two-way complementation and for deterministic recognition of one-way liveness languages.

## Extracted instruments

- [MI-000500: Pass to a minimal idempotent corner without losing unit lifts](../instruments/MI-000500.md)
- [MI-000501: Turn deterministic sink reachability into one tree contour tour](../instruments/MI-000501.md)

## Dependencies and antecedents

Finite semigroup powers, idempotent corners and relation composition; partial functions, edge counting and cyclic orders at tree vertices.

Classical finite semigroup structure; Sipser halting traversal and Lange-McKenzie-Tapp reversible simulation, as cited by the source.

## Review and formalization scope

Read the complete minimal-corner and relation-restriction proofs and the companion sink-tree and tree-tour proofs, with their acceptance-reachability application. The diagram representation, loss amplification and state lower bounds were not certified.

The targets specify growing-alphabet complementation and determinization bounds with denominator 127, and a separate one-way liveness bound with denominator 31 and convention-dependent quadratic state factor. The scope document and all linked Comparator definitions and targets were read. Their main target proofs contain sorry; no solution or Lean project was built.

Minimality is in the idempotent nesting order and finiteness supplies idempotent powers. The sink graph has one successor per vertex; nondeterministic transition graphs need not have tree components.

[Batch record](../../batches/B050/README.md)
