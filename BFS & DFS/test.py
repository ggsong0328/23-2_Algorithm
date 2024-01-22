from collections import deque

N = int(input())
water = [list(map(int, input().split())) for _ in range(N)]

shark_size = 2
shark_eat = 0
for i in range(N):
    for j in range(N):
        if water[i][j] == 9:
            shark_pos = (i, j)
            water[i][j] = 0 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[False]*N for _ in range(N)]
    queue = deque([(0, x, y)])
    visited[x][y] = True
    while queue:
        time, x, y = queue.popleft()
        if 0 < water[x][y] < shark_size:  
            water[x][y] = 0 
            return time, x, y  
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and shark_size >= water[nx][ny]:
                visited[nx][ny] = True
                queue.append((time+1, nx, ny)) 
    return -1, x, y  

time = 0
while True:
    t, x, y = bfs(*shark_pos)
    if t == -1:  
        break
    time += t
    shark_eat += 1
    if shark_eat == shark_size: 
        shark_size += 1
        shark_eat = 0
    shark_pos = (x, y)

print(time)
