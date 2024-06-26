import sys

N, M = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))

r = max(trees)
l = 0
ans = r // 2
while l <= r:
    sum_ = 0
    for n in trees:
        if n - ans > 0:
            sum_ += n - ans

    if sum_ >= M:
        l = ans+1

    elif sum_ < M:
        r = ans-1

    ans = (l + r) // 2

print(ans)
