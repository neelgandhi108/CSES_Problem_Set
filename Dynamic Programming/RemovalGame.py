# Removal Game

def solve(N, x):
    p = [0] * (N + 1)
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    found = [[False for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        p[i] = p[i - 1] + x[i - 1]

    def sum_range(l, r):
        return p[r] - p[l - 1]

    def recursive_solve(l, r):
        if found[l][r]:
            return dp[l][r]
        if l == r:
            return x[l - 1]
        found[l][r] = True
        dp[l][r] = max(x[l - 1] + sum_range(l + 1, r) - recursive_solve(l + 1, r), 
                       x[r - 1] + sum_range(l, r - 1) - recursive_solve(l, r - 1))
        return dp[l][r]

    return recursive_solve(1, N)

# Accepting input from the user
N = int(input())
x = list(map(int, input().split()))

# Solving the problem
result = solve(N, x)
print(result)

