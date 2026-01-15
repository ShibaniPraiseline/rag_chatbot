import numpy as np

class Retriever:
    def __init__(self, index, text_chunks, embedder, k=3):
        self.index = index
        self.text_chunks = text_chunks
        self.embedder = embedder
        self.k = k

    def retrieve(self, query: str):
        # 🔥 FIX: embed the query
        query_embedding = self.embedder.embed([query])
        query_embedding = np.array(query_embedding).astype("float32")

        scores, indices = self.index.search(query_embedding, self.k)

        return [self.text_chunks[i] for i in indices[0]]
