from langchain_core.messages import HumanMessage, AIMessage

from prompt import PromptWithRetrievedContextAndHistory

chat_history = [HumanMessage(
    content="Can LangSmith help test my LLM applications?"), AIMessage(content="Yes!")]

conversational_retrieval_chain = PromptWithRetrievedContextAndHistory()
conversational_retrieval_chain.invoke(data={
    "chat_history": chat_history,
    "input": "how can langsmith help with testing?"
})
