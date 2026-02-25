# Vector Search with FAISS

FAISS is a library developed by Meta for efficient similarity search and clustering of dense vectors. It is widely used in RAG systems to perform nearest neighbor search over document embeddings.

Key concepts:
- IndexFlatL2: exact search using L2 distance.
- IVF indexes: approximate search for large-scale datasets.
- GPU support: accelerates search for millions of vectors.

For small to medium projects, IndexFlatL2 is often sufficient and easy to use.
