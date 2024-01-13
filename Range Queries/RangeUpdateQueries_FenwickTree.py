# Range Update Queries

def fenwick_tree_range_update(N, Q, initial_values, operations):
    # Initialize the Fenwick tree
    fenwick_tree = [0] * (N + 2)

    def update(idx, val):
        while idx <= N + 1:
            fenwick_tree[idx] += val
            idx += idx & -idx

    def query(idx):
        sum = 0
        while idx > 0:
            sum += fenwick_tree[idx]
            idx -= idx & -idx
        return sum

    # Initial range updates
    for i, value in enumerate(initial_values, 1):
        update(i, value)
        update(i + 1, -value)

    # Process operations and store the results
    results = []
    for operation in operations:
        t = operation[0]
        if t == 1:
            a, b, x = operation[1], operation[2], operation[3]
            update(a, x)
            update(b + 1, -x)
        elif t == 2:
            k = operation[1]
            results.append(query(k))

    return results

# Test the function with the provided test case
N = 8
Q = 3
initial_values = [3, 2, 4, 5, 1, 1, 5, 3]
operations = [(2, 4), (1, 2, 5, 1), (2, 4)]

print(fenwick_tree_range_update(N, Q, initial_values, operations))
