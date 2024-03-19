from langchain_core.prompts import ChatPromptTemplate
from model import llm

# hardcode the prompt
print(llm.invoke("how can langsmith help with testing?"),
      file=open("output.txt", "a"))

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

chain = prompt | llm

print(chain.invoke({"input": "how can langsmith help with testing?"}), file=open(
    "output.txt", "a"))
