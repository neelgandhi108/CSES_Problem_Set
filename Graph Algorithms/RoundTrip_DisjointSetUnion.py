# Round Trip

def find_cycle(N, M, edges):
    p = [0] * (N + 1)
    ds = [-1] * (N + 1)
    G = [[] for _ in range(N + 1)]

    def dfs(u):
        for v in G[u]:
            if v != p[u]:
                p[v] = u
                dfs(v)

    def find(u):
        if ds[u] < 0:
            return u
        ds[u] = find(ds[u])
        return ds[u]

    def merge(u, v):
        u = find(u)
        v = find(v)
        if u == v:
            return False
        if ds[u] < ds[v]:
            u, v = v, u
        ds[v] += ds[u]
        ds[u] = v
        return True

    for a, b in edges:
        if not merge(a, b):
            dfs(a)
            ans = []
            u = b
            while u != 0:
                ans.append(u)
                u = p[u]
            ans.append(b)
            return ans
        else:
            G[a].append(b)
            G[b].append(a)

    return "IMPOSSIBLE"

# Test the function with the provided test case
N = 5
M = 6
edges = [(1, 3), (1, 2), (5, 3), (1, 5), (2, 4), (4, 5)]

print(find_cycle(N, M, edges))
