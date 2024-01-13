# Range Xor Queries

def calculate_xor_ranges(N, Q, x, queries):
    # Compute the prefix XOR
    prefix_xor = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_xor[i] = prefix_xor[i - 1] ^ x[i - 1]

    # Process each query and store the results
    results = []
    for a, b in queries:
        result = prefix_xor[b] ^ prefix_xor[a - 1]
        results.append(result)

    return results

# Test the function with a given test case
N = 8
Q = 4
x = [3, 2, 4, 5, 1, 1, 5, 3]
queries = [(2, 4), (5, 6), (1, 8), (3, 3)]

print(calculate_xor_ranges(N, Q, x, queries))
