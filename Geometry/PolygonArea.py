N = int(input())
x = []
y = []

for _ in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

x.append(x[0])
y.append(y[0])

ans = 0
for i in range(N):
    ans += x[i] * y[i + 1]
    ans -= y[i] * x[i + 1]

print(abs(ans))