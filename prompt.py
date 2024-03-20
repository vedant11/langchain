from typing import Any

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain, create_history_aware_retriever

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

    def __init__(self, instruction=""):
        self.chain = ChatPromptTemplate.from_messages([
            ("system", instruction),
            ("user", "{input}")
        ]) | llm

    def invoke(self, input: str):
        return print("\n-----\n", self.chain.invoke({"input": input}), file=open("output.txt", "a"))


class PromptWithRetrievedContext:
    chain: Any = None

    def __init__(self):
        # context comes from data_index/vector
        prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:    
        <context>
        {context}
        </context>
        Question: {input}""")
        document_chain = create_stuff_documents_chain(llm, prompt)

        # retriever brings relevant documents from the vector
        retriever = vector.as_retriever()
        # retriever will provide the relevent context(document) to the prompt(document chain)
        # AFTER the 'new-prompt'(retrieval chain) is invoked with a user input
        # note: we could instead pass the context by ourselves as "context": [Document(page_content="langsmith can let you visualize test results")]
        # but we want the retriever/vector to dynamically pass the most relevant documents as per the input
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        self.chain = retrieval_chain

    def invoke(self, input: str):
        return print("\n-----\n", self.chain.invoke({"input": input})["answer"], file=open("output.txt", "a"))


class PromptWithRetrievedContextAndHistory:
    chain: Any = None

    def __init__(self):
        # retriever chain that returns the context documents
        # based on the chat history and prompt to generate the search query to find relevant documents
        prompt = ChatPromptTemplate.from_messages([
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
        ])
        retriever = vector.as_retriever()
        retriever_chain = create_history_aware_retriever(
            llm, retriever, prompt)
        # if we invoke this chain, it will output documents
        # that are relevant to the chat history and input
        # but this is just a part of the chain!

        # retrieval chain that uses history-aware-retriever instead of a retriever
        # context below is passed by the history-aware-retriever
        prompt = ChatPromptTemplate.from_messages([
            ("system",
             "Answer the user's questions based on the below context:\n\n{context}"),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
        ])
        document_chain = create_stuff_documents_chain(llm, prompt)
        retrieval_chain = create_retrieval_chain(
            retriever_chain, document_chain)
        self.chain = retrieval_chain

    def invoke(self, data):
        if not ["chat_history", "input"] == list(data.keys()):
            raise ValueError(
                "The input data should be a dictionary with keys 'chat_history' and 'input'")
        return print("\n-----\n", self.chain.invoke({
            "chat_history": data.get("chat_history"),
            "input": data.get("input")
        })["answer"], file=open("output.txt", "a"))
