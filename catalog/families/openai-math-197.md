---
id: openai-math-197
record_type: family
title: Counterexample to Kaplansky’s direct-finiteness conjecture
source_family: '197'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Algebra and operator algebras
source_paper_ids:
- P-000002
- P-000003
- P-000004
- P-000009
instrument_ids:
- MI-000043
- MI-000044
- MI-000045
- MI-000046
headline: Counterexample to Kaplansky’s direct-finiteness conjecture; a non-sofic group as a consequence
central_instrument: 'An “incidence criterion”: a hypergraph of degree $`\ell+1`$ and girth 12 plus vectors with block-sum 0 and total $`-I`$ yields $`ab=1,\ ba\ne1`$ after gluing copies of $`\mathbb{F}_\ell^2`$, averaging, character-twisted HNN packing, and a homomorphism to the field that exposes a rank-deficient Gram matrix.'
novelty_assessment: new criterion; parts combination
formalization_summary: files; search terminates at h ≤ 217
statement_faithfulness: yes (non-soficity excluded)
dependencies: type-F corollary only
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, 125 files, search certified at $`h \le 217`$ new criterion
map_formalization_summary: 'yes'
---

# Counterexample to Kaplansky’s direct-finiteness conjecture

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000002](../papers/P-000002.md)
- [P-000003](../papers/P-000003.md)
- [P-000004](../papers/P-000004.md)
- [P-000009](../papers/P-000009.md)

## Family description

Source status as recorded in the direction paper: Lean, 125 files, search certified at $`h \le 217`$ new criterion

The construction gives a finite field of characteristic two, a finitely presented group G with odd torsion, and a, b in K\[G\] with $`ab=1,\ ba\ne1`$. Such a group would be non-sofic by Elek–Szabó, and the construction would also contradict Gottschalk’s surjunctivity conjecture.

## Extracted instruments.

- [MI-000043: The incidence criterion](../instruments/MI-000043.md)

- [MI-000044: Polynomial pairing on a punctured affine space](../instruments/MI-000044.md)

- [MI-000045: Hole trades with random slabs and the local lemma](../instruments/MI-000045.md)

- [MI-000046: Character-twisted HNN packing and the sandwich certificate](../instruments/MI-000046.md)

## Reused.

Elek–Szabó for non-soficity; Dykema–Juschenko reduction; HNN embedding; Newton interpolation; Lovász local lemma; Linnik via Xylouris.

## Caveats.

The construction was not executed at the prescribed scale (q up to $`2^{217}`$, dimension $`\ge 1200`$); the certificate is algebraic. The Lean statement does not include non-soficity. The repository supplies a formalization for the odd-characteristic companion, but not for the torsion-free companion dated 4 October.

## Recorded assessment

- Novelty: new criterion; parts combination
- Formalization: files; search terminates at h ≤ 217
- Statement coverage: yes (non-soficity excluded)
- Dependencies: type-F corollary only
- Antecedents: —
