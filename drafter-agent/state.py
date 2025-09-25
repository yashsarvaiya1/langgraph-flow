from typing import TypedDict,Sequence,Annotated,Optional
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage],add_messages]
    document: str
    draft: str
    feedback: str
    satisfied: bool
    counter: int
