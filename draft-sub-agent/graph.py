from .state import AgentState
from .node import tools_node,agent_node
from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import tools_condition

gb = StateGraph(AgentState)
gb.add_node("agent",agent_node)
gb.add_node("tools",tools_node)

gb.add_edge(START,"agent")
gb.add_conditional_edges("agent",tools_condition,{"tools":"tools",END:END})
gb.add_edge("tools","agent")

memory = InMemorySaver()
graph = gb.compile(checkpointer=memory)
