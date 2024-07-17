def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, u, v):
    root_x = find(parent, u)
    root_y = find(parent, v)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_y] < rank[root_x]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal_mst(graph):
    mst = []
    parent = []
    rank = []

    edges = sorted(graph['edges'])

    for node in range(graph['vertices']):
        parent.append(node)
        rank.append(0)

    i = 0
    e = 0

    while e < graph['vertices'] - 1:
        weight, u, v = edges[i]
        i += 1

        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            mst.append((u, v, weight))
            e += 1
            union(parent, rank, u, v)

    return mst

vertices = int(input("Enter the number of vertices: "))

graph = {'vertices': vertices, 'edges': []}
e = int(input("Enter the number of edges"))

for _ in range(e):
    edge_input = input("Enter an edge (u v w): ")
    u, v, w = map(int, edge_input.split())
    graph['edges'].append((w, u, v))

mst = kruskal_mst(graph)
print("\nMinimum Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")
