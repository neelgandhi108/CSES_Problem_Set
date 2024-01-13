# Counting Towers

def compute_dp(N, dp):
    MOD = 10**9 + 7
    dp[1] = 2
    dp[2] = 8
    for i in range(3, N + 1):
        dp[i] = ((6 * dp[i - 1] - 7 * dp[i - 2]) % MOD + MOD) % MOD
    return dp[N]

def find_values(T, N_values):
    max_N = max(N_values)
    dp = [0] * (max_N + 1)
    results = []
    for N in N_values:
        results.append(compute_dp(N, dp))
    return results

# Accepting input from the user
T = int(input())
N_values = [int(input()) for _ in range(T)]

# Finding the values for each test case
results = find_values(T, N_values)
for result in results:
    print(result)

