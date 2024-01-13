# Coin Combinations I

def count_combinations(N, X, coins):
    MOD = 10**9 + 7
    dp = [0] * (X + 1)
    dp[0] = 1

    for i in range(X):
        if dp[i] != 0:
            for c in coins:
                if i + c <= X:
                    dp[i + c] = (dp[i + c] + dp[i]) % MOD

    return dp[X]

# Accepting input from the user
N, X = map(int, input().split())
coins = list(map(int, input().split()))

# Counting combinations
result = count_combinations(N, X, coins)
print(result)

