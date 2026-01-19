import faiss

class VectorIndexer:
    def __init__(self):
        self.index = None

    def load_index(self, index_path):
        self.index = faiss.read_index(index_path)
