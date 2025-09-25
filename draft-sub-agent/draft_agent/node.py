from .state import DraftState
from langgraph.types import interrupt
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def llm_node(state:DraftState):
    """You are special draft assistant. you will help user to draft anything - mail, letter, presentation, research paper."""
    if state.get("satisfied", True) == True:
        response = llm.invoke(state["messages"])
        draft_content = response.content
    else:
        response = llm.invoke([state["draft"] + f"update this as follow: " + state["feedback"]])
        draft_content = response.content
    return {"messages":[response],"draft":draft_content}

def feedback_node(state:DraftState):
    """you will ask for a feedback about drafted document"""

    state["feedback"] = interrupt({
            "question":"Are you happy with your Draft?? else provide feedback",
            "draft": state["draft"]
        })

    state["satisfied"] = state["feedback"].lower() == "yes"
    return state

def should_continue(state:DraftState):
    """this will decide to rather end or continue drafting"""
    if state.get("satisfied") == False:
        return "draft"
    else:
        return "exit"
