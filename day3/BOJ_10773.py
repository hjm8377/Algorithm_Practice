import sys
from collections import deque

K = int(sys.stdin.readline().strip())

q = deque()
for _ in range(K):
    n = int(sys.stdin.readline().strip())

    if n:
        q.append(n)
    else:
        q.pop()

print(sum(q))