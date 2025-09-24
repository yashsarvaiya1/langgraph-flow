from .state import AgentState
from .node import should_continue,loop_node,greeting_node
from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import InMemorySaver

gb = StateGraph(AgentState)
gb.add_node("greeting",greeting_node)
gb.add_node("loop",loop_node)

gb.add_edge(START,"greeting")
gb.add_conditional_edges("greeting",should_continue,{"loop":"loop","exit":END})
gb.add_edge("loop","greeting")

memory = InMemorySaver()
graph = gb.compile(checkpointer=memory)
