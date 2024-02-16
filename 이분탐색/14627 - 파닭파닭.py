import sys

input = sys.stdin.readline

def slice(len, arr):
    cnt = 0
    for i in arr:
        cnt += i // len
    return cnt


S, C = map(int, input().split())

L = [int(input()) for _ in range(S)]


L.sort()

start = 1
end = max(L)
maxS = 0

while start <= end:
    mid = (start + end) // 2
    if slice(mid, L) >= C:
        maxS = mid
        start = mid + 1
    else:
        end = mid - 1
        
answer = sum(L) - (maxS * C)
print(answer)
