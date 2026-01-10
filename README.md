# RAG Chatbot using FastAPI and FAISS

A simple Retrieval-Augmented Generation (RAG) system that allows users to query documents and receive context-aware answers using vector search and large language models.

## 📌 Project Overview

This project implements a basic Retrieval-Augmented Generation (RAG) pipeline using Python.  
It enables users to ask questions over provided documents by retrieving relevant chunks using vector similarity search and generating answers grounded in the retrieved content.

## ❓ Problem Statement

Large Language Models (LLMs) often generate incorrect or hallucinated answers when they do not have access to domain-specific knowledge.  
This project addresses that issue by retrieving relevant information from documents before generating responses, ensuring answers are context-aware and fact-based.

## 🏗️ System Architecture

The system follows a standard RAG workflow:

1. Documents are loaded and split into smaller chunks  
2. Each chunk is converted into vector embeddings  
3. Embeddings are stored in a FAISS vector index  
4. User queries are embedded and matched against stored vectors  
5. The most relevant chunks are sent to the language model  
6. The model generates an answer based on retrieved context  

## 🧩 Architecture Diagram

### Query-Time Flow
User → FastAPI → FAISS Retriever → Context Chunks → Answer Generator → Response

### Indexing Flow
Document → Loader → Chunker → Embeddings → FAISS Index

**Flow:**

User Query  
→ FastAPI Backend  
→ Vector Retriever (FAISS)  
→ Relevant Document Chunks  
→ Answer Generator (LLM)  
→ Final Response

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- FAISS
- Sentence Transformers
- Uvicorn

## 📂 Project Structure

rag_chatbot/
├── app.py # FastAPI entry point
├── ingest/
│ ├── loader.py # Document loading
│ ├── chunker.py # Text chunking
│ └── retriever.py # FAISS-based retrieval
├── rag/
│ └── generator.py # Answer generation
├── data/
│ └── sample.pdf # Example document
├── requirements.txt
└── README.md


## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
▶️ Running the Application
Start the FastAPI server:

bash
Copy code
uvicorn app:app --reload
The API will be available at:
http://127.0.0.1:8000

API documentation (Swagger UI):
http://127.0.0.1:8000/docs

🧪 Example Usage
Provide a document (PDF)

Ask a question related to the document

The system retrieves relevant content and generates a grounded response

🎓 Learning Outcomes
Understanding of Retrieval-Augmented Generation (RAG)

Working with vector embeddings and FAISS

Building APIs using FastAPI

Structuring a machine learning backend project

Managing Python virtual environments

