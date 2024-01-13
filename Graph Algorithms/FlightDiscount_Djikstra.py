# Flight Discount Djikstra

import heapq

def shortest_path_with_coupon(N, M, edges):
    INF = float('inf')
    dist = [[INF for _ in range(N + 1)] for _ in range(2)]
    G = [[] for _ in range(N + 1)]

    # Building the graph
    for a, b, c in edges:
        G[a].append((b, c))

    # Priority queue with (distance, node, coupon_used)
    Q = []
    dist[0][1] = dist[1][1] = 0
    heapq.heappush(Q, (0, 1, True))  # Starting with coupon available

    while Q:
        d, u, coupon = heapq.heappop(Q)

        if dist[not coupon][u] < d:
            continue

        for v, w in G[u]:
            # Without using a coupon
            if dist[1][v] > d + w:
                dist[1][v] = d + w
                heapq.heappush(Q, (dist[1][v], v, coupon))

            # Using a coupon if available
            if coupon and dist[0][v] > d + w // 2:
                dist[0][v] = d + int(w // 2)
                heapq.heappush(Q, (dist[0][v], v, False))

    return min(dist[0][N], dist[1][N])

# Accepting input from the user
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(M)]

# Calculating shortest path
result = shortest_path_with_coupon(N, M, edges)
print(result)

