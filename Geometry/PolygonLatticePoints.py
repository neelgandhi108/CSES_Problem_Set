import math
N = int(input())
x = []
y = []

for _ in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

x.append(x[0])
y.append(y[0])

area = 0
boundary = 0

for i in range(N):
    area += x[i] * y[i + 1] - y[i] * x[i + 1]

    if x[i + 1] == x[i]:
        boundary += abs(y[i + 1] - y[i])
    elif y[i + 1] == y[i]:
        boundary += abs(x[i + 1] - x[i])
    else:
        boundary += math.gcd(abs(x[i + 1] - x[i]), abs(y[i + 1] - y[i]))

area = abs(area)
inside = (area + 2 - boundary) // 2

print(inside, boundary)