# Question

Summarize key matrix calculus results used in ML and optimization.

# Answer

**Notation conventions:**
- Numerator layout: $\frac{\partial y}{\partial \mathbf{x}}$ has same shape as $\mathbf{x}^T$
- Gradient $\nabla f$ is a column vector

**Essential derivatives:**

| Expression | Derivative |
|------------|------------|
| $\mathbf{a}^T \mathbf{x}$ | $\mathbf{a}$ |
| $\mathbf{x}^T \mathbf{A} \mathbf{x}$ | $(\mathbf{A} + \mathbf{A}^T)\mathbf{x}$ |
| $\mathbf{x}^T \mathbf{A} \mathbf{x}$ (sym $\mathbf{A}$) | $2\mathbf{A}\mathbf{x}$ |
| $||\mathbf{x}||^2$ | $2\mathbf{x}$ |
| $||\mathbf{Ax} - \mathbf{b}||^2$ | $2\mathbf{A}^T(\mathbf{Ax} - \mathbf{b})$ |
| $\log \det(\mathbf{X})$ | $\mathbf{X}^{-1}$ |
| $\text{tr}(\mathbf{AX})$ | $\mathbf{A}^T$ |

**Hessian:** $\mathbf{H} = \nabla^2 f = \frac{\partial^2 f}{\partial \mathbf{x} \partial \mathbf{x}^T}$

For $f(\mathbf{x}) = \mathbf{x}^T \mathbf{A} \mathbf{x}$: $\mathbf{H} = \mathbf{A} + \mathbf{A}^T$

**Chain rule:**
$\frac{\partial f}{\partial \mathbf{x}} = \frac{\partial f}{\partial \mathbf{y}} \frac{\partial \mathbf{y}}{\partial \mathbf{x}}$

**ML applications:**

1. **Linear regression normal equations:**
   $\nabla_\beta ||\mathbf{y} - \mathbf{X}\beta||^2 = 0 \Rightarrow \hat{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$

2. **Logistic regression:** Gradient and Hessian for Newton's method

3. **Neural networks:** Backpropagation is chain rule

4. **Gaussian MLE:** Derivatives of log-likelihood involve $\Sigma^{-1}$

**Common identities:**
- $\nabla_{\mathbf{X}} \text{tr}(\mathbf{X}^T \mathbf{A}) = \mathbf{A}$
- $\nabla_{\mathbf{X}} \text{tr}(\mathbf{A}\mathbf{X}\mathbf{B}) = \mathbf{A}^T\mathbf{B}^T$
