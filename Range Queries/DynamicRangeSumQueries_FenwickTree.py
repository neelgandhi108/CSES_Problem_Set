# Correcting the code to properly handle Fenwick tree operations

def fenwick_tree_operations(N, Q, initial_values, operations):
    # Initialize the Fenwick tree and input array
    fenwick_tree = [0] * (N + 1)
    x = [0] * (N + 1)

    def update(idx, val):
        diff = val - x[idx]
        x[idx] = val
        while idx <= N:
            fenwick_tree[idx] += diff
            idx += idx & -idx

    def query(idx):
        sum = 0
        while idx > 0:
            sum += fenwick_tree[idx]
            idx -= idx & -idx
        return sum

    # Populate the Fenwick tree with initial values
    for i, value in enumerate(initial_values, 1):
        update(i, value)

    # Process operations and store the results
    results = []
    for t, a, b in operations:
        if t == 1:
            update(a, b)
        else:
            results.append(query(b) - query(a - 1))

    return results

# Test the function with the provided test case
N = 8
Q = 4
initial_values = [3, 2, 4, 5, 1, 1, 5, 3]
operations = [(2, 1, 4), (2, 5, 6), (1, 3, 1), (2, 1, 4)]

print(fenwick_tree_operations(N, Q, initial_values, operations))
