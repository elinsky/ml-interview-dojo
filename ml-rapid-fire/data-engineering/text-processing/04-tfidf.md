# TF-IDF

**Q:** What is TF-IDF and why is it better than raw counts?
- Components
- Formula
- Intuition

**A:**

- **TF-IDF**: Term Frequency × Inverse Document Frequency
- **Components**:
  - TF(t,d) = count of term t in document d (or normalized)
  - IDF(t) = log(N / df_t) where N = total docs, df_t = docs containing t
- **Formula**: TF-IDF(t,d) = TF(t,d) × IDF(t)
- **Intuition**:
  - High TF: term appears often in this document (relevant)
  - High IDF: term is rare across corpus (discriminative)
  - Common words (the, is) get low weight (appear everywhere)
  - Rare discriminative words get high weight
- **Sklearn**: `TfidfVectorizer`
- **Finance example**: identifying key topics in SEC filings — words like "bankruptcy" rare but important

---
