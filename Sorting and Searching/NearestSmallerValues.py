N = int(input().strip())
x = [0] + [int(i) for i in input().split()]
ds = [0] * (N + 1)

for i in range(1, N + 1):
    k = i - 1
    while x[k] >= x[i]:
        k = ds[k]
    ds[i] = k
    print(ds[i], end=' ' if i < N else '\n')
