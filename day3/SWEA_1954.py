T = int(input())

for t in range(T):
    N = int(input())

    ans = [[0 for _ in range(N)] for _ in range(N)]

    i = 0
    j = 0

    # 방향 우선순위 우/하/좌/상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    direction = 0
    for num in range(1, N*N+1):

        ans[i][j] = num

        ni = i + di[direction]
        nj = j + dj[direction]

        if ni < 0 or ni >= N or nj < 0 or nj >= N or ans[ni][nj] != 0:
            direction = (direction + 1) % 4
            ni = i + di[direction]
            nj = j + dj[direction]

        i = ni
        j = nj

    print(f'#{t+1}')
    for x in range(N):
        for y in range(N):
            print(ans[x][y], end=" ")
        print()
