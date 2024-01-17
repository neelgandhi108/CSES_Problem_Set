N = int(input())
ans = 0
maxN = 3005
B = [0] * maxN

def f(X):
    return X * (X - 1)

for i in range(N):
    B[i] = int(input(), 2)

for i in range(N):
    for j in range(i + 1, N):
        ans += f((bin(B[i] & B[j]).count('1')))

print(ans >> 1)
