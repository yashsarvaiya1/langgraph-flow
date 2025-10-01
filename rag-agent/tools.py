from langchain_core.tools import tool, InjectedToolCallId
from langchain_core.messages import ToolMessage
from typing import Annotated
from langgraph.types import Command
from .embedding import create_embeddings

vector_store = create_embeddings()


@tool
def smart_retrieve(query: str, tool_call_id: Annotated[str, InjectedToolCallId]):
    """If user asks anything related to the Docker use this tool for returning the information"""

    docs = vector_store.similarity_search(query, k=4)

    if not docs:
        return Command(
            update={
                "context": "No data found",
                "messages": [ToolMessage("No data Found", tool_call_id=tool_call_id)],
            }
        )

    context_text = "Retrieved Documents:\n\n"
    for i, doc in enumerate(docs, 1):
        context_text += f"Document {i}: \n{doc.page_content}\n\n"

    return Command(
        update={
            "context": context_text,
            "messages": [ToolMessage(context_text, tool_call_id=tool_call_id)],
        }
    )

tools = [smart_retrieve]
