from .graph import app

app.get_graph().print_ascii()

result  = app.invoke({"node_message": "Yash"})

print(result["node_message"])
