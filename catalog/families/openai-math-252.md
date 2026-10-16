---
id: openai-math-252
record_type: family
title: Finite-field rank lower bounds and punctured-line tensor certificates
source_family: '252'
source_collection: openai/math
batch_id: B030
subject: Group theory
source_paper_ids:
- P-000193
instrument_ids:
- MI-000348
- MI-000349
headline: The source claims a torsion-free word-hyperbolic group that is not residually finite.
central_instrument: Hadamard bounds and divisibility retain rank under reduction modulo a fixed prime.
  Low-degree interpolation on punctured lines assembles a block diagonal matrix from low-rank local matrices.
novelty_assessment: Hadamard determinant bounds, trace-based stable rank and finite-field power sums are
  classical. Their selected combination gives an explicit certificate conditional on the source incidence
  and group-presentation inputs; global non-residual-finiteness is not certified.
formalization_summary: Read TorsionFreeHyperbolic.lean. The target requires absence of nontrivial finite-order
  elements, uniformly thin geodesic Cayley triangles and failure of residual finiteness. The manuscript
  nonlinearity corollary is not part of that target. The inspected Comparator contains a sorry target;
  no Lean build or kernel verification was performed.
statement_faithfulness: The prime is larger than the squared row-norm bound; it need not be coprime to
  the finite group order. Every punctured line omits only its own mark, retaining other marks and exceptional-point
  incidences.
dependencies: Integer minors, Hadamard inequality, finite-field elimination, regular permutation traces,
  Lagrange interpolation and rank subadditivity.
antecedents: Classical determinant, stable-rank and finite-field polynomial identities; no claim of first
  priority for their assembly.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite-field rank lower bounds and punctured-line tensor certificates

## Source manuscript and claim

[A torsion-free hyperbolic group that is not residually finite](../papers/P-000193.md), by OpenAI, September 23, 2026.

The source claims a torsion-free word-hyperbolic group that is not residually finite.

## Extracted instruments

- [MI-000348: Retain matrix rank modulo a prime using row norms and determinant divisibility](../instruments/MI-000348.md)
- [MI-000349: Assemble a block diagonal rank certificate from low-degree punctured-line weights](../instruments/MI-000349.md)

## Dependencies and antecedents

Integer minors, Hadamard inequality, finite-field elimination, regular permutation traces, Lagrange interpolation and rank subadditivity.

Classical determinant, stable-rank and finite-field polynomial identities; no claim of first priority for their assembly. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full rank-under-reduction proof and trace calculation, local factorization interface and global tensor certificate. The random incidence construction, link conditions and geometric hyperbolicity/torsion arguments were not audited.

Read TorsionFreeHyperbolic.lean. The target requires absence of nontrivial finite-order elements, uniformly thin geodesic Cayley triangles and failure of residual finiteness. The manuscript nonlinearity corollary is not part of that target. The inspected Comparator contains a sorry target; no Lean build or kernel verification was performed.

The prime is larger than the squared row-norm bound; it need not be coprime to the finite group order. Every punctured line omits only its own mark, retaining other marks and exceptional-point incidences.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/252.md) · [Batch record](../../batches/B030/README.md)
