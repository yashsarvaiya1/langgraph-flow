from typing import TypedDict

class AgentState(TypedDict):
    name: str
    greeting: str
    mood: str
    rating: int
    message: str
