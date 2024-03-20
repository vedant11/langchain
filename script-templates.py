from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI bot. Your name is {name}."),
    ("human", "Hello, how are you doing?"),
    ("ai", "I'm doing well, thanks!"),
    ("human", "{user_input}"),
])

messages = template.format_prompt(
    name="Bob",
    user_input="What is your name?"
)
print(messages)

TEMPLATE = """Give me details about {country}"""

""" ChatPromptTemplate considers message/template as HumanMessage by default
so this is same as 
> template = ChatPromptTemplate.from_messages([("human", TEMPLATE)])
OR
> human_template = HumanMessagePromptTemplate.from_template(TEMPLATE)
> chat_template = ChatPromptTemplate.from_template(human_template)
"""
template = ChatPromptTemplate.from_template(TEMPLATE)
messages = template.format_prompt(country="France")
print(messages)
