from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self, index, chunks, model_name="all-MiniLM-L6-v2"):
        self.index = index
        self.chunks = chunks
        self.model = SentenceTransformer(model_name)

    def retrieve(self, query: str, k: int = 3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, k)
        return [self.chunks[i] for i in indices[0]]
