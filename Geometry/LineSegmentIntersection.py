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


def line_intersect(P1, P2, P3, P4):
    # Parallel case
    if (P2 - P1) * (P4 - P3) == 0:
        # Collinear case, check bounding boxes
        if P1.cross(P2, P3) == 0:
            if max(P1.x, P2.x) < min(P3.x, P4.x) or max(P1.y, P2.y) < min(P3.y, P4.y):
                print("NO")
                return
            if max(P3.x, P4.x) < min(P1.x, P2.x) or max(P3.y, P4.y) < min(P1.y, P2.y):
                print("NO")
                return
            print("YES")
            return

        # Non-collinear parallel lines never intersect
        print("NO")
        return

    # Non-parallel case
    if not ((P1.cross(P2, P3) <= 0 and P1.cross(P2, P4) >= 0) or (P1.cross(P2, P3) >= 0 and P1.cross(P2, P4) <= 0)):
        print("NO")
        return
    if not ((P3.cross(P4, P1) <= 0 and P3.cross(P4, P2) >= 0) or (P3.cross(P4, P1) >= 0 and P3.cross(P4, P2) <= 0)):
        print("NO")
        return

    print("YES")


T = int(input())
for _ in range(T):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    P1, P2, P3, P4 = Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)
    line_intersect(P1, P2, P3, P4)
