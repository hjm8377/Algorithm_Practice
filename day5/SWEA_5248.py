def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    list_people = list(map(int, input().split()))

    parent = [n for n in range(N + 1)]
    rank = [0] * (N + 1)

    for i in range(0, 2 * M, 2):
        union(parent, rank, list_people[i], list_people[i + 1])

    ans = set()
    for i in range(1, N + 1):
        ans.add(find(parent, i))

    print(f'#{t} {len(ans)}')