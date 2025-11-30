# Pearson vs Spearman Correlation

**Q:** When should you use Spearman instead of Pearson correlation?
- What each measures
- When to use Spearman
- Key difference in robustness

**A:**

- **Pearson**: measures linear relationship between raw values
- **Spearman**: measures monotonic relationship between ranks (Pearson applied to ranks)
- **Use Spearman when**:
  - Relationship is monotonic but not linear
  - Data has outliers (rank-based = more robust)
  - Ordinal data
  - Non-normal distributions
- **Example**: Spearman better for relating fund rankings over time, or when returns have fat tails

---
