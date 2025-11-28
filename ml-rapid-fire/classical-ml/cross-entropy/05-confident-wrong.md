# Cross-Entropy: Confident and Wrong

**Q:** What happens to cross-entropy loss when prediction is confident and wrong?

**A:** Approaches infinity (very high loss). This is the key property that penalizes confident wrong predictions harshly.

From the formula: if y=1 and a≈0, then -ln(a) → ∞. The log function severely penalizes predictions that are both confident and wrong. — 202101120828 Cross-Entropy Cost

---
