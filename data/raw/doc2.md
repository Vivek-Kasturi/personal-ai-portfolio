# Chunking Strategies for RAG Systems

Chunking is the process of splitting long documents into smaller pieces that can be embedded and retrieved efficiently. Good chunking is critical for RAG performance.

Common strategies:
- Fixed-size chunks (e.g., 500 tokens with 50 token overlap)
- Semantic chunking based on headings or paragraphs
- Hybrid approaches that combine structure and size constraints

Tradeoffs:
- Too small: context becomes fragmented and loses meaning.
- Too large: retrieval becomes noisy and less precise.

A practical starting point is 400–600 tokens per chunk with 10–20% overlap.
