from .state import AgentState

def greeting_node(state:AgentState):
    """this will add the greeting message"""
    if state["name"]:
        state["greeting"] = f"Hello {state["name"]}, "
    else: 
        state["greeting"] = "Hello Random!"
    state["message"] = f"{state["greeting"]}\n"
    return state

def happy_node(state:AgentState):
    """this will print a happy message"""
    state["message"] = state["message"] + f"Oh! Happy to see that you are doing great!"
    return state

def sad_node(state:AgentState):
    """this will print a sad message"""
    state["message"] = state["message"] + f"Sorry! to see you in this state."
    return state

def check_mood(state:AgentState):
    if state["mood"] == "happy":
        return "happy"
    else:
        return "sad"

def service_node(state:AgentState):
    """this node indicates the completion of service"""
    state["message"] = state["message"] + f"\n service is completed"
    return state

def better_node(state:AgentState):
    """if the rating is good then this message will be print"""
    state["message"] = state["message"] + f"\n Thanks for your Response, we will try to be more better."
    return state

def worst_node(state:AgentState):
    """if the rating is bad then this message will be print"""
    state["message"] = state["message"] + f"\n Sorry to hear that. We will imporve with your valuable feedback!"
    return state

def check_rating(state:AgentState):
    if state["rating"] > 5:
        return "good"
    else: 
        return "bad"

def leave_node(state:AgentState):
    """this indicates the end of stay"""
    state["message"] = state["message"] + f"\n Thank you for your Visit!"
    return state
