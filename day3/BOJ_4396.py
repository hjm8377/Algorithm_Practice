import sys

n = int(sys.stdin.readline().strip())

board = []
play = []

for _ in range(n):
    board.append(sys.stdin.readline().strip())
for _ in range(n):
    play.append(sys.stdin.readline().strip())

ans = []
bomb_flag = False
check = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for x in range(n):
    played = []
    for y in range(n):
        if play[x][y] == 'x':
            if board[x][y] == '*':
                bomb_flag = True
            cnt = 0
            for dx, dy in check:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == '*':
                    cnt += 1

            played.append(str(cnt))
        else:
            played.append('.')
    ans.append(played)

for x in range(n):
    for y in range(n):
        if bomb_flag and board[x][y] == '*':
            print('*', end='')
        else:
            print(ans[x][y], end='')
    print()
