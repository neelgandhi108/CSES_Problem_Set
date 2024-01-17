class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.y - self.y * other.x

    def cross(self, b, c):
        return (b - self) * (c - self)


T = int(input())
for _ in range(T):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    P = [Point(x1, y1), Point(x2, y2), Point(x3, y3)]

    cross = P[0].cross(P[1], P[2])
    if cross < 0:
        print("RIGHT")
    elif cross > 0:
        print("LEFT")
    else:
        print("TOUCH")
