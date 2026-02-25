from typing import List, Dict, Any
import requests


class VectorStoreClient:
    def __init__(
        self,
        host: str,
        port: int,
        collection_name: str
    ):
        self.base_url = f"http://{host}:{port}"
        self.collection_name = collection_name

    def search(self, vector: List[float], top_k: int = 5):

        url = f"{self.base_url}/collections/{self.collection_name}/points/search"

        payload = {
            "vector": vector,
            "limit": top_k,
            "with_payload": True
        }

        response = requests.post(url, json=payload)

        if response.status_code != 200:
            return []

        return response.json().get("result", [])

    def upsert(self, points):

        url = f"{self.base_url}/collections/{self.collection_name}/points"

        payload = {
            "points": points
        }

        response = requests.put(url, json=payload)

        return response.json()

    def create_collection(self, vector_size: int = 384):

        url = f"{self.base_url}/collections/{self.collection_name}"

        payload = {
            "vectors": {
                "size": vector_size,
                "distance": "Cosine"
            }
        }

        requests.put(url, json=payload)