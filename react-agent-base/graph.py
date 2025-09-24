from .state import AgentState
from .node import tools,llm_node
from langgraph.graph import StateGraph,START,END
from langgraph.prebuilt import ToolNode,tools_condition

gb = StateGraph(AgentState)

tool_node = ToolNode(tools)
gb.add_node("tools",tool_node)
gb.add_node("llm",llm_node)

gb.add_edge(START,"llm")
gb.add_conditional_edges("llm",tools_condition,{"tools":"tools","__end__":END})
gb.add_edge("tools","llm")

graph = gb.compile()
