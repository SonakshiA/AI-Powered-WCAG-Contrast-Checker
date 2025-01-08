import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint

HUGGINGFACE_API_TOKEN = load_dotenv("HUGGINGFACEHUB_API_TOKEN")
repo_id="Qwen/QwQ-32B-Preview"
llm=HuggingFaceEndpoint(repo_id=repo_id,max_new_tokens=256,temperature=0.7)

def recommend_foreground_color(background_color):
    response = llm.invoke(f"Recommend foreground colors for background color #{background_color} to satisfy WACG AA Level Guidelines in list form. Do not give any extra information")
    print(response)
    return response
