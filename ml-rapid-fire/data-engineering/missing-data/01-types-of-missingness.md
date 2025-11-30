# Types of Missing Data

**Q:** What are the three types of missing data mechanisms?
- MCAR
- MAR
- MNAR
- Why it matters

**A:**

- **MCAR (Missing Completely at Random)**: missingness unrelated to any data
  - Example: sensor randomly fails
  - Safe to drop or impute simply
- **MAR (Missing at Random)**: missingness depends on observed data, not the missing value itself
  - Example: men less likely to report weight (depends on gender, not weight)
  - Can model missingness from other features
- **MNAR (Missing Not at Random)**: missingness depends on the missing value itself
  - Example: high earners don't report income
  - Hardest to handle, may need domain knowledge
- **Why it matters**: determines which imputation methods are valid and whether analysis will be biased

---
