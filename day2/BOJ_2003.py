import sys

N, M = map(int, sys.stdin.readline().strip().split())
num_list = list(map(int, sys.stdin.readline().strip().split()))

cnt = 0
l, r = 0, 0
current_sum = 0
while True:

    if current_sum < M:
        if r < N:
            current_sum += num_list[r]
            r += 1
        else:
            break

    elif current_sum > M:
        current_sum -= num_list[l]
        l += 1

    else:
        cnt += 1
        current_sum -= num_list[l]
        l += 1

print(cnt)
