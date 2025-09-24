from .graph import graph
from langgraph.types import Command

graph.get_graph().print_ascii()

config = {"configurable": {"thread_id":"unique"}}

result = graph.invoke({"counter":0},config)
    
while "__interrupt__" in result:
    interrupt_data = result["__interrupt__"][0].value
    print(f"INTERRUPT: {interrupt_data}")
    
    user_input = input("Your response: ")
    result = graph.invoke(Command(resume=user_input), config)

print(result)
