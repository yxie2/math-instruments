---
id: openai-math-157
record_type: family
title: Counterexample to Hadwiger’s conjecture
source_family: '157'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Combinatorics and theoretical computer science
source_paper_ids:
- P-000012
- P-000014
- P-000017
instrument_ids:
- MI-000031
- MI-000032
- MI-000033
headline: Counterexample to Hadwiger’s conjecture
central_instrument: 'Algebraic “hole relation”: non-edges certified by a symmetric bilinear identity whose terms cancel around any triangle leaving $`0=1`$, so the complement is triangle-free. Connected matchings are excluded by an entropy-minimizing container argument.'
novelty_assessment: new
formalization_summary: files
statement_faithfulness: yes, Mathlib chromatic number and clique minors
dependencies: 'no'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, 276 files, no explicit graph new
map_formalization_summary: 'yes'
---

# Counterexample to Hadwiger’s conjecture

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000012](../papers/P-000012.md)
- [P-000014](../papers/P-000014.md)
- [P-000017](../papers/P-000017.md)

## Family description

Source status as recorded in the direction paper: Lean, 276 files, no explicit graph new

The source constructs arbitrarily large m-vertex graphs with independence number $`\le 2`$ and connected-matching number $`<m/100`$, where every pair of matching edges must have an edge between their endpoint sets. The resulting Hadwiger number is $`h(G)<26m/75+2/3`$, hence $`h(G)<0.347m`$ for sufficiently large $`m`$, while $`\chi\ge\chi_f\ge m/2`$. This would also refute the Reed–Seymour fractional weakening and the Füredi–Gyárfás–Simonyi connected-matching conjecture. Parameters: $`g=10^9+1`$, $`m=2^{1000\cdot g\cdot M_0\cdot n}`$; the Lean extracts m from an eventually-true filter statement.

## Extracted instruments.

- [MI-000031: The hole relation with tensor certification](../instruments/MI-000031.md)

- [MI-000032: Entropy-minimizing container argument](../instruments/MI-000032.md)

- [MI-000033: Scalar recipe / gradient realization / collision machine](../instruments/MI-000033.md)

## Reused.

Plummer–Stiebitz–Toft $`\alpha \le 2`$ reduction; Cambie’s connected-matching-to-minor count; Kleitman–Winston; Csiszár; Ford–Fulkerson; weak regularity; Laurent–Mourrain flat extension.

## Caveats.

The argument gives neither an explicit graph nor an explicit clique-minor number. Many subsequence/compactness steps are non-quantitative by design (“No exponential rate uniform over all stages is asserted”). Illingworth–Steiner’s separate result of 28 September 2026 disproves the dominating variant [source](../../direction/references.md#src:dominating), which requires a stronger kind of clique-minor model. A counterexample to that variant need not violate Hadwiger’s conjecture itself. Both constructions use graphs with $`\alpha\le2`$. The repository supplies a Lean development for the claim surveyed here, but it was not compiled for this survey.

## Recorded assessment

- Novelty: new
- Formalization: files
- Statement coverage: yes, Mathlib chromatic number and clique minors
- Dependencies: no
- Antecedents: —
