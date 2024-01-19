import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
computer = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    computer[x].append(y)
    computer[y].append(x)

visited = [False] * (n + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    while queue:
        v = queue.popleft()
        for i in (computer[v]):
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                cnt += 1
    return cnt


print(bfs(1))