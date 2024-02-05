from dotenv import load_dotenv
import os

# Open AI LLM Integration
# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

# Local Llama 2 
from langchain_community.llms import Ollama
llm = Ollama(model="llama2")

llm.invoke("What is the meaning of life?")