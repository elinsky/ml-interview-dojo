# Min-Max Scaling

**Q:** What is min-max scaling and when should you use it?
- Formula
- Properties of result
- When to use vs standardization

**A:**

- **Formula**: x' = (x - x_min) / (x_max - x_min)
- **Result**: values in [0, 1] (or custom range [a, b])
- **When to use**:
  - Need bounded range (e.g., image pixels, neural network inputs with sigmoid/tanh)
  - Data is not Gaussian
  - No significant outliers (outliers compress the rest of the data)
- **Sklearn**: `MinMaxScaler`
- **Drawback**: sensitive to outliers — one extreme value squashes all others

---
