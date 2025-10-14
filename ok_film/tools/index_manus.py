import argparse
import json
import httpx
from qdrant_client import QdrantClient, models

LMSTUDIO_URL = "http://172.20.10.6:1234/v1/embeddings"
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "ok_film_manus"

def get_embedding(text):
    """
    Gets a text embedding from a local LMStudio server.
    """
    try:
        response = httpx.post(
            LMSTUDIO_URL,
            json={"input": text, "model": "text-embedding-bge-m3"},
            headers={"Content-Type": "application/json"},
            timeout=60,
        )
        response.raise_for_status()
        return response.json()["data"][0]["embedding"]
    except (httpx.ConnectError, httpx.ReadTimeout) as e:
        print(f"❌ Could not connect to LMStudio at {LMSTUDIO_URL}")
        print("   Please ensure LMStudio is running and the server is started.")
        return None
    except Exception as e:
        print(f"❌ An error occurred while getting embeddings: {e}")
        return None

def index_manuscript(manus_path):
    """
    Reads the manuscript, generates embeddings, and upserts them to Qdrant.
    """
    with open(manus_path, 'r', encoding='utf-8') as f:
        manus = json.load(f)

    client = QdrantClient(url=QDRANT_URL)
    
    # Create collection if it doesn't exist
    try:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE), # bge-m3 has 1024 dimensions
        )
        print(f"📚 Collection '{COLLECTION_NAME}' created in Qdrant.")
    except Exception as e:
        print(f"⚠️  Could not create collection (it may already exist): {e}")


    points = []
    for scene in manus.get('scenes', []):
        for event in scene.get('events', []):
            text_to_embed = f"{event['character']}: {event['dialogue']} {event['visual']}"
            embedding = get_embedding(text_to_embed)
            
            if embedding:
                points.append(models.PointStruct(
                    id=f"{scene['scene_id']}_{event['time']}",
                    vector=embedding,
                    payload={
                        "scene": scene['scene_id'],
                        "time": event['time'],
                        "character": event['character'],
                        "dialogue": event['dialogue'],
                        "visual": event['visual'],
                        "audio": event['audio']
                    }
                ))

    if points:
        client.upsert(collection_name=COLLECTION_NAME, points=points, wait=True)
        print(f"✅ Successfully indexed {len(points)} points from the manuscript.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Index the film manuscript into Qdrant.")
    parser.add_argument("--manus", default="scripts/our_manus_timed.json", help="Path to the timed manuscript JSON file.")
    args = parser.parse_args()
    index_manuscript(args.manus)