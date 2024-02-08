import sys
input = sys.stdin.readline

N, L = map(int, input().split())

leaks = list(map(int, input().split()))

leaks.sort()

count = 1
start = leaks[0]

for leak in leaks[1:]:
    if leak in range(start, start + L):
        continue
    else:
        start = leak
        count += 1

print(count)