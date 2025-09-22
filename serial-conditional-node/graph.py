from .state import AgentState
from .node import *
from langgraph.graph import StateGraph,START,END

gb = StateGraph(AgentState)
gb.add_node("greeting",greeting_node)
gb.add_node("happy",happy_node)
gb.add_node("sad",sad_node)
gb.add_node("service",service_node)
gb.add_node("better",better_node)
gb.add_node("worst",worst_node)
gb.add_node("leave",leave_node)

gb.add_edge(START,"greeting")
gb.add_conditional_edges("greeting",check_mood,{"happy":"happy","sad":"sad"})
gb.add_edge("happy","service")
gb.add_edge("sad","service")
gb.add_conditional_edges("service",check_rating,{"good":"better","bad":"worst"})
gb.add_edge("better","leave")
gb.add_edge("worst","leave")
gb.add_edge("leave",END)

graph = gb.compile()
