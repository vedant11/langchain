from prompt import PromptWithRetrievedContext

# seting basic retrieval chain and invoking it
retrieval_prompt = PromptWithRetrievedContext(
    context="langsmith can let you visualize test results")
retrieval_prompt.invoke("how can langsmith help with testing?")
