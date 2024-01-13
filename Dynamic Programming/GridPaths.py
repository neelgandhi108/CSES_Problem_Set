# Grid Paths

def count_paths(N, grid):
    MOD = 10**9 + 7
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    dp[1][1] = 1 if grid[0][0] == '.' else 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if grid[i-1][j-1] == '.':
                if grid[i - 2][j -1 ] == '.':
                    dp[i][j] += dp[i - 1][j]
                if grid[i - 1][j] == '.':                
                    dp[i][j] += dp[i][j - 1]
                dp[i][j] %= MOD

    return dp[N][N]

# Accepting input from the user
N = int(input())
grid = [input() for i in range(N)]

# Counting the number of paths
result = count_paths(N, grid)
print(result)

