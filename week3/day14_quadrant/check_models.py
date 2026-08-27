import os
from dotenv import load_dotenv
from groq import Groq

# Load the API key from your .env file
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Ask Groq for the list of models this API key can use
models = client.models.list()

print("Available models for your exact API key:")
for m in models.data:
    print(f"- {m.id}")