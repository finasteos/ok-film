import argparse
import httpx
from qdrant_client import QdrantClient

LMSTUDIO_URL = "http://172.20.10.6:1234/v1/embeddings"
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "ok_film_repo"

def get_embedding(text):
    """Gets a text embedding from a local LMStudio server."""
    try:
        response = httpx.post(
            LMSTUDIO_URL,
            json={"input": text, "model": "text-embedding-bge-m3"},
            headers={"Content-Type": "application/json"},
            timeout=60,
        )
        response.raise_for_status()
        return response.json()["data"][0]["embedding"]
    except Exception as e:
        print(f"❌ An error occurred while getting embeddings: {e}")
        return None

def search_repository(query):
    """Searches the repository index for a given query."""
    client = QdrantClient(url=QDRANT_URL)
    
    query_embedding = get_embedding(query)
    
    if query_embedding:
        search_result = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_embedding,
            limit=5 # Return the top 5 results
        )
        
        print(f"🔍 Top 5 search results for '{query}':\n")
        for i, result in enumerate(search_result):
            if result.payload:
                print(f"  {i+1}. [Score: {result.score:.4f}] {result.payload.get('file_path')} (chunk {result.payload.get('chunk_index')})")
                print(f"     \"{result.payload.get('content', '')[:100]}...\"\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search the repository index.")
    parser.add_argument("query", help="The search query.")
    args = parser.parse_args()
    search_repository(args.query)