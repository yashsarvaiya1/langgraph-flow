from typing import TypedDict,Sequence,Optional,Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class DraftState(TypedDict):
    messages: Annotated[Sequence[BaseMessage],add_messages]
    draft: str
    feedback: str
    satisfied: bool
    counter: int
