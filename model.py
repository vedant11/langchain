from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
# take environment variables from .env.
load_dotenv()

llm = ChatOpenAI()
