def longest_increasing_subsequence(N, sequence):
    S = []
    for a in sequence:
        # Find the position to insert the current element
        index = bisect_right(S, a)

        # If it's the largest element, simply append it
        if index == len(S):
            S.append(a)
        else:
            # Otherwise, replace the element at the found position
            S[index] = a

    return len(S)

# Function to perform binary search
def bisect_right(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]: 
            hi = mid
        else: 
            lo = mid + 1
    return lo

N = int(input())
sequence = list(map(int, input().split()))

# Finding the length of the longest increasing subsequence
result = longest_increasing_subsequence(N, sequence)
print(result)

