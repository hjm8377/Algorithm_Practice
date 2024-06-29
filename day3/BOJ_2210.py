import sys
from collections import deque


def dfs(board, x, y):
    stack = deque([(x, y, '')]) # x, y, prev_num_in_str

    nums = []

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while stack:
        x, y, prev_num = stack.pop()
        prev_num += str(board[x][y])

        if len(prev_num) == 6:
            nums.append(prev_num)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 5 and 0 <= ny < 5 and len(prev_num) < 6:
                stack.append((nx, ny, prev_num))

    return nums


board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]

num_set = set()
for i in range(5):
    for j in range(5):
        num_set.update(dfs(board, i, j))
print(len(num_set))