---
id: openai-math-087
record_type: family
title: The Mahler conjectures
source_family: 087
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Analysis and geometry
source_paper_ids:
- P-000053
- P-000060
- P-000071
instrument_ids:
- MI-000016
- MI-000017
- MI-000018
headline: Mahler conjecture, symmetric and general
central_instrument: Replace each real strip by a complex lens with uniform boundary coordinate (Gross’s conformal Skorokhod map); push Lelong-number Jacobian mass to the boundary as $`k\to\infty`$; the volume product becomes a sum of feasibility probabilities over signed simplices packing inside the polar.
novelty_assessment: new feasible-simplex identity; rest combination
formalization_summary: 'original: symmetric; general/polar modules supplied, unbuilt'
statement_faithfulness: symmetric statement only in initial extraction
dependencies: 'no'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: 'original inspection: symmetric Lean coverage only; broader solution modules supplied, unbuilt new identity'
map_formalization_summary: symmetric
---

# The Mahler conjectures

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000053](../papers/P-000053.md)
- [P-000060](../papers/P-000060.md)
- [P-000071](../papers/P-000071.md)

## Family description

Source status as recorded in the direction paper: original inspection: symmetric Lean coverage only; broader solution modules supplied, unbuilt new identity

For origin-symmetric convex bodies $`K\subset\mathbb R^n`$, the source claims $`|K||K^\circ|\ge4^n/n!`$, with equality for linear images of Hanner polytopes. For general convex bodies, use the Santaló point $`s(K)\in\operatorname{int}K`$ and define
``` math
P(K)=|K|\,|(K-s(K))^\circ|.
```
The general claim is $`P(K)\ge(n+1)^{n+1}/(n!)^2`$, with equality exactly for simplices; for a simplex its Santaló point is its centroid. Thus the equality statement for the polar is made after the indicated centering. In the symmetric case $`s(K)=0`$. The third source claims $`c_G(\operatorname{int}K\times\operatorname{int}K^\circ)=4`$ for origin-symmetric $`K\subset\mathbb R^n`$ and $`n\ge2`$, with embeddings at every capacity strictly below 4. The initial extraction inspected symmetric formalization coverage only. The snapshot also supplies general-Mahler and symmetric-polar solution modules; a `sorry` in a comparator challenge is a statement placeholder, not evidence that the separate solution module is a stub. None was built here.

## Extracted instruments.

- [MI-000016: The conformal lens](../instruments/MI-000016.md)

- [MI-000017: Holomorphic mass pushed to the boundary](../instruments/MI-000017.md)

- [MI-000018: Feasible-simplex identity](../instruments/MI-000018.md)

## Reused.

Gross 2019; Demailly; Cauchy–Binet; Hanner’s formulas; Lima and Hansen–Lima (the Lean reproves the median-to-Hanner step itself); Fradelizi–Meyer; Klartag 2018 for the general case.

## Caveats.

The general-body argument uses about twenty selected decimal constants and SymPy certificates. Its reasoning summary leaves the conclusion dependent on uniform scalar inequalities. The symmetric paper presents a self-contained argument without that qualification.

## Recorded assessment

- Novelty: new feasible-simplex identity; rest combination
- Formalization: original: symmetric; general/polar modules supplied, unbuilt
- Statement coverage: symmetric statement only in initial extraction
- Dependencies: no
- Antecedents: —
