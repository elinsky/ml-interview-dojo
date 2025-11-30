# Bag of Words

**Q:** What is the bag of words representation?
- How it works
- Advantages
- Disadvantages

**A:**

- **How it works**: represent document as vector of word counts
  - Vocabulary of all unique words → indices
  - Each document → sparse vector of counts
  - Ignores word order
- **Advantages**:
  - Simple, interpretable
  - Works well for many tasks
  - Sparse representation (efficient storage)
- **Disadvantages**:
  - Loses word order and context ("dog bites man" = "man bites dog")
  - High dimensionality (vocabulary size)
  - Doesn't capture semantics (synonyms treated as unrelated)
- **Sklearn**: `CountVectorizer`
- **Variant**: binary BoW (1 if word present, 0 otherwise)

---
