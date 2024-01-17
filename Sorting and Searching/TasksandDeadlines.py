maxN = 2 * 10**5

N = int(input())
tasks = []

for _ in range(N):
    a, d = map(int, input().split())
    tasks.append((a, d))

tasks.sort(key=lambda x: (x[0], x[1]))

timer = 0
reward = 0

for i in range(N):
    timer += tasks[i][0]
    reward += (tasks[i][1] - timer)

print(reward)
