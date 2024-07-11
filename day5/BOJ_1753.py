import sys
import heapq

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

dist = [float('inf') for _ in range(V)]
dist[K-1] = 0

pq = [(0, K)]
heapq.heapify(pq)
while pq:
    current_dist, current_node = heapq.heappop(pq)

    if current_node in graph:
        if current_dist > dist[current_node - 1]:
            continue

        for next_node, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < dist[next_node - 1]:
                dist[next_node - 1] = distance
                heapq.heappush(pq, (distance, next_node))

for i in dist:
    print(i if i != float('inf') else 'INF')
