# Dice Combinations - Distinct Ways


def count_dice_combinations(N):
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for j in range(1, 7):
            if i - j >= 0:
                dp[i] = (dp[i] + dp[i - j]) % MOD

    return dp[N]

# Accepting input from the user
N = int(input())
result = count_dice_combinations(N)
print(result)

