from algorithm import BellmanFord
from graph import Graph
from edge import Edge

graph = Graph(6)

graph.addEdge(0, 1, 0)
graph.addEdge(0, 2, 0)
graph.addEdge(0, 3, 0)
graph.addEdge(0, 4, 0)
graph.addEdge(0, 5, 0)

graph.addEdge(1, 3, 3)
graph.addEdge(1, 4, 1)
graph.addEdge(2, 1, 2)
graph.addEdge(2, 3, 2)
graph.addEdge(3, 4, 0)
graph.addEdge(3, 5, 6)
graph.addEdge(4, 5, 1)
graph.addEdge(5, 2, -2)

graph.addEdge(4, 1, -1)
graph.addEdge(3, 2, -2)
graph.addEdge(4, 3, 0)
graph.addEdge(2, 5, 2)

bellmanFord = BellmanFord()
d = bellmanFord.calculateShortestPath(graph, 0)

for i in range(graph.V):
    print("The cost to get from node % d to % d is: % 5.2f" % (0, i, d[i]))
