import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
war = [list(sys.stdin.readline()) for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    war[x][y] = 0

    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if war[nx][ny] == color:
                    queue.append((nx, ny))
                    war[nx][ny] = 0
    return cnt

w_cnt = 0
b_cnt = 0
for i in range(M):
    for j in range(N):
        if war[i][j] == 'W':
            w_cnt += (bfs(i, j, 'W'))**2
        elif war[i][j] == 'B':
            b_cnt += (bfs(i, j, 'B'))**2
print(w_cnt, b_cnt)
            