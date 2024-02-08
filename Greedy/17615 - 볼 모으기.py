import sys
input = sys.stdin.readline

N = int(input())
Balls = input().strip()


result=[]

temp = Balls.rstrip('R')
result.append(temp.count('R'))

temp = Balls.rstrip('B')
result.append(temp.count('B'))

temp = Balls.lstrip('R')
result.append(temp.count('R'))

temp = Balls.lstrip('B')
result.append(temp.count('B'))

print(min(result))


