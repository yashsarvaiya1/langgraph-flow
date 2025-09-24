from .state import AgentState
from langgraph.types import interrupt

def greeting_node(state:AgentState):
    """this node will check name and initializing greeting"""
    if not state.get("name"):
        user_input = interrupt("Please enter your name: ")
        state["name"] = user_input

    state["greeting"] = f"Hello, {state["name"]}. Warm Greeting"
    state["message"] = []
    print(state)
    return state

def loop_node(state:AgentState):
    """this loop node will append the greetings to the message state"""
    state["counter"] += 1
    state["message"].append(state["greeting"])
    print(state)
    return state

def should_continue(state:AgentState):
    """This will check wheter to stop or loop"""
    if state["counter"] < 5:
        return "loop"
    else:
        return "exit"
