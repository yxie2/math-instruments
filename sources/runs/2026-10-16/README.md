# October 16 extraction checkpoint

This checkpoint records the expansion through B046. The run was authorized for nine hours, from 04:54:25 to 13:54:25 UTC. The [machine-readable checkpoint](checkpoint.json) gives the actual snapshot time, source and catalogue commits, merged PRs, verification program hashes and remaining work.

| Catalogue measure | Starting catalogue | This checkpoint | Added |
| --- | ---: | ---: | ---: |
| Instruments | 115 | 471 | 356 |
| Source manuscript records | 81 | 254 | 173 |
| Problem families | 38 | 211 | 173 |
| Curated patterns | 11 | 14 | 3 |

The run published 44 extraction batches, B002–B044 and B046, plus the B045 curation round. All 45 batch PRs were merged after successful catalogue CI. B001 already contains the direction paper's original two groups of families; repository batch numbers should not be confused with those groups.

Coverage is **211 of 372 families**, leaving **161 pending**. This is selected-instrument coverage, not a claim that every paper or proof within each family has been audited. The [coverage table](../../../tables/coverage.md) and [batch index](../../../batches/README.md) give the full status.

## Evidence recorded

- All 44 added finite verification programs passed a fresh run from isolated copies, including bundled data.
- All 764 distinct cited source-file hashes and 911 exact TeX-label locations matched the pinned source cache.
- Catalogue identifiers, cross-references, generated exports and local links passed validation.
- The fixed direction-paper edition is unchanged from starting commit `cd0f7b4`.
- No Lean solution was built or kernel-checked, and no source headline theorem is certified by these checks. Antecedent comparisons were targeted rather than exhaustive.

Thirty-nine rerun result files matched the recorded JSON exactly. The five earliest batches recorded NumPy 2.4.4 and were rerun with 2.5.4. Three numerical summaries changed only at floating-point rounding scale, at most about $3\times10^{-16}$ in absolute value; all their assertions passed. The original recorded results are preserved.

## How to use the expansion

The [research guide](../../../methodology/research-guide.md) starts from proof obstacles, then points to instruments and the hypotheses required for transfer. Three patterns connect exact constraint preservation, adaptive information and operator domains. The [hypothesis controls](../../../methodology/hypothesis-controls.md) provide explicit small counterexamples to several unjustified shortcuts.

The source manifests retain exact locations and hashes; each card separates mathematical content, source role, antecedents, checks, limitations and proposed applications. Curation does not convert a proposed use into a demonstrated result.

## Resume point

The next available identifiers are **B047**, **MI-000472** and **P-000255**. Candidate next families are 339, 344, 345 and 349, covering entropy rigidity, the metric Blaschke problem, closed geodesics and least-volume geometry. They remain pending, and this checkpoint makes no extraction or correctness claim about them.

Use `scripts/check_batches.py` and `scripts/check_source_bindings.py` to repeat the respective checks; instructions are in [B045](../../../batches/B045/README.md). Later work should retain the pinned source version or explicitly record a new version and compare the affected passages.
