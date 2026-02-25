import os
import json
import faiss
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

DATA_DIR = "data/raw"
INDEX_PATH = "data/faiss.index"
META_PATH = "data/metadata.json"

def load_documents():
    docs = []
    for fname in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, fname)
        if fname.endswith(".md") or fname.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                docs.append((fname, f.read()))
    return docs

def chunk_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    chunks = []
    metadata = []

    for fname, text in docs:
        for chunk in splitter.split_text(text):
            chunks.append(chunk)
            metadata.append({"source": fname, "text": chunk})
    return chunks, metadata

def build_faiss_index(chunks, metadata):
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    print("Embedding chunks...")
    embeddings = model.encode(chunks, show_progress_bar=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)

    with open(META_PATH, "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"Saved index to {INDEX_PATH}")
    print(f"Saved metadata to {META_PATH}")

if __name__ == "__main__":
    docs = load_documents()
    chunks, metadata = chunk_documents(docs)
    build_faiss_index(chunks, metadata)
