from langchain_core.tools import tool
from .draft_agent.agent import run_agent



@tool
def drafting_tool(draft_query:str):
    """this sub-agent is specialize in drafting any type of document or mail or anything."""

    document_respone = run_agent(query=draft_query)
    return document_respone
        
tools = [drafting_tool]
