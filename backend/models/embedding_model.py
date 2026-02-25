# backend/models/embedding_model.py

from sentence_transformers import SentenceTransformer
from typing import List


class EmbeddingModel:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode(self, text: str) -> List[float]:
        embedding = self.model.encode([text])[0]
        return embedding.tolist()