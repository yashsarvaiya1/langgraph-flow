from .graph import graph
from langgraph.types import Command
from langchain_core.messages import HumanMessage

config = {"configurable": {"thread_id":"unique"}}

while True:
    user_input = input("\nYou: ")
    if user_input == "exit":
        break

    result = graph.invoke({"messages": HumanMessage(content=user_input)}, config)

    while "__interrupt__" in result:
        interrupt_data = result["__interrupt__"][0].value
        user_response = input(interrupt_data["question"])
        result = graph.invoke(Command(resume=user_response), config)
    
    if "messages" in result:
        for message in result["messages"]:
            message.pretty_print()
    
