'''
def Jelly(x, y, map):
    if x == N - 1 and y == N - 1: 
        return True
    if map[x][y] == 0 or map[x][y] == -1:
        return False
    if x + map[x][y] < N and Jelly(x + map[x][y], y, map):
        return True
    if y + map[x][y] < N and Jelly(x, y + map[x][y], map):
        return True
    return False

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

if Jelly(0, 0, map):
    print("HaruHaru")
else:
    print("Hing")

시간 초과ㅠㅠ
'''


from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        if x == y == n - 1:  # 목표 지점 도달 시
            return "HaruHaru"
        for nx, ny in [(x + arr[x][y], y), (x, y + arr[x][y])]:  # 오른쪽, 아래로 이동
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:  # 범위 내이고 방문하지 않았다면
                visited[nx][ny] = True
                q.append((nx, ny))
    return "Hing"  # 모든 경우를 탐색한 후에도 도달하지 못한 경우

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
visited[0][0] = True
print(bfs(0, 0))



