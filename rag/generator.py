from transformers import pipeline

class AnswerGenerator:
    def __init__(self):
        self.generator = pipeline(
            "text-generation",
            model="gpt2",
            max_new_tokens=150
        )

    def generate(self, question: str, context: list[str]) -> str:
        prompt = f"""
Answer the question using ONLY the context below.

Context:
{' '.join(context)}

Question:
{question}

Answer:
"""
        output = self.generator(prompt)
        return output[0]["generated_text"]
