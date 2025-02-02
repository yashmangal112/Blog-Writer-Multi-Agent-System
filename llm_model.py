from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
# os.environ["GROQ_API_KEY"] = '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'

LLM_MODEL = ChatGroq(
    model="groq/llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=1024,
    timeout=30,
    max_retries=2,
)