import sys
from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    land[x][y] = 0
    queue = deque()
    queue.append([x, y])
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and land[nx][ny] == 1:
                land[nx][ny] = 0
                queue.append([nx, ny])

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    land = []
    cnt = 0
    for _ in range(h):
        land.append(list(map(int, sys.stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)