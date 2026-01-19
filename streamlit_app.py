import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="RAG Chatbot")

st.title("📄 RAG Document Chatbot")

query = st.text_input("🔍 Enter your question")

if st.button("Get Answer"):
    if not query.strip():
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            response = requests.post(
                API_URL,
                json={"question": query}
            )

            if response.status_code == 200:
                data = response.json()
                st.success("Answer")
                st.write(data["answer"])

                with st.expander("📚 Retrieved Context"):
                    for i, chunk in enumerate(data["retrieved_context"], 1):
                       st.write(f"Chunk {i}: {chunk}")
            else:
                st.error("Backend error")
