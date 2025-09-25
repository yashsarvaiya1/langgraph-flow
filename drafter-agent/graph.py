from .state import AgentState
from .node import tools_node,drafting_node
from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import tools_condition

gb = StateGraph(AgentState)
gb.add_node("tools",tools_node)
gb.add_node("drafter",drafting_node)

gb.add_edge(START,"drafter")
gb.add_conditional_edges("drafter",tools_condition,{"tools":"tools",END:END})
gb.add_edge("tools","drafter")

memory = InMemorySaver()
graph = gb.compile(checkpointer=memory)
