import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n, s = map(str, sys.stdin.readline().strip().split())
    n = int(n) - 1

    print(s[:n] + s[n+1:])


