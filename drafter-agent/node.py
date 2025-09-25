from .state import AgentState
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langgraph.types import interrupt, Command
from langchain_core.tools import tool, InjectedToolCallId
from langgraph.prebuilt import ToolNode, tools_condition
from typing import Annotated
from langchain_core.messages import ToolMessage, SystemMessage, HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


@tool
def extract_satisfaction(
    draft: str, counter: int, tool_call_id: Annotated[str, InjectedToolCallId]
):
    """Get user satisfaction after showing draft"""

    feedback = interrupt(
        {"message": "Are you satisfied with this? (yes/feedback)", "draft": draft}
    )

    satisfied = feedback.lower() == "yes"

    state_update = {
        "draft": draft,
        "feedback": feedback,
        "counter": counter + 1,
        "satisfied": satisfied,
        "messages": [
            ToolMessage(content=f"Feedback: {feedback}", tool_call_id=tool_call_id)
        ],
    }

    return Command(update=state_update)


tools = [extract_satisfaction]
llm_tools = llm.bind_tools(tools)
tools_node = ToolNode(tools)


def drafting_node(state: AgentState):
    print(
        f"[Debug] Satisfied: {state.get('satisfied')}, Counter: {state.get('counter', 0)}"
    )

    # Fix: Reverse the logic
    if state.get("satisfied") == True:
        # User is satisfied - normal conversation mode
        response = llm.invoke(state["messages"])
        return {"messages": [response]}

    else:
        # Drafting mode - need to create or improve draft
        if state.get("counter", 0) == 0:
            # First draft - create new document
            system_prompt = SystemMessage(
                content="""You are a helpful assistant that drafts documents. 
            When user asks for drafting, create the document and then IMMEDIATELY call the extract_satisfaction tool 
            with the draft content to get feedback."""
            )

            response = llm_tools.invoke([system_prompt] + list(state["messages"]))

        else:
            # Improve existing draft based on feedback
            system_prompt = SystemMessage(
                content=f"""Improve this draft based on user feedback:

CURRENT DRAFT:
{state.get('draft', '')}

USER FEEDBACK: 
{state.get('feedback', '')}

Create an improved version and then call extract_satisfaction tool with the new draft."""
            )

            response = llm_tools.invoke([system_prompt] + list(state["messages"]))

        return {"messages": [response]}
