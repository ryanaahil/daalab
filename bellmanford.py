def printArr(graph, V, dist):
    print("Vertex Distance from Source")
    for i in range(V):
        print("{0}\t\t{1}".format(i, dist[i]))

def BellmanFord(graph, V, src):
    dist = [float("Inf")] * V
    dist[src] = 0

    for _ in range(V - 1):
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return
    printArr(graph, V, dist)


num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))
graph = []
V = num_vertices

print("Enter edges as 'u v w', where u = source, v = destination, w = weight:")
for _ in range(num_edges):
    u, v, w = map(int, input().split())
    graph.append([u, v, w])
source_vertex = int(input("Enter the source vertex: "))

BellmanFord(graph, V, source_vertex)
