---
id: openai-math-181
record_type: family
title: Overlap potentials and low-error vertex folding
source_family: '181'
source_collection: openai/math
batch_id: B012
subject: Combinatorics
source_paper_ids:
- P-000121
instrument_ids:
- MI-000200
- MI-000201
headline: The source claims an absolute constant C such that every finite simple graph on n vertices has
  an edge partition into at most Cn simple cycles and single edges.
central_instrument: A logarithmic potential pays for vertex duplication across recursive splits. Random
  pairings compress graph order while an explicit collision budget preserves a simple quotient.
novelty_assessment: Sparse-cut recursion and first-moment collision counting are established. The selected
  candidate refinements are the overlap-sensitive potential and the folding hypotheses that control external
  common neighbors.
formalization_summary: CycleDecomposition.lean states existence of an absolute positive linear constant
  for an exact edge partition into simple cycles and single edges, including edgeless graphs. It does
  not optimize the constant. Scope documents and Comparator declarations were compared. No Lean solution
  was built or kernel-checked; the extracted auxiliary results are not separately certified targets.
statement_faithfulness: Logarithms in the source are base two. Split pieces may overlap in vertices, counted
  with multiplicity. Folding preserves isolated quotient vertices and requires neighbor bounds at vertices
  outside the folding sets too.
dependencies: Recursive potential accounting; sparse vertex separators; uniform perfect pairings with
  a dummy vertex in odd size; loop and parallel-edge collision counts.
antecedents: Conlon, Fox and Sudakov use sparse-cut charging in cycle decomposition. The probabilistic
  method and quotient cleanup are classical; the selected bookkeeping is specific to the source.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Overlap potentials and low-error vertex folding

## Source manuscript and claim

[A linear cycle-and-edge decomposition of every graph](../papers/P-000121.md), by OpenAI, September 24, 2026.

The source claims an absolute constant C such that every finite simple graph on n vertices has an edge partition into at most Cn simple cycles and single edges.

## Extracted instruments

- [MI-000200: A reciprocal-logarithm potential pays for overlapping recursive pieces](../instruments/MI-000200.md)
- [MI-000201: Random pair folding makes a simple quotient with a linear collision budget](../instruments/MI-000201.md)

## Dependencies and antecedents

Recursive potential accounting; sparse vertex separators; uniform perfect pairings with a dummy vertex in odd size; loop and parallel-edge collision counts.

Conlon, Fox and Sudakov use sparse-cut charging in cycle decomposition. The probabilistic method and quotient cleanup are classical; the selected bookkeeping is specific to the source. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the overlap-potential argument and complete pair-folding proof. The full routing, batch-resolution and induction arguments were not audited.

CycleDecomposition.lean states existence of an absolute positive linear constant for an exact edge partition into simple cycles and single edges, including edgeless graphs. It does not optimize the constant. Scope documents and Comparator declarations were compared. No Lean solution was built or kernel-checked; the extracted auxiliary results are not separately certified targets.

Logarithms in the source are base two. Split pieces may overlap in vertices, counted with multiplicity. Folding preserves isolated quotient vertices and requires neighbor bounds at vertices outside the folding sets too.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/181.md) · [Batch record](../../batches/B012/README.md)
