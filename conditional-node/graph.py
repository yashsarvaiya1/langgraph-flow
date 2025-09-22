from .state import AgentState
from .node import sub_node,sum_node,numbers_node,decide
from langgraph.graph import StateGraph,START,END

gb = StateGraph(AgentState)
gb.add_node("number",numbers_node)
gb.add_node("sum",sum_node)
gb.add_node("sub",sub_node)

gb.add_edge(START,"number")
gb.add_conditional_edges("number",decide,{"SUM":"sum","SUB":"sub"})
gb.add_edge("sum",END)
gb.add_edge("sub",END)

graph = gb.compile()
