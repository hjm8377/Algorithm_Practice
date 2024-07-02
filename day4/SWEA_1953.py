from collections import deque


def bfs(world, N, M, R, C, L):
    queue = deque([(R, C, 1)])
    visited = [[False for _ in range(M)] for _ in range(N)]
    area = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    movable = [[], directions, directions[:2], directions[2:],
               [directions[0], directions[3]], [directions[1], directions[3]],
               directions[1:3], [directions[0], directions[2]]]
    while queue:
        x, y, step = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        area += 1

        for dx, dy in movable[world[x][y]]:
            dx_r, dy_r = -dx, -dy
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and step < L:
                if (dx_r, dy_r) in movable[world[nx][ny]]:
                    queue.append((nx, ny, step + 1))

    return area


T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    world = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t} {bfs(world, N, M, R, C, L)}')

