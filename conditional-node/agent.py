from .graph import graph
from .state import AgentState

graph.get_graph().print_ascii()

result = graph.invoke({'operation':"+"})
print(result)


state1 = AgentState(num1=20,num2=10,operation="-")
 # i am defining number in the node. so numbers will be overridden.
result = graph.invoke(state1)

print(result)
