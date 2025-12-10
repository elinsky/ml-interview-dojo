# Diagnosing Bias vs Variance

**Q:** How do you diagnose high bias vs high variance using learning curves?

**A:**

**High Bias (underfitting)**:
- Training and validation error both **high**
- Curves **converge** at high error
- More data won't help

**High Variance (overfitting)**:
- Training error **low**, validation error **high**
- Large **gap** between curves
- More data typically helps

"Graph training examples on the x-axis and validation accuracy on the y-axis. This graph can tell you if adding more training data will improve model accuracy." [@russell2010artificial, p. 702]

---
