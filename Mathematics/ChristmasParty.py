MOD = 10**9 + 7
maxN = 10**6

def fn():
    dp = [0] * (maxN + 1)
    dp[2] = 1
    for i in range(3, maxN + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % MOD
    return dp

dp = fn()
N = int(input())
print(dp[N])

