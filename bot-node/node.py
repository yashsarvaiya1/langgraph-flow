from langchain_google_genai import ChatGoogleGenerativeAI
from .state import State
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def process(state:State):
    response= llm.invoke(state["messages"])
    response.pretty_print()

    
