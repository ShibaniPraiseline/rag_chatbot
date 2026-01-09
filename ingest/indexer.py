import faiss
import pickle
from sentence_transformers import SentenceTransformer

class VectorIndexer:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.text_chunks = []

    def build_index(self, chunks: list[str]):
        embeddings = self.model.encode(chunks, show_progress_bar=True)
        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

        self.text_chunks = chunks

    def save(self, path="vector_store.pkl"):
        with open(path, "wb") as f:
            pickle.dump((self.index, self.text_chunks), f)

    def load(self, path="vector_store.pkl"):
        with open(path, "rb") as f:
            self.index, self.text_chunks = pickle.load(f)
