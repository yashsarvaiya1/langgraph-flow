from .state import AgentState
from .tools import tools
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash").bind_tools(tools)


def llm_node(state: AgentState):
    response = llm.invoke(state["messages"])
    print(state.get("name", "No name provided"))
    print(state.get("age", "Not Provided"))
    print(state.get("greeting", "No Greeting"))
    return {"messages": [response]}
