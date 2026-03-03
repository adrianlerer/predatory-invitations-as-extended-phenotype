# Data Directory

This directory contains structured data files for the analysis of predatory journal invitations.

## Files

### `invitations_corpus.csv`
Complete corpus of invitation emails analyzed in this study.

**Columns:**
- `case_id`: Unique identifier (1-8)
- `journal_name`: Name of the journal
- `publisher`: Publisher name
- `sender_name`: Name of email sender
- `sender_email`: Email address of sender
- `discipline_claimed`: Journal's claimed discipline
- `discipline_actual`: Actual paper discipline
- `issn_claimed`: ISSN provided in invitation
- `date_received`: Date of receipt
- `pso_score`: PSO Index score (0-5)

### `coding_matrix.csv`
Binary coding matrix for pattern identification.

**Columns:**
- `case_id`: Links to invitations_corpus
- `disciplinary_mismatch`: 0/1
- `mimetic_legitimacy`: 0/1
- `emotional_hooks`: 0/1
- `friction_minimization`: 0/1
- `automation_indicators`: 0/1
- `financial_extraction`: 0/1

### `pso_index_scores.csv`
Calculated PSO Index scores with component breakdown.

**Columns:**
- `case_id`: Links to invitations_corpus
- `mismatch_score`: 0-1
- `mimicry_score`: 0-1
- `hooks_score`: 0-1
- `friction_score`: 0-1
- `automation_score`: 0-1
- `pso_total`: Sum (0-5)
- `classification`: "LEGITIMATE" or "PSO"

## Data Processing

All data files are UTF-8 encoded CSV files with headers. Missing values are represented as `NA`.

## Privacy Note

All personally identifying information has been anonymized or pseudonymized. Email addresses are structural examples only (e.g., "editor@publisher.org").
