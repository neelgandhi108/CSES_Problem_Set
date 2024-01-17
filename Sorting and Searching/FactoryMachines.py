N, T = map(int, input().split())
k = list(map(int, input().split()))

def check(t):
    cnt = 0
    for i in range(N):
        cnt += t // k[i]
        if cnt >= T:
            return True
    return False

lo = 0
hi = 10**18

while lo <= hi:
    mid = lo + (hi - lo) // 2
    if check(mid):
        hi = mid - 1
    else:
        lo = mid + 1

print(lo)
