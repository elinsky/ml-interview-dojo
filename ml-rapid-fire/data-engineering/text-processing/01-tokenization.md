# Tokenization

**Q:** What is tokenization and what are the main approaches?
- Definition
- Word-level
- Subword-level
- Character-level

**A:**

- **Definition**: splitting text into discrete units (tokens) for processing
- **Word-level**: split on whitespace/punctuation
  - Simple, interpretable
  - Large vocabulary, OOV (out-of-vocabulary) problem
- **Subword-level**: split into subword units
  - BPE (Byte Pair Encoding): iteratively merge frequent pairs
  - WordPiece: used in BERT
  - Handles OOV by breaking into known subwords
- **Character-level**: each character is a token
  - No OOV, tiny vocabulary
  - Long sequences, loses word meaning
- **Trade-off**: vocabulary size vs sequence length vs semantic granularity
- **Finance example**: tokenizing earnings call transcripts for sentiment analysis

---
