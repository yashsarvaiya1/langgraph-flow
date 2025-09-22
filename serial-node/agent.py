from .graph import graph
from .state import AgentState

# has to pass the {} else gives error for required argument. even though we are setting up every state field
result = graph.invoke({})

print(result)
