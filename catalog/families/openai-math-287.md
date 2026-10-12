---
id: openai-math-287
record_type: family
title: All free group factors are isomorphic
source_family: '287'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Algebra and operator algebras
source_paper_ids:
- P-000024
instrument_ids:
- MI-000050
- MI-000051
- MI-000052
headline: All free group factors isomorphic; fundamental group $`\mathbb{R}_{+}`$
central_instrument: '“Small cocycle with a prescribed word value”: a Fox-derivative cocycle $`\ell^{2}`$-tiny on each generator that accumulates a full unitary factor on a long word with free prefixes, because spectral cutoffs of the prefix-sum operator give approximate inverses in the required vector norm (the limiting free Poisson law has no atom at 0). A trace-preserving flow then absorbs a generator.'
novelty_assessment: combination
formalization_summary: modules, in docs not catalogue
statement_faithfulness: reads faithful
dependencies: no (family 298 later, uncited)
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, 77 modules, in docs but not catalogue combination proves more than it states
map_formalization_summary: 'yes'
---

# All free group factors are isomorphic

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000024](../papers/P-000024.md)

## Family description

Source status as recorded in the direction paper: Lean, 77 modules, in docs but not catalogue combination proves more than it states

$`L(\mathbb{F}_n)\cong L(\mathbb{F}_{n+1})`$ for $`n \ge 3`$ by exhibiting a freely generating Haar n-tuple inside $`L(\mathbb{F}_{n+1})`$; $`L(\mathbb{F}_2)\cong L(\mathbb{F}_3)`$ via Dykema’s amplification at $`t=\sqrt{2}`$; Rădulescu’s dichotomy then makes all interpolated free group factors $`L(\mathbb{F}_r)`$, $`1<r\le\infty`$, isomorphic with fundamental group $`\mathbb{R}_{>0}`$. One consequence is that free entropy dimensions would not be generator invariants. The claim differs from expectations recorded in the initial extraction; Popa 2024 and Schafhauser–Tikuisis–White 2025 list the problem as open.

## Extracted instruments.

- [MI-000050: Small cocycle with a prescribed word value](../instruments/MI-000050.md)

- [MI-000051: Trace-preserving polynomial flow driven by conjugates of a bounded logarithm](../instruments/MI-000051.md)

- [MI-000052: Adaptive error budgets and L²-density  ⇒ W^(*)-generation](../instruments/MI-000052.md)

## Reused.

Voiculescu’s free probability; Fox calculus; Ricard–Xu Khintchine; cyclomorphy as a model; Nielsen moves; Dykema amplification and Rădulescu dichotomy (the Lean avoids both and proves $`L(\mathbb{F}_3)\cong L(\mathbb{F}_\infty)`$ directly).

## Caveats.

The claimed result would refute the Connes–Shlyakhtenko $`L^2`$-Betti conjecture for $`L(\mathbb{F}_n)`$; this consequence is not discussed in the source. A broader free-product absorption statement would require separate hypotheses and is not asserted here. The reasoning summary identifies trace preservation and limiting generation as dependencies.

## Recorded assessment

- Novelty: combination
- Formalization: modules, in docs not catalogue
- Statement coverage: reads faithful
- Dependencies: no (family 298 later, uncited)
- Antecedents: —
