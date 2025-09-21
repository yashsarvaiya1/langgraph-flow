from .state import ComplimentState

def compliment_node(state: ComplimentState):
    """simple node that will compliment the user with state"""
    state["name"] = state["name"] + " you are the best at Tech!"
    return state

