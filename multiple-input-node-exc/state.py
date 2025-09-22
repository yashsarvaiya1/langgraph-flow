from typing import TypedDict,List

class AgentState(TypedDict):
    name: str
    values: List[int]
    operation: str
    result: str
