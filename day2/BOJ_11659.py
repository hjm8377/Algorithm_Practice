import sys

N, M = map(int, sys.stdin.readline().strip().split())
num_list = list(map(int, sys.stdin.readline().strip().split()))

sum_acc = [0]
for i in range(0, N):
    sum_acc.append(num_list[i]+sum_acc[i])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())

    print(sum_acc[j] - sum_acc[i-1])