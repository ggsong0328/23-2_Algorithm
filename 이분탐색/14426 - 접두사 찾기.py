import sys
input = sys.stdin.readline

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid][:len(target)] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

N, M = map(int, input().split())

words = []

for _ in range(N):
    words.append(input().strip())

words.sort()
    
count = 0    
    
for _ in range(M):
    prefix = input().strip()
    if binary_search(words, prefix):
        count += 1
print(count)