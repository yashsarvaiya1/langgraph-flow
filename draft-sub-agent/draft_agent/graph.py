from .state import DraftState
from .node import llm_node,feedback_node,should_continue
from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import InMemorySaver

gb = StateGraph(DraftState)
gb.add_node("draft",llm_node)
gb.add_node("feedback",feedback_node)

gb.add_edge(START,"draft")
gb.add_edge("draft","feedback")
gb.add_conditional_edges("feedback",should_continue,{"draft":"draft","exit":END})

memory = InMemorySaver()
draft_graph = gb.compile(checkpointer=memory)

