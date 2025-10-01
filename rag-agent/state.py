from typing import Annotated,Sequence,Optional,TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class RagState(TypedDict):
    messages: Annotated[Sequence[BaseMessage],add_messages]
    context: Optional[str]
