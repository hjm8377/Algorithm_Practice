import sys
from collections import deque


def dfs(board):
    N = len(board)

    min_cost = float('inf')
    for i in range(N):
        stack = deque([(i, 0, set())])

        while stack:
            x, cost, visited = stack.pop()
            visited.add(x)

            if cost >= min_cost:
                continue

            if len(visited) == N and board[x][i]:
                min_cost = min(min_cost, cost+board[x][i])
                continue

            for n in range(N):  # 다음 도시
                if n != x and n not in visited and board[x][n]:
                    new_visited = set(visited)
                    new_visited.add(n)
                    stack.append((n, cost + board[x][n], new_visited))

    return min_cost


N = int(sys.stdin.readline().strip())
W = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
print(dfs(W))
