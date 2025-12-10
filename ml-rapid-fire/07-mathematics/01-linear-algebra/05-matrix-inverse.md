# Matrix Inverse

**Q:** What is a matrix inverse and when does it exist?
- Definition
- When it exists
- Key properties
- Computational considerations

**A:**

- **Definition**: A⁻¹ such that AA⁻¹ = A⁻¹A = I
- **Exists when**: matrix is square AND full rank (det(A) ≠ 0)
- **Properties**:
  - (A⁻¹)⁻¹ = A
  - (AB)⁻¹ = B⁻¹A⁻¹ (reverse order!)
  - (Aᵀ)⁻¹ = (A⁻¹)ᵀ
- **Computational note**: rarely compute inverse directly; solve Ax = b instead (more stable, faster)
- **Pseudoinverse**: A⁺ exists for non-square matrices (used in least squares)

---
