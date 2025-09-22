from .graph import graph


graph.get_graph().print_ascii()

result = graph.invoke({"name":"YASH","age":23,"skills":["python","agents","devops"]})

print(result["message"])
