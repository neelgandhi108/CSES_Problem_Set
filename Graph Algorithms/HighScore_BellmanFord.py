# High Score  - Bellman Ford

def shortest_path_with_negative_weights(N, M, edges):
    INF = float('inf')
    dp = [INF] * (N + 1)
    dp[1] = 0

    G = [[] for _ in range(N + 1)]
    GR = [[] for _ in range(N + 1)]
    for edge in edges:
        a, b, c = edge
        G[a].append(b)
        GR[b].append(a)

    def dfs(u, visited, graph):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v, visited, graph)

    vis = [False] * (N + 1)
    visR = [False] * (N + 1)
    dfs(1, vis, G)
    dfs(N, visR, GR)

    improvement = True
    for iter in range(N):
        if not improvement:
            break
        improvement = False
        for a, b, c in edges:
            w = -c
            if dp[b] > dp[a] + w:
                dp[b] = dp[a] + w
                improvement = True
                if iter == N - 1 and vis[b] and visR[b]:
                    return -1

    return -dp[N]

# Accepting input from the user
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(M)]

# Calculating shortest path with possibility of negative weights
result = shortest_path_with_negative_weights(N, M, edges)
print(result)



