# langchain

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

### Retrieval Augmented Generation

1. Retrieval
2. Prompt
3. Chat Model

### Agents

1. Prompt
2. Model
3. Output Parser
4. Tools

### Storage and Indexing

1. Document Loader
2. Text Splitter
3. Embeddings
4. Vector Store

### Extraction

1. Document Loader
2. Prompt
3. Model
4. Output Parser
