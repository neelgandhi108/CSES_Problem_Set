# Building Teams

def bipartite_teams(N, M, edges):
    G = [[] for _ in range(N + 1)]
    vis = [False] * (N + 1)
    team = [False] * (N + 1)
    possible = True

    # Constructing the graph
    for a, b in edges:
        G[a].append(b)
        G[b].append(a)

    def dfs(u, p=0):
        nonlocal possible
        for v in G[u]:
            if v != p:
                if not vis[v]:
                    team[v] = not team[u]
                    vis[v] = True
                    dfs(v, u)
                elif team[v] == team[u]:
                    possible = False

    # Check for bipartiteness using DFS
    for i in range(1, N + 1):
        if not vis[i]:
            vis[i] = True
            dfs(i)

    if not possible:
        return "IMPOSSIBLE"
    else:
        return [1 if team[i] else 2 for i in range(1, N + 1)]

# Test the function with the provided test case
N = 5
M = 3
edges = [(1, 2), (1, 3), (4, 5)]

bipartite_teams(N, M, edges)
