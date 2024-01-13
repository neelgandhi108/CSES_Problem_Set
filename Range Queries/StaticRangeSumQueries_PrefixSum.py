# Static Range Sum Queries

def calculate_sums(N, Q, x, queries):
    # Compute the prefix sum
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + x[i - 1]

    # Process each query and store the results
    results = []
    for a, b in queries:
        result = prefix_sum[b] - prefix_sum[a - 1]
        results.append(result)

    return results

# Test the function with the provided test case
N = 8
Q = 4
x = [3, 2, 4, 5, 1, 1, 5, 3]
queries = [(2, 4), (5, 6), (1, 8), (3, 3)]

print(calculate_sums(N, Q, x, queries))
