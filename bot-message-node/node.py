from .state import AgentState
from langchain_core.messages import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm  = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def bot(state:AgentState):
    """this will generate the llm response and appends it to state"""
    response = llm.invoke(state["messages"])
    state["messages"].append(AIMessage(content=response.content))
    return state
    
