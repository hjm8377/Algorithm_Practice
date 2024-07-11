from collections import deque

T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    tree_list = list(map(int, input().split()))

    tree = [[0, 0] for _ in range(max(tree_list) + 1)]
    for i in range(0, 2 * E, 2):
        parent = tree_list[i]
        child = tree_list[i+1]

        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child

    cnt = 1
    stack = deque([N])
    while stack:
        parent = stack.pop()

        child1, child2 = tree[parent]
        if child1 != 0:
            cnt += 1
            stack.append(child1)
        if child2 != 0:
            cnt += 1
            stack.append(child2)

    print(f'#{t} {cnt}')
