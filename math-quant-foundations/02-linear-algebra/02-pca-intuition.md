# Question

Explain PCA intuitively and its applications in quantitative finance.

# Answer

**PCA finds orthogonal directions of maximum variance in data.**

**Algorithm:**
1. Center data (subtract mean)
2. Compute covariance matrix $\Sigma$
3. Find eigenvalues/eigenvectors of $\Sigma$
4. Project data onto top $k$ eigenvectors

**Intuition:** Rotate axes to align with data's natural spread. First PC captures most variance, second captures most remaining variance (orthogonal to first), etc.

**Mathematical formulation:**

First PC: $w_1 = \arg\max_{||w||=1} w^T \Sigma w$

This is the eigenvector with largest eigenvalue.

**Variance explained:** $\frac{\lambda_k}{\sum_i \lambda_i}$ for component $k$

**Finance applications:**

1. **Factor models:** First few PCs often correspond to:
   - PC1: Market factor (all stocks move together)
   - PC2-3: Sector/style factors
   
2. **Yield curve modeling:** 3 PCs explain ~99% of Treasury curve moves:
   - PC1: Level (parallel shift)
   - PC2: Slope (steepening/flattening)
   - PC3: Curvature (butterfly)

3. **Risk management:** Reduce dimensionality of large covariance matrices

4. **Statistical arbitrage:** Find mean-reverting combinations

**Limitations:**
- Linear only (consider kernel PCA for nonlinear)
- Sensitive to scaling (normalize first?)
- Assumes variance = importance
