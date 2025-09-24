from typing import TypedDict,Sequence,Optional,Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage],add_messages]
    name: Optional[str]
    age: Optional[int]
    greeting: Optional[str]

