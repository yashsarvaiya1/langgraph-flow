from langchain_core.tools import tool
from .state import AgentState
from langgraph.types import interrupt

# @tool
# def greeting_tool(state:AgentState):
#     """Call this tool when user asks for greeting or introduction message. 
#     This will greet the user with their name and age."""

#     if not state.get("name"):
#         state["name"] = interrupt({"question": "What's your name?", "type": "name_request"})
#     if not state.get("age"):
#         state["age"] = int(interrupt({"question": "What's your age?", "type": "age_request"}))

#     state["greeting"] = f"Hello {state['name']}! Nice to meet you. At {state['age']} years old, you're in a great phase of life!" 

# @tool 
# def extract_info(name:str = None,age:str = None,state:AgentState = None):
#     """Call this tool when user mentions their name or age in conversation.
#     This will store the name and age information."""

#     if name:
#         state["name"] = name
#     if age:  
#         state["age"] = age
    
#     return f"Got it! Stored your information."

# tools = [greeting_tool]
