from .graph import graph

graph.get_graph().print_ascii()

result = graph.invoke({'values':[1,2,3,4,5], 'name':"YASH", "result": "Just Normal Value"})

print(result)
print(result["values"])
print(result["result"])
