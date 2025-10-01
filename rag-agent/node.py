from .state import RagState
from .tools import tools
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import ToolNode

load_dotenv()

llm  = ChatGoogleGenerativeAI(model="gemini-2.5-flash").bind_tools(tools)
tools_node = ToolNode(tools)

def llm_node(state:RagState):
    """you are helpful assistant and will help user with every task, for docker related task use the tool."""

    response = llm.invoke(state["messages"])
    return {"messages":[response]}


