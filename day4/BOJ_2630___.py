import sys


def paper_check(paper, w, b):   # paper arr, white, blue
    N = len(paper)
    if all(0 not in l for l in paper):
        return w + 1, b
    elif all(1 not in l for l in paper):
        return w, b + 1
    else:
        paper_check(paper[:N][:N], w, b)
        paper_check(paper[:N][N:], w, b)
        paper_check(paper[N:][:N], w, b)
        paper_check(paper[N:][N:], w, b)


N = int(sys.stdin.readline().strip())
paper = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

print(paper_check(paper, 0, 0))
