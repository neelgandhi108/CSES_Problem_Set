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


def point_line_intersect(P1, P2, P3):
    if P2.cross(P1, P3) != 0:
        return False
    return min(P2.x, P3.x) <= P1.x <= max(P2.x, P3.x) and min(P2.y, P3.y) <= P1.y <= max(P2.y, P3.y)


def point_in_polygon(P, N):
    cnt = 0
    boundary = False
    for i in range(1, N + 1):
        j = 1 if i == N else i + 1
        if point_line_intersect(P[0], P[i], P[j]):
            boundary = True

        if P[i].x <= P[0].x < P[j].x and P[0].cross(P[i], P[j]) < 0:
            cnt += 1
        elif P[j].x <= P[0].x < P[i].x and P[0].cross(P[j], P[i]) < 0:
            cnt += 1

    if boundary:
        return "BOUNDARY"
    elif cnt % 2 == 1:
        return "INSIDE"
    else:
        return "OUTSIDE"


N, M = map(int, input().split())
P = [Point() for _ in range(N + 1)]
for i in range(1, N + 1):
    P[i].x, P[i].y = map(int, input().split())
for _ in range(M):
    P[0].x, P[0].y = map(int, input().split())
    print(point_in_polygon(P, N))