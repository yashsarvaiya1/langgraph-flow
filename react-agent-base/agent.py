from .graph import graph
from langchain_core.messages import HumanMessage

graph.get_graph().print_ascii()

user_input = input("Enter your Request: ")
result = graph.invoke({"messages":HumanMessage(content=user_input)})
result["messages"][-1].pretty_print()

user_input = ""
while user_input != "exit":
    user_input = input("Enter your Request: ")
    result = graph.invoke({"messages":HumanMessage(content=user_input)})
    for message in result["messages"]:
        message.pretty_print()
    # for just response use - result["messages"][-1].pretty_print()

