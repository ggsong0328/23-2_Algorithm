import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

board = [[0] * N for _ in range(N)]

for _  in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x - 1][y - 1] = 1
    

L = int(sys.stdin.readline())

snake = deque()

for _ in range(L):
    A, C = sys.stdin.readline().split()
    X = int(A)
    snake.append((X, C))
    
time = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cur_x, cur_y = 0, 0

dir = 0

queue = deque()
queue.append((cur_x, cur_y))
while True:
    nx = cur_x + dx[dir]
    ny = cur_y + dy[dir]
    time += 1
    if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in queue:
        break
    queue.append((nx, ny))
    
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        queue.popleft()
    cur_x, cur_y = nx, ny
    if snake and time == snake[0][0]:
        _, C = snake.popleft()
        if C == "D":
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4

print(time)




