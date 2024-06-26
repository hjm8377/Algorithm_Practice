import sys
from collections import deque


def dfs(num_list, N, M):
    ans = []

    stack = deque([[0, [], set()]]) # idx, 수열, visited

    while stack:
        idx, nums, visited = stack.pop()

        if len(nums) == M:
            ans.append(nums)

        for n in range(idx, N):
            if n not in visited:
                new_visited = set(visited)
                new_visited.add(n)

                new_nums = sorted(nums + [num_list[n]])
                stack.append([n, new_nums, new_visited])
    return ans


N, M = map(int, sys.stdin.readline().strip().split())
num_list = list(map(int, sys.stdin.readline().strip().split()))

for i in sorted(dfs(num_list, N, M)):
    for j in i:
        print(j, end=' ')
    print()
