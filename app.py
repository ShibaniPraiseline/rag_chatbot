from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import numpy as np

app = FastAPI(title="RAG Chatbot - Internship Grade")

# -----------------------------
# 1. Load documents (knowledge)
# -----------------------------
documents = [
    "RAG stands for Retrieval Augmented Generation. It combines information retrieval with text generation.",
    "FAISS is a library for efficient similarity search and clustering of dense vectors.",
    "FastAPI is a modern, fast Python web framework used for building APIs."
]

# -----------------------------
# 2. Embedding model
# -----------------------------
embedder = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = embedder.encode(documents)

# -----------------------------
# 3. FAISS index
# -----------------------------
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))

# -----------------------------
# 4. LLM (local, free)
# -----------------------------
llm = pipeline(
    "text-generation",
    model="distilgpt2",
    max_new_tokens=150
)

# -----------------------------
# 5. Request schema
# -----------------------------
class Query(BaseModel):
    question: str

# -----------------------------
# 6. RAG endpoint
# -----------------------------
@app.post("/ask")
def ask(query: Query):
    # Embed query
    query_embedding = embedder.encode([query.question])

    # Retrieve top document
    distances, indices = index.search(np.array(query_embedding), k=1)
    context = documents[indices[0][0]]

    # Evidence-bounded prompt
    prompt = f"""
You are an AI assistant.
Answer the question ONLY using the context below.
If the answer is not in the context, say "I don't know based on the given information."

Context:
{context}

Question:
{query.question}

Answer:
"""

    response = llm(prompt)[0]["generated_text"]

    return {
        "question": query.question,
        "retrieved_context": context,
        "answer": response
    }
