import faiss
import pickle

class VectorIndexer:
    def __init__(self):
        self.index = None
        self.text_chunks = None

    # OPTIONAL: only for local index building
    def build_index(self, embeddings, chunks):
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        self.text_chunks = chunks

    # ✅ REQUIRED for deployment
    def load_index(self, index_path, chunks_path):
        self.index = faiss.read_index(index_path)
        with open(chunks_path, "rb") as f:
            self.text_chunks = pickle.load(f)
