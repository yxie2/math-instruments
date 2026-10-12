# Record format

Records are Markdown files with a YAML metadata block between `---` lines at the beginning. The body contains the mathematical description and source discussion.

All records require `id`, `record_type`, `title`, `batch_id`, and `updated`. See the [templates](../templates/README.md) for the fields used by each record type.

| Record type | Identifier | Relationships |
|---|---|---|
| Instrument | `MI-` followed by six digits | `family_ids`, `source_paper_ids`, `case_study_ids` |
| Paper | `P-` followed by six digits | `family_ids` |
| Family | Collection-qualified identifier, initially `openai-math-NNN` | `source_paper_ids`, `instrument_ids` |
| Pattern | `PAT-` followed by three digits | Linked examples in the body |
| Batch | `B` followed by three digits | `family_ids`, `instrument_ids`, `paper_ids` in `manifest.yaml` |
| Case study | `CS-` followed by three digits | `instrument_ids` in `metadata.yaml` |

Identifiers are stable and must not be recycled. Family and instrument associations are reciprocal. A source-paper association may identify family context; `source_binding` and the description distinguish that from exact manuscript attribution.

`review_status` and `novelty_status` describe recorded evidence. They must not be silently upgraded by an import or format conversion. The body records the scope of the assessment and its supporting references.

`scripts/validate_catalog.py` checks identifiers, references, reciprocal associations, local links, batch membership, fixed source hashes and the freshness of generated views. It validates catalogue consistency, not mathematical proofs.
