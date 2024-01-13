# Elevator Rides

def min_gondola_trips(N, X, weights):
    INF = float('inf')
    dp = [(INF, 0) for _ in range(1 << N)]
    dp[0] = (1, 0)

    for mask in range(1, 1 << N):
        for i in range(N):
            if mask & (1 << i):
                can = dp[mask ^ (1 << i)]
                if can[1] + weights[i] <= X:
                    can = (can[0], can[1] + weights[i])
                else:
                    can = (can[0] + 1, weights[i])
                dp[mask] = min(dp[mask], can)

    return dp[(1 << N) - 1][0]

# Accepting input from the user
N, X = map(int, input().split())
weights = list(map(int, input().split()))

# Finding the minimum number of gondola trips
result = min_gondola_trips(N, X, weights)
print(result)

