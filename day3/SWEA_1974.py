T = int(input())

center = [1, 4, 7]
check = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
for t in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    ans = 1
    for i in range(9):
        w = set()
        h = set()
        for j in range(9):
            w.add(sudoku[i][j])
            h.add(sudoku[j][i])

        if len(w) != 9 or len(h) != 9:
            ans = 0
            break
    if ans:
        for i in center:
            for j in center:
                rect = set()

                for di, dj in check:
                    ni, nj = i + di, j + dj
                    rect.add(sudoku[ni][nj])

                if len(rect) != 9:
                    ans = 0
                    break
            if not ans:
                break

    print(f'#{t} {ans}')