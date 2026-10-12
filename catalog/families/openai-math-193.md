---
id: openai-math-193
record_type: family
title: Serre’s positivity conjecture
source_family: '193'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Number theory and arithmetic geometry
source_paper_ids:
- P-000048
instrument_ids:
- MI-000065
- MI-000066
- MI-000067
headline: Serre positivity in ramified mixed characteristic
central_instrument: '“Rank quotient”: sequences of finite-length modules along the p-power-root tower modulo negligible normalized rank, packaged as perfect complexes over a connective algebra so K-theoretic descent acts on asymptotic perfectoid data; ordinary and perfectoid Euler characteristics compared only after Galois norms.'
novelty_assessment: new device
formalization_summary: 'no'
statement_faithfulness: —
dependencies: no (Lech paper cited as related)
antecedents: Suslin–Voevodsky orbit lemma
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: not formalized new device
map_formalization_summary: 'no'
---

# Serre’s positivity conjecture

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000048](../papers/P-000048.md)

## Family description

Source status as recorded in the direction paper: not formalized new device

For a commutative Noetherian regular local ring $`R`$ of dimension $`d`$ and nonzero finitely generated $`R`$-modules $`M,N`$ with $`\ell_R(M\otimes_R N)<\infty`$ and $`\dim_R M+\dim_R N=d`$, the source claims $`\chi^R(M,N)=\sum_{i=0}^d(-1)^i\ell_R(\mathrm{Tor}_i^R(M,N))>0`$, without a restriction on characteristic or ramification. The previously open case was ramified mixed characteristic $`V[[x]]/(p-f)`$, $`p\in\mathfrak m^2`$, which Bhatt–Hochster–Ma still called “the most tantalizing problem that remains”. Load-bearing external inputs (Cai–Lee–Ma–Schwede–Tucker perfectoidization results, Land–Tamme cdh descent for truncating invariants, Ma’s Frobenius vanishing) were compared with their arXiv statements in the initial extraction.

## Extracted instruments.

- [MI-000065: Supported rational descent](../instruments/MI-000065.md)

- [MI-000066: Rank quotient and supported asymptotic complexes](../instruments/MI-000066.md)

- [MI-000067: Two norm comparisons instead of invariance of individual evaluations](../instruments/MI-000067.md)

## Reused.

Serre’s reduction to prime pairs via Roberts and Gillet–Soulé vanishing; Cohen–Gabber normalization; Faltings normalized length; CLMST perfectoidization in mixed characteristic and perfection plus Monsky and Roberts in characteristic p; Bhatt–Hochster–Ma’s “only $`H_{0}`$ survives” mechanism via a Koszul-polynomial trick.

## Caveats.

The argument relies on several results from 2022–2026. Further checking should focus on the Verdier-quotient identification $`\simeq\mathrm{Perf}(H)`$ and its base change, spectral sequences on idempotent summands that need not lift to chain maps, and the interaction between ultralimits and ordinary limits. A December 2025 AI-generated note had already asserted the prime-quotient form; the paper treats it as a claim rather than an established theorem. The initial extraction retrieved primary sources directly but did not complete fresh searches for this family.

## Recorded assessment

- Novelty: new device
- Formalization: no
- Statement coverage: —
- Dependencies: no (Lech paper cited as related)
- Antecedents: Suslin–Voevodsky orbit lemma
