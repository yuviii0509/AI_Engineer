from fastapi import FastAPI, UploadFile, File
from Backend.models import MatchRequest
from Backend.matching import match_resume
from Backend.llm import ask_llm
from Backend.parser import extract_text

import os
import json
from Backend.memory import save_resume, get_resume

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Portfolio Backend Running 🚀"}


@app.get("/chat")
def chat(question: str):
    return {
        "question": question,
        "response": "Chat API Working 🚀"
    }


@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):

    # Create Uploads folder if it doesn't exist
    os.makedirs("Uploads", exist_ok=True)

    # Save uploaded resume
    file_path = os.path.join("Uploads", file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Extract text from PDF
    text = extract_text(file_path)

    # Read Resume Parser Prompt
    with open("Prompts/resume_parser.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    # Create messages for LLM
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": text
        }
    ]

    # Get AI Response
    parsed_resume = ask_llm(messages)

    # Convert JSON string to Python Dictionary
    parsed_resume = json.loads(parsed_resume)
    save_resume(parsed_resume)

    return {
        "filename": file.filename,
        "parsed_resume": parsed_resume
    }


@app.post("/match_resume")
async def match_resume_api(request: MatchRequest):

    with open("Prompts/jd_matcher.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    result = match_resume(
        request.resume,
        request.job_description,
        system_prompt
    )

    result = json.loads(result)
    return {
        "result": result
    }