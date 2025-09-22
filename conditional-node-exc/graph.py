from .state import AgentState
from .node import *
from langgraph.graph import StateGraph,START,END

gb = StateGraph(AgentState)
gb.add_node("sum1",sum_node)
gb.add_node("sub1",sub_node)
gb.add_node("sum2",sum_again_node)
gb.add_node("sub2",sub_again_node)
gb.add_node("formating",formatting)

gb.add_conditional_edges(START,decide_route,{"sum":"sum1","sub":"sub1"})
gb.add_conditional_edges("sum1",decide_again_route,{"sum":"sum2","sub":"sub2"})
gb.add_conditional_edges("sub1",decide_again_route,{"sum":"sum2","sub":"sub2"})
gb.add_edge("sum2","formating")
gb.add_edge("sub2","formating")
gb.add_edge("formating",END)

graph = gb.compile()
