from .state import AgentState
from .node import message_node
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph,START,END

gb = StateGraph(AgentState)
gb.add_node("message",message_node)

gb.add_edge(START,"message")
gb.add_edge("message",END)

memory = InMemorySaver()

graph = gb.compile(checkpointer=memory)
