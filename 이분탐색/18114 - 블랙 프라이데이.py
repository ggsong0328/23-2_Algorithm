'''
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
N, C = map(int, input().split())

W = list(map(int, input().split()))

W.sort()

answer = 0

for i in range(N):
if W[i] == C:
answer = 1
break
if binary_search(W, C - W[i]):
answer = 1
break
if answer == 1:
break

if answer == 0:
for i in range(N):
for j in range(i + 1, N):
if binary_search(W, C - W[i] + W[j]):
answer = 1
break
if answer == 1:
break

print(answer)

#시간 초과.....
'''

'''
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

N, C = map(int, input().split())
W = list(map(int, input().split()))

W.sort() 

two_items = []
for i in range(N):
    for j in range(i+1, N):
        two_items.append(W[i] + W[j])

two_items.sort() 

answer = 0

for w in W:
    if w == C or binary_search(two_items, C - w):
        answer = 1
        break

print(answer)

#중복....
'''

'''
import sys

def binary_search(arr, target, idx):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid][0] == target and arr[mid][1] != idx and arr[mid][2] != idx:
            return True
        elif arr[mid][0] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

input = sys.stdin.readline

N, C = map(int, input().split())
W = list(map(int, input().split()))

W.sort()  

two_items = []
for i in range(N):
    for j in range(i+1, N):
        two_items.append((W[i] + W[j], i, j))

two_items.sort()

answer = 0
for i in range(N):
    if W[i] == C:
        answer = 1
        break
    if binary_search(two_items, C - W[i], i):
        answer = 1
        break

print(answer)
'''

'''
import sys

def two_pointer(arr, target):
    start = 0
    end = len(arr) - 1
    while start < end:
        current_sum = arr[start] + arr[end]
        if current_sum == target:
            return True
        elif current_sum < target:
            start += 1
        else:
            end -= 1
    return False

input = sys.stdin.readline

N, C = map(int, input().split())
W = list(map(int, input().split()))

W.sort()  

answer = 0
for i in range(N):
    if W[i] == C:
        answer = 1
        break
    if two_pointer(W[i+1:], C - W[i]):
        answer = 1
        break

print(answer)

# 투포인터도 시간초과....
'''


import sys
input = sys.stdin.readline

def binary_search(start, end, arr, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

N, C = map(int, input().split())

W = list(map(int, input().split()))
W.sort()

flag = False
if binary_search(0, N - 1, W, C): # 1개
    flag = True
else:
    for i in range(N):
        if binary_search(i + 1, N - 1, W, C-W[i]): # 2개
            flag = True
            break
    if not flag:
        for i in range(N):
            for j in range(i + 1, N):
                if binary_search(j + 1, N - 1, W, C - (W[i] + W[j])): # 3개
                    flag = True
                    break
            if flag:
                break
            
if flag:
    print(1)
else:
    print(0)
