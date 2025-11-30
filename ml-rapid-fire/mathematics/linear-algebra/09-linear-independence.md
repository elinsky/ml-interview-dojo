# Linear Independence

**Q:** What is linear independence and how do you check for it?
- Definition
- How to check
- Relationship to rank
- ML relevance

**A:**

- **Definition**: vectors {v₁, ..., vₖ} are linearly independent if Σᵢcᵢvᵢ = 0 implies all cᵢ = 0
- **Intuition**: no vector can be written as combination of others
- **Check by**: form matrix with vectors as columns; if rank = number of vectors, they're independent
- **Relationship to rank**: rank = max number of linearly independent columns
- **ML relevance**:
  - Multicollinearity: features are linearly dependent → unstable coefficients
  - Basis vectors must be independent
  - Neural network: redundant neurons don't add capacity

---
