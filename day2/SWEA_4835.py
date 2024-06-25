T = int(input())

for t in range(T):
    _, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    num_max = 0
    num_min = 10000000
    for i in range(len(num_list)-M+1):
        if sum(num_list[i:i+M]) > num_max:
            num_max = sum(num_list[i:i+M])
        if sum(num_list[i:i+M]) < num_min:
            num_min = sum(num_list[i:i+M])
    print(f'#{t+1} {num_max-num_min}')