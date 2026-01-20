📄 RAG-Based Document Question Answering Chatbot

🔍 Problem Statement
Large Language Models (LLMs) are powerful but cannot reliably answer questions about private or custom documents such as PDFs, reports, or internal notes because these documents are not part of their training data. Directly prompting an LLM with an entire document is inefficient, costly, and prone to hallucinations due to context window limitations.

This project solves the problem by building a Retrieval-Augmented Generation (RAG) based chatbot that allows users to ask natural language questions about a document and receive accurate, context-grounded answers.

🎯 Objective

Enable question answering over PDF documents

Prevent hallucinations by grounding answers in retrieved document context

Use modern embedding models and vector search

Demonstrate a clean, modular RAG architecture suitable for production
🧠 Solution Overview (RAG Architecture)

This system follows a Retrieval-Augmented Generation (RAG) pipeline:
PDF Document
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embedding Generation
   ↓
Vector Store (FAISS)
   ↓
Query Embedding
   ↓
Semantic Retrieval
   ↓
LLM Answer Generation
   ↓
User Interface

Key Idea

Instead of sending the entire document to the LLM, the system:

Retrieves only the most relevant chunks using vector similarity search

Injects those chunks into the LLM prompt

Forces the model to answer only from retrieved context

This improves accuracy, efficiency, and trustworthiness.

🏗️ Project Architecture
rag-chatbot/
│
├── ingest/
│   ├── embedder.py        # Generates embeddings using SentenceTransformer
│   ├── indexer.py         # Loads FAISS vector index
│
├── rag/
│   ├── retriever.py       # Retrieves relevant chunks from FAISS
│   ├── generator.py      # Generates answers using LLM (Ollama)
│
├── vector_store/
│   ├── index.faiss        # FAISS vector index
│   ├── chunks.pkl        # Stored text chunks
│
├── utils/
│   ├── load_pdf.py        # PDF text extraction
│
├── api.py                 # FastAPI backend
├── streamlit_app.py       # Streamlit frontend
├── requirements.txt
└── README.md


🔧 Tech Stack

Backend: FastAPI

Frontend: Streamlit

Vector Store: FAISS

Embeddings: Sentence Transformers

LLM: Ollama (local inference)

Language: Python 3.10+



⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/rag-document-chatbot.git
cd rag-document-chatbot

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
Start FastAPI Backend
uvicorn app:app --reload


Backend runs at:

http://127.0.0.1:8000

Start Streamlit Frontend
streamlit run streamlit_app.py

🚀 How It Works (Runtime Flow)

User enters a question in the Streamlit UI

Question is sent to FastAPI backend

Backend embeds the query

FAISS retrieves top-k relevant chunks

Retrieved context is injected into the LLM prompt

LLM generates a grounded answer

Answer + retrieved context is shown to the user

📌 Features

Offline RAG system

Local LLM via Ollama

Fast semantic search

Clean modular architecture

Easy deployment

🎥 Demo

See demo_video.md for demo link and walkthrough.

📌 Future Enhancements

Multi-document upload

Chat history

Hybrid search (BM25 + FAISS)

Cloud deployment (Docker)

👩‍💻 Author

Shibani M – CSE III yr
AI | NLP | RAG Systems | Backend Development

✅ Deployment Notes (Important)

✔ This WILL work in deployment if:

Ollama is installed on server OR

You replace it with OpenAI / HuggingFace API

FAISS index is rebuilt in production

✔ For cloud:

Use Docker

Replace 127.0.0.1 with service hostname

Disable --reload
