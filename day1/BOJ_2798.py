n, m = map(int, input().split())
cards = list(map(int, input().split()))
sum_ = 0

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            tmp1 = cards[i]
            tmp2 = cards[j]
            tmp3 = cards[k]
            tmp_sum_ = tmp1 + tmp2 + tmp3
            if tmp_sum_ >= sum_ and tmp_sum_ <= m:
                sum_ = tmp_sum_
print(sum_)