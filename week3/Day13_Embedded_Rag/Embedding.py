import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq    
import numpy as np
from sentence_transformers import SentenceTransformer


def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

model= SentenceTransformer('all-MiniLM-L6-v2')  #384 ka Model----->Jitna tagda model hoga utna hi accurate answer milega like #14000 wala model
text="Machine learning is Fun."

# embedding=model.encode(text)
# print(embedding.shape)
# print(embedding[0:10])  #384 ka shape hoga

t1="There are 24 paid leaves"
t2="Vastegone hoiyaaaaaa"

v1=model.encode(t1)
v2=model.encode(t2)
print(cosine_similarity(v1,v2))  #0.8 ka similarity score aayega