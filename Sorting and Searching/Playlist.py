N = int(input())
k, l, ans = 0, 1, 0
mp = {}

values_lst = input().split()
for r in range(1, N + 1):
    k = values_lst[r-1]
    if k in mp:
        ans = max(ans, r - l)
        l = max(l, mp[k] + 1)
        mp[k] = r
    else:
        ans = max(ans, r - l + 1)
        mp[k] = r

ans = max(N - l + 1, ans)
print(ans)
