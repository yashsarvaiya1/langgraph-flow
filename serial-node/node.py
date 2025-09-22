from .state import AgentState

def first_node(state:AgentState):
    """this node will set the name"""
    state["name"] = "YASH"
    return state

def second_node(state:AgentState):
    """this will add a perssonalized greeting message"""
    state["greeting"] = f"Hello, {state["name"]}. Good Morning."
    return state
