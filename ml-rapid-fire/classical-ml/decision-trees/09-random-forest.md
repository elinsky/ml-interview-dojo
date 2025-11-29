# Random Forest

**Q:** What is Random Forest?

**A:**

- **Bagging + random feature selection** at each split
- Each tree trained on bootstrap sample
- At each split, only consider **random subset of features** (typically √p)
- **Decorrelates trees** → reduces variance more than bagging alone
- Provides easy **feature importance** measurement

[[202104160934]] [[202104161606]]

---
