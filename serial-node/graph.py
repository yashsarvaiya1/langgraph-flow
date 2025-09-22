from .state import AgentState
from .node import first_node,second_node
from langgraph.graph import StateGraph,START,END

gb = StateGraph(AgentState)
gb.add_node("name_node", first_node)
gb.add_node("greeter",second_node)

gb.add_edge(START,"name_node")
gb.add_edge("name_node","greeter")
gb.add_edge("greeter",END)

graph = gb.compile()
