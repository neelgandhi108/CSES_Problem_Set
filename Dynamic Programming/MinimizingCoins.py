# Minimizing Coins

def min_coins(N, X, coins):
    INF = float('inf')
    dp = [INF] * (X + 1)
    dp[0] = 0

    for c in coins:
        for j in range(X - c + 1):
            if dp[j] != INF:
                dp[j + c] = min(dp[j + c], dp[j] + 1)

    return -1 if dp[X] == INF else dp[X]

# Accepting input from the user
N, X = map(int, input().split())
coins = list(map(int, input().split()))

# Finding the minimum number of coins
result = min_coins(N, X, coins)
print(result)

