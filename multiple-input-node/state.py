from typing import TypedDict , List

class AgentState(TypedDict):
    values: List[int]
    name: str
    result: str
