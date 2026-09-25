from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
You are EduGenie, a learning assistant.

Create a learning path for:

{topic}

Organize it as:

1. Beginner level
2. Basic concepts
3. Intermediate level
4. Advanced level
5. Practice activities
6. Suggested learning resources

Keep it simple and student-friendly.
"""

    return generate_text(prompt)