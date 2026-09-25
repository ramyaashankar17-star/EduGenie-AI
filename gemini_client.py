import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Please add it to the .env file."
    )


client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.5-flash"


def generate_text(prompt: str) -> str:
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            if not response.text:
                return "Sorry, I couldn't generate a response."

            return response.text.strip()

        except Exception as e:
            error_message = str(e)

            if "503" in error_message and attempt < 2:
                time.sleep(3)
                continue

            return f"AI Error: {error_message}"