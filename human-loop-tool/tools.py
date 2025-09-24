from langchain.tools import tool
from langgraph.types import interrupt, Command
from langchain_core.messages import ToolMessage
from langchain_core.tools import InjectedToolCallId
from typing import Annotated

@tool
def greeting_tool(name: str = None, age: int = None, tool_call_id: Annotated[str, InjectedToolCallId] = None):
    """ONLY call this tool when user specifically asks for a personalized greeting or introduction.
    Do NOT use for general conversation, jokes, questions, or other topics."""
    
    if not name:
        name = interrupt({"question": "Please share your name: "})
    
    if not age:
        age = int(interrupt({"question": "Please share you age: "}))
    
    greeting_msg = f"Hello, {name}. you are {age} years old."
    
    # REQUIRED: Must include ToolMessage in the update
    state_update = {
        "name": name,
        "age": age,
        "greeting": greeting_msg,
        "messages": [ToolMessage(greeting_msg, tool_call_id=tool_call_id)]  # ← This is required!
    }
    
    return Command(update=state_update)

tools = [greeting_tool]
