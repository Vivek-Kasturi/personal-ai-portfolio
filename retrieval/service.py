# retrieval/service.py

from typing import List, Dict, Any
import numpy as np

from backend.models.embedding_model import EmbeddingModel
from backend.vector_store.client import VectorStoreClient


class RetrievalService:
    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_client: VectorStoreClient,
        top_k: int = 5,
    ):
        self.embedding_model = embedding_model
        self.vector_client = vector_client
        self.top_k = top_k

    def embed_query(self, query: str) -> List[float]:
        return self.embedding_model.encode(query)

    def retrieve(self, query: str) -> List[Dict[str, Any]]:
        """
        Main retrieval pipeline
        """

        query_vector = self.embed_query(query)

        results = self.vector_client.search(
            vector=query_vector,
            top_k=self.top_k
        )

        return self._rerank_results(query, results)

    # ----------------------------
    # Reranking
    # ----------------------------

    def _rerank_results(self, query: str, results):

        scored = []

        for doc in results:

            payload = doc.get("payload", {})
            score = doc.get("score", 0)

            scored.append({
                "content": payload.get("content", ""),
                "metadata": payload.get("metadata", {}),
                "score": float(score)
            })

        scored.sort(key=lambda x: x["score"], reverse=True)

        # Remove duplicates
        unique = []
        seen = set()

        for item in scored:
            if item["content"] not in seen:
                unique.append(item)
                seen.add(item["content"])

        return unique[: self.top_k]
    # ----------------------------
    # Similarity Utility
    # ----------------------------

    @staticmethod
    def _cosine_similarity(a, b) -> float:
        if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
            return 0.0

        return float(np.dot(a, b) /
                     (np.linalg.norm(a) * np.linalg.norm(b)))