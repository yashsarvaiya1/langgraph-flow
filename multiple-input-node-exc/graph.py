from .state import AgentState
from .node import exc_node
from langgraph.graph import StateGraph,START,END

gb = StateGraph(AgentState)
gb.add_node("process",exc_node)
gb.add_edge(START,"process")
gb.add_edge("process",END)

graph = gb.compile()
