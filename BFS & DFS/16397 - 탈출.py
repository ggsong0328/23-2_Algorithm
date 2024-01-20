import sys
from collections import deque

N, T, G = map(int, sys.stdin.readline().split())

limit = 1000000

visited = [False] * limit

def B_number(n):
    result = n * 2
    if result >= 100000:
        return n
    digits = [int(digit) for digit in str(result)]
    for i in range(len(digits)):
        if digits[i] != 0:
            digits[i] -= 1
            break
        
    modified_result = int(''.join(map(str, digits)))
    return modified_result

def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True
    
    while queue:
        cur, num = queue.popleft()
        if num > T:
            return 'ANG'
        if cur == G:
            return num
        
        if cur + 1 < limit and not visited[cur + 1]:
            queue.append((cur + 1, num + 1))
            visited[cur + 1] = True
        
        if cur * 2 < limit and not visited[B_number(cur)]:
            queue.append((B_number(cur), num + 1))
            visited[B_number(cur)] = True
            

    return 'ANG'
    
print(bfs(N))
