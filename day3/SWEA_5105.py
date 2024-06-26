from collections import deque

def bfs(maze, N):
    queue = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                queue.append((i, j, 0)) # x, y, step

    while queue:
        x, y, step = queue.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if maze[nx][ny] == 3:
                    return step
                elif maze[nx][ny] == 0:
                    maze[nx][ny] = 1
                    queue.append((nx, ny, step + 1))
    return 0


T = int(input())

for t in range(1, T+1):
    N = int(input())

    maze = []
    for i in range(N):
        tmp = []
        for j in input():
            tmp.append(int(j))
        maze.append(tmp)

    print(f'#{t} {bfs(maze, N)}')

