from itertools import permutations


def length(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    return abs(x1 - x2) + abs(y1 - y2)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    coordinates = list(map(int, input().split()))
    # 회사 집 고객 좌표

    start = (coordinates[0], coordinates[1])
    end = (coordinates[2], coordinates[3])
    customer = []
    for i in range(4, N * 2 + 4, 2):
        c = (coordinates[i], coordinates[i+1])
        customer.append(c)

    customer_perm = permutations(customer, N)
    min_length = float('inf')
    for customers in customer_perm:
        sum_local = 0

        sum_local += length(start, customers[0])
        for n in range(N - 1):
            sum_local += length(customers[n], customers[n+1])
        sum_local += length(customers[N-1], end)

        min_length = min(min_length, sum_local)

    print(f'#{t} {min_length}')
