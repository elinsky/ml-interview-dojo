# Gini Impurity

**Q:** What is Gini impurity?

**A:**

- Measures how "impure" a node is (how mixed the classes are)
- **Formula**: G = 1 - Σpₖ² where pₖ = proportion of class k
- **G = 0** → pure node (all same class)
- **G = 0.5** → maximally impure (binary 50/50 split)
- When evaluating split: **weight** child Gini by (n_child / n_parent)

[[202104160836]]

---
