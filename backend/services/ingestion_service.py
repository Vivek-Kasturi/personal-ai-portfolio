from typing import List
from backend.models.embedding_model import EmbeddingModel
from backend.vector_store.client import VectorStoreClient
import uuid


class IngestionService:
    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_client: VectorStoreClient,
        chunk_size: int = 500
    ):
        self.embedding_model = embedding_model
        self.vector_client = vector_client
        self.chunk_size = chunk_size

    def chunk_text(self, text: str) -> List[str]:
        return [
            text[i:i + self.chunk_size]
            for i in range(0, len(text), self.chunk_size)
        ]

    def ingest(self, document_text: str, metadata: dict = None):

        metadata = metadata or {}

        chunks = self.chunk_text(document_text)

        points = []

        for chunk in chunks:

            vector = self.embedding_model.encode(chunk)

            point = {
                "id": str(uuid.uuid4()),
                "vector": vector,
                "payload": {
                    "content": str(chunk),
                    "metadata": metadata
                }
            }

            points.append(point)

        self.vector_client.upsert(points)

        return {
            "status": "success",
            "chunks_ingested": len(points)
        }