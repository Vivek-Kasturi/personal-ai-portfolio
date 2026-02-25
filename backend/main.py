from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional

from backend.models.embedding_model import EmbeddingModel
from backend.vector_store.client import VectorStoreClient
from retrieval.service import RetrievalService
from backend.services.ingestion_service import IngestionService


# ----------------------------
# App Initialization
# ----------------------------

app = FastAPI(title="Retrieval Backend Service")


# ----------------------------
# Model + Vector DB Setup
# ----------------------------

embedding_model = EmbeddingModel(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_client = VectorStoreClient(
    host="localhost",
    port=6333,
    collection_name="knowledge_base"
)
try:
    vector_client.create_collection()
except:
    pass


# ----------------------------
# Services
# ----------------------------

retrieval_service = RetrievalService(
    embedding_model=embedding_model,
    vector_client=vector_client,
    top_k=5
)

ingestion_service = IngestionService(
    embedding_model=embedding_model,
    vector_client=vector_client
)


# ----------------------------
# Request Schemas
# ----------------------------

class QueryRequest(BaseModel):
    query: str


class IngestRequest(BaseModel):
    text: str
    metadata: Optional[Dict] = None


class RetrievalResponse(BaseModel):
    results: List[Dict]


# ----------------------------
# Routes
# ----------------------------

@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/retrieve", response_model=RetrievalResponse)
async def retrieve_context(request: QueryRequest):
    try:
        results = retrieval_service.retrieve(request.query)
        return RetrievalResponse(results=results)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ingest")
async def ingest_document(request: IngestRequest):
    try:
        result = ingestion_service.ingest(
            document_text=request.text,
            metadata=request.metadata
        )

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ----------------------------
# Server Entry
# ----------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )