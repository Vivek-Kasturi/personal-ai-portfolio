# Hybrid Retrieval: Combining BM25 and Vector Search

Hybrid retrieval combines keyword-based search (e.g., BM25) with dense vector search. This approach leverages the strengths of both methods.

BM25:
- Great for exact matches, rare terms, and acronyms.
- Works well when users know specific keywords.

Vector search:
- Captures semantic similarity.
- Handles paraphrasing and natural language queries.

A simple hybrid strategy is to retrieve candidates from both BM25 and FAISS, then merge and rerank them.
