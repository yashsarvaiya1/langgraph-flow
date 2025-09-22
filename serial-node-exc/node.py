from .state import AgentState

def name_node(state:AgentState):
    """this nodes adds a peronalized greeting message"""
    state["message"] = f"Long Time No see {state["name"]}, "
    return state

def age_node(state:AgentState):
    """this nodes adds a mesage regarding the age"""
    state["message"] = state["message"] + f"Your Age is {state["age"]}. "
    return state

def skills_node(state:AgentState):
    """this shows the skills of the user"""
    state["message"] = state["message"] + f"Your skills are {state['skills']}."
    return state
