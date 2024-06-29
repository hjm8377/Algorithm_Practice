import sys
from collections import deque


def dfs(farm, M, N):
    stack = deque([])
    visited = [[False for _ in range(N)] for _ in range(M)]

    area = 0
    for i, line in enumerate(farm):
        for j, _ in enumerate(line):
            if farm[i][j] and not visited[i][j]:
                stack.append((i, j))
                while stack:
                    x, y = stack.pop()
                    visited[x][y] = True

                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and farm[nx][ny]:
                            stack.append((nx, ny))
                area += 1

    print(area)


T = int(sys.stdin.readline().strip())
for t in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    farm = [[0 for _ in range(N)] for _ in range(M)]
    for k in range(K):
        x, y = map(int, sys.stdin.readline().strip().split())
        farm[x][y] = 1

    dfs(farm, M, N)