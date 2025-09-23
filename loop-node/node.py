from .state import State

def greeting_node(state:State):
    """this node will initialize the greeting state"""
    state["greeting"] = "Hello User, Warm Greeting."
    state["message"] = []
    state["counter"] = 0 #for manual runtime initializaion comment this line
    return state

def loop_node(state:State):
    """this loop node will append the greetings to the message state"""
    state["message"].append(state["greeting"])
    state["counter"] += 1
    return state

def should_continue(state:State):
    """this will check wheter to loop back or end"""
    if state["counter"] < 5:
        return "loop"
    else: 
        return "exit"

    
