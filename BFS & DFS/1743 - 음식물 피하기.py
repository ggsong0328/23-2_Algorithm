import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
food = [[0]*M for _ in range(N)]

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    food[x - 1][y - 1] = 1
visited = [ [False]*M for _ in range(N) ] 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if food[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    queue.append((nx, ny))


answer = 0
for i in range(N):
    for j in range(M):
        if food[i][j] == 1 and not visited[i][j]:
            cnt = 0
            bfs(i, j)
            answer = max(answer, cnt)

print(answer)