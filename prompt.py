from typing import Any

from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from model import llm
from data_index import vector


class Prompt:
    chain: Any = None

    def __init__(self):
        self.chain = llm

    def invoke(self, input: str):
        return print("-----\n", self.chain.invoke(input), file=open("output.txt", "a"))


class PromptWithTemplate:
    chain: Any = None

    def __init__(self, prompt=""):
        self.chain = ChatPromptTemplate.from_messages([
            ("system", prompt),
            ("user", "{input}")
        ]) | llm

    def invoke(self, input: str):
        return print("-----\n", self.chain.invoke({"input": input}), file=open("output.txt", "a"))


class PromptWithRetrievedContext:
    chain: Any = None

    def __init__(self, context=""):
        context_template = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:    

<context>
{context}
</context>

Question: {input}""")
        document_chain = create_stuff_documents_chain(llm, context_template)

        # bring documents from the retriever to the prompt class
        retriever = vector.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        self.chain = retrieval_chain

    def invoke(self, prompt: str):
        return print("-----\n", self.chain.invoke({"input": prompt})["answer"], file=open("output.txt", "a"))
