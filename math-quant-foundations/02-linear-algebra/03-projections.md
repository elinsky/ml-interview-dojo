# Question

What is an orthogonal projection? How is it used in regression and least squares?

# Answer

**Orthogonal projection** of $b$ onto subspace spanned by columns of $A$:

$\hat{b} = A(A^T A)^{-1} A^T b = Pb$

where $P = A(A^T A)^{-1} A^T$ is the **projection matrix**.

**Properties of P:**
- $P^2 = P$ (idempotent): projecting twice = projecting once
- $P^T = P$ (symmetric)
- Eigenvalues are 0 or 1
- $\text{rank}(P) = \text{tr}(P) = $ dimension of subspace

**Connection to OLS regression:**

For $y = X\beta + \epsilon$:

$\hat{\beta} = (X^T X)^{-1} X^T y$

$\hat{y} = X\hat{\beta} = X(X^T X)^{-1} X^T y = Py$

The fitted values are the projection of $y$ onto column space of $X$.

**Residuals are orthogonal to predictions:**
$\hat{\epsilon} = y - \hat{y} = (I - P)y$
$X^T \hat{\epsilon} = 0$

**Finance applications:**

1. **Beta estimation:** Regress stock returns on market returns
2. **Hedging:** Project payoff onto tradeable instruments
3. **Replication:** Find portfolio that best mimics target
4. **Orthogonalization:** Gram-Schmidt to create uncorrelated factors

**Geometric insight:** Least squares finds the point in column space of $X$ closest to $y$. The residual is perpendicular to this subspace.
