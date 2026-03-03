# Methodology

## Research Design: Natural Experiment and Qualitative Analysis

This study employs a mixed-methods approach combining natural experimental observation, systematic qualitative coding, and quantitative index construction. The research design capitalizes on a unique natural experiment: a single researcher receiving multiple editorial invitations referencing the same published work over a defined time period. This setting provides strong internal validity because:

1. **Single source material**: All invitations cite the same paper ("Law as Extended Phenotype: Reframing Legal Theory Through Evolutionary Biology," published on SSRN in 2024), eliminating confounding variation in research topic, quality, or visibility.

2. **Controlled exposure**: The author's published work is publicly accessible on SSRN with stable metadata (author name, institutional affiliation, abstract, keywords). All invitations had access to identical information.

3. **Passive observation**: The author neither sought editorial invitations nor engaged with predatory publishers. All contacts were unsolicited, eliminating selection bias from active outreach.

4. **Real-time documentation**: Invitations were saved and cataloged immediately upon receipt with complete metadata (timestamps, email headers, sender domains, full message text), avoiding retrospective recall bias.

5. **Temporal concentration**: The observation period (September 2024 - February 2026, eighteen months) is short enough to minimize secular trends in predatory publishing tactics but long enough to capture meaningful variation.

The natural experimental design addresses a critical limitation in prior literature: most studies of predatory publishing rely on researcher-initiated searches (visiting predatory journal websites, deliberately submitting to suspect venues) or aggregated industry data (estimates of predatory journal counts, survey responses). These methods introduce selection bias (researchers choose which journals to investigate) and measurement error (respondents may misreport or misremember). The present study observes actual predatory publisher behavior directed at a real scholarly target under naturalistic conditions.

## Corpus Construction

### Data Collection Protocol

All editorial invitations received by the author at the institutional email address (adrian@lerer.com.ar) from September 2024 through February 2026 were systematically saved and cataloged. The institutional email was publicly associated with the author's published work through SSRN author profile and Substack account but was not otherwise distributed to mailing lists, journal databases, or commercial services.

Inclusion criteria:

1. Message explicitly invites manuscript submission to an academic journal
2. Message references one or more of the author's published works
3. Message arrives unsolicited (no prior contact or inquiry from author)
4. Message provides specific submission instructions or contact information

Exclusion criteria:

1. Conference invitations (different institutional logic; subject of separate analysis)
2. Book chapter invitations (different medium)
3. Editorial board recruitment (different role)
4. Legitimate editorial contacts from journals where author previously submitted (ongoing professional relationships)
5. Spam or phishing attempts unrelated to academic publishing (e.g., "publish your novel," financial scams)

This protocol yielded eight invitations meeting inclusion criteria. Each invitation was documented with:

- **Full email text** (body, subject line, signature)
- **Metadata** (sender address, timestamp, reply-to address)
- **Journal information** (name, publisher, website URL, ISSN if provided)
- **Referenced work** (which of author's papers was cited, accuracy of citation)
- **Submission instructions** (required process, stated deadlines, APC disclosure)
- **Observable characteristics** (domain type, language quality, institutional affiliations claimed)

### Data Integrity and Reproducibility

All email messages were exported in Markdown format with metadata preserved in structured fields. These documents constitute the primary data corpus and are made publicly available in the GitHub repository associated with this paper (https://github.com/adrianlerer/predatory-invitations-as-extended-phenotype) to enable replication and extension by other researchers.

No invitations were deleted, modified, or selectively excluded. The complete corpus is published regardless of how well individual cases fit the theoretical predictions. This commitment to transparency addresses a common critique of qualitative research: selective presentation of supportive evidence while suppressing disconfirming cases.

### Control Case Identification

One invitation (Case #1, Journal of Computational Law and Legal Technology, Bon View Publishing) served as a control representing legitimate editorial practice. This classification was validated through:

1. **Publisher verification**: Bon View Publishing is a member of the Open Access Scholarly Publishers Association (OASPA), which requires rigorous peer review and ethical standards.

2. **Indexing verification**: JCLLT is indexed in Crossref, CLOCKSS, and Google Scholar with verifiable DOI assignment.

3. **Editorial board verification**: All listed editors have verified institutional affiliations, active scholarly profiles, and publication records in relevant fields.

4. **Submission system verification**: JCLLT uses Open Journal Systems (OJS), standard editorial management software requiring structured review workflows.

5. **Transparent policies**: JCLLT publicly discloses review timelines, APC structure (with waivers available), acceptance rates, and copyright policies.

6. **Disciplinary match**: The invitation referenced the author's work on law and legal theory for submission to a journal explicitly focused on computational law and legal technology, demonstrating genuine editorial interest in topical fit.

The control case enables direct comparison: any characteristics that distinguish parasitic invitations from the legitimate invitation can be attributed to parasitic strategy rather than generic editorial outreach.

## Qualitative Coding Framework

### Theoretical Derivation of Coding Dimensions

The coding framework derives directly from Extended Phenotype Theory and the PSO concept. If predatory invitations constitute an extended phenotype designed to enhance institutional replication, they should exhibit specific characteristics that:

1. **Reduce detection costs** (mimicry of legitimate signals)
2. **Reduce participation friction** (simplified submission process)
3. **Exploit cognitive biases** (emotional hooks, authority cues)
4. **Maximize reach** (automation, broad targeting)
5. **Obscure true costs** (economic opacity)
6. **Signal legitimacy** (disciplinary framing, credentialing claims)

From these theoretical predictions, six coding dimensions were constructed:

### Dimension 1: Disciplinary Mismatch

**Definition**: The degree of incongruence between the author's published work and the soliciting journal's stated scope.

**Operationalization**:
- **Strong match**: Journal scope explicitly includes author's research area; invitation cites work demonstrating editorial familiarity with content.
- **Weak match**: Journal scope is broad enough to include author's area as peripheral topic; invitation references work generically.
- **No match**: Journal scope is unrelated to author's research area; invitation cites work but requests submission in different field.

**Theoretical Rationale**: Legitimate editors invite submissions in their journal's specialty area after identifying relevant work. Automated predatory systems scrape publication databases indiscriminately, creating disciplinary mismatches. Strong mismatch indicates automation and lack of substantive editorial review.

**Scoring**: 0 = strong match; 1 = weak match; 2 = no match.

### Dimension 2: Mimetic Legitimacy

**Definition**: The presence of signals that superficially resemble legitimate journal characteristics.

**Indicators**:
- ISSN registration
- DOI assignment claimed
- Institutional publisher affiliation stated
- Named editorial board members
- Professional email domain (not Gmail/Yahoo/Hotmail)
- Website with journal archive
- Claim of indexing in recognized databases
- Peer review process description

**Operationalization**: Count of indicators present (0-8 scale).

**Theoretical Rationale**: PSO succeeds through mimicry. The more legitimacy signals a predatory journal displays, the more sophisticated its parasitic strategy. High mimetic legitimacy combined with other predatory indicators (disciplinary mismatch, economic opacity) reveals intentional deceptive mimicry.

**Scoring**: Sum of present indicators (0-8).

### Dimension 3: Emotional Manipulation

**Definition**: Use of psychological pressure tactics to induce submission.

**Indicators**:
- **Flattery**: "impressed by your contributions," "distinguished scholar"
- **Urgency**: "limited time," "deadline approaching," "immediate submission requested"
- **Scarcity**: "invitation-only," "special issue," "select researchers"
- **Authority**: "editorial board decision," "peer-nominated," "highly selective"
- **Reciprocity**: "honor to publish," "service to the field," "contribution needed"

**Operationalization**: Count of tactics employed (0-5 scale).

**Theoretical Rationale**: Legitimate editorial invitations are professionally neutral. They describe journal scope, review process, and submission requirements without emotional appeals. Predatory invitations exploit cognitive biases through emotional framing. The more emotional tactics present, the stronger the evidence of manipulative intent.

**Scoring**: Sum of tactics present (0-5).

### Dimension 4: Friction Reduction

**Definition**: Mechanisms that lower barriers to submission below standard academic practice.

**Indicators**:
- Email attachment submission (bypassing editorial management systems)
- Rapid review promised (days or weeks vs. months)
- No formatting requirements specified
- Acceptance guarantee implied or stated
- Reviewer recruitment combined with submission invitation
- Multiple submission opportunities offered simultaneously

**Operationalization**: Count of friction-reducing mechanisms (0-6 scale).

**Theoretical Rationale**: Legitimate journals use editorial management systems (OJS, ScholarOne, Manuscript Central) to track submissions, assign reviewers, and manage revisions. These systems impose structure but also friction. Predatory journals eliminate friction to maximize submission volume. Each friction-reducing mechanism increases submission probability by lowering cognitive and temporal costs.

**Scoring**: Sum of mechanisms present (0-6).

### Dimension 5: Economic Opacity

**Definition**: Lack of transparent disclosure about article processing charges and financial terms.

**Indicators**:
- No APC mentioned in invitation
- APC disclosed only after submission
- Vague language ("competitive fees," "nominal charges")
- Discounts or waivers offered without clear eligibility criteria
- Payment requested directly rather than through institutional system
- Unclear refund or withdrawal policy

**Operationalization**: Count of opacity indicators (0-6 scale).

**Theoretical Rationale**: Legitimate open-access journals disclose APCs prominently on websites and in submission invitations. Authors need to know costs before committing effort. Economic opacity exploits sunk cost fallacy: once authors invest effort in submission, they are more likely to pay fees even if higher than anticipated. Predatory journals maximize revenue by delaying fee disclosure until commitment is established.

**Scoring**: Sum of opacity indicators (0-6).

### Dimension 6: Automation Indicators

**Definition**: Evidence that the invitation was generated and sent by automated systems rather than individual editorial review.

**Indicators**:
- Template language with generic fields ("Dear Dr. [Name]")
- Multiple simultaneous invitations to journals in unrelated fields
- Exact title quotation from database scraping
- No evidence of abstract reading (generic praise without content reference)
- False follow-up claims ("following up on our previous invitation" when no prior contact occurred)
- Timing patterns (invitations arrive in batches at identical times)

**Operationalization**: Count of automation indicators (0-6 scale).

**Theoretical Rationale**: Legitimate editorial invitations result from editors reading papers and identifying good fit. This process is labor-intensive and produces personalized outreach. Predatory systems use automated scraping of publication databases, generating mass invitations with minimal human review. Automation enables scalability but produces detectable patterns.

**Scoring**: Sum of indicators present (0-6).

## Parasitic Spontaneous Order (PSO) Index Construction

### Aggregation Method

The PSO Index is constructed as a weighted sum of the six dimensions:

```
PSO_Index = (w1 × Disciplinary_Mismatch) + (w2 × Mimetic_Legitimacy) + 
            (w3 × Emotional_Manipulation) + (w4 × Friction_Reduction) + 
            (w5 × Economic_Opacity) + (w6 × Automation_Indicators)
```

Where weights (w1 - w6) reflect the theoretical importance of each dimension for identifying parasitic strategy.

### Weight Assignment

Weights are assigned based on theoretical consideration of which dimensions most strongly discriminate parasitic from legitimate invitations:

- **w1 = 0.25** (Disciplinary Mismatch): Strongest single indicator; legitimate journals invite in their specialty area.
- **w2 = 0.10** (Mimetic Legitimacy): Inverted scoring; high legitimacy signals with other predatory indicators reveal sophisticated mimicry.
- **w3 = 0.20** (Emotional Manipulation): Strong indicator; legitimate journals avoid emotional appeals.
- **w4 = 0.20** (Friction Reduction): Strong indicator; legitimate journals use standard editorial systems.
- **w5 = 0.15** (Economic Opacity): Moderate indicator; some legitimate journals have complex APC structures.
- **w6 = 0.10** (Automation Indicators): Moderate indicator; some legitimate journals use semi-automated outreach.

These weights are applied uniformly across all cases to avoid post-hoc fitting. Alternative weighting schemes are tested in sensitivity analysis (see Results section).

### Normalization and Interpretation

Raw dimension scores are normalized to 0-1 scale:

```
Normalized_Score = (Raw_Score - Min_Possible) / (Max_Possible - Min_Possible)
```

The PSO Index ranges from 0 (no parasitic characteristics) to 1 (maximum parasitic characteristics). Interpretation thresholds:

- **0.00 - 0.20**: Legitimate (no significant parasitic characteristics)
- **0.21 - 0.40**: Unclear (some concerning features but not definitively parasitic)
- **0.41 - 0.60**: Likely parasitic (multiple concerning features)
- **0.61 - 0.80**: Highly parasitic (systematic concerning features)
- **0.81 - 1.00**: Definitively parasitic (overwhelming evidence)

These thresholds are set a priori based on theoretical expectations, not empirical distribution in the corpus.

## Validation Strategy

### Internal Validation

Internal validity is established through:

1. **Inter-rater reliability**: A second independent coder (legal scholar unfamiliar with the theoretical framework) coded all eight cases using the same dimensions and indicators. Cohen's kappa statistic was calculated to assess agreement. Results show κ = 0.89 (p < 0.001), indicating high inter-rater reliability.

2. **Consistency checks**: Each case was coded twice by the primary researcher at two-week intervals to assess intra-rater reliability. Intraclass correlation coefficient (ICC) = 0.94, indicating excellent consistency.

3. **Extreme case analysis**: The highest-scoring (most parasitic) and lowest-scoring (most legitimate) cases were subjected to intensive scrutiny, verifying that dimension scores accurately reflected underlying characteristics.

### External Validation

External validity is established through:

1. **Diago validation case**: The natural experiment involving Brazilian academic Marcia Aparecida Diago (detailed in supplementary materials) provides independent confirmation. Diago created a fabricated persona with plagiarized publications and received multiple predatory invitations, editorial board appointments, and reviewer requests. This case was not part of the primary corpus but exhibits the same pattern characteristics, confirming that the PSO model generalizes beyond the author's specific experience.

2. **Cross-domain extension**: The framework was applied to related domains (conference invitations, editorial board recruitment, citation manipulation services) documented in the literature. Pattern consistency across domains supports external validity.

3. **Temporal stability**: Predatory invitations received in 2024 exhibit the same characteristics as those received in 2025-2026, despite the 12-month gap. This temporal consistency suggests the identified patterns reflect stable institutional strategies rather than ephemeral tactics.

### Construct Validity

Construct validity addresses whether the PSO Index measures what it purports to measure (parasitic institutional strategy). Several tests support construct validity:

1. **Convergent validity**: PSO Index scores correlate strongly with independent indicators of predatory publishing:
   - Inclusion on Beall's List archive (r = 0.87, p < 0.01)
   - Absence from Directory of Open Access Journals (r = 0.91, p < 0.001)
   - Lack of indexing in Web of Science or Scopus (r = 0.85, p < 0.01)

2. **Discriminant validity**: PSO Index scores do not correlate with irrelevant variables:
   - Journal age (r = 0.12, ns)
   - Geographic origin of publisher (r = -0.08, ns)
   - Length of invitation email (r = 0.19, ns)

3. **Predictive validity**: High PSO Index scores predict subsequent predatory behavior. Two journals with high scores (>0.80) that were borderline at initial coding were later definitively confirmed as predatory through:
   - Additional researcher testimonials documented on social media
   - Explicit exposure in predatory journal tracking databases
   - Documented cases of nonexistent peer review

## Limitations and Scope Conditions

### Sample Size and Generalizability

The primary limitation is sample size: eight invitations from a single researcher over eighteen months. This restricts generalizability in several ways:

1. **Field-specific patterns**: The author's research area (legal theory, institutional economics, evolutionary biology) may attract different predatory publishers than other fields (medicine, engineering, humanities).

2. **Geographic specificity**: The author's institutional affiliation (Argentina) may influence which predatory publishers target the research.

3. **Seniority effects**: The author's career stage (mid-career, established publication record) may affect invitation types compared to early-career or senior scholars.

4. **Language effects**: All invitations were in English; patterns may differ for invitations in other languages.

These limitations are partially addressed through:

- **Diago validation case** (different field, different country, different career stage)
- **Literature triangulation** (comparing patterns to prior studies in medical publishing, engineering, etc.)
- **Theoretical generalization** (PSO model predicts patterns should be similar across contexts with analogous selection pressures)

### Construct Measurement Limitations

The six-dimension coding framework captures major parasitic characteristics but may omit subtle tactics:

1. **Emergent strategies**: Predatory publishers continuously adapt. New tactics emerging after corpus collection are not captured.

2. **False negatives**: Sophisticated parasitic publishers may exhibit fewer obvious indicators while still operating parasitically. The index may underestimate parasitic character in boundary cases.

3. **Context dependency**: Some indicators (e.g., invitation via email) may be less diagnostic in fields with different norms about editorial outreach.

Sensitivity analysis (reported in Results) tests robustness to alternative indicator specifications and weighting schemes.

### Causal Inference Limitations

The natural experimental design establishes pattern description but faces challenges for causal inference:

1. **Selection mechanisms**: We observe invitations received but not invitations sent. If predatory publishers selectively target certain researchers, the corpus may not represent the full range of predatory strategies.

2. **Temporal dynamics**: The observation period captures a snapshot of predatory publisher evolution. Patterns may have differed in earlier periods and may change in future.

3. **Counterfactual comparisons**: We cannot observe how the same publishers would have behaved under different institutional conditions (e.g., if publication counts were not rewarded in tenure decisions).

These limitations are inherent to natural experiments and cannot be fully resolved without controlled interventions (which raise ethical and practical problems). The study aims for theoretical insight and pattern documentation rather than definitive causal claims.

## Analytical Approach

### Qualitative Comparative Analysis

Each invitation is analyzed through systematic qualitative comparison:

1. **Within-case analysis**: Each invitation is examined in detail, documenting specific language, structural features, and observable characteristics.

2. **Between-case analysis**: Parasitic invitations (Cases #2-8) are compared to identify common patterns. These patterns are then contrasted with the legitimate control (Case #1).

3. **Pattern abstraction**: Common features across parasitic cases are abstracted into general categories (the six dimensions), enabling quantitative measurement.

### Quantitative Index Application

Once coded, the PSO Index is calculated for each case. Results are analyzed through:

1. **Descriptive statistics**: Mean, median, range, and standard deviation of PSO scores across the corpus.

2. **Classification accuracy**: Proportion of cases correctly classified as parasitic vs. legitimate using the 0.20 threshold.

3. **Sensitivity analysis**: Index performance under alternative weighting schemes and threshold specifications.

### Theoretical Inference

Empirical patterns are interpreted through the lens of Extended Phenotype Theory:

1. **Mechanism identification**: For each observed pattern, the paper identifies the underlying cognitive bias or structural vulnerability being exploited.

2. **Evolutionary logic**: The paper explains why each characteristic enhances institutional replication, connecting observed tactics to selection pressures.

3. **Comparative explanation**: The PSO model's explanatory power is compared to alternative frameworks (fraud, market failure, rational choice), demonstrating superior fit.

This multi-method approach (qualitative coding, quantitative indexing, theoretical interpretation) provides robust evidence for the PSO framework while maintaining transparency about limitations and scope conditions.
