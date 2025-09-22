from .state import AgentState
from .graph import graph

graph.get_graph().print_ascii()

state = AgentState(num1=10,num2=20,num3=30,operation="+",operation2="+")

result = graph.invoke(state)

print(result)
