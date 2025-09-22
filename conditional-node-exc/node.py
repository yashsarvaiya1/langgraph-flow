from .state import AgentState

def sum_node(state:AgentState):
    """this will add num1 and num2 of the state"""
    state["result"] = state["num1"] + state["num2"]
    state["message"] = state["result"]
    return state

def sub_node(state:AgentState):
    """this will sub num1 and num2 of the state"""
    state["result"] = state["num1"] - state["num2"]
    state["message"] = state["result"]
    return state

def decide_route(state:AgentState):
    """this will decide to go either addition or substraction"""
    if state["operation"] == "+":
        return "sum"
    else:
        return "sub"

def sum_again_node(state:AgentState):
    """this will add previous result and num3"""
    state["result"] = state["result"] + state["num3"]
    return state

def sub_again_node(state:AgentState):
    """this will minus result and num3"""
    state["result"] = state["result"] + state["num3"]
    return state

def decide_again_route(state:AgentState):
    """this will decide the route for the second operation"""
    if state["operation2"] == "+":
        return "sum"
    else:
        return "sub"

def formatting(state:AgentState):
    """this will generate the final message containing the answer"""
    state["message"] = f"{state["num1"]} {state["operation"]} {state['num2']} = {state["message"]} {state['operation2']} {state['num3']} = {state['result']}."
    return state
