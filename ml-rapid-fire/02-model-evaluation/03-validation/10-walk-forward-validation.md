# Walk-Forward Validation

**Q:** What is walk-forward validation and what are the two approaches?

**A:**
- Train on past → validate/test on later timestamps
- Expanding window: train [t₀..t₃], validate [t₄]; train [t₀..t₄], validate [t₅]...
  - More data, but older data may drift
- Sliding window: train [t₀..t₃], validate [t₄]; train [t₁..t₄], validate [t₅]...
  - Emphasizes recency, good under drift

---
