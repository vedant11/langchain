from prompt import Prompt, PromptWithTemplate

harcoded_prompt = Prompt()
flexible_prompt = PromptWithTemplate(
    "You are world class technical documentation writer.")

harcoded_prompt.invoke("how can langsmith help with testing?")
flexible_prompt.invoke("how can langsmith help with testing?")
