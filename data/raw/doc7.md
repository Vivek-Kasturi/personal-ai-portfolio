# Latency Considerations in RAG Systems

Latency in a RAG system comes from several components:
- Embedding computation for the query
- Vector or hybrid retrieval
- Reranking
- LLM generation

To optimize latency:
- Cache embeddings for frequent queries.
- Use efficient indexes like FAISS.
- Limit reranking to a small candidate set.
- Use streaming responses from the LLM.

Measuring retrieval latency, LLM latency, and total latency separately helps identify bottlenecks.
