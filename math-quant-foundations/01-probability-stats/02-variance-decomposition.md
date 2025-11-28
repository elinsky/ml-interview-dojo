# Question

Explain the Law of Total Variance and its applications in finance.

# Answer

**Law of Total Variance (Variance Decomposition):**

$\text{Var}(X) = E[\text{Var}(X|Y)] + \text{Var}(E[X|Y])$

Or mnemonically: **"Total variance = average conditional variance + variance of conditional means"**

**Intuition:**
- First term: Average uncertainty *within* groups
- Second term: Uncertainty *between* group means

**Derivation sketch:**

$\text{Var}(X) = E[X^2] - (E[X])^2$

Apply tower property and expand.

**Finance applications:**

1. **Factor models:** Total stock variance = idiosyncratic variance + factor variance
   
   $\text{Var}(r_i) = \beta_i^2 \text{Var}(r_m) + \text{Var}(\epsilon_i)$

2. **Regime-switching models:** Decompose volatility into within-regime and between-regime components

3. **Hierarchical models:** Understand variance at different levels (e.g., sector vs. stock-specific)

4. **ANOVA:** This is the mathematical foundation of analysis of variance

**Example:** Stock returns conditional on market regime (bull/bear):
- Within-regime variance: How volatile is the stock in each regime?
- Between-regime variance: How different are average returns across regimes?
