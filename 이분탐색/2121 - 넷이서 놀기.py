import sys

input = sys.stdin.readline

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


N = int(input())

A, B = map(int, input().split())

coordinate = []

for _ in range(N):
    coordinate.append(list(map(int, input().split())))
    
coordinate.sort()

count = 0

for i in range (N):
    x = coordinate[i][0]
    y = coordinate[i][1]
    
    if (binary_search(coordinate, [x + A, y]) and binary_search(coordinate, [x, y + B]) and binary_search(coordinate, [x + A, y + B])):
        count += 1
        
print(count)