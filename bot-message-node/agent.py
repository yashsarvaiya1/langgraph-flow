from .graph import graph
from langchain_core.messages import HumanMessage

graph.get_graph().print_ascii()

state = {"messages": []}
user_input = ""
while user_input != "exit":
    user_input = input("\n\nYou: ")
    state["messages"].append(HumanMessage(content=user_input))
    result = graph.invoke(state)
    print(result)
    