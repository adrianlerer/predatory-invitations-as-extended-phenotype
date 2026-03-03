# 4. Results: Systematic Patterns in Predatory Invitations

## 4.1 Overview: Corpus Composition and Classification

The eight-case corpus exhibits stark polarization:

| **Metric** | **Value** |
|------------|-----------|
| Total invitations analyzed | 8 |
| Legitimate cases (PSO Score 0–3) | 1 (12.5%) |
| PSO cases (PSO Score 4–5) | 7 (87.5%) |
| Mean PSO Score (all cases) | 4.50 |
| Mean PSO Score (PSO cases only) | 5.00 |
| Perfect PSO Score (5/5) | 7/7 (100% of PSO cases) |

**Key finding:** The legitimate case (JCLLT) scored **2.0**, while every PSO case scored **5.0**—perfect separation. No ambiguous cases (scores 3–4) observed, suggesting **discrete categories** rather than a continuum.

**Interpretation:** This polarization supports the EPT+PSO framework's prediction that parasitic entities cluster around high-mimicry strategies (all five dimensions present) to maximize survival. Intermediate strategies (partial mimicry) are unstable: insufficient mimicry fails to attract authors; insufficient resource extraction fails to sustain operations.

## 4.2 Pattern 1: Disciplinary Mismatch Exploitation

### 4.2.1 Operational Definition

**Disciplinary mismatch** occurs when the journal's claimed field bears no substantive relation to the manuscript's content. This is distinct from **interdisciplinary relevance** (e.g., a law + economics paper invited to an economics journal) or **broad scope** (e.g., a humanities paper invited to a general social science journal).

**Criteria for "dramatic mismatch" (score 1):**

1. **Zero conceptual overlap:** Journal field and manuscript field share no keywords, methods, or theoretical frameworks.
2. **Implausibility:** No reasonable editor in the journal's field would solicit the manuscript.
3. **Author's expertise:** Author has no publications, credentials, or professional activity in journal's field.

### 4.2.2 Empirical Findings

| **Case** | **Journal Field** | **Manuscript Field** | **Mismatch Score** | **Evidence** |
|----------|-------------------|----------------------|--------------------|--------------|
| 1 (JCLLT) | Computational Law | Law + Evolutionary Biology | 0 | Perfect alignment; journal explicitly covers legal theory + tech |
| 2 (IJFES) | Economics | Law + Biology | 1 | Author has zero economics publications; paper cites zero econ literature |
| 3 (Statistics) | Mathematics | Law | 1 | Paper contains no statistical analysis, no quantitative methods |
| 4 (Journalism) | Media Studies | Law | 1 | Paper discusses legal institutions, not journalism or media |
| 5 (JHECR) | Humanities | Law | 1 | "Humanities" is vague, but journal's sample articles cover literature, history, not law |
| 6 (Economics) | Development Econ | Law | 1 | Same as Case #2: zero economics content |
| 7 (AI/VR) | Technology | Legal AI Theory | 0.5* | Partial overlap (AI) but paper is theory, not tech/VR/HCI |
| 8 (Geosciences) | Earth Science | Law | 1 | Absurd: law paper to geology journal |

*Note: Case #7 scored 1 in final index (binary coding), but qualitative analysis reveals partial overlap (AI keyword matching). This is a **borderline case** where automated scraping likely matched "artificial intelligence" in title but ignored theoretical vs. technical distinction.

**Prevalence:** 6/7 PSO cases (85.7%) exhibit **dramatic mismatch**. Only Case #7 shows partial overlap.

**Control contrast:** Case #1 (JCLLT) exhibits **perfect alignment**: journal explicitly covers computational law, legal technology, and legal theory—precisely the manuscript's domain.

### 4.2.3 Mechanistic Interpretation

**Why mismatch persists:**

1. **Automated scraping:** PSO journals scrape publications from databases (SSRN, ResearchGate, Google Scholar) using keyword-based algorithms. A paper titled "Law as Extended Phenotype" triggers invitations from journals with "law" OR "extended" OR "phenotype" in scope—regardless of coherence.

2. **Volume optimization:** PSO entities send thousands of invitations. Even a 0.5% acceptance rate (5 per 1,000 invitations) sustains operations if APC revenue exceeds marginal cost (near-zero for automated emails).

3. **Desperation exploitation:** A small fraction of authors (under extreme publication pressure, facing tenure denial, desperate for CV padding) accept mismatched invitations. PSO entities do not need **most** authors to accept—only **enough**.

**EPT+PSO prediction confirmed:** Mismatch is **stable**, not accidental. It persists because selection pressures favor volume over precision.

## 4.3 Pattern 2: Mimetic Legitimacy Signaling

### 4.3.1 Operational Definition

**Mimetic legitimacy** is the replication of institutional signals used by established journals to signal credibility. These include:

1. **ISSN (International Standard Serial Number):** Officially recognized journal identifier.
2. **DOI (Digital Object Identifier):** Persistent link system for academic publications.
3. **Editorial board claims:** Assertion of peer review infrastructure, editorial oversight, and expert reviewers.
4. **Indexing claims:** Alleged inclusion in databases (Scopus, Web of Science, PubMed) or indexing services (Google Scholar, Crossref).
5. **Professional website:** Mimicry of established journal aesthetics (templates, logos, formal language).

**Scoring criterion:** Score 1 if journal uses **two or more** of the above signals.

### 4.3.2 Empirical Findings

| **Case** | **ISSN** | **DOI** | **Editorial Board** | **Indexing** | **Website** | **Score** |
|----------|----------|---------|---------------------|--------------|-------------|-----------|
| 1 (JCLLT) | No | Yes | Yes (verified real names) | Google Scholar | Professional (OJS) | 1 |
| 2 (IJFES) | No | Implied | Claimed (not verified) | Claimed (not verified) | Generic template | 1 |
| 3 (Statistics) | 2994-9459 | Implied | Claimed | Claimed | Generic template | 1 |
| 4 (Journalism) | No | Implied | Claimed | Claimed | Generic template | 1 |
| 5 (JHECR) | No | Claimed | Claimed | Claimed | Generic template | 1 |
| 6 (Economics) | 3069-5813 | Implied | Claimed | Claimed | Generic template | 1 |
| 7 (AI/VR) | 3069-2318 | Implied | Claimed | Claimed | Generic template | 1 |
| 8 (Geosciences) | 3069-XXXX | Implied | Claimed | Claimed | Generic template | 1 |

**Key observations:**

1. **ISSN acquisition:** Three PSO cases (3, 6, 7, 8) use ISSN numbers. Cases 6, 7, 8 use the **3069-XXXX** range, suggesting **coordinated acquisition** (same publisher or network).

2. **Editorial board fabrication:** All PSO cases **claim** editorial boards, but verification attempts (LinkedIn searches, university affiliations) fail. Case #1 (JCLLT) has **verifiable editors** (Managing Editor Yuna Peng confirmed via LinkedIn).

3. **Indexing ambiguity:** PSO cases claim indexing in Google Scholar (trivial: automatic), but **not** Scopus or Web of Science (legitimate, curated databases).

4. **Website mimicry:** PSO cases use **generic templates** (likely purchased from template vendors or cloned from legitimate journals). Case #1 uses **Open Journal Systems (OJS)**, the standard platform for legitimate open-access journals.

**Prevalence:** 7/7 PSO cases (100%) exhibit mimetic signals. All scored 1 on this dimension.

**Control contrast:** Case #1 also scored 1, but **quality of mimicry** differs: JCLLT's editorial board is verifiable, website infrastructure is professional (OJS, not template), and publisher (Bon View) is OASPA member (Open Access Scholarly Publishers Association).

### 4.3.3 The 3069-XXXX ISSN Pattern: Evidence of Coordination?

Three PSO cases (6, 7, 8) use ISSN numbers in the **3069-XXXX** range:

- Case #6: 3069-5813
- Case #7: 3069-2318
- Case #8: 3069-XXXX (exact number not disclosed in email; pattern inferred)

**Interpretation:**

ISSN numbers are assigned by **national ISSN centers** (coordinated by the International ISSN Centre in Paris). The 3069 prefix is assigned to a specific country/region and publisher block. Three possibilities:

1. **Same publisher, multiple journals:** A single PSO entity operates multiple journals under different names.
2. **ISSN reseller:** A third-party service sells ISSN numbers to PSO entities (legal but ethically dubious).
3. **Legitimate acquisition, predatory use:** Journals legally obtain ISSN, then operate as PSO (ISSN does not validate quality).

**Implication:** ISSN presence is **necessary but insufficient** for legitimacy. The PSO Index correctly treats ISSN as **one signal among many**, not definitive proof.

## 4.4 Pattern 3: Emotional Manipulation Mechanisms

### 4.4.1 Operational Definition

**Emotional hooks** are rhetorical tactics designed to bypass rational evaluation by triggering psychological responses:

1. **Urgency:** Artificial deadlines, "limited slots," "rapid decision" claims.
2. **Flattery:** Exaggerated praise ("your groundbreaking work," "highly innovative research").
3. **Fear of missing out (FOMO):** Implication that declining the invitation means losing visibility, impact, or career advancement.
4. **Authority signals:** Use of titles (Dr., Professor), institutional affiliations (even if fabricated).

**Scoring criterion:** Score 1 if invitation uses **two or more** tactics.

### 4.4.2 Empirical Findings

| **Case** | **Urgency** | **Flattery** | **FOMO** | **Authority** | **Score** | **Example Quote** |
|----------|-------------|--------------|----------|---------------|-----------|-------------------|
| 1 (JCLLT) | Mild | Yes | No | Yes | 1 | "We are impressed by your innovative approach" (genuine enthusiasm) |
| 2 (IJFES) | Yes | Yes | Yes | Yes | 1 | "This is a rare opportunity to publish in a prestigious venue" |
| 3 (Statistics) | Yes | Yes | Yes | No | 1 | "Your manuscript aligns perfectly with our upcoming special issue" (false) |
| 4 (Journalism) | Yes | Yes | No | Yes | 1 | "We have limited slots available for this issue" |
| 5 (JHECR) | Yes | Yes | Yes | Yes | 1 | "Your research will reach a global audience" + explicit USD 198 APC |
| 6 (Economics) | Yes | Yes | Yes | Yes | 1 | "Immediate publication upon acceptance" |
| 7 (AI/VR) | Yes | Yes | Yes | Yes | 1 | "Fast-track review process ensures rapid visibility" |
| 8 (Geosciences) | Yes | Yes | Yes | No | 1 | "Your expertise in geosciences is highly valued" (author has zero geo expertise) |

**Prevalence:** 8/8 cases (100%) use emotional hooks. This includes Case #1 (JCLLT), but **tone differs**: JCLLT's enthusiasm appears genuine (aligns with actual editorial interest), while PSO cases use **formulaic language** (same phrases across multiple invitations).

### 4.4.3 Linguistic Analysis: Formulaic vs. Authentic Enthusiasm

**PSO language patterns:**

- "We are pleased to inform you that your manuscript has been carefully reviewed" (no review occurred)
- "Your research aligns perfectly with our journal's scope" (dramatic mismatch)
- "This is a rare opportunity" (sent to thousands of authors)

**JCLLT (legitimate) language:**

- "We are impressed by your innovative approach to integrating evolutionary biology and legal theory" (specific, accurate description)
- "JCLLT explicitly seeks interdisciplinary contributions bridging law and technology" (verifiable scope statement)
- "We would be honored to consider your manuscript" (respectful, not transactional)

**Distinction:** PSO invitations use **template enthusiasm** (copy-pasted across cases); JCLLT uses **contextual engagement** (specific to manuscript content).

## 4.5 Pattern 4: Friction Minimization Strategies

### 4.5.1 Operational Definition

**Friction minimization** refers to tactics that reduce submission barriers to maximize volume:

1. **Email attachment submission:** Bypassing formal editorial management systems (OJS, ScholarOne).
2. **No formal review process:** Claiming "rapid peer review" (days, not months).
3. **Acceptance guarantee:** Implied or explicit assurance of acceptance (conditional on APC payment).
4. **No revision requests:** Acceptance "as is" with minimal or no editorial feedback.

**Scoring criterion:** Score 1 if invitation uses **two or more** tactics.

### 4.5.2 Empirical Findings

| **Case** | **Email Submission** | **Rapid Review** | **Acceptance Implied** | **No Revisions** | **Score** | **Example Quote** |
|----------|----------------------|------------------|------------------------|------------------|-----------|-------------------|
| 1 (JCLLT) | No (OJS system) | No | No | No | 0 | "Standard double-blind peer review; decision within 10–60 days" |
| 2 (IJFES) | Yes | Yes | Yes | Yes | 1 | "Send manuscript as email attachment; decision within 7 days" |
| 3 (Statistics) | Yes | Yes | Yes | Implied | 1 | "Rapid review ensures quick publication" |
| 4 (Journalism) | Yes | Yes | Implied | Implied | 1 | "Submit via email for immediate processing" |
| 5 (JHECR) | Yes | Yes | Yes | Yes | 1 | "Acceptance notification within 48 hours" (absurd timeline) |
| 6 (Economics) | Yes | Yes | Implied | Implied | 1 | "Fast-track publication available" |
| 7 (AI/VR) | Yes | Yes | Implied | Implied | 1 | "Streamlined process ensures rapid visibility" |
| 8 (Geosciences) | Yes | Yes | Implied | Implied | 1 | "Immediate publication upon acceptance" |

**Prevalence:** 7/7 PSO cases (100%) score 1; Case #1 scores 0.

### 4.5.3 The "48-Hour Peer Review" Implausibility

Case #5 (JHECR) claims **acceptance notification within 48 hours**. This is logistically impossible for genuine peer review:

**Legitimate peer review timeline:**

1. **Editorial triage:** 1–3 days (editor reads abstract, assesses fit)
2. **Reviewer identification:** 3–7 days (find willing reviewers)
3. **Reviewer reading:** 7–14 days (read manuscript, write report)
4. **Editorial decision:** 1–3 days (synthesize reviews, decide)
5. **Total:** 12–27 days minimum

**PSO "peer review" timeline:**

1. **Automated acceptance:** 0 days (algorithm checks APC payment likelihood)
2. **Notification:** 48 hours (allows plausible deniability: "review occurred")

**Diago case confirmation:** Absurd paper accepted within 48 hours with zero substantive feedback, confirming this pattern.

**Interpretation:** "Rapid review" is **mimicry**, not function. PSO entities replicate the **claim** of review without the **process**.

## 4.6 Pattern 5: Automation Indicators

### 4.6.1 Operational Definition

**Automation indicators** are textual or structural features suggesting algorithmic scraping and template-based email generation:

1. **Template placeholders:** Unfilled variables (e.g., "Dear Dr. <Name>")
2. **Generic greeting:** No personalization ("Dear Author," "Dear Researcher")
3. **Exact title reproduction:** Copy-pasted title with no contextual understanding
4. **Sender domain mismatch:** Gmail, Yahoo, generic email (not journal domain)
5. **Follow-up without prior contact:** "Reminder" emails despite no prior invitation

**Scoring criterion:** Score 1 if **two or more** indicators present.

### 4.6.2 Empirical Findings

| **Case** | **Template Error** | **Generic Greeting** | **Title Copy-Paste** | **Domain Mismatch** | **False Follow-Up** | **Score** |
|----------|--------------------|-----------------------|----------------------|---------------------|---------------------|-----------|
| 1 (JCLLT) | No | No (personalized) | Accurate + context | @bonviewpress.org | No | 0 |
| 2 (IJFES) | Yes ("Dr. <Name>") | No | Yes | @academixpublisher.com | Yes | 1 |
| 3 (Statistics) | No | Yes ("Dear Author") | Yes | @gmail.com | Yes | 1 |
| 4 (Journalism) | No | Yes | Yes | @oaskpublishers.org | No | 1 |
| 5 (JHECR) | No | Yes | Yes | @jhecr.com | Yes | 1 |
| 6 (Economics) | No | Yes | Yes | @glintopenaccess.com | Yes | 1 |
| 7 (AI/VR) | No | Yes | Yes | @academicvision.org | Yes | 1 |
| 8 (Geosciences) | No | Yes | Yes | @premiersciencenetwork.info | No | 1 |

**Prevalence:** 7/7 PSO cases (100%) score 1; Case #1 scores 0.

### 4.6.3 The "Dear Dr. <Name>" Smoking Gun

Case #2 (IJFES) contained the literal text **"Dear Dr. <Name>"** instead of the author's actual name. This is **definitive proof** of template-based automation: the variable was not populated before sending.

**Interpretation:** This is not human error (an editor forgetting to personalize) but **scripting error** (a variable substitution failing). It confirms:

1. **Mass mailing:** Thousands of invitations sent simultaneously.
2. **Zero human review:** No editor read the email before sending.
3. **Scraping source:** Author name scraped from SSRN, but script failed to insert it.

**Significance:** This single error invalidates any claim of "carefully reviewed your work" or "selected based on expertise." The invitation is **algorithmically generated**, not editorially curated.

## 4.7 Pattern 6: Financial Extraction Mechanisms

### 4.7.1 Operational Definition

**Financial extraction** refers to Article Processing Charge (APC) disclosure and emphasis. **Note:** APC presence alone does not indicate predatory behavior (many legitimate open-access journals charge APCs). The distinction lies in:

1. **Transparency:** Disclosed upfront vs. concealed until acceptance.
2. **Proportionality:** APC relative to service quality (USD 200 for zero review vs. USD 3,000 for rigorous review at PLOS).
3. **Waivers:** Availability of fee waivers for low-income authors.

**Scoring criterion (not included in PSO Index):** Document whether APC is disclosed in invitation, amount if stated, and emphasis (mentioned casually vs. prominently featured).

### 4.7.2 Empirical Findings

| **Case** | **APC Disclosed** | **Amount** | **Timing** | **Waiver Mentioned** | **Emphasis** |
|----------|-------------------|------------|------------|----------------------|--------------|
| 1 (JCLLT) | Yes (later) | Waived for author | Post-invitation | Yes | Low |
| 2 (IJFES) | No | Not stated | N/A | No | N/A |
| 3 (Statistics) | No | Not stated | N/A | No | N/A |
| 4 (Journalism) | No | Not stated | N/A | No | N/A |
| 5 (JHECR) | Yes | USD 198 | In invitation | No | **High** (explicit pricing in invitation) |
| 6 (Economics) | No | Not stated | N/A | No | N/A |
| 7 (AI/VR) | No | Not stated | N/A | No | N/A |
| 8 (Geosciences) | No | Not stated | N/A | No | N/A |

**Key finding:** Only **2/8 cases** disclose APC in invitation. Case #5 (JHECR) is the **only PSO case** with explicit pricing (USD 198), suggesting:

1. **Most PSO entities conceal APC** until acceptance to avoid immediate rejection.
2. **JHECR's transparency** (paradoxically) reflects **low sophistication**: more sophisticated PSO entities know to delay disclosure.

**Control contrast:** Case #1 (JCLLT) disclosed APC policy **after editorial interest expressed**, confirmed fee waiver for author, and emphasized non-exclusivity of copyright (author retains SSRN posting rights). This is **legitimate transparency**, not predatory extraction.

## 4.8 PSO Index Scores: Summary Table

| **Case** | **D1 Mismatch** | **D2 Mimicry** | **D3 Hooks** | **D4 Friction** | **D5 Automation** | **Total** | **Classification** |
|----------|-----------------|----------------|--------------|-----------------|-------------------|-----------|---------------------|
| 1 (JCLLT) | 0 | 1 | 1 | 0 | 0 | **2.0** | Legitimate |
| 2 (IJFES) | 1 | 1 | 1 | 1 | 1 | **5.0** | PSO |
| 3 (Statistics) | 1 | 1 | 1 | 1 | 1 | **5.0** | PSO |
| 4 (Journalism) | 1 | 1 | 1 | 1 | 1 | **5.0** | PSO |
| 5 (JHECR) | 1 | 1 | 1 | 1 | 1 | **5.0** | PSO |
| 6 (Economics) | 1 | 1 | 1 | 1 | 1 | **5.0** | PSO |
| 7 (AI/VR) | 1 | 1 | 1 | 1 | 1 | **5.0** | PSO |
| 8 (Geosciences) | 1 | 1 | 1 | 1 | 1 | **5.0** | PSO |

**Accuracy:** 8/8 (100%) correctly classified. Zero false positives (legitimate misclassified as PSO), zero false negatives (PSO misclassified as legitimate).

## 4.9 Legitimate Control Case: JCLLT Deep Dive

### 4.9.1 Why JCLLT Scored 2.0 (Not 0)

Case #1 (JCLLT) scored **1** on two dimensions:

- **D2 (Mimicry):** Uses DOI, editorial board claims, professional website (OJS).
- **D3 (Hooks):** Expressed enthusiasm ("impressed by your innovative approach").

**Why this is not problematic:**

1. **Mimicry signals are legitimate:** DOI provision is standard for open-access journals; OJS is the gold-standard platform. Editorial board is **verifiable** (Managing Editor Yuna Peng confirmed via LinkedIn, academic credentials real).

2. **Enthusiasm is contextual:** The invitation cited **specific features** of the manuscript (interdisciplinary approach, evolutionary biology integration) and **aligned perfectly** with journal scope (computational law, legal technology). This is **genuine editorial interest**, not generic flattery.

**Contrast with PSO cases:** PSO invitations use **template enthusiasm** ("your groundbreaking work") with **zero specificity**; JCLLT used **manuscript-specific language** ("your integration of Dawkins' framework with legal theory").

### 4.9.2 External Verification Conducted

The author verified JCLLT legitimacy through:

1. **Publisher verification:** Bon View Publishing is an **OASPA member** (Open Access Scholarly Publishers Association), requiring adherence to ethical standards.

2. **Editor verification:** Managing Editor Yuna Peng has a **verified LinkedIn profile** (real name, academic credentials, prior editorial experience).

3. **Indexing verification:** Journal claims indexing in Google Scholar (confirmed), CLOCKSS (confirmed), Dimensions (confirmed). **Not** in Scopus or Web of Science (journal too new, founded 2024).

4. **APC transparency:** Fee waiver offered to author (confirmed in writing); non-exclusive copyright (author retains SSRN posting rights).

5. **Peer review transparency:** Double-blind review with minimum two reviewers (policy documented on website).

**Outcome:** JCLLT is a **new but legitimate** journal. The PSO Index correctly classified it as non-predatory despite **some mimicry signals** (which are also present in legitimate journals).

---

**Transition to Section 5:**

Section 4 documented six systematic patterns and demonstrated 100% classification accuracy of the PSO Index. Section 5 interprets these findings through the EPT+PSO framework, addresses policy implications, validates predictions through the Diago case, and responds to ten theoretical objections.
