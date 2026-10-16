---
id: openai-math-098
record_type: family
title: Separated scales, derivative rigidity and compact metric obstructions
source_family: 098
source_collection: openai/math
batch_id: B003
subject: Convex and metric geometry
source_paper_ids:
- P-000088
instrument_ids:
- MI-000130
- MI-000131
- MI-000132
headline: The source claims a fixed doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding
  and a compact obstruction in every infinite-dimensional real Banach space.
central_instrument: A sparse-scale sheet construction has bounded local covering complexity; lexicographic
  derivative extrema and crossings force arbitrarily large finite-dimensional packings.
novelty_assessment: Candidate construction and proof assembly for the Hilbert case; differentiation, packing,
  finite-witness compactness and Dvoretzky are established inputs. No exhaustive priority audit is claimed.
formalization_summary: The DoublingHilbert Comparator specifies doubling constant 76800 for one fixed
  Hilbert subset. CompactBanach specifies a universal constant for compact subsets of all infinite-dimensional
  real Banach spaces and excludes all finite-dimensional normed targets. No Lean solution was built.
statement_faithfulness: The initial sheet space has finite-support displacement tuples and is not asserted
  compact. Compactness is obtained by a separate finite-witness assembly. The set is chosen before the
  target dimension and distortion.
dependencies: Euclidean Rademacher differentiation, Lebesgue differentiation, compactness of derivative
  data, line integration, variance identities, finite-dimensional packing and the finite-dimensional Dvoretzky
  theorem.
antecedents: Lang–Plaut formulate the Hilbert problem; Lafforgue–Naor and others give related obstructions
  above exponent two; Laakso supplies separation-versus-stretch precedents. The source distinguishes a
  withdrawn Schioppa preprint.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Separated scales, derivative rigidity and compact metric obstructions

## Source manuscript and claim

[A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding](../papers/P-000088.md), by OpenAI, September 25, 2026.

The source claims a fixed doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding and a compact obstruction in every infinite-dimensional real Banach space.

## Extracted instruments

- [MI-000130: Separated displacement scales keep unbounded sheet multiplicity uniformly doubling](../instruments/MI-000130.md)
- [MI-000131: Lexicographic derivative extrema turn crossing sheets into a packing obstruction](../instruments/MI-000131.md)
- [MI-000132: Finite Hilbert obstructions can be assembled into a compact obstruction in any Banach space](../instruments/MI-000132.md)

## Dependencies and antecedents

Euclidean Rademacher differentiation, Lebesgue differentiation, compactness of derivative data, line integration, variance identities, finite-dimensional packing and the finite-dimensional Dvoretzky theorem.

Lang–Plaut formulate the Hilbert problem; Lafforgue–Naor and others give related obstructions above exponent two; Laakso supplies separation-versus-stretch precedents. The source distinguishes a withdrawn Schioppa preprint. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the construction, covering estimate, derivative-energy argument, crossing argument and compact transfer. Checked covering constants and the abstract compactness/packing implications. This is selected argument review, not an independent formal certification of the source theorem.

The DoublingHilbert Comparator specifies doubling constant 76800 for one fixed Hilbert subset. CompactBanach specifies a universal constant for compact subsets of all infinite-dimensional real Banach spaces and excludes all finite-dimensional normed targets. No Lean solution was built.

The initial sheet space has finite-support displacement tuples and is not asserted compact. Compactness is obtained by a separate finite-witness assembly. The set is chosen before the target dimension and distortion.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/098.md) · [Batch record](../../batches/B003/README.md)
