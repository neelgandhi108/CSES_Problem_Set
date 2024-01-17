maxN = 2 * 10**5 + 1

N = int(input())
x = list(map(int, input().split()))
pos = [0] * maxN

for i in range(1, N + 1):
    pos[x[i - 1]] = i

cnt = 1
for i in range(2, N + 1):
    if pos[i - 1] > pos[i]:
        cnt += 1

print(cnt)
