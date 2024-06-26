T = int(input())

# for t in range(T):
#     _, M = map(int, input().split())
#     num_list = list(map(int, input().split()))
#
#     num_max = 0
#     num_min = 10000000
#     for i in range(len(num_list)-M+1):
#         if sum(num_list[i:i+M]) > num_max:
#             num_max = sum(num_list[i:i+M])
#         if sum(num_list[i:i+M]) < num_min:
#             num_min = sum(num_list[i:i+M])

for t in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    sum_acc = [0]
    for i in range(N):
        sum_acc.append(sum_acc[i] + num_list[i])

    num_max = 0
    num_min = 10000000
    for i in range(N-M+1):
        sum_ = sum_acc[i+M] - sum_acc[i]
        num_max = max(num_max, sum_)
        num_min = min(num_min, sum_)

    print(f'#{t+1} {num_max-num_min}')