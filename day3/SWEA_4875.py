from collections import deque


def dfs(maze, N):
    stack = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                stack.append((i, j))

    flag = 0
    while stack:
        x, y = stack.pop()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if maze[nx][ny] == 3:
                    flag = 1
                elif maze[nx][ny] == 0:
                    maze[nx][ny] = 1
                    stack.append((nx, ny))
    return flag


T = int(input())

for t in range(1, T+1):
    N = int(input())

    maze = []
    for i in range(N):
        tmp = []
        for j in input():
            tmp.append(int(j))
        maze.append(tmp)

    print(f'#{t} {dfs(maze, N)}')

