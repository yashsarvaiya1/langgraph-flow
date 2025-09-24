from .state import AgentState
# from .tools import tools
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


def llm_node(state: AgentState):
    """LLM processes messages and decides on tool usage 
    also update the state - extracting value from the request if you find the same field
    also add the greeting message in this format - hello {name}, welcome. you are {age} years old.
    """ 
    response = llm.invoke(state["messages"])
    print(state)
    return {"messages": [response]}
