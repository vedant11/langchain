from langchain_core.prompts import ChatPromptTemplate
from model import llm
from typing import Any


class Prompt:
    chain: Any = None

    def __init__(self):
        self.chain = llm

    def invoke(self, input: str):
        return print(self.chain.invoke(input), file=open("output.txt", "a"))


class PromptWithTemplate:
    chain: Any = None

    def __init__(self, prompt=""):
        self.chain = ChatPromptTemplate.from_messages([
            ("system", prompt),
            ("user", "{input}")
        ]) | llm

    def invoke(self, input: str):
        return print(self.chain.invoke({"input": input}), file=open("output.txt", "a"))
