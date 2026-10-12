# Contributing

Contributions can add an extracted instrument, improve a source comparison, correct a mathematical statement, or document an application. Use a pull request for an edit and an issue for a question or proposed investigation.

## Add an extraction

1. Read the [extraction method](methodology/extraction.md) and choose the source manuscript and version.
2. Check the [instrument index](tables/instruments.md) for an existing entry. Reuse its identifier when correcting or extending the same instrument.
3. Copy the appropriate [template](templates/README.md) into `catalog/`. Allocate the next unused identifier; never renumber existing records.
4. Record the full statement or construction, hypotheses, parameters, source locator, role in the original proof, antecedents and qualifications. Keep proposed extensions separate from the extracted claim.
5. Add or update the paper and family records. Update their reciprocal instrument and paper links.
6. Create or update a batch manifest under `batches/`, listing all added or revisited records. A later batch may revisit an existing family.
7. Regenerate the tables and exports, validate, and describe the change in `CHANGELOG.md`.

```sh
python -m pip install -r requirements.txt
python scripts/build_indexes.py
python scripts/validate_catalog.py
```

The canonical records are Markdown files with YAML front matter. Edit those records; files marked as generated in `tables/` and `exports/` are derived views. The historical edition under `editions/` stays fixed.

## Evidence and attribution

Source references should identify a public manuscript, version or commit, and a theorem, lemma, equation, page or section where available. State which claims are from the source and which are your own deductions. Give hypotheses and parameter restrictions the same prominence as conclusions.

Record novelty comparisons, mathematical review, formalization and applications separately. Supply the scope and evidence for any new review status. A successful computation is not automatically a proof, and supplied Lean files are not automatically a checked development.

Keep credit for source authors and prior work. Contributions of original material use this repository's Apache-2.0 license; preserve the applicable notices for third-party material. Link to a source paper rather than adding an unrelated collection of PDFs.

## Add a case study

Use the [case-study template](templates/case-study.md). Identify the exact instrument inputs, adaptations, target problem, result, assumptions and public evidence. Update each input instrument's `case_study_ids` and `reuse_status`.

## Corrections

Explain the old statement, the correction and its source. Preserve identifiers so citations remain useful. An instrument may remain in the catalogue with a corrected, disputed or withdrawn status; do not silently erase its history.
