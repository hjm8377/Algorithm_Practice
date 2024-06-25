import sys

n = int(sys.stdin.readline().strip())

log = {}
for _ in range(n):
    name, status = map(str, sys.stdin.readline().strip().split())
    log[name] = status

ans = sorted(log.items(), key=lambda x: (x[1], x[0]), reverse=True)

for i in ans:
    if i[1] == 'enter':
        print(i[0])