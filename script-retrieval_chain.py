from prompt import PromptWithRetrievedContext

# seting basic retrieval chain and invoking it
# can only answer single questions
retrieval_chain = PromptWithRetrievedContext()
retrieval_chain.invoke("how can langsmith help with testing?")
