from collections import deque

N = int(input())
a, b = map(int, input().split())
M = int(input())

family = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        for _ in range(len(queue)):
            v = queue.popleft()
            if v == b:
                return count
            for i in family[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        count += 1
    return -1

print(bfs(a))