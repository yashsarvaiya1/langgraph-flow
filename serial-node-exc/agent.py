from .graph import graph

result = graph.invoke({"name":"YASH","age":23,"skills":["python","agents","devops"]})

print(result["message"])
