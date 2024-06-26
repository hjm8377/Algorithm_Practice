import sys
from collections import deque


def bfs(tomatoes, N, M):
    queue = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    day = -1

    for i in range(N):
        for j in range(M):
            # 익은 토마토를 큐에 추가
            if tomatoes[i][j] == 1:
                queue.append((i, j))

    while queue:
        day += 1

        for _ in range(len(queue)):
            x, y = queue.popleft()
            # 익은 토마토 주위 확인
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = 1
                    queue.append((nx, ny))

    for t in tomatoes:
        if 0 in t:
            day = -1

    return day


M, N = map(int, sys.stdin.readline().strip().split())
tomatoes = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

print(bfs(tomatoes, N, M))
