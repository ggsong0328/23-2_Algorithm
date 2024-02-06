import sys

input = sys.stdin.readline

N = int(input())
problems = input().strip()

color_switches = 0

for i in range(1, N):
    if problems[i] != problems[i - 1]:  # 이전 색상과 현재 색상이 다르면
        color_switches += 1  # 색상이 바뀌는 부분 카운트

print((color_switches // 2 + color_switches % 2) + 1)
