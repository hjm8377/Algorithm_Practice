import sys


def paper_check(paper, x, y, size):

    color = paper[x][y]
    same_color = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                same_color = False
                break
        if not same_color:
            break

    if same_color:
        if color == 0:
            return 1, 0
        else:
            return 0, 1
    else:
        mid = size // 2
        w1, b1 = paper_check(paper, x, y, mid)
        w2, b2 = paper_check(paper, x, y + mid, mid)
        w3, b3 = paper_check(paper, x + mid, y, mid)
        w4, b4 = paper_check(paper, x + mid, y + mid, mid)

    return w1 + w2 + w3 + w4, b1 + b2 + b3 + b4


N = int(sys.stdin.readline().strip())
paper = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

white, blue = paper_check(paper, 0, 0, N)
print(white)
print(blue)
