import faiss
import json
from sentence_transformers import SentenceTransformer

INDEX_PATH = "data/faiss.index"
META_PATH = "data/metadata.json"

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
index = faiss.read_index(INDEX_PATH)

with open(META_PATH, "r") as f:
    metadata = json.load(f)

def retrieve(query, k=5):
    q_emb = model.encode([query])
    D, I = index.search(q_emb, k)
    results = [metadata[i] for i in I[0]]
    return results

if __name__ == "__main__":
    query = input("Enter query: ")
    results = retrieve(query)

    print("\nTop 5 Chunks:\n")
    for r in results:
        print("SOURCE:", r["source"])
        print(r["text"])
        print("-" * 80)
    