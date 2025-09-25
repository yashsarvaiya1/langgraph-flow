from .state import AgentState
from .tools import tools
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import ToolNode

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash").bind_tools(tools)

def agent_node(state:AgentState):
    """you are helpful assistant, and have access of tools, use them if required"""
    respone = llm.invoke(state["messages"])
    return {"messages":[respone]}

tools_node = ToolNode(tools)
