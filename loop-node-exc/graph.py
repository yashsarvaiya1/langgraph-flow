from .state import AgentState
from .node import *
from langgraph.graph import StateGraph,START,END

gb = StateGraph(AgentState)
gb.add_node("init",init_node)
gb.add_node("guess",generate_guess_node)
gb.add_node("correct", correct_node)
gb.add_node("wrong",wrong_node)
gb.add_node("upper",update_upper_node)
gb.add_node("lower",update_lower_node)
gb.add_node("loop",loop_node)

gb.add_edge(START,"init")
gb.add_edge("init","guess")
gb.add_conditional_edges("guess",check_guess,{"correct":"correct","wrong":"wrong","loop":"loop"})
gb.add_edge("correct",END)
gb.add_edge("wrong",END)

gb.add_conditional_edges("loop",check_update_bound,{"upper":"upper","lower":"lower"})
gb.add_edge("upper","guess")
gb.add_edge("lower","guess")

graph = gb.compile()

