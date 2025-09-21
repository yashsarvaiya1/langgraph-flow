from .state import NodeState

def greeting_node(state:NodeState):
    """simple node that adds the greeting mesage with state"""
    state["node_message"] = state["node_message"] + "hello, there i hope you are fine!"
    return state


