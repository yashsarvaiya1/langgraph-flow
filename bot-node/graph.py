from .state import State
from .node import process
from langgraph.graph import StateGraph,START,END

gb = StateGraph(State)
gb.add_node("process",process)

gb.add_edge(START,"process")
gb.add_edge("process",END)

graph = gb.compile()
