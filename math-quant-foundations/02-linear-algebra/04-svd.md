# Question

Explain Singular Value Decomposition (SVD) and its applications.

# Answer

**SVD:** Any $m \times n$ matrix $A$ can be decomposed as:

$A = U \Sigma V^T$

where:
- $U$ ($m \times m$): Orthogonal, columns are left singular vectors
- $\Sigma$ ($m \times n$): Diagonal, singular values $\sigma_1 \geq \sigma_2 \geq ... \geq 0$
- $V$ ($n \times n$): Orthogonal, columns are right singular vectors

**Key properties:**

1. **Always exists** (unlike eigendecomposition)
2. **Singular values = square roots of eigenvalues of $A^T A$**
3. **Rank = number of nonzero singular values**
4. **$||A||_2 = \sigma_1$** (spectral norm)
5. **$||A||_F = \sqrt{\sum \sigma_i^2}$** (Frobenius norm)

**Low-rank approximation (Eckart-Young theorem):**

Best rank-$k$ approximation: $A_k = \sum_{i=1}^k \sigma_i u_i v_i^T$

Minimizes $||A - A_k||$ in both spectral and Frobenius norms.

**Applications:**

1. **Pseudoinverse:** $A^+ = V \Sigma^+ U^T$ for least squares
2. **PCA:** SVD of centered data gives principal components
3. **Dimensionality reduction:** Keep top $k$ singular vectors
4. **Condition number:** $\kappa = \sigma_1 / \sigma_n$
5. **Noise reduction:** Truncate small singular values
6. **Matrix completion:** Netflix prize approach

**Numerical stability:** More stable than eigendecomposition for non-symmetric matrices.
