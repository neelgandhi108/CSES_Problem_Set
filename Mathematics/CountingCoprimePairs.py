maxX = 10**6 + 1

def init():
    b = [False, False] + [True] * (maxX - 2)
    primes = []
    for i in range(2, int(maxX**0.5) + 1):
        if b[i]:
            for j in range(i*i, maxX, i):
                b[j] = False
    for i in range(2, maxX):
        if b[i]:
            primes.append(i)
    return primes, b

def compute(x, primes, b, dp):
    pf = []
    for p in primes:
        if x == 1:
            break
        elif b[x]:
            pf.append(x)
            break

        if x % p != 0:
            continue
        pf.append(p)
        while x % p == 0:
            x //= p

    K = len(pf)
    ans = 0
    for mask in range(1 << K):
        mu = 1
        for i in range(K):
            if mask & (1 << i):
                mu *= pf[i]

        k = bin(mask).count("1")
        ans += -dp[mu] if k & 1 else dp[mu]
        dp[mu] += 1

    return ans

primes, b = init()
N = int(input())
arr = list(map(int, input().split()))
ans = 0
dp = [0] * maxX
for x in arr:
    ans += compute(x, primes, b, dp)
print(ans)