from .graph import graph

graph.get_graph().print_ascii()

# has to pass the {} else gives error for required argument. even though we are setting up every state field
result = graph.invoke({})

print(result)
