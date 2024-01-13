# Book Shop

def max_pages(N, X, prices, pages):
    dp = [-1] * (X + 1)
    dp[0] = 0

    for i in range(N):
        for j in range(X - prices[i], -1, -1):
            if dp[j] != -1:
                dp[j + prices[i]] = max(dp[j + prices[i]], dp[j] + pages[i])

    for i in range(1, X + 1):
        dp[i] = max(dp[i], dp[i - 1])
        
    return dp[X]

# Accepting input from the user
N, X = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))

# Finding the maximum number of pages
result = max_pages(N, X, prices, pages)
print(result)

