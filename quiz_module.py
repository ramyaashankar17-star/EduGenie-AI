import json

from gemini_client import generate_text


def generate_quiz(topic: str):
    prompt = f"""
Create a short educational quiz about:

{topic}

Create exactly 3 multiple-choice questions.

Each question must have:
- question
- options: exactly 4 options
- answer: the correct option
- explanation: short explanation

Return ONLY valid JSON.

Use this exact format:

[
    {{
        "question": "Question here",
        "options": [
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "answer": "Option A",
        "explanation": "Short explanation"
    }}
]
"""

    result = generate_text(prompt)

    try:
        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

        quiz = json.loads(result)

        if not isinstance(quiz, list):
            raise ValueError("Quiz response is not a list.")

        return quiz

    except Exception:
        return {
            "error": "Quiz generation failed.",
            "raw_response": result
        }