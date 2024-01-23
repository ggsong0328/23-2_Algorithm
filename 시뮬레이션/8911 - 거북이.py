import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x, y, head = 0, 0, 0
    pos = []
    pos.append([x, y])
    move = list(sys.stdin.readline())
    for i in range(len(move)):
        if move[i] == 'F':
            if head == 0:
                y += 1
            elif head == 1:
                x -= 1
            elif head == 2:
                y -= 1
            elif head == 3:
                x += 1
        elif move[i] == 'B':
            if head == 0:
                y -= 1
            elif head == 1:
                x += 1
            elif head == 2:
                y += 1
            elif head == 3:
                x -= 1
        elif move[i] == 'L':
            head = (head + 1) % 4
        elif move [i] == 'R':
            head = (head - 1) % 4
        pos.append([x, y])
    min_x = min(pos, key=lambda p: p[0])[0]
    max_x = max(pos, key=lambda p: p[0])[0]
    min_y = min(pos, key=lambda p: p[1])[1]
    max_y = max(pos, key=lambda p: p[1])[1]

    width = max_x - min_x
    height = max_y - min_y
    area = width * height

    print(area)

    
