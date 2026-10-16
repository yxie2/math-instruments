# Completion of the remaining October-release families

Snapshot through **B047**, at `5cc26f51e4d9eede21a42bc19c82404f44e9f87b`. This continuation begins after the completed nine-hour run and has the requested target of selected extraction coverage for all 372 pinned release families.

At this snapshot: **479 instruments, 258 manuscript records, 215 families and 14 recurring patterns**. **157 families remain pending.** The [live coverage table](../../../tables/coverage.md) may include later batches.

| Batch | Families added | Instruments added | Manuscripts extracted | Publication |
| --- | --- | --- | --- | --- |
| [B047](../../../batches/B047/README.md) | 4 | 8 | 4 | [PR](https://github.com/yxie2/math-instruments/pull/49) |

The [machine-readable checkpoint](checkpoint.json) records merged batches and the next identifiers. The [earlier timed-run checkpoint](../2026-10-16/README.md) remains a separate historical record.

Starting with B047, source manifests explicitly distinguish extracted manuscripts from inventory-only companions. Each source passage must belong to its instrument's listed manuscript, and the companion partition must match the pinned inventory. Inventory-only status does not imply that a manuscript's arguments were read. The earlier inventory path for the CAT(0) companion in family 337 was corrected against the pinned source tree; release counts did not change.

Each batch records selected proof reads, primary-source comparisons and checks with their limitations. Numerical and finite algebraic checks do not certify the source headline theorems. Comparator target statements containing `sorry` are not successful Lean builds. No exhaustive novelty certification or independent human review is claimed. The fixed edition of the direction paper is unchanged.
