# Question

What are eigenvectors and eigenvalues? Why do they matter for PCA and covariance matrices?

# Answer

**Definition:** For matrix $A$, vector $v$ is an eigenvector with eigenvalue $\lambda$ if:

$Av = \lambda v$

The matrix scales $v$ without changing its direction.

**Key properties:**

1. **Symmetric matrices** (like covariance matrices) have:
   - Real eigenvalues
   - Orthogonal eigenvectors
   - Spectral decomposition: $A = Q\Lambda Q^T$

2. **Positive definite matrices** have all positive eigenvalues

3. **Trace = sum of eigenvalues:** $\text{tr}(A) = \sum \lambda_i$

4. **Determinant = product of eigenvalues:** $\det(A) = \prod \lambda_i$

**Connection to PCA:**

For covariance matrix $\Sigma$:
- Eigenvectors = principal component directions
- Eigenvalues = variance explained by each component
- $\lambda_1 \geq \lambda_2 \geq ... \geq \lambda_p$

**Finance applications:**

1. **Risk decomposition:** Eigenvalues of correlation matrix show independent risk factors
2. **Dimensionality reduction:** Keep top $k$ components, discard noise
3. **Condition number:** $\kappa = \lambda_{max}/\lambda_{min}$ measures matrix stability
4. **Random matrix theory:** Marcenko-Pastur distribution for sample covariance eigenvalues

**Numerical computation:** Power iteration, QR algorithm, or SVD (more stable)
