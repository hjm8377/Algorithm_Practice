import sys
from collections import deque

V, E = map(int, sys.stdin.readline().strip().split())
K = int(sys.stdin.readline().strip())   # 시작 노드

# graph = [[0 for _ in range(V)] for _ in range(V)]
graph = dict()
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    if u in graph:
        graph[u].append([v, w])
    else:
        graph.update({u: [[v, w]]})

dist = ['INF' for _ in range(V)]
dist[K-1] = 0
stack = deque([[K, 0]]) # node, acc_dist
while stack:
    current_node, acc_dist = stack.pop()
    if current_node in graph:
        for next_node, weight in graph[current_node]:
            if dist[next_node - 1] == 'INF':
                if current_node == K:
                    dist[next_node - 1] = weight
                else:
                    dist[next_node - 1] = acc_dist + weight
            else:
                if dist[next_node - 1] > acc_dist + weight:
                    dist[next_node - 1] = acc_dist + weight

            stack.append([next_node, acc_dist + weight])

for i in dist:
    print(i)
