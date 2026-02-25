# Cross-Encoder Reranking

Reranking is the process of taking an initial set of retrieved documents and reordering them using a more powerful model. Cross-encoders are often used for this because they jointly encode the query and document.

Advantages:
- Higher relevance accuracy than pure vector similarity.
- Better handling of subtle semantic differences.

Disadvantages:
- Slower and more expensive than bi-encoders.
- Typically used only on the top-k candidates (e.g., top 50).

In a RAG system, reranking can significantly improve the quality of the final context passed to the LLM.
