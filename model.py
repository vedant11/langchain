import os

from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
# take environment variables from .env.
load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")
openai_chat_model = os.environ.get("OPENAI_CHAT_MODEL")

llm = ChatOpenAI(openai_api_key=openai_api_key, model_name=openai_chat_model)
