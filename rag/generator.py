import requests

class AnswerGenerator:
    def __init__(self, model="mistral"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, question, context_chunks):
        # limit context (VERY IMPORTANT)
        context = "\n\n".join(context_chunks[:3])

        prompt = f"""
Answer the question using ONLY the context below.
If the answer is not in the context, say "Not found in document".

Context:
{context}

Question:
{question}

Answer:
"""

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]
