from .graph import draft_graph
from langchain_core.messages import HumanMessage
from langgraph.types import Command

def run_agent(query:str):
    config = {"configurable":{"thread_id":"unique_key"}}
    while True:
        response = draft_graph.invoke({"messages":[HumanMessage(content=query)]},config)
        while "__interrupt__" in response:
            interrupt_data = response["__interrupt__"][0].value
            print(f"\nDraft: {interrupt_data.get('draft', 'No draft available')}")
            user_response = input(f"{interrupt_data['question']}: ")
            response = draft_graph.invoke(Command(resume=user_response),config)
        # return response["messages"][-1].content
        return response["draft"]
