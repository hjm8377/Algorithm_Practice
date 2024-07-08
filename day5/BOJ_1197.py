import sys


def find(parent, x):
    return x if parent[x] == x else find(parent, parent[x])


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


V, E = map(int, sys.stdin.readline().strip().split())

info = []
for _ in range(E):
    node1, node2, weight = map(int, sys.stdin.readline().strip().split())
    info.append([node1, node2, weight])
info.sort(key=lambda x: x[2])

sum_w = 0
parent = [v for v in range(V + 1)]
for node1, node2, weight in info:
    if find(parent, node1) != find(parent, node2):
        sum_w += weight
        union(parent, node1, node2)

print(sum_w)
