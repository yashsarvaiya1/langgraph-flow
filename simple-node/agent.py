from .graph import app


result  = app.invoke({"node_message": "Yash"})

print(result["node_message"])
