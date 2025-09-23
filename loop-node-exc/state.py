from typing import TypedDict,List

class AgentState(TypedDict):
    number: int
    guess: List[int]
    counter: int
    lower: int
    upper: int
    message: str
