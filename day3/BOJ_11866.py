import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
people = deque([i for i in range(1, N + 1)])

print("<", end='')
while people:
    for _ in range(K - 1):
        people.append(people.popleft())
    a = people.popleft()
    if people:
        print(a, end=', ')
    else:
        print(a, end='')
print(">")
