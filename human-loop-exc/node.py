from .state import AgentState
from langgraph.types import interrupt


# def get_name(state: AgentState):
#     """this will ask user for a name"""
#     state["name"] = interrupt({"question": "What is your name?", "test": "test string"})
#     return state


# def get_age(state: AgentState):
#     """this will ask user for a age"""
#     state["age"] = int(
#         interrupt({"question": "What is your Age?", "test": "test_string"})
#     )
#     return state

def get_name():
    """this will ask user for a name"""
    return interrupt({"question": "What is your name?", "test": "test string"})

def get_age():
    """this will ask user for a age"""
    return int(
        interrupt({"question": "What is your Age?", "test": "test_string"})
    )

def message_node(state: AgentState):
    """initial node for the graph to activate"""
    if not state.get("name"):
        state["name"] = get_name()

    if not state.get("age"):
        state["age"] = get_age()

    # state["message"] = f"{state["name"]} - {state["age"]}."
    # return state
    return {"message": f"{state["name"]} - {state["age"]}."}
