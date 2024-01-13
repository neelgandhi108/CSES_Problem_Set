# Cycle Finding  Bellman-Ford algorithm

def find_negative_cycle(N, M, edges):
    INF = float('inf')
    dp = [INF] * (N + 1)
    dp[1] = 0
    p = [0] * (N + 1)

    ptr = -1
    for iter in range(N):
        ptr = 0
        for a, b, c in edges:
            if dp[b] > dp[a] + c:
                dp[b] = dp[a] + c
                p[b] = a
                ptr = b

    if ptr == 0:
        return "NO"

    # Detecting the negative cycle
    for i in range(N):
        ptr = p[ptr]

    cycle = []
    v = ptr
    while True:
        cycle.append(v)
        v = p[v]
        if v == ptr and len(cycle) > 1:
            break

    cycle.reverse()
    return "YES\n" + ' '.join(map(str, cycle))

# Accepting input from the user
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(M)]

# Finding a negative cycle in the graph
result = find_negative_cycle(N, M, edges)
print(result)

