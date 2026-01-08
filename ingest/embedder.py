from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

# Load embedding model once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_chunks(chunks):
    """
    Convert text chunks into vector embeddings.
    """
    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=True
    )
    return embeddings


def build_faiss_index(embeddings):
    """
    Build a FAISS index from embeddings.
    """
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


def save_index(index, chunks, path="vector_store"):
    """
    Persist FAISS index and metadata.
    """
    os.makedirs(path, exist_ok=True)

    faiss.write_index(index, f"{path}/index.faiss")

    with open(f"{path}/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)


def load_index(path="vector_store"):
    """
    Load FAISS index and metadata.
    """
    index = faiss.read_index(f"{path}/index.faiss")

    with open(f"{path}/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    return index, chunks
