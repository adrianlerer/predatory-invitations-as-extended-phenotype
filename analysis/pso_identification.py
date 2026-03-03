#!/usr/bin/env python3
"""
PSO Identification Tool
Automated identification of Parasitic Spontaneous Order patterns in journal invitations

Author: Ignacio Adrián Lerer
License: CC BY 4.0
"""

import pandas as pd
import numpy as np
from pathlib import Path

def load_corpus(data_dir='../data'):
    """Load invitations corpus and coding matrix"""
    corpus = pd.read_csv(Path(data_dir) / 'invitations_corpus.csv')
    coding = pd.read_csv(Path(data_dir) / 'coding_matrix.csv')
    return corpus, coding

def calculate_pso_index(coding_matrix):
    """
    Calculate PSO Index for each invitation
    
    PSO Index = sum of binary indicators across 5 dimensions:
    - Disciplinary mismatch
    - Mimetic legitimacy
    - Emotional hooks
    - Friction minimization
    - Automation indicators
    
    Returns DataFrame with scores and classifications
    """
    dimensions = [
        'disciplinary_mismatch',
        'mimetic_legitimacy',
        'emotional_hooks',
        'friction_minimization',
        'automation_indicators'
    ]
    
    scores = coding_matrix[dimensions].sum(axis=1)
    classifications = scores.apply(lambda x: 'PSO' if x >= 4 else 
                                              'SUSPICIOUS' if x == 3 else 
                                              'LEGITIMATE')
    
    results = pd.DataFrame({
        'case_id': coding_matrix['case_id'],
        'pso_index': scores,
        'classification': classifications
    })
    
    return results

def generate_report(corpus, scores):
    """Generate human-readable analysis report"""
    merged = corpus.merge(scores, on='case_id')
    
    print("=" * 70)
    print("PSO IDENTIFICATION REPORT")
    print("=" * 70)
    print(f"\nTotal invitations analyzed: {len(merged)}")
    print(f"Legitimate journals: {(merged['classification'] == 'LEGITIMATE').sum()}")
    print(f"PSO confirmed: {(merged['classification'] == 'PSO').sum()}")
    print(f"Suspicious (manual review): {(merged['classification'] == 'SUSPICIOUS').sum()}")
    
    print("\n" + "-" * 70)
    print("DETAILED RESULTS")
    print("-" * 70)
    
    for _, row in merged.iterrows():
        status_emoji = "✅" if row['classification'] == 'LEGITIMATE' else "🔴"
        print(f"\n{status_emoji} Case #{row['case_id']}: {row['journal_name']}")
        print(f"   Publisher: {row['publisher']}")
        print(f"   Field mismatch: {row['discipline_claimed']} ← {row['discipline_actual']}")
        print(f"   PSO Index: {row['pso_index']}/5")
        print(f"   Classification: {row['classification']}")
    
    print("\n" + "=" * 70)
    
    # Summary statistics
    pso_rate = (merged['classification'] == 'PSO').mean() * 100
    print(f"\nPSO prevalence rate: {pso_rate:.1f}%")
    
    return merged

def main():
    """Main execution"""
    print("Loading data...")
    corpus, coding = load_corpus()
    
    print("Calculating PSO Index...")
    scores = calculate_pso_index(coding)
    
    print("Generating report...\n")
    results = generate_report(corpus, scores)
    
    # Optional: save results
    output_path = Path('../data') / 'pso_analysis_results.csv'
    results.to_csv(output_path, index=False)
    print(f"\nResults saved to: {output_path}")

if __name__ == '__main__':
    main()
