from langgraph.graph import StateGraph,START,END
from .state import RagState
from .node import llm_node,tools_node
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import tools_condition


gb = StateGraph(RagState)
gb.add_node("llm",llm_node)
gb.add_node("tools",tools_node)

gb.add_edge(START,"llm")
gb.add_conditional_edges("llm",tools_condition,{"tools":"tools",END:END})
gb.add_edge("tools","llm")

memory = InMemorySaver()
graph = gb.compile(checkpointer=memory)


