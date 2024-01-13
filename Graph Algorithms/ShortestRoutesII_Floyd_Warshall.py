def floyd_warshall(N, M, Q, edges, queries):
    INF = float('inf')
    dist = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

    # Initialize distances with edges
    for a, b, c in edges:
        dist[a][b] = min(dist[a][b], c)
        dist[b][a] = min(dist[b][a], c)

    # Distance to self is zero
    for i in range(1, N + 1):
        dist[i][i] = 0

    # Floyd-Warshall algorithm
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Answer queries
    results = []
    for a, b in queries:
        results.append(-1 if dist[a][b] == INF else dist[a][b])

    return results

# Accepting input from the user
N, M, Q = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(M)]
queries = [tuple(map(int, input().split())) for i in range(Q)]

# Calculating shortest paths for each query
results = floyd_warshall(N, M, Q, edges, queries)
for result in results:
    print(result)
