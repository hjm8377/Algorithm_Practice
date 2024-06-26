N, K = map(int, input().split())
temp = list(map(int, input().split()))

current_sum = sum(temp[:K])
max_sum = current_sum

for i in range(1, N - K + 1):
    current_sum = current_sum - temp[i - 1] + temp[i + K - 1]
    max_sum = max(max_sum, current_sum)

print(max_sum)