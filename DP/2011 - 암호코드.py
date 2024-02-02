import sys


code = [0]
code += list((sys.stdin.readline()))

code.pop()
#print(code)
n = len(code)

if int(code[1]) == 0:
    print(0)

else:
    DP = [0] * n
    DP[0], DP[1] = 1, 1

    for i in range(2, n):
        if int(code[i]) > 0:
            #print(int(code[i]))
            DP[i] += DP[i - 1]
        if int(code[i-1]) * 10 + int(code[i]) >= 10 and int(code[i-1]) * 10 + int(code[i]) <= 26:
            #print(int(code[i-1]) * 10 + int(code[i]))
            DP[i] += DP[i - 2]
            
            
    print(DP[n - 1] % 1000000)
