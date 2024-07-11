import sys
from collections import deque


def DSLR(op, n):
    if op == 'D':
        return 2*n % 10000
    elif op == 'S':
        return n-1 if n > 0 else 9999
    elif op == 'L':
        if n < 1000:
            tmp = str(n)
            while len(tmp) < 4:
                tmp = '0' + tmp
        else:
            tmp = str(n)
        return int(tmp[1:] + tmp[0])
    elif op == 'R':
        if n < 1000:
            tmp = str(n)
            while len(tmp) < 4:
                tmp = '0' + tmp
        else:
            tmp = str(n)
        return int(tmp[3] + tmp[:3])


def bfs(A, B):
    queue = deque([(A, '')])
    visited = set([A])
    opers = ['D', 'S', 'L', 'R']

    while queue:
        current, path = queue.popleft()

        if current == B:
            return path

        for oper in opers:
            new_n = DSLR(oper, current)
            if new_n not in visited:
                visited.add(new_n)
                queue.append((new_n, path + oper))

    return ''


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))
