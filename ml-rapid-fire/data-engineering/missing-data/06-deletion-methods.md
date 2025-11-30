# Deletion Methods for Missing Data

**Q:** When is it appropriate to delete rows or columns with missing data?
- Listwise deletion
- Column deletion
- Risks

**A:**

- **Listwise deletion** (drop rows): remove any row with missing values
  - Appropriate when: MCAR, small fraction missing, large dataset
  - Risk: reduces sample size, biased if not MCAR
- **Column deletion** (drop features): remove features with too many missing values
  - Rule of thumb: drop if >50-70% missing (but depends on importance)
  - Risk: losing potentially predictive information
- **Pairwise deletion**: use all available data for each calculation
  - Used in correlation matrices
  - Can lead to inconsistent estimates
- **Best practice**: analyze missingness pattern first, understand why data is missing before choosing method

---
