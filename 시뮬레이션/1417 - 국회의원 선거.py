import sys

N = int(sys.stdin.readline())

vote = []

for i in range(N):
    vote.append(int(sys.stdin.readline()))
    
cnt = 0

while max(vote) != vote[0]:
    vote[vote.index(max(vote))] -= 1
    vote[0] += 1
    cnt += 1
    
if vote.count(max(vote)) > 1:
    print(cnt + 1)
else:
    print(cnt)