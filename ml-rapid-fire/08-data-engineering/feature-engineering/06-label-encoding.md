# Label Encoding

**Q:** What is label encoding and when is it appropriate?
- How it works
- When to use
- When NOT to use

**A:**

- **How it works**: assign integer to each category (e.g., red=0, green=1, blue=2)
- **When to use**:
  - Ordinal variables with natural order (low < medium < high)
  - Tree-based models (can split on any threshold)
  - Target variable encoding for classification
- **When NOT to use**:
  - Nominal variables with no order (color, country) in linear/distance-based models
  - Creates false ordinal relationship (model thinks blue > green > red)
- **Sklearn**: `LabelEncoder` (for targets), `OrdinalEncoder` (for features)

---
