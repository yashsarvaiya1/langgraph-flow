# LangGraph Flow Examples

This repository contains various examples and implementations of LangGraph-based applications, demonstrating different patterns and use cases for building AI agent workflows.

## Project Structure

The project is organized into several modules, each demonstrating different patterns:

### Basic Patterns
- `simple-node/`: Basic example of a single node graph
- `serial-node/`: Demonstrates sequential node execution
- `conditional-node/`: Shows conditional branching in graph execution
- `multiple-input-node/`: Handles multiple inputs in nodes
- `loop-node/`: Demonstrates loop patterns in graph execution

### Advanced Patterns
- `bot-message-node/`: Chatbot implementation with message handling
- `human-loop-llm/`: Human-in-the-loop pattern with LLM integration
- `draft-sub-agent/`: Sub-agent pattern for document drafting
- `react-agent-base/`: ReAct pattern implementation for agents
- `rag-agent/`: Retrieval-Augmented Generation (RAG) implementation with vector store

## Prerequisites

- Python 3.8+
- Virtual environment (recommended)

## Dependencies

```bash
pip install -r requirements.txt
```

Main dependencies:
- langgraph: Core framework for building agent workflows
- langchain[google-genai]: LangChain with Google Generative AI integration
- python-dotenv: For environment variable management
- pydantic: For data validation
- grandalf: For graph visualization
- langchain-text-splitters: For document chunking
- langchain-community: For document loading
- Google Generative AI: For embeddings and LLM

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yashsarvaiya1/langgraph-flow.git
cd langgraph-flow
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```env
GOOGLE_API_KEY=your_api_key_here
```

## Running the Examples

Each module can be run independently. Here are some examples:

### Simple Node
```bash
python -m simple-node.agent
```

### Conditional Node
```bash
python -m conditional-node.agent
```

### Human Loop LLM
```bash
python -m human-loop-llm.agent
```

### Draft Sub-Agent
```bash
python -m draft-sub-agent.agent
```

## Module Descriptions

### Simple Node
Basic example showing how to create a single-node graph. Demonstrates the fundamental concepts of LangGraph.

### Serial Node
Shows how to chain multiple nodes together in a sequence, with each node processing the output of the previous node.

### Conditional Node
Demonstrates how to implement decision-making in your graph, where the flow can take different paths based on conditions.

### Multiple Input Node
Shows how to handle multiple inputs in a single node, useful for aggregating or processing multiple data sources.

### Loop Node
Demonstrates how to implement iteration patterns in your graph, useful for repetitive tasks or continuous processing.

### Bot Message Node
Implementation of a chatbot that can handle message-based interactions, showing how to manage conversation state.

### Human Loop LLM
Shows how to integrate human interaction into your LLM-based workflows, useful for supervised or semi-supervised applications.

### Draft Sub-Agent
Demonstrates the sub-agent pattern, where a specialized agent is used for specific tasks (in this case, document drafting).

### RAG Agent
Implements Retrieval-Augmented Generation (RAG) pattern using vector store for document storage and retrieval. Features include:
- PDF document loading and chunking
- Vector embeddings using Google's text-embedding-004 model
- In-memory vector store for similarity search
- Smart retrieval tool for context-aware responses

To use the RAG agent:
1. Place your PDF documents in the `rag-agent/documents` folder
2. Run the agent:
```bash
python -m rag-agent.agent
```
The agent will process the documents and respond to queries using relevant document context.

### React Agent Base
Implementation of the ReAct (Reasoning and Acting) pattern, showing how to build more sophisticated agents that can reason about their actions.

## Best Practices

1. Always use virtual environments
2. Keep API keys in .env file
3. Use proper error handling in nodes
4. Implement proper logging for debugging
5. Test graph execution with different inputs

## Troubleshooting

- If you get import errors, make sure you're running from the correct directory
- For visualization errors, ensure you have graphviz installed
- For API errors, check your API key in the .env file

## Contributing

Feel free to contribute by:
1. Forking the repository
2. Creating a feature branch
3. Committing your changes
4. Opening a pull request

## License

This project is open source and available under the MIT License.
