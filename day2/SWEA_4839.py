def find(l, r, target):
    cnt = 0
    while l <= r:
        cnt += 1
        c = int((l+r) / 2)

        if c == target:
            break

        if c > target:
            r = c
        if c < target:
            l = c

    return cnt


T = int(input())


for t in range(T):
    P, A, B = map(int, input().split())

    res_A = find(1, P, A)
    res_B = find(1, P, B)

    if res_A < res_B:
        winner = 'A'
    elif res_A > res_B:
        winner = 'B'
    else:
        winner = 0
    print(f'#{t+1} {winner}')