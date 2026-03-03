# Analysis Directory

This directory contains scripts for automated PSO identification and pattern analysis.

## Files

### `pso_identification.py`
Python script for automated identification of Parasitic Spontaneous Order (PSO) patterns in journal invitations.

**Features:**
- Loads invitations corpus from CSV
- Calculates PSO Index scores
- Identifies patterns across dimensions
- Generates classification report

**Dependencies:**
- pandas
- numpy
- scikit-learn (optional, for clustering)

**Usage:**
```bash
python pso_identification.py
```

**Output:**
- Console report with PSO classifications
- Optional: visualization plots
- Optional: export results to CSV

## Methodology

The PSO Index is calculated across 5 binary dimensions:

1. **Disciplinary Mismatch** (0/1)
   - Paper field ≠ Journal field
   
2. **Mimetic Legitimacy** (0/1)
   - Uses ISSN, DOI, "peer review" claims
   
3. **Emotional Hooks** (0/1)
   - Flattery, urgency, scarcity language
   
4. **Friction Minimization** (0/1)
   - Email submission, rapid review promises
   
5. **Automation Indicators** (0/1)
   - Template errors, exact title scraping, phantom follow-ups

**Scoring:**
- PSO Index = Sum of dimensions (0-5)
- **Threshold:** ≥4 → PSO confirmed
- **3:** Suspicious, requires manual review
- **≤2:** Likely legitimate

## Future Enhancements

- Machine learning classifier training
- NLP-based automatic pattern detection
- Integration with DOAJ/Scopus APIs for venue validation
- Real-time email scanner plugin
