from langgraph.graph import StateGraph,START,END
from .state import NodeState
from .node import greeting_node

graph = StateGraph(NodeState)
graph.add_node("greeter", greeting_node)

graph.add_edge(START,"greeter")
graph.add_edge("greeter",END)

app = graph.compile()


