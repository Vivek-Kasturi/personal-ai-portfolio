# Evaluating RAG Systems

Evaluating a RAG system requires more than just model metrics. You need to measure:

- Retrieval quality: precision@k, recall@k, MRR
- Answer quality: faithfulness, relevance, completeness
- System metrics: latency, throughput, cost per query

Tools like RAGAS can automate parts of this evaluation by scoring how well the answer aligns with the retrieved context and the ground truth.
