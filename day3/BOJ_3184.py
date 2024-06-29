import sys
from collections import deque


def bfs(field, R, C):
    queue = deque()
    visited = set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    sheep, wolf = 0, 0
    for i, line in enumerate(field):
        for j, c in enumerate(line):
            if c == 'o' and (i, j) not in visited:
                queue.append((i, j))  # x, y
                visited.add((i, j))
            elif c == 'v' and (i, j) not in visited:
                queue.append((i, j))
                visited.add((i, j))

            sheep_cnt, wolf_cnt = 0, 0
            while queue:
                x, y = queue.popleft()
                if field[x][y] == 'o':
                    sheep_cnt += 1
                elif field[x][y] == 'v':
                    wolf_cnt += 1

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in visited and field[nx][ny] != '#':
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        # if field[nx][ny] == 'v':
                        #     wolf_cnt += 1
                        # elif field[nx][ny] == 'o':
                        #     sheep_cnt += 1

            if sheep_cnt > wolf_cnt:
                sheep += sheep_cnt
            else:
                wolf += wolf_cnt

    return sheep, wolf


R, C = map(int, sys.stdin.readline().strip().split())
field = [sys.stdin.readline().strip() for _ in range(R)]

for i in bfs(field, R, C):
    print(i, end=' ')
