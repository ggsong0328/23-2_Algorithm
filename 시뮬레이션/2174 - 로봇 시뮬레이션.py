dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

def solve():
    A, B = map(int, input().split())
    N, M = map(int, input().split())
    
    robots = [0] + [list(map(str, input().split())) for _ in range(N)]
    for robot in robots[1:]:
        robot[0], robot[1], robot[2] = int(robot[0]), int(robot[1]), direction[robot[2]]
        
    grid = [[0]*(A+1) for _ in range(B+1)]
    for i in range(1, N+1):
        grid[robots[i][1]][robots[i][0]] = i
    
    for _ in range(M):
        robot_num, cmd, repeat = map(str, input().split())
        robot_num, repeat = int(robot_num), int(repeat)
        
        if cmd == 'L':
            robots[robot_num][2] = (robots[robot_num][2] - repeat) % 4
        elif cmd == 'R':
            robots[robot_num][2] = (robots[robot_num][2] + repeat) % 4
        else:
            for _ in range(repeat):
                nx = robots[robot_num][0] + dx[robots[robot_num][2]]
                ny = robots[robot_num][1] + dy[robots[robot_num][2]]
                
                if nx < 1 or nx > A or ny < 1 or ny > B:
                    return f"Robot {robot_num} crashes into the wall"
                
                if grid[ny][nx] != 0:
                    return f"Robot {robot_num} crashes into robot {grid[ny][nx]}"
                
                grid[robots[robot_num][1]][robots[robot_num][0]] = 0
                grid[ny][nx] = robot_num
                robots[robot_num][0], robots[robot_num][1] = nx, ny
                
    return "OK"

print(solve())
