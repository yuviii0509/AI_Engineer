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
role="user"
prompt="Suggest a name for my food company. suggest 1 name only "

#System
message_system={
    "role":"system",
    "content":"You are my brand manager who suggests name for food brand"
}
#Message me role and content
message = {
    "role": role,
    "content": prompt
}
messages=[message_system, message]

#Temperature bydefault is always 0 which means safe
#reponse meh model, msg thaa usme temperature bhi abhi add kiya mostly range [0,1,2] hi lena
response = client.chat.completions.create( model=model, messages=messages, temperature=0)
# print(response)

print("#########################################")

answer=response.choices[0].message.content
print(answer)