import sys
from typing import List, Tuple

def square(x):
    return x * x

def dist(A, B):
    dx = A[0] - B[0]
    dy = A[1] - B[1]
    return square(dx) + square(dy)

def solve(PX: List[Tuple[int, int]], PY: List[Tuple[int, int]], best=[sys.maxsize]):
    len_px = len(PX)
    if len_px == 1:
        return

    mid = len_px // 2
    midX = PX[mid][0]

    LX = PX[:mid]
    RX = PX[mid:]

    LY = [p for p in PY if p[0] <= midX]
    RY = [p for p in PY if p[0] > midX]

    solve(LX, LY, best)
    solve(RX, RY, best)

    stripe = [p for p in PY if abs(p[0] - midX) < best[0]]

    for i in range(len(stripe)):
        for j in range(i + 1, min(i + 7, len(stripe))):
            best[0] = min(best[0], dist(stripe[i], stripe[j]))


N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

PX = sorted(P, key=lambda x: x[0])
PY = sorted(P, key=lambda x: x[1])

best = [sys.maxsize]
solve(PX, PY, best)
print(best[0])