import sys
from collections import deque


def dfs(board, sx, sy):
    N = len(board)
    stack = deque([(sx, sy, 0)]) # current x, y, cost
    visited = [[False for _ in range(N)] for _ in range(N)]

    min_cost = float('inf')
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while stack:
        x, y, cost = stack.pop()
        visited[x][y] = True

        if cost >= min_cost:
            continue

        if (x == N - 1 and y == N - 1 and sx == sy == 0) or (x == 0 and y == 0 and sx == sy == N - 1):
            min_cost = min(cost, min_cost)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] and not visited[nx][ny]:
                stack.append((nx, ny, cost + board[nx][ny]))

    return min_cost


N = int(sys.stdin.readline().strip())
W = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

print(dfs(W, 0, 0) + dfs(W, N-1, N-1))
