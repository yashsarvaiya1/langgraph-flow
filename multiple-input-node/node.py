from .state import AgentState

def process_values(state:AgentState):
    """this functions handdles multiple values of states"""

    state["result"] = f"Hi There!, {state["name"]}, your sum is {sum(state["values"])}"
    return state 
