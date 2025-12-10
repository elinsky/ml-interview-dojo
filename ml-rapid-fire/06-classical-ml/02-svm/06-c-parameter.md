# The C Parameter

**Q:** What does the C parameter control in SVM?

**A:**

- Controls **regularization** — inverse of regularization strength (default=1)
- Tradeoff between margin width and classification errors
- **Small C**: wide margin, more errors allowed → lower variance, higher bias
- **Large C**: narrow margin, fewer errors → higher variance, lower bias
- C → 0: maximal margin; C → ∞: hard margin (no errors)
- Typical tuning: GridSearchCV with exponentially-spaced values (0.001 to 1000)

[[202104170846]]

---
