from .graph import graph
from IPython.display import Image,display

display(Image(graph.get_graph().draw_mermaid_png()))

result = graph.invoke({'values':[1,2,3,4,5], 'name':"YASH", "result": "Just Normal Value"})

print(result)
print(result["values"])
print(result["result"])
