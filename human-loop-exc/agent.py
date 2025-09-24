from .graph import graph
from langgraph.types import Command

config = {"configurable": {"thread_id":"unique"}}

# for checking the diffrent outcome
result = graph.invoke({},config) # 2 interruptions
# result = graph.invoke({"name":"yash"},config) # 1 interruptions
# result = graph.invoke({"name":"yash","age":23},config) # 0 interruptions

while "__interrupt__" in result:
    print("Interruption:")
    interrrupt_data = result["__interrupt__"][0].value
    print(interrrupt_data["test"])
    user_input = input(interrrupt_data["question"])
    result = graph.invoke(Command(resume=user_input),config)

print(result)
    
