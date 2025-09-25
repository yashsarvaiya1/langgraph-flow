from .graph import graph
from langchain_core.messages import HumanMessage
from langgraph.types import Command


graph.get_graph().print_ascii()

config = {"configurable":{"thread_id":"unique"}}

while True:
    user_input = input("\nYou: ")
    if user_input == "exit":
        break

    result = graph.invoke({"messages": [HumanMessage(content=user_input)]},config)

    while "__interrupt__" in result:
        interrupt_data = result["__interrupt__"][0].value

        print(interrupt_data["draft"])
        user_respone = input(interrupt_data["message"])

        result = graph.invoke(Command(resume=user_respone),config)

    result["messages"][-1].pretty_print()
