from .state import AgentState
from .graph import graph

graph.get_graph().print_ascii()

state1 = AgentState(name="Yash",mood="happy",rating=9)
state2 = AgentState(name="SMIT",mood="sad",rating=4)

print(graph.invoke(state1))
print(graph.invoke(state2))
