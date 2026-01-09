from fastapi import FastAPI
from pydantic import BaseModel

from ingest.loader import load_pdf
from ingest.chunker import chunk_text
from ingest.indexer import VectorIndexer
from rag.retriever import Retriever
from rag.generator import AnswerGenerator

app = FastAPI()

class Query(BaseModel):
    question: str

# ----------- BUILD INDEX ON STARTUP -----------

pdf_text = load_pdf("data/sample.pdf")
chunks = chunk_text(pdf_text)

indexer = VectorIndexer()
indexer.build_index(chunks)

retriever = Retriever(indexer.index, indexer.text_chunks)
generator = AnswerGenerator()

# ----------- API -----------

@app.post("/ask")
def ask(query: Query):
    context = retriever.retrieve(query.question)
    answer = generator.generate(query.question, context)

    return {
        "question": query.question,
        "retrieved_context": context,
        "answer": answer
    }
