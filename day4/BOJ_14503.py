import sys

# Read the input
N, M = map(int, sys.stdin.readline().strip().split())
r, c, d = map(int, sys.stdin.readline().strip().split())
# d: 0 = 북, 1 = 동, 2 = 남, 3 = 서

room = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# Directions: 0 = 북, 1 = 동, 2 = 남, 3 = 서
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cleaning_cnt = 0

x, y = r, c

while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if room[x][y] == 0:
        cleaning_cnt += 1
        room[x][y] = 2  # Mark as cleaned

    clean = False
    for _ in range(4):
        d = (d + 3) % 4
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            x, y = nx, ny
            clean = True
            break

    if not clean:
        dx, dy = directions[(d + 2) % 4]
        nx, ny = x + dx, y + dy

        if not (0 <= nx < N and 0 <= ny < M) or room[nx][ny] == 1:
            break

        x, y = nx, ny

print(cleaning_cnt)