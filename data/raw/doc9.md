# Minimal RAG Pipeline Design

A minimal RAG pipeline has the following steps:

1. Load and chunk documents.
2. Embed chunks and store them in a vector index.
3. At query time, embed the query.
4. Retrieve the top-k most similar chunks.
5. Build a prompt that includes the query and retrieved context.
6. Call the LLM and return the answer.

This baseline is essential before adding agents, tools, or complex orchestration.
