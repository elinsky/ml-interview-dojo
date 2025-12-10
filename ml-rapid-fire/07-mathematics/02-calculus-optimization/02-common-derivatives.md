# Common Derivatives

**Q:** What are the derivatives of common functions in ML?
- Power, exponential, logarithm
- Activation functions

**A:**

- **Power rule**: d/dx[xⁿ] = nxⁿ⁻¹
- **Exponential**: d/dx[eˣ] = eˣ
- **Logarithm**: d/dx[ln(x)] = 1/x
- **Activation functions**:
  - Sigmoid σ(x): σ(x)(1 - σ(x))
  - Tanh: 1 - tanh²(x)
  - ReLU: 1 if x > 0, else 0 (undefined at 0)
  - Softmax: σᵢ(δᵢⱼ - σⱼ) where δᵢⱼ is Kronecker delta
- **Log-sum-exp**: d/dx[log(Σᵢeˣⁱ)] = softmax(x)

---
