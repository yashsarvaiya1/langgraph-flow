from .graph import graph
from langchain_core.messages import HumanMessage

graph.get_graph().print_ascii()

config = {"configurable": {"thread_id":"unique"}}

while True:
    user_input = input("\nYou: ")
    if user_input == "exit":
        break

    result = graph.invoke({"messages":[HumanMessage(content=user_input)]},config)

    for message in result["messages"]:
        message.pretty_print()
