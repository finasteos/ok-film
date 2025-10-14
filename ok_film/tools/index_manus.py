import argparse
import os
import httpx
from qdrant_client import QdrantClient, models
import git
from uuid import uuid4

LMSTUDIO_URL = "http://172.20.10.6:1234/v1/embeddings"
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "ok_film_repo"
CHUNK_SIZE = 512 # Number of characters per chunk

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
    except (httpx.ConnectError, httpx.ReadTimeout):
        print(f"❌ Could not connect to LMStudio at {LMSTUDIO_URL}")
        print("   Please ensure LMStudio is running and the server is started.")
        return None
    except Exception as e:
        print(f"❌ An error occurred while getting embeddings: {e}")
        return None

def get_git_ignored_files(repo_path):
    """Returns a set of git ignored files."""
    repo = git.Repo(repo_path, search_parent_directories=True)
    ignored_files = repo.ignored(repo.untracked_files)
    return set(ignored_files)

def index_repository(repo_path):
    """Reads all non-ignored files, generates embeddings, and upserts them to Qdrant."""
    client = QdrantClient(url=QDRANT_URL)
    
    try:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE),
        )
        print(f"📚 Collection '{COLLECTION_NAME}' created in Qdrant.")
    except Exception as e:
        print(f"⚠️  Could not create collection (it may already exist): {e}")

    ignored_files = get_git_ignored_files(repo_path)
    points = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, repo_path)

            if relative_path in ignored_files or ".git" in relative_path:
                continue

            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                chunks = [content[i:i+CHUNK_SIZE] for i in range(0, len(content), CHUNK_SIZE)]
                
                for i, chunk in enumerate(chunks):
                    embedding = get_embedding(chunk)
                    if embedding:
                        points.append(models.PointStruct(
                            id=str(uuid4()),
                            vector=embedding,
                            payload={
                                "file_path": relative_path,
                                "chunk_index": i,
                                "content": chunk
                            }
                        ))
            except Exception as e:
                print(f"Could not process file {file_path}: {e}")

    if points:
        client.upsert(collection_name=COLLECTION_NAME, points=points, wait=True)
        print(f"✅ Successfully indexed {len(points)} chunks from the repository.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Index the entire repository into Qdrant.")
    parser.add_argument("--path", default=".", help="Path to the repository to index.")
    args = parser.parse_args()
    index_repository(args.path)