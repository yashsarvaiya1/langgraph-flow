from typing import TypedDict,Sequence,Annotated,Optional
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage],add_messages]
    name: Optional[str]
    age: Optional[int]
    greeting:str
