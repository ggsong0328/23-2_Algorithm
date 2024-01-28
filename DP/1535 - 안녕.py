import sys

N = int(sys.stdin.readline())

L = [0] + list(map(int, sys.stdin.readline().split()))
J = [0] + list(map(int, sys.stdin.readline().split()))

DP = [[0] * 101 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        if L[i] > j: # 인사를 하지 않는 경우 + 체력이 0 이하로 떨어지면 안됨
            DP[i][j] = DP[i-1][j]
        else: # 인사를 하는 경우
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-L[i]] + J[i]) #i-1번째 사람까지 생각했을 때, 체력이 j-L[i]일 때 얻을 수 있는 최대 기쁨에 현재 사람에게 인사를 해서 얻는 기쁨을 더함

print(DP[N][100])