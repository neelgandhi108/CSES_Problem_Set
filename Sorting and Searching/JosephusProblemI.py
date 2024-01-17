# Implement the order statistics tree as a class
class OrderStatisticsTree:
    def __init__(self):
        self.tree = []

    def insert(self, val):
        self.tree.append(val)

    def find_by_order(self, k):
        return self.tree[k]

    def erase(self, val):
        self.tree.remove(val)

    def size(self):
        return len(self.tree)


N = int(input())
T = OrderStatisticsTree()

for i in range(1, N + 1):
    T.insert(i)

idx = 1
while T.size() > 0:
    idx %= T.size()
    x = T.find_by_order(idx)
    T.erase(x)
    print(x, end=" \n"[T.size() == 0])
    idx += 1
