---
id: openai-math-156
record_type: family
title: Borsuk’s conjecture fails in dimension 9
source_family: '156'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Combinatorics, geometry and complexity
source_paper_ids:
- P-000018
instrument_ids:
- MI-000086
- MI-000087
- MI-000088
headline: Borsuk’s conjecture fails in dimension 9
central_instrument: 'The set of rank-one projectors of $`\mathbb{R}^{4}`$ (a copy of $`\mathbb{R}P^3`$ in $`\mathbb{R}^{9}`$) needs at least 11 pieces: an “odd spectral extension” turns any 10-cover into an odd map between 9-spheres, and degree analysis at the tight Borsuk–Ulam bound forces a 10-vertex $`\mathbb{R}P^3`$-like complex that cannot exist.'
novelty_assessment: combination leaning new
formalization_summary: files, exact reals
statement_faithfulness: yes, compact set, diam $\sqrt{2}$, no ten-cover
dependencies: no (unrefereed GitHub note cited, not used)
antecedents: Ky Fan-type refinements
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, 275 files, exact real arithmetic combination leaning new
map_formalization_summary: 'yes'
---

# Borsuk’s conjecture fails in dimension 9

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000018](../papers/P-000018.md)

## Family description

Source status as recorded in the direction paper: Lean, 275 files, exact real arithmetic combination leaning new

The set X of rank-one projectors $`uu^{\mathsf T}`$, $`|u|=1`$, in the trace-one affine hyperplane of $`\mathrm{Sym}_4(\mathbb{R})`$, which is isometric to $`\mathbb{R}^9`$ under the Frobenius metric, has diameter $`\sqrt{2}`$ and cannot be covered by ten sets of smaller diameter, so $`b(X)\ge 11>10`$; by adjoining points, Borsuk fails for all $`d \ge 9`$. The previous range cited by the initial extraction was $`d \ge 64`$ (Jenrich–Brouwer). The witness is a compact copy of $`\mathbb{R}P^3`$, not a finite set; no finite 9-dimensional counterexample follows.

## Extracted instruments.

- [MI-000086: Odd spectral extension of an admissible map](../instruments/MI-000086.md)

- [MI-000087: Equality-case degree analysis](../instruments/MI-000087.md)

- [MI-000088: Six-label triangle systems](../instruments/MI-000088.md)

## Reused.

Projector embedding (Conway–Hardin–Sloane); partitions of unity; Sard; Borsuk–Ulam; mod-2 local degree; Stiefel–Whitney classes; Hinrichs–Richter point adjoining.

## Caveats.

The counterexample is continuous and does not settle finite-set Borsuk in $`\mathbb{R}^{9}`$. Its convex hull gives a convex-body counterexample, a consequence not discussed in the source. The paper cites an unrefereed AI-assisted GitHub note by Grinsztajn concerning dimension 63, without using it as an input. The literature comparison was limited.

## Recorded assessment

- Novelty: combination leaning new
- Formalization: files, exact reals
- Statement coverage: yes, compact set, diam $\sqrt{2}$, no ten-cover
- Dependencies: no (unrefereed GitHub note cited, not used)
- Antecedents: Ky Fan-type refinements
