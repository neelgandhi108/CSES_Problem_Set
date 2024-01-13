
# Money Sums

def find_possible_sums(N, coins):
    maxX = 100000
    dp = [False] * (maxX + 1)
    dp[0] = True

    for x in coins:
        for j in range(maxX - x, -1, -1):
            if dp[j]:
                dp[j + x] = True

    sums = [i for i in range(1, maxX + 1) if dp[i]]
    return len(sums), sums

# Accepting input from the user
N = int(input())
coins = list(map(int, input().split()))

# Finding all possible sums
count, possible_sums = find_possible_sums(N, coins)
print(count)
print(' '.join(map(str, possible_sums)))

