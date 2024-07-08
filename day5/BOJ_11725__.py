import sys

N = int(sys.stdin.readline().strip())

tree = [0 for _ in range(N+1)]
visited = {1}
for n in range(N-1):
    num1, num2 = map(int, sys.stdin.readline().strip().split())

    if num1 == 1:
        tree[num2] = 1

    elif num2 == 1:
        tree[num1] = 1

    elif tree[num1] != 0:
        tree[num2] = num1

    elif tree[num2] != 0:
        tree[num1] = num2

    else:
        tree[num1] = num2
        tree[num2] = num1

for n in range(2, N+1):
    print(tree[n])
