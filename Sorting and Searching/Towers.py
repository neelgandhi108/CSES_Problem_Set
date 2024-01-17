N = int(input())
S = set()

values = input().split()
for i in range(N):
    k = values[i]
    if k in S:
        S.remove(k)
    S.add(k)

print(len(S))
