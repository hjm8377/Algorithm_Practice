def boom(balloons, x, y, N, M):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    ans = balloons[x][y]
    for i in range(4):
        nx, ny = x + dx[i],  y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and balloons[nx][ny]:
            ans += balloons[nx][ny]

    return ans


T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    balloons = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        balloons.append(tmp)

    ans = []
    for i in range(N):
        for j in range(M):
            ans.append(boom(balloons, i, j, N, M))

    print(f'#{t+1} {max(ans)}')