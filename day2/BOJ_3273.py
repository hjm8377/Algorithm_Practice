import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

num_list.sort()

l, r = 0, n-1
cnt = 0
while l < r:
    sum_ = num_list[l] + num_list[r]
    if sum_ > x:
        r -= 1
    elif sum_ < x:
        l += 1
    else:
        cnt += 1
        r -= 1
        l += 1

print(cnt)