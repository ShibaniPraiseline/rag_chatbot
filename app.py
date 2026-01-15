from fastapi import FastAPI
from pydantic import BaseModel

from ingest.loader import load_pdf
from ingest.chunker import chunk_text
from ingest.indexer import VectorIndexer
from rag.retriever import Retriever
from rag.generator import AnswerGenerator
from ingest.embedder import Embedder




app = FastAPI(title="RAG Chatbot API")

class Query(BaseModel):
    question: str

# ----------- STARTUP -----------

print("📌 Building vector index...")
pdf_text = load_pdf("data/sample.pdf")
chunks = chunk_text(pdf_text)

embedder = Embedder()

indexer = VectorIndexer()
indexer.build_index(chunks)

retriever = Retriever(
    index=indexer.index,
    text_chunks=indexer.text_chunks,
    embedder=embedder
)
generator = AnswerGenerator()

print("✅ RAG system ready!")

# ----------- API -----------

@app.post("/ask")
def ask(query: Query):
    context_chunks = retriever.retrieve(query.question)

    answer = generator.generate(
        query.question,
        context_chunks
    )

    return {
        "question": query.question,
        "context": context_chunks,
        "answer": answer
    }
