from collections import deque

N = int(input())
map_data = [list(map(int, list(input()))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count
    count += 1
    map_data[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and map_data[nx][ny] == 1:
            dfs(nx, ny)

result = []
for i in range(N):
    for j in range(N):
        if map_data[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i)