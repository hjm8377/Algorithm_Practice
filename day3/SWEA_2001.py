T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    flies = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_flies = 0
            for k in range(M):
                for l in range(M):
                    sum_flies += flies[i+k][j+l]

            max_flies = max(max_flies, sum_flies)

    print(f'#{t} {max_flies}')