import sys

def maxSum(A):
    n = len(A)
    DP = [0] * n
    DP[0] = A[0]
    for k in range(1, n):
        DP[k] = max(DP[k-1] + A[k], A[k])
    return max(DP)

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

print(maxSum(num))
