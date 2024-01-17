maxN = 2 * 10**4

def scanBinary():
    res = 0
    line = input()
    for c in line:
        res <<= 1
        res += int(c)
    return res

N, ans = map(int, input().split())
b = [0] * N

for i in range(N):
    b[i] = scanBinary()

for i in range(N):
    for j in range(i+1, N):
        ans = min(ans, bin(b[i] ^ b[j]).count('1'))

print(ans)
