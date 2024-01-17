def dfs(u, G, sz):
    sz[u] = 1
    for v in G[u]:
        dfs(v, G, sz)
        sz[u] += sz[v]


N = int(input())
p = [0] * (N + 1)
G = [[] for _ in range(N + 1)]
sz = [0] * (N + 1)

values = input().split()
for i in range(2, N + 1):
    p[i] = int(values[i-2])
    G[p[i]].append(i)

dfs(1, G, sz)

for i in range(1, N + 1):
    print(sz[i] - 1, end=' ' if i < N else '\n')

