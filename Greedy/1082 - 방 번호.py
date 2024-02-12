import sys

input = sys.stdin.readline

N = int(input())

prices = list(map(int, input().split()))

M = int(input())

DP = [-float("inf") for _ in range(M + 1)]

for i in range(N-1, -1, -1):
    for j in range(prices[i], M + 1):
        DP[j] = max(DP[j], DP[j - prices[i]] * 10 + i, i) # 현재 인덱스값도 넣어줘야함...
        
print(DP[M])