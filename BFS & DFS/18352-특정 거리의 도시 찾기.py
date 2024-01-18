from collections import deque
import sys

def bfs(city, start, distance):
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for i in city[cur]:
            if distance[i] == -1:
                distance[i] = distance[cur] + 1
                queue.append(i)

N, M, K, X = map(int, sys.stdin.readline().split())
city = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    city[A].append(B)

distance = [-1] * (N + 1)
distance[X] = 0

bfs(city, X, distance)

#print(distance)

if distance.count(K):
    for i in range(1, N + 1):
        if distance[i] == K:
            print(i)
else:
    print(-1)
