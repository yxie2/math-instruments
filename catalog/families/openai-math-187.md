---
id: openai-math-187
record_type: family
title: Finite envelope certificates for strategies against unrestricted replies
source_family: '187'
source_collection: openai/math
batch_id: B020
subject: Combinatorics
source_paper_ids:
- P-000154
instrument_ids:
- MI-000269
- MI-000270
headline: The source gives a strategy for planar Snaky within 21 actual Maker moves, with a 251-cell support
  inside a 17 by 17 board.
central_instrument: Conditional winning templates compose by owning the common intersection of child envelopes.
  The same algebra normalizes reduced envelopes, and a finite recursive certificate gives a bounded strategy
  against replies anywhere.
novelty_assessment: Territory-based proof trees and core/neighborhood situations precede the release in
  Sieben (2008). The 21-move certificate and its particular composition data are source-specific. This
  batch reconstructs that entire finite certificate; it does not certify optimality of the move bound.
formalization_summary: Read the scope and the definitions and targets in all three linked Comparators,
  excluding inspection of each literal entry in the older 35-move table. SnakyTwentyOne targets a legal
  21-move strategy; SnakyCertificate targets older 35-move reconstruction data. Although the scope table
  describes SnakyConditional as conditional templates, its actual selected statement is a global 35-move
  legal strategy. The 251-cell finite-board restriction is not in the 21-move target. These files specify
  targets with sorry placeholders; no Lean solution was built or kernel-checked.
statement_faithfulness: Every counted Maker move claims a fresh cell. Already-owned pivots require a fresh
  replacement move. Breaker may reply outside all envelopes. Heights decrease along chosen children; no
  final Breaker move is needed before winning.
dependencies: Finite set unions and intersections, square-grid isometries, recursive certificate parsing,
  induction on height and legal fresh-move bookkeeping.
antecedents: 'Sieben, Proof Trees for Weak Achievement Games (2008), Sections 2 and 3: territories, proof
  sequences and core/neighborhood situations.'
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite envelope certificates for strategies against unrestricted replies

## Source manuscript and claim

[Snaky in 21 Maker moves](../papers/P-000154.md), by OpenAI, None.

The source gives a strategy for planar Snaky within 21 actual Maker moves, with a 251-cell support inside a 17 by 17 board.

## Extracted instruments

- [MI-000269: Owned envelope intersections compose finite certificates against every reply](../instruments/MI-000269.md)
- [MI-000270: Reduced envelopes normalize exactly and commute with template composition](../instruments/MI-000270.md)

## Dependencies and antecedents

Finite set unions and intersections, square-grid isometries, recursive certificate parsing, induction on height and legal fresh-move bookkeeping.

Sieben, Proof Trees for Weak Achievement Games (2008), Sections 2 and 3: territories, proof sequences and core/neighborhood situations. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete composition, strategy, finite-board and reduced-normalization arguments, certificate grammar and short upstream verifier. Ran the upstream 21-move verifier and a separately written parser checking all nodes and local reply classes. The older 25- and 35-move tables were not reconstructed in this batch.

Read the scope and the definitions and targets in all three linked Comparators, excluding inspection of each literal entry in the older 35-move table. SnakyTwentyOne targets a legal 21-move strategy; SnakyCertificate targets older 35-move reconstruction data. Although the scope table describes SnakyConditional as conditional templates, its actual selected statement is a global 35-move legal strategy. The 251-cell finite-board restriction is not in the 21-move target. These files specify targets with sorry placeholders; no Lean solution was built or kernel-checked.

Every counted Maker move claims a fresh cell. Already-owned pivots require a fresh replacement move. Breaker may reply outside all envelopes. Heights decrease along chosen children; no final Breaker move is needed before winning.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/187.md) · [Batch record](../../batches/B020/README.md)
