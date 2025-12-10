# Text Preprocessing

**Q:** What are common text preprocessing steps?
- Cleaning
- Normalization
- When to skip

**A:**

- **Cleaning**:
  - Remove HTML tags, URLs, special characters
  - Handle contractions (don't → do not)
  - Remove or handle numbers
- **Normalization**:
  - Lowercasing (careful: US ≠ us)
  - Stemming: reduce to root (running → run) — aggressive, rule-based
  - Lemmatization: reduce to lemma (better → good) — uses vocabulary
  - Remove stopwords (the, is, at) — but context-dependent
- **When to skip**:
  - Modern transformers often work better with minimal preprocessing
  - Case matters for NER (Apple vs apple)
  - Stopwords matter for sentiment ("not good")
- **Tools**: NLTK, spaCy, regex

---
