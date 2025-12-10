# Multi-Head Attention

**Q:** Why use multi-head attention instead of single attention?

**A:**

- Each head learns different types of relationships
- E.g., one head for grammar, another for syntax, another for content
- Concat all heads → linear projection to combine
- More expressive than single attention of same size
- Typical: 8-12 heads

**See also:** [[202105270800 Transformers]]

---
