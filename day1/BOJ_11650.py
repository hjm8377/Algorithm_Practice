import sys

N = int(sys.stdin.readline().strip())

coordinates = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())

    coordinates.append((x, y))

coordinates.sort(key=lambda a: (a[0], a[1]))

for x, y in coordinates:
    print(x, y)