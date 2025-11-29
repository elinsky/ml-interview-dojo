# What is an SVM?

**Q:** What is a Support Vector Machine (SVM)?

**A:**

- **Maximal-margin classifier** — finds hyperplane that maximizes distance to nearest points
- Used for **classification** (SVC), **regression** (SVR), and **outlier detection**
- Hyperplane equation: w·x + b = 0
- Prediction: sign(w·x + b) → above line = class 1, below = class 0
- **Magnitude** of output indicates confidence
- Can handle **non-linear** boundaries via kernel trick

---
