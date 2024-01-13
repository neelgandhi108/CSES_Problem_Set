# Shortest Routes I

import heapq

def dijkstra(N, M, edges):
    G = [[] for _ in range(N + 1)]
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    Q = [(0, 1)]  # Priority queue with (distance, node)

    # Building the graph
    for a, b, c in edges:
        G[a].append((b, c))

    # Dijkstra's algorithm
    while Q:
        d, u = heapq.heappop(Q)
        if d > dist[u]:
            continue
        for v, w in G[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(Q, (dist[v], v))

    return dist[1:]

# Accepting input from the user
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(M)]

# Calculating shortest paths
shortest_paths = dijkstra(N, M, edges)
print(' '.join(map(str, shortest_paths)))
