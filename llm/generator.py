from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_new_tokens=200
)


def generate_answer(context, question):
    """
    Generate an answer strictly based on provided context.
    """
    prompt = f"""
You are an assistant answering questions using ONLY the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
    response = generator(prompt)
    return response[0]["generated_text"]
