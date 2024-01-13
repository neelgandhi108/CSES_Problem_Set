# Counting Rooms

def count_rooms(N, M, grid):
    # Direction vectors for Up, Down, Left, Right
    h = [1, -1, 0, 0]
    v = [0, 0, 1, -1]

    # Initialize visited matrix
    vis = [[False for _ in range(M)] for _ in range(N)]

    # Mark walls as visited
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '#':
                vis[i][j] = True

    def dfs(x, y):
        vis[x][y] = True
        for i in range(4):
            dx, dy = x + h[i], y + v[i]
            if 0 <= dx < N and 0 <= dy < M and not vis[dx][dy]:
                dfs(dx, dy)

    # Count rooms using DFS
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not vis[i][j]:
                dfs(i, j)
                cnt += 1

    return cnt

# Accepting input from the user
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# Calling the function to count rooms
num_rooms = count_rooms(N, M, grid)
print(num_rooms)


