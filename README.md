📄 RAG Document Chatbot

A Retrieval-Augmented Generation (RAG) based document chatbot that allows users to upload documents and ask questions using semantic search and LLM-based answer generation.

🔧 Tech Stack

Backend: FastAPI

Frontend: Streamlit

Vector Store: FAISS

Embeddings: Sentence Transformers

LLM: Ollama (local inference)

Language: Python 3.10+

📂 Project Structure
rag-document-chatbot/
├── app.py
├── streamlit_app.py
├── ingest/
├── rag/
├── vector_store/
├── data/
├── requirements.txt
├── README.md
└── .gitignore

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

🧠 How It Works

Document Loader loads PDF files

Chunker splits text into semantic chunks

Embedder converts chunks into embeddings

FAISS stores vectors for similarity search

Retriever fetches relevant context

Generator uses LLM to answer user queries

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

Shibani M – CSE
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