from .state import State
from .node import *
from langgraph.graph import StateGraph,START,END

gb = StateGraph(State)
gb.add_node("greeting",greeting_node)
gb.add_node("loop",loop_node)

gb.add_edge(START,"greeting")
gb.add_edge("greeting","loop")
gb.add_conditional_edges("loop",should_continue,{"loop":"loop","exit":END})

graph = gb.compile()
