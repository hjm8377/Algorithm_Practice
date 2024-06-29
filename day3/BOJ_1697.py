import sys
from collections import deque

def bfs(start, target):
    queue = deque([(start, 0)])
    visited = [False] * 100001 
    visited[start] = True

    while queue:
        x, time = queue.popleft()

        if x == target:
            return time

        # 걷기 1
        if x + 1 <= 100000 and not visited[x + 1]:
            visited[x + 1] = True
            queue.append((x + 1, time + 1))
        # 걷기 2
        if x - 1 >= 0 and not visited[x - 1]:
            visited[x - 1] = True
            queue.append((x - 1, time + 1))
        # 순간이동
        if x * 2 <= 100000 and not visited[x * 2]:
            visited[x * 2] = True
            queue.append((x * 2, time + 1))

N, K = map(int, sys.stdin.readline().strip().split())

print(bfs(N, K))
