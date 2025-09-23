from .graph import graph
from langchain_core.messages import HumanMessage

user_input = ""
while user_input != "exit":
    user_input = input("You: ")
    message_input = HumanMessage(content=user_input)
    message_input.pretty_print()
    graph.invoke({"messages": [message_input]})
