from gemini_client import generate_text


def summarize_text(text: str) -> str:
    prompt = f"""
You are EduGenie, an educational assistant.

Summarize the following text for a student.

Text:
{text}

Requirements:
- Keep the main ideas.
- Remove unnecessary repetition.
- Use simple English.
- Present important points clearly.
- Make it useful for revision.
"""

    return generate_text(prompt)