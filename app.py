from fastapi import FastAPI
from ingest.indexer import VectorIndexer
from ingest.embedder import Embedder
from rag.retriever import Retriever
from rag.generator import AnswerGenerator
import pickle

app = FastAPI(title="RAG Chatbot API")

# Load FAISS index
indexer = VectorIndexer()
indexer.load_index("vector_store/index.faiss")

# Load chunks
with open("vector_store/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Create embedder
embedder = Embedder()

# Create retriever + generator
retriever = Retriever(indexer.index, chunks, embedder)
generator = AnswerGenerator()

@app.post("/ask")
def ask(query: dict):
    context = retriever.retrieve(query["question"])
    answer = generator.generate(query["question"], context)
    return {"answer": answer, "retrieved_context":chunks}
