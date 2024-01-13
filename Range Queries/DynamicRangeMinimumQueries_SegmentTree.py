# Dynamic Range Minimum Queries
class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.lo = [0] * (4 * size)
        self.hi = [0] * (4 * size)
        self.mn = [float('inf')] * (4 * size)

    def init(self, i, l, r, values):
        self.lo[i] = l
        self.hi[i] = r
        if l == r:
            self.mn[i] = values[l - 1]
            return
        m = (l + r) // 2
        self.init(2 * i, l, m, values)
        self.init(2 * i + 1, m + 1, r, values)
        self.pull(i)

    def pull(self, i):
        self.mn[i] = min(self.mn[2 * i], self.mn[2 * i + 1])

    def assign(self, i, l, r, v):
        if l > self.hi[i] or r < self.lo[i]:
            return
        if l <= self.lo[i] and self.hi[i] <= r:
            self.mn[i] = v
            return
        self.assign(2 * i, l, r, v)
        self.assign(2 * i + 1, l, r, v)
        self.pull(i)

    def minimum(self, i, l, r):
        if l > self.hi[i] or r < self.lo[i]:
            return float('inf')
        if l <= self.lo[i] and self.hi[i] <= r:
            return self.mn[i]
        lmin = self.minimum(2 * i, l, r)
        rmin = self.minimum(2 * i + 1, l, r)
        self.pull(i)
        return min(lmin, rmin)


def segment_tree_operations(N, Q, initial_values, operations):
    tree = SegmentTree(N)
    tree.init(1, 1, N, initial_values)

    results = []
    for t, a, b in operations:
        if t == 1:
            tree.assign(1, a, a, b)
        elif t == 2:
            results.append(tree.minimum(1, a, b))

    return results


# Test the function with the provided test case
N = 8
Q = 4
initial_values = [3, 2, 4, 5, 1, 1, 5, 3]
operations = [(2, 1, 4), (2, 5, 6), (1, 2, 3), (2, 1, 4)]

print(segment_tree_operations(N, Q, initial_values, operations))
