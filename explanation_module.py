from gemini_client import generate_text


def explain_topic(topic: str) -> str:
    prompt = f"""
You are EduGenie, a beginner-friendly educational assistant.

Explain the following topic in a simple way.

Topic:
{topic}

Give the explanation using:

1. Simple definition
2. Main idea
3. Important points
4. Simple real-life example
5. Short conclusion

Use easy English suitable for a beginner.
"""

    return generate_text(prompt)