import sys

N = int(sys.stdin.readline().strip())
dungchi = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    dungchi.append((x, y))

for i, (x, y) in enumerate(dungchi):
    rank = N
    for j, (p, q) in enumerate(dungchi):
        if i == j:
            pass
        elif x >= p or y >= q:
            rank -= 1

    print(rank, end=' ')

