# Matrix Multiplication

**Q:** How does matrix multiplication work and what are the key rules?
- Dimension requirement
- Result dimensions
- How to compute
- Associativity and commutativity

**A:**

- **Dimension requirement**: (m × n) · (n × p) — inner dimensions must match
- **Result**: (m × n) · (n × p) = (m × p)
- **Computation**: Cᵢⱼ = Σₖ AᵢₖBₖⱼ (row i of A dot column j of B)
- **Properties**:
  - Associative: (AB)C = A(BC)
  - NOT commutative: AB ≠ BA in general
  - Distributive: A(B + C) = AB + AC
- **Intuition**: each column of result is a linear combination of columns of A

---
