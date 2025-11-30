# N-grams

**Q:** What are n-grams and why use them?
- Definition
- Why useful
- Trade-offs

**A:**

- **Definition**: contiguous sequence of n tokens
  - Unigram (n=1): "the", "cat", "sat"
  - Bigram (n=2): "the cat", "cat sat"
  - Trigram (n=3): "the cat sat"
- **Why useful**:
  - Captures some word order and context
  - Phrases have meaning beyond individual words ("not good" vs "good")
  - Simple extension of bag of words
- **Trade-offs**:
  - Vocabulary explodes: O(V^n) possible n-grams
  - Most n-grams rare → very sparse
  - Typically use n ≤ 3 and filter by frequency
- **Sklearn**: `CountVectorizer(ngram_range=(1,2))` for unigrams + bigrams
- **Example**: "New York" as bigram captures city name that unigrams miss

---
