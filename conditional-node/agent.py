from .graph import graph

graph.get_graph().print_ascii()

result = graph.invoke({'operation':"+"})

print(result)
