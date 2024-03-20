# langchain

LangChain gives you the building blocks to interface with any language model.

## Repo Guide

-   (script-chain.py)
-   (script-retrieval_chain.py)
    -   A retriever can be backed by anything, DB, data store, internet, or a vector store
-   (script-conversational_retrieval_chain.py)
    -   chains above answer only one history-independent question
    -   this can handle follow-up questions as well

## Usages

### LLMs and Prompts

This includes prompt management, prompt optimization, a generic interface for all LLMs, and common utilities for working with LLMs.

### Chains:

Chains go beyond a single LLM call and involve sequences of calls (whether to an LLM or a different utility). LangChain provides a standard interface for chains, lots of integrations with other tools, and end-to-end chains for common applications.

### Data Augmented Generation:

Data Augmented Generation involves specific types of chains that first interact with an external data source to fetch data for use in the generation step. Examples include summarization of long pieces of text and question/answering over specific data sources.

### Agents:

Agents involve an LLM making decisions about which Actions to take, taking that Action, seeing an Observation, and repeating that until done. LangChain provides a standard interface for agents, a selection of agents to choose from, and examples of end-to-end agents.

### Memory:

Memory refers to persisting state between calls of a chain/agent. LangChain provides a standard interface for memory, a collection of memory implementations, and examples of chains/agents that use memory.

### Evaluation:

[BETA] Generative models are notoriously hard to evaluate with traditional metrics. One new way of evaluating them is using language models themselves to do the evaluation. LangChain provides some prompts/chains for assisting in this.

## Abstractions

### Retrieval-Augmented Generation

1. Retrieval: Retriever retrieves the important context only, to be passed to the LLM, which was not included in the training data.
2. Prompt
3. Chat Model

### Agents

1. Prompt: The inputs to language models are often called prompts
    1. Prompts generate structured messages from user input. They are casted into `Messages` for `ChatModels` and `str` for `LanguageModels`. `PromptValue` is the interface-like common class.
    2. User input string to these final structured input to models are handled by `PromptTemplates`.
    3. Types:
        1. `MessagePromptTemplate`: Consists of `role` and `PromptTemplate`. Could be: `HumanMessagePromptTemplate`, `AIMessagePromptTemplate`, or `SystemMessagePromptTemplate`, depending on the `role`.
        2. `ChatPromptTemplate`: Consists of list of PromptTemplates depending on variety of roles. Think of it as giving the history of conversation, i.e. list of messages by AI, User, System, or other roles.
2. Model
    1. Types: LLMs and ChatModels (built upon LLMs and tuned for conversation)
    2. ChatModels take input as a `Message`: attrs: `role` and `content`; different message classes are present in langchain for different roles.
        1. `content` is either a string or list of dictionaries (for multi-modal input). The message can be classified into `HumanMessage` or `AIMessage`
        2. `SystemMessage` tells model how to behave.
        3. `FunctionMessage` represents the output of a function call
        4. `ToolMessage` represents the output of a tool call
3. Output Parser: Formats AIMessage into human-readable strings
4. Tools

### Storage and Indexing

1. Document Loader: WebBaseLoader for internet
2. Text Splitter
3. Embeddings: OpenAIEmbeddings
4. Vector Store: Data is embedded into this store for indexing

### Extraction

1. Document Loader
2. Prompt
3. Model
4. Output Parser
