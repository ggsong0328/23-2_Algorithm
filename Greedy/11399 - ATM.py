import sys

input = sys.stdin.readline

N = int(input())

money = list(map(int, input().split()))

sorted_money = sorted(money)

sum = 0

for i in range(N):
    for j in range(0, i+1):
        sum += sorted_money[j]
    
print(sum)