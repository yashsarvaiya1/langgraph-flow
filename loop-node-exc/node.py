from .state import AgentState
import random

def init_node(state:AgentState):
    """this will generate the new random number and initialize the guess list and upper and lower bound"""
    state["counter"] = 0
    state["number"] = random.randint(1,20)
    state["guess"] = []
    state["lower"] = 1
    state["upper"] = 20
    return state

def generate_guess_node(state:AgentState):
    """this will generate the guess and append to list"""
    state["guess"].append(random.randint(state["lower"],state["upper"]))
    state["counter"] += 1
    print(state)
    return state

def check_guess(state:AgentState):
    if state["number"] == state["guess"][-1]:
        return "correct"
    elif state["counter"] < 7:
        return "loop"
    else:
        return "wrong"

def correct_node(state:AgentState):
    """this will congratulate the user for guessing the correct number"""
    state["message"] = f"Great you guessed the number {state['number']} in {len(state['guess'])} tries."
    return state
def wrong_node(state:AgentState):
    """this will print the bad message"""
    state["message"] = f"you are out of your guess tries, please try again."
    return state
def loop_node(state:AgentState):
    """this is rest node for the after condition"""
    return state

def check_update_bound(state:AgentState):
    """this will check the wheter to update the lower bound or upper bound"""
    if state["number"] < state["guess"][-1]:
        return "upper"
    else:
        return "lower"

def update_lower_node(state:AgentState):
    """this will update the lower bound"""
    state["lower"] = state["guess"][-1]
    return state

def update_upper_node(state:AgentState):
    """this will update upper bound"""
    state["upper"] = state["guess"][-1]
    return state

