from groq import Groq
from Backend.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

MODEL = "llama-3.3-70b-versatile"


def ask_llm(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message.content