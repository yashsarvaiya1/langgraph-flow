from .state import AgentState
from .node import process_values
from  langgraph.graph import StateGraph,START,END

gb = StateGraph(AgentState)
gb.add_node("sum",process_values)
gb.add_edge(START,"sum")
gb.add_edge("sum",END)

graph = gb.compile()
