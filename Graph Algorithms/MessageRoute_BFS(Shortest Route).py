# Message Route

from collections import deque

def shortest_path(N, M, edges):
    G = [[] for _ in range(N + 1)]
    vis = [False] * (N + 1)
    p = [0] * (N + 1)
    dist = [0] * (N + 1)

    # Constructing the graph
    for a, b in edges:
        G[a].append(b)
        G[b].append(a)

    # BFS to find the shortest path from node 1 to N
    q = deque([1])
    vis[1] = True
    while q:
        u = q.popleft()
        for v in G[u]:
            if not vis[v]:
                dist[v] = dist[u] + 1
                vis[v] = True
                p[v] = u
                q.append(v)

    if not vis[N]:
        return "IMPOSSIBLE"

    # Reconstruct the path from N to 1
    u = N
    path = []
    while u != 0:
        path.append(u)
        u = p[u]

    return len(path), path[::-1]

# Test the function with the provided test case
N = 5
M = 5
edges = [(1, 2), (1, 3), (1, 4), (2, 3), (5, 4)]

path_length, path = shortest_path(N, M, edges)
print(path_length)
print(' '.join(map(str, path)))
