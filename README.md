# Math Instruments

**Extraction, Curation, and Applications**

A growing collection of mathematical instruments extracted from OpenAI’s research papers, with source references, structured descriptions, and studies of subsequent applications.

The aim is to identify new lemmas, constructions, inequalities, objects, structures and proof mechanisms introduced in the source arguments. Extraction comes first; validity, novelty and possible reuse are then subjects for further study. The structured descriptions also give readers a route into the source papers.

## Direction paper

**Ying Xie — [What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics](https://zenodo.org/records/23319145)**. Preprint, 2026.

[Research direction](direction/README.md) · [Extraction method](methodology/extraction.md) · [How to cite](CITATION.cff)

[Find an instrument for your problem](methodology/research-guide.md): a guide to exact constraints, adaptive choices and operator estimates, with concrete starting points and the hypotheses needed for reuse.

## Browse the collection

<!-- catalogue-navigation:start -->

| Browse | Contents |
| --- | --- |
| [Mathematical instruments](tables/instruments.md) | 799 extracted entries, each with a stable identifier |
| [Source papers](tables/papers.md) | 526 manuscript records across the selected families |
| [Problem families](tables/families.md) | 372 family accounts with claims, antecedents and caveats |
| [Recurring patterns](catalog/patterns/README.md) | 14 approaches connecting the source arguments |
| [Tables and review status](tables/README.md) | Family maps, formalization, dependencies and antecedents |
| [Extraction batches](batches/README.md) | Extraction rounds and source versions |
| [Release coverage](tables/coverage.md) | 372 of 372 families catalogued; 0 pending |
| [Use case studies](case-studies/README.md) | Subsequent investigations using extracted instruments |
| [Catalogue exports](exports/README.md) | JSON and CSV for search and further analysis |

<!-- catalogue-navigation:end -->

## A use case: stationary descent

How can a stationary process move downward on almost every step, and how much dependence must that behavior retain? [CS-002: Stationary descent and its information cost](case-studies/CS-002-stationary-descent/README.md) follows two extracted instruments, MI-000098 and MI-000014, into this probability question. The study develops a sharp atomless information bound and an explicit finite-state optimum whose value is invariant under rearranging the state probabilities.

Read Ying Xie's preprint, [From Extracted Instruments to Mathematical Insight: A Case Study in Stationary Descent](https://zenodo.org/records/23408425), for the exploration, proofs, physical interpretation and comparison with earlier work. It illustrates how researchers can select a mechanism from the catalogue, adapt the question and investigate the resulting mathematics; historical priority of the finite formula remains unresolved.

## Extraction releases

The catalogue continues beyond the direction paper through [numbered extraction batches](batches/README.md), covering quantum information, geometric inequalities, dimension reduction and analytic mechanisms. Each new batch records exact source locations, targeted antecedent comparisons and the scope of its checks. The [coverage table](tables/coverage.md) now accounts for **all 372 October-release families**, with selected instruments from each family. The catalogue contains **799 instruments and 526 manuscript records**; this does not mean all 719 release manuscripts received a complete extraction or proof review.

The [completion checkpoint and audit](sources/runs/2026-10-16-completion/README.md) record the final 161 families, 328 added instruments and 40 merged batches. All 84 finite verification programs passed a fresh run; the provenance audit matched 1,618 source files and 1,586 label bindings. The [earlier October 16 checkpoint](sources/runs/2026-10-16/README.md) remains available as a historical record.

Batch B001 imports the direction manuscript’s 38 family entries and all 115 instrument descriptions. The 81 source-paper records include related and companion manuscripts; 81 is a source-coverage count, not a count of separately extracted papers. The initial maps and all four manuscript tables are retained in the [fixed import edition](editions/zenodo-23319145/README.md).

The source is the public [OpenAI mathematics repository](https://github.com/openai/math), pinned to revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` for B001. Its initial release contained 722 manuscripts; the inspected snapshot contains 719 after three withdrawals. This project is maintained independently by Ying Xie.

The descriptions retain the source claims, qualifications and preliminary novelty assessments. Inclusion does not establish novelty or certify a proof. [Assessment and evidence](methodology/assessment.md) explains the separate treatment of mathematical review, formalization and reuse.

## Grow the catalogue

Use the [record templates](templates/README.md) and [contribution guide](CONTRIBUTING.md) to add instruments, source comparisons, corrections or case studies. Keep existing identifiers when updating an entry. A later batch can revisit an existing family or introduce new families.

```sh
python -m pip install -r requirements.txt
python scripts/build_indexes.py
python scripts/validate_catalog.py
```

## Citation and attribution

Cite the [direction paper](https://zenodo.org/records/23319145) for this research approach, identify the repository release or commit when using its curated records, and cite the linked source manuscripts for their mathematical contributions. Source references and hashes are recorded under [sources/](sources/README.md).

Maintainer: **Ying Xie**, Kennesaw State University — yxie2@kennesaw.edu.

See [LICENSE](LICENSE), [NOTICE](NOTICE), and the [changelog](CHANGELOG.md).
