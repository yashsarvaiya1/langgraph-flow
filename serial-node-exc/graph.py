from .state import AgentState
from .node import name_node,age_node,skills_node
from langgraph.graph import StateGraph,START,END

gb = StateGraph(AgentState)
gb.add_node("name",name_node)
gb.add_node("age",age_node)
gb.add_node("skill",skills_node)

gb.add_edge(START,"name")
gb.add_edge("name","age")
gb.add_edge("age","skill")
gb.add_edge("skill",END)

graph = gb.compile()
