from .state import AgentState
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain_core.messages import SystemMessage

load_dotenv()


@tool
def add(a:int,b:int)-> str:
    """This Tool will add 2 numbers, use this tool for performing the additions.

    Args:
        a (int): first number
        b (int): second number

    Returns:
        str: it will returns a sum of both in this format, i.e. - 22 + 22 = 44
    """

    return f"{a} + {b} = {a+b}"
    

tools = [add]

llm  = ChatGoogleGenerativeAI(model="gemini-2.5-flash").bind_tools(tools)

def llm_node(state:AgentState):
    """this node function can use tools as well as can solve the other user requets."""
    system_prompt = SystemMessage(content=""""You are a helpful assistant. 
    IMPORTANT: When users ask you to perform mathematical operations like addition, 
    you MUST use the available tools. Do NOT calculate manually. 
    Always use the 'add' tool for addition operations.""")
    response = llm.invoke([system_prompt] + state["messages"])
    return {"messages": [response]}
 