# Introduction to Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is a pattern where a language model is combined with an external knowledge source, such as a vector database or document store. Instead of relying purely on parametric memory, the model retrieves relevant context at query time and conditions its generation on that context.

The core idea is simple:
1. Encode the user query into an embedding.
2. Retrieve the most similar chunks from a document store.
3. Build a prompt that includes both the query and the retrieved context.
4. Ask the LLM to answer using only that context.

RAG improves factual accuracy, reduces hallucinations, and allows models to stay up to date without retraining.
