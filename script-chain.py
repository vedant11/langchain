from prompt import Prompt, PromptWithTemplate
from langchain_core.output_parsers import StrOutputParser

hardcoded_prompt = Prompt()
flexible_prompt = PromptWithTemplate(
    "You are world class technical documentation writer.")

# add output parsers
hardcoded_prompt.chain = hardcoded_prompt.chain | StrOutputParser()
flexible_prompt.chain = flexible_prompt.chain | StrOutputParser()

# invoking the prompts
hardcoded_prompt.invoke("how can langsmith help with testing?")
flexible_prompt.invoke("how can langsmith help with testing?")
