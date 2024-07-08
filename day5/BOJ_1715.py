import sys
import heapq

N = int(sys.stdin.readline().strip())

heap = []
for n in range(N):
    heapq.heappush(heap, int(sys.stdin.readline().strip()))

min_sum = 0
while True:
    if len(heap) == 1:
        break
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)

    min_sum += (num1+num2)
    heapq.heappush(heap, num1+num2)

print(min_sum)
