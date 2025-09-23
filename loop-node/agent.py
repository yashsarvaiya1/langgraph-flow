from .graph import graph

# to check out the graph https://mermaid.live/ open this andd paste the text in the cmd.
print(graph.get_graph().draw_mermaid())

result = graph.invoke({})

print(result)
