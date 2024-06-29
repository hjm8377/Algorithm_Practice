import sys
from collections import deque


def bfs(maze, N, M):
    queue = deque([(0, 0, 0, 0)]) # x, y, step, break_num
    visited = [[[False, False] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y, step, break_num = queue.popleft()

        if x == N-1 and y == M-1:
            return step + 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == '0' and not visited[nx][ny][break_num]:
                    visited[nx][ny][break_num] = True
                    queue.append((nx, ny, step + 1, break_num))
                elif maze[nx][ny] == '1' and break_num == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, step + 1, 1))

    return -1


N, M = map(int, sys.stdin.readline().strip().split())
maze = [sys.stdin.readline().strip() for _ in range(N)]

# start (0,0), end (N-1, M-1)
print(bfs(maze, N, M))
