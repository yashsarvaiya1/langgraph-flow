from typing import TypedDict,List

class AgentState(TypedDict):
    name: str
    greeting: str
    message: List[str]
    counter: int

