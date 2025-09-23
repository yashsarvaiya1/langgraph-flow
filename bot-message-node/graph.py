from .state import AgentState
from .node import bot
from langgraph.graph import StateGraph,START,END

gb = StateGraph(AgentState)
gb.add_node("bot",bot)

gb.add_edge(START,"bot")
gb.add_edge("bot",END)

graph = gb.compile()
