import sys
from collections import deque

T = int(input())

for t in range(1, T + 1):
    string = sys.stdin.readline().strip()

    stack = deque()

    for s in string:
        if not stack:
            stack.append(s)
        elif (stack[-1] == '(' and s == ')') or (stack[-1] == ')' and s == '()'):
            stack.pop()
        else:
            stack.append(s)

    print('NO' if stack else 'YES')