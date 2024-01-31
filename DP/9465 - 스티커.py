import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    DP = [[0] * n for _ in range(2)]
    DP[0][0], DP[1][0] = sticker[0][0], sticker[1][0]
     
    if n > 1:
        DP[0][1] = DP[1][0] + sticker[0][1]
        DP[1][1] = DP[0][0] + sticker[1][1]
    for i in range(2, n):
        DP[0][i] = max(DP[1][i-1], DP[1][i-2]) + sticker[0][i]
        DP[1][i] = max(DP[0][i-1], DP[0][i-2]) + sticker[1][i]
    print(max(DP[0][n-1], DP[1][n-1]))