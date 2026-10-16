# B045 — Cross-family curation and reproducibility audit

This curation round adds three patterns and a [research guide](../../methodology/research-guide.md) to help readers choose instruments by the obstacle in their own proof. It adds no instrument, family or manuscript count.

- [Preserve exact constraints through approximation](../../catalog/patterns/preserve-exact-constraints-through-approximation.md)
- [Control what an adaptive choice can observe](../../catalog/patterns/control-what-an-adaptive-choice-can-observe.md)
- [Match operator estimates to their domain and order](../../catalog/patterns/match-operator-estimates-to-their-domain.md)

The connections are methodological comparisons. They do not assert a new common theorem, an independently verified application or historical priority.

## October 16 checkpoint

The expansion B002–B044 adds 348 instrument records from 169 previously uncatalogued families and 169 source manuscripts. Including B001, the catalogue has 463 instruments, 250 manuscript records and 207 of the release's 372 families. The remaining 165 families are visible in the [coverage table](../../tables/coverage.md). B001's 81 manuscript records include related and companion papers; manuscript counts do not mean that every paper received a separate complete extraction.

All 43 new verification programs passed a fresh run from isolated copies. The provenance audit matched 754 distinct source-file hashes and 902 exact label-line bindings across 43 source manifests. The fixed direction-paper edition is unchanged from the starting repository commit `cd0f7b4`. The machine-readable [audit summary](verification/audit-summary.json) records the program hashes and outcomes.

Each extraction PR passed the repository's catalogue CI before merge. CI checks catalogue structure, references, generated views and the fixed edition; it does not build Lean proofs or rerun the mathematical programs. The aggregate audit is a separate run.

The selected source arguments, finite calculations, Comparator inspection and historical comparisons have different scopes. They are described in each batch and card. Neither this audit nor a catalogued-family status certifies the source headline theorem. No Lean solution was built or kernel-checked in this run.

## Reproduce the finite checks

Install the catalogue and verification dependencies, then run:

```sh
python -m pip install -r requirements.txt -r batches/verification-requirements.txt
python scripts/check_batches.py --output verification-runs/october-check
python scripts/validate_catalog.py
```

The runner copies each verification directory, including bundled data, into the output directory and writes fresh results there. It leaves the recorded batch results unchanged. B001 is an import and has no added mathematical verification program; B045 is curation and has none either.

Source hashes can be checked against a checkout or cache of the pinned upstream files with `python scripts/check_source_bindings.py --source-root PATH`. The tool verifies the recorded bytes and exact label lines. It does not validate the mathematical statements in those files.
