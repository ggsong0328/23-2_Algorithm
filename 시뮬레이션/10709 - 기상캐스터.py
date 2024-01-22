import sys

H, W = map(int, sys.stdin.readline().split())
JOI = [sys.stdin.readline() for _ in range(H)]
cloud = [[0] * W for _ in range(H)]
for i in range(H):
    cnt = -1
    flag = False
    for j in range(W):
        if JOI[i][j] == 'c':
            flag = True
            cnt = 0
            cloud[i][j] = cnt
            cnt += 1
        else:
            if flag == True:
                cloud[i][j] = cnt
                cnt += 1
            else:
                cloud[i][j] = cnt
            

for i in range(H):
    for j in range(W):
        print(cloud[i][j], end=' ')
    print()