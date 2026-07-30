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
prompt="Explain how internet works."
message = {
    "role": role,
    "content": prompt
}
messages=[message]

#Normal way of getting response

# response = client.chat.completions.create( model=model, messages=messages)
# # print(response)
# answer=response.choices[0].message.content
# print(answer)


#Using Streaming way of getting response
#Response = stream

stream=client.chat.completions.create(model=model, messages=messages, stream=True)  #By default Stream false hota hai Likhne ki jarurt nhi

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)

