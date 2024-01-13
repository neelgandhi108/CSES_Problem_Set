# Labyrinth

from collections import deque

def find_path(N, M, grid):
    # Direction vectors for Up, Down, Left, Right
    h = [1, -1, 0, 0]
    v = [0, 0, 1, -1]
    directions = ['D', 'U', 'R', 'L']

    # Initialize visited matrix and parent matrix
    vis = [[False for _ in range(M)] for _ in range(N)]
    par = [['' for _ in range(M)] for _ in range(N)]
    dist = [[0 for _ in range(M)] for _ in range(N)]

    # Identify start and end points
    sx = sy = ex = ey = -1
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '#':
                vis[i][j] = True
            elif grid[i][j] == 'A':
                sx, sy = i, j
            elif grid[i][j] == 'B':
                ex, ey = i, j

    # BFS to find the path
    vis[sx][sy] = True
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy = x + h[i], y + v[i]
            if 0 <= dx < N and 0 <= dy < M and not vis[dx][dy]:
                par[dx][dy] = directions[i]
                dist[dx][dy] = dist[x][y] + 1
                vis[dx][dy] = True
                q.append((dx, dy))

    if not vis[ex][ey]:
        return "NO"

    # Trace back the path
    path = []
    cx, cy = ex, ey
    while (cx, cy) != (sx, sy):
        path.append(par[cx][cy])
        if par[cx][cy] == 'D':
            cx -= 1
        elif par[cx][cy] == 'U':
            cx += 1
        elif par[cx][cy] == 'R':
            cy -= 1
        elif par[cx][cy] == 'L':
            cy += 1

    return "YES\n" + str(dist[ex][ey]) + "\n" + ''.join(reversed(path))

# Accepting input from the user
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# Calling the function to count rooms
num_rooms = find_path(N, M, grid)
print(num_rooms)