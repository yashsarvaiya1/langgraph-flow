from .state import AgentState

def decide(state:AgentState):
    if state["operation"] == "+":
        return "SUM"
    else:
        return "SUB"

def sum_node(state:AgentState):
    """this will handdle the summation of numbers"""
    state["result"] = state["num1"] + state["num2"]
    state["result"] = f"the result is {state["result"]}"
    return state

def sub_node(state:AgentState):
    """this node will handle the substraction of  numbers"""
    state["result"] = state["num1"] - state["num2"]
    state["result"] = f"the result is {state["result"]}"
    return state

def numbers_node(state:AgentState):
    """this will handle the initialization of the numbers"""
    state["num1"] = 10
    state["num2"] = 15
    return state
