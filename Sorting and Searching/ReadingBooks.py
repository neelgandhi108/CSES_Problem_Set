N = int(input())
mx = -float("inf")
sum = 0

values = input().split()
for i in range(N):
    t = int(values[i])
    mx = max(mx, t)
    sum += t

print(max(sum, 2 * mx))
