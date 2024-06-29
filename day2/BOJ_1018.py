import sys

N, M = map(int, sys.stdin.readline().strip().split())
board = [sys.stdin.readline().strip() for _ in range(N)]

min_cnt = 64
for x in range(N - 8 + 1):
    for y in range(M - 8 + 1):

        cnt = 0
        for i in range(8):
            for j in range(8):
                # 2가지 1. 좌상=흰색, 2. 좌상=검은색
                if (i + j) % 2 == 0:
                    if board[x + i][y + j] != 'W':
                        cnt += 1
                else:
                    if board[x + i][y + j] != 'B':
                        cnt += 1
        min_cnt = min(min_cnt, cnt)

        cnt = 0
        for i in range(8):
            for j in range(8):
                # 2가지 1. 좌상=흰색, 2. 좌상=검은색
                if (i + j) % 2 == 0:
                    if board[x + i][y + j] != 'B':
                        cnt += 1
                else:
                    if board[x + i][y + j] != 'W':
                        cnt += 1
        min_cnt = min(min_cnt, cnt)

print(min_cnt)