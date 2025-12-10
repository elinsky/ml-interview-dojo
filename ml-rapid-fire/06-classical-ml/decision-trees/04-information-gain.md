# Information Gain / Entropy

**Q:** What is information gain and entropy in decision trees?

**A:**

- **Entropy** = measure of disorder/uncertainty: H = -Σ pᵢ log₂(pᵢ)
- **Entropy = 0** → pure node; **Entropy = 1** → maximally impure (binary)
- **Information gain** = entropy before split - weighted entropy after split
- Higher information gain = better split
- Used by ID3, C4.5 algorithms

---
