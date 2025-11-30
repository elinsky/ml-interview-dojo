# Missing Indicator Features

**Q:** When should you add a missing indicator feature?
- What it is
- When useful
- Implementation

**A:**

- **What it is**: binary feature indicating whether original value was missing
- **When useful**:
  - Missingness itself is informative (MAR or MNAR)
  - Example: missing credit score might indicate thin file (predictive of risk)
  - Lets model learn different behavior for missing vs imputed values
- **Implementation**:
  - Add binary column: 1 if missing, 0 otherwise
  - Impute original column with any method
  - Use both columns as features
- **Sklearn**: `SimpleImputer(add_indicator=True)` or `MissingIndicator`
- **Finance example**: missing financial statement data might indicate private company or data quality issues

---
