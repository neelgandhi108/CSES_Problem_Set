from collections import deque

N, M = map(int, input().split())  # Reading N and M
G = [[] for _ in range(N+1)]  # Graph
in_degree = [0] * (N+1)  # In-degree
ans = [set() for _ in range(N+1)]  # Bitset replaced by set

# Reading graph edges
for _ in range(M):
    a, b = map(int, input().split())
    G[b].append(a)
    in_degree[a] += 1

# Queue for BFS
Q = deque()

# Initializing the queue
for i in range(1, N+1):
    if in_degree[i] == 0:
        ans[i].add(i)
        Q.append(i)

# BFS
while Q:
    u = Q.popleft()
    for v in G[u]:
        ans[v].update(ans[u])  # Union of sets
        in_degree[v] -= 1
        if in_degree[v] == 0:
            ans[v].add(v)
            Q.append(v)

# Output result
for i in range(1, N+1):
    print(len(ans[i]), end=' ' if i < N else '\n')
