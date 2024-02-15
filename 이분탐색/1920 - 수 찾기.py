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
A = list(map(int, input().split()))

A.sort()

M = int(input())
check = list(map(int, input().split()))

for i in range(M):
    if binary_search(A, check[i]):
        print(1)
    else:
        print(0)