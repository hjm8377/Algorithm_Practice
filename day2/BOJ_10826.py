import sys

fibo = [0, 1]
for i in range(2, 10001):
    fibo.append(fibo[i - 1] + fibo[i - 2])

n = int(sys.stdin.readline().strip())
print(fibo[n])