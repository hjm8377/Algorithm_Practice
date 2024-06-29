# bus 0번 출발 N번 도착
# 한번 충전으로 K번 이동 가능

T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    # K: 한번 충전으로 이동 가능한 정류장 수
    # N: 종점
    # M: 충전기 개수

    charger = list(map(int, input().split()))
    node = [1 if n in charger else 0 for n in range(N+1)]

    cnt = 0
    i = 0
    while i < N - K:
        next_node = [j for j in range(i+1, i+1+K)]
        if node[i+1:i+1+K] == [0 for _ in range(K)]:
            break

        for n in next_node[::-1]:
            if n in charger:
                cnt += 1
                i = n
                break


    print(f'#{t} {cnt if i >= N-K else 0}')



