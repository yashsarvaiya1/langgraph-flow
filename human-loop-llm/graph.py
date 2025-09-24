from .state import AgentState
# from .tools import tools
from .node import llm_node
from langgraph.graph import StateGraph,START,END
from langgraph.prebuilt import ToolNode,tools_condition
from langgraph.checkpoint.memory import InMemorySaver

gb = StateGraph(AgentState)
gb.add_node("llm",llm_node)

# tools_node = ToolNode(tools)
# gb.add_node("tools",tools_node)

gb.add_edge(START,"llm")
# gb.add_conditional_edges("llm",tools_condition,{"tools":"tools",END:END})
gb.add_edge("llm",END)

memory = InMemorySaver()
graph = gb.compile(checkpointer=memory)

