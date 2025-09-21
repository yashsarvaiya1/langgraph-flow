from langgraph.graph import StateGraph,START,END
from .state import ComplimentState
from .node import compliment_node

graph_builder = StateGraph(ComplimentState)
graph_builder.add_node("complimentor",compliment_node)
graph_builder.add_edge(START,"complimentor")
graph_builder.add_edge("complimentor",END)

graph = graph_builder.compile()
