# ingest/embed_index.py

from ingest.loader import load_pdf
from ingest.chunker import chunk_text
from ingest.embedder import Embedder
from ingest.indexer import VectorIndexer
import pickle

# 1️⃣ Load PDF & chunk
pdf_text = load_pdf("data/sample.pdf")
chunks = chunk_text(pdf_text)

# 2️⃣ Create embeddings
embedder = Embedder()
embeddings = embedder.encode(chunks)  # Encode all chunks

# 3️⃣ Build & save FAISS index
indexer = VectorIndexer()
indexer.build_index(embeddings)
indexer.save_index("vector_store/index.faiss")

# 4️⃣ Save chunks for retrieval
with open("vector_store/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("✅ Index and embeddings saved!")
