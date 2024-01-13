# Array Description

def count_sequences(N, M, x):
    MOD = 10**9 + 7
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    # Initialize the first row
    if x[0]:
        dp[1][x[0]] = 1
    else:
        for i in range(1, M + 1):
            dp[1][i] = 1

    # Dynamic programming
    for i in range(2, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = dp[i - 1][j]
            if j != 1:
                dp[i][j] += dp[i - 1][j - 1]
            if j != M:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD

        if x[i - 1]:
            for j in range(M + 1):
                if j != x[i - 1]:
                    dp[i][j] = 0

    return sum(dp[N]) % MOD

# Accepting input from the user
N, M = map(int, input().split())
x = list(map(int, input().split()))

# Counting the number of valid sequences
result = count_sequences(N, M, x)
print(result)

