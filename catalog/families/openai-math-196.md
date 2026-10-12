---
id: openai-math-196
record_type: family
title: Counterexample to Kaplansky’s zero-divisor conjecture
source_family: '196'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Algebra and operator algebras
source_paper_ids:
- P-000010
instrument_ids:
- MI-000040
- MI-000041
- MI-000042
headline: Counterexample to Kaplansky’s zero-divisor conjecture
central_instrument: Projective-plane label sets with pairwise odd intersections make every vertex of the “simultaneous-step” product graph odd-degree, so every component is even and the product vanishes mod 2. Collapse is excluded by a girth-conditioned random-matching estimate plus a Lipton–Tarjan reduction of planar pairings.
novelty_assessment: combination; separator step new
formalization_summary: files incl. the classifying complex
statement_faithfulness: 'yes'
dependencies: 'no'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, 124 files, includes finite 2-dim K(G,1) combination; separator step new
map_formalization_summary: 'yes'
---

# Counterexample to Kaplansky’s zero-divisor conjecture

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000010](../papers/P-000010.md)

## Family description

Source status as recorded in the direction paper: Lean, 124 files, includes finite 2-dim K(G,1) combination; separator step new

The source constructs a finitely presented torsion-free group with a finite two-dimensional classifying complex and nonzero $`\alpha`$, $`\beta`$ in $`\mathbb{F}_2[G]`$ with $`\alpha\beta=0`$. The construction is non-constructive: 8258 generators, a random graph on $`n\gtrsim e^{300000}`$ vertices. The initial extraction cites 2026 revisions by Mineyev and Shin that describe the conjecture as open.

## Extracted instruments.

- [MI-000040: Odd cross-intersection parity mechanism](../instruments/MI-000040.md)

- [MI-000041: Bounded-pattern estimate for a girth-conditioned random-matching model with prescribed types](../instruments/MI-000041.md)

- [MI-000042: Planar-separator extraction plus cone-picture band surgery](../instruments/MI-000042.md)

## Reused.

Graphical presentations; projective-plane incidence parity; configuration model with switchings; Ollivier’s density counting; Lipton–Tarjan; Brown’s periodic-resolution argument.

## Caveats.

The result concerns characteristic two and does not provide a concrete presentation. The source explicitly addresses quantifier order and the dependence introduced by conditioning. Its Lean development was not compiled here. A separate direct-finiteness manuscript dated 4 October adapts this machinery and is not formalized.

## Recorded assessment

- Novelty: combination; separator step new
- Formalization: files incl. the classifying complex
- Statement coverage: yes
- Dependencies: no
- Antecedents: —
