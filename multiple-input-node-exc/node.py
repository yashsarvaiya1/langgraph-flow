from .state import AgentState
import math

def exc_node(state:AgentState):
    """handling the values list based on the operation for user"""
    if state["operation"] == "+":
        state["result"] = f"hello, {state['name']}, your sum is {sum(state['values'])}"
    if state["operation"] == "*":
        state["result"] = f"hello, {state['name']}, your multiplication is {math.prod(state['values'])}"

    return state
