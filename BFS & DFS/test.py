import sys,math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,k,x = map(int,input().split())

graph = [[] for b in range(n+1)]
visited = [False for b in range(n+1)]
way = [math.inf for b in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

for i in graph[x]:
    way[i] = 1

cnt = 0
def DFS(a):
    global cnt
    cnt += 1
    visited[a] = True

    for i in graph[a]:  
        if visited[i] == False :
            
            way[i] = min(way[i], cnt)
            DFS(i)     

    cnt -=1

DFS(x)
flag = False

#print(way)

for w in range(len(way)):
    if way[w] == k:
        print(w)
        flag = True

if not flag:
    print(-1)