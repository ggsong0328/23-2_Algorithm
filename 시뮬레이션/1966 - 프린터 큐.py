import sys
from collections import deque
T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    priority = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while priority:
        max_pri = max(priority)
        front = priority.popleft()
        M -= 1
        
        if max_pri == front:
            count += 1
            if M < 0:
                print(count)
                break
        else:
            priority.append(front)
            if M < 0:
                M = len(priority) - 1

