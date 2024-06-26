import sys
from collections import deque


def bfs(graph, start):
    visited = set()
    q = deque([start])

    while q:
        vertex = q.popleft()
        if vertex not in visited:
            visited.add(vertex)

            q.extend([node for node in graph[vertex] if node not in visited])

    return len(visited) - 1


N = int(sys.stdin.readline().strip())
pair = int(sys.stdin.readline().strip())

net = {i: [] for i in range(1, N+1)}
for _ in range(pair):
    p, c = map(int, sys.stdin.readline().strip().split())
    net[p].append(c)
    net[c].append(p)

print(bfs(net, 1))
