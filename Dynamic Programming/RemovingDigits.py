
# Removing Digits

def min_steps_to_zero(N):
    INF = float('inf')
    dp = [INF] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        d = i
        while d > 0:
            if d % 10 != 0:
                dp[i] = min(dp[i], dp[i - (d % 10)] + 1)
            d //= 10

    return dp[N]

# Accepting input from the user
N = int(input())
result = min_steps_to_zero(N)
print(result)

