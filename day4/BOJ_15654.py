import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().strip().split())
num_list = list(map(int, sys.stdin.readline().strip().split()))

ans = list(permutations(num_list, M))
ans.sort()

for a in ans:
    for i in a:
        print(i, end=' ')
    print()
