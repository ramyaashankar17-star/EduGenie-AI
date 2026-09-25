from gemini_client import generate_text


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and accurately.

Question:
{question}

Instructions:
- Use simple language.
- Give a direct answer.
- Explain important points.
- Use examples when useful.
- Keep the answer suitable for a student.
"""

    return generate_text(prompt)