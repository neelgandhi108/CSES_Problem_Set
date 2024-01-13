# Static Range Minimum Queries

def range_minimum_query(N, Q, x, queries):
    # Initialize the sparse table
    logN = 19
    sparse_table = [[0] * logN for _ in range(N)]

    # Copy the input array to the first column of the sparse table
    for i in range(N):
        sparse_table[i][0] = x[i]

    # Build the sparse table
    for j in range(1, logN):
        for i in range(N - (1 << j) + 1):
            sparse_table[i][j] = min(sparse_table[i][j-1], sparse_table[i + (1 << (j-1))][j-1])

    # Process each query and store the results
    results = []
    for a, b in queries:
        a -= 1
        b -= 1
        length = b - a + 1
        k = length.bit_length() - 1
        result = min(sparse_table[a][k], sparse_table[b - (1 << k) + 1][k])
        results.append(result)

    return results

# Test the function with the provided test case
N = 8
Q = 4
x = [3, 2, 4, 5, 1, 1, 5, 3]
queries = [(2, 4), (5, 6), (1, 8), (3, 3)]

print(range_minimum_query(N, Q, x, queries))
