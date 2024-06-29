T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    flag = 0
    for x in range(N):
        for y in range(N):
            if y + M <= N:
                word = board[x][y:y+M]
                if word == word[::-1]:
                    flag = 1
                    print(f'#{t} {word}')
                    break
            if x + M <= N:
                word = ''
                for i in range(x, x+M):
                    word += board[i][y]
                if word == word[::-1]:
                    flag = 1
                    print(f'#{t} {word}')
                    break
        if flag:
            break
