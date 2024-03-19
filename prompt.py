from langchain_core.prompts import ChatPromptTemplate
from model import llm


class Prompt:
    def __init__(self):
        self.prompt = llm

    def invoke(self, input: str):
        return print(self.prompt.invoke(input), file=open("output.txt", "a"))


class PromptWithTemplate:
    def __init__(self, prompt=""):
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", prompt),
            ("user", "{input}")
        ])

    def invoke(self, input: str):
        return print(self.prompt.invoke({"input": input}), file=open("output.txt", "a"))
