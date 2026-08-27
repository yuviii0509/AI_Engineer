import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key Kaha Bhai???")

client = Groq(api_key=my_api_key)

model= "llama-3.3-70b-versatile"

#Step 1........(Knowledge Base...providing the knowledge of content in the form of a dictionary)
knowledge_base={
   "age": "Yuvraj is 20 years old",
   "net worth": "Yuvraj has a net worth of 1 crore rupees"
}

#Step 2.........(Retrieve the answer from the knowledge base)
def retrieve_info(question):
    question_lower=question.lower()
    if "age" in question_lower:
        return knowledge_base["age"]
    elif "net worth" in question_lower:
        return knowledge_base["net worth"]
    else:
        return "Sorry, I don't have information on that."



def ask_llm(question):
    context=retrieve_info(question)

    sys_prompt=f"""Answer in one line only. 
    Answer only based on the content provided in the knowledge base.
      If the answer is not present in the knowledge base, then say 'Sorry, I don't have information on that.' 
      Do not Hallucinate. Do not make up any answer. Here is the context: {context} """
    system_message={
        "role": "system",
        "content": sys_prompt
    }

    message={
        "role": "user",
        "content": question
    }
    messages=[system_message, message]
    response = client.chat.completions.create(model=model,messages=messages)
    answer = response.choices[0].message.content
    return answer

question = "Who is Yuvraj Singh?"
print(ask_llm(question))
