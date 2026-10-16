---
id: openai-math-190
record_type: family
title: Rigid binary anchors and repair obstructions from shared leaves
source_family: '190'
source_collection: openai/math
batch_id: B013
subject: Combinatorics
source_paper_ids:
- P-000125
instrument_ids:
- MI-000208
- MI-000209
headline: The source claims failure of every polynomial induced ordered-matrix removal bound for one explicit
  66-by-66 binary pattern, allowing arbitrary binary edits.
central_instrument: A dense anchor with a shattering corner forces every copy into one designated mode.
  Correlated tree-path sampling avoids protected edits while opposite bit constraints propagate to one
  shared leaf.
novelty_assessment: Anchoring, bounded trace complexity and edit-distance lower bounds are established
  themes. The candidate combination is a fixed binary anchor with opposite tree orders and a shared-leaf
  contradiction; hitting old copies is explicitly separated from repairing the matrix.
formalization_summary: MatrixRemoval.lean defines the explicit 66-by-66 pattern, increasing row and column
  maps, exact zero-and-one matching, arbitrary Hamming edits and failure of every positive polynomial
  lower bound on normalized copies. Scope text and Comparator statements were compared. No Lean solution
  was built or kernel-checked; the auxiliary instruments are not separate certified targets.
statement_faithfulness: Rows and columns are independently ordered. Every pattern entry, including zero,
  must match. The edit lower bound permits changing either bit value and does not assume original-copy
  hitting is a repair.
dependencies: Dense and distinct anchor rows and columns; bounded unions of suffix traces; binary tree
  position orders; uniform marginals with shared path indices; a cellwise union bound and bit propagation.
antecedents: Alon and Ben-Eliezer state the ordered binary-matrix polynomial-removal question and distinguish
  ordered from permutation-invariant settings. Earlier ternary lower bounds do not settle this binary
  construction.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Rigid binary anchors and repair obstructions from shared leaves

## Source manuscript and claim

[Polynomial removal fails for ordered binary matrices](../papers/P-000125.md), by OpenAI, September 25, 2026.

The source claims failure of every polynomial induced ordered-matrix removal bound for one explicit 66-by-66 binary pattern, allowing arbitrary binary edits.

## Extracted instruments

- [MI-000208: A shattering corner and dense prefix force an ordered binary anchor into one mode](../instruments/MI-000208.md)
- [MI-000209: Protected-cell sampling and opposite bit propagation separate copy hitting from repair](../instruments/MI-000209.md)

## Dependencies and antecedents

Dense and distinct anchor rows and columns; bounded unions of suffix traces; binary tree position orders; uniform marginals with shared path indices; a cellwise union bound and bit propagation.

Alon and Ben-Eliezer state the ordered binary-matrix polynomial-removal question and distinguish ordered from permutation-invariant settings. Earlier ternary lower bounds do not settle this binary construction. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full construction, anchor pinning, copy count and arbitrary-edit distance proofs. Finite checks exercise the anchor and body mechanisms; they do not enumerate all 66-by-66 submatrices or all edits of a large constructed matrix.

MatrixRemoval.lean defines the explicit 66-by-66 pattern, increasing row and column maps, exact zero-and-one matching, arbitrary Hamming edits and failure of every positive polynomial lower bound on normalized copies. Scope text and Comparator statements were compared. No Lean solution was built or kernel-checked; the auxiliary instruments are not separate certified targets.

Rows and columns are independently ordered. Every pattern entry, including zero, must match. The edit lower bound permits changing either bit value and does not assume original-copy hitting is a repair.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/190.md) · [Batch record](../../batches/B013/README.md)
