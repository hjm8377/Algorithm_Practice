import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_pq = []
    max_pq = []
    entry_map = {}
    count = 0

    for _ in range(k):
        s, n = input().split()
        n = int(n)

        if s == 'I':
            heapq.heappush(min_pq, n)
            heapq.heappush(max_pq, -n)
            if n in entry_map:
                entry_map[n] += 1
            else:
                entry_map[n] = 1
            count += 1

        elif s == 'D':
            if count == 0:
                continue
            if n == 1:
                while max_pq:
                    max_val = -heapq.heappop(max_pq)
                    if entry_map[max_val] > 0:
                        entry_map[max_val] -= 1
                        count -= 1
                        break
            elif n == -1:
                while min_pq:
                    min_val = heapq.heappop(min_pq)
                    if entry_map[min_val] > 0:
                        entry_map[min_val] -= 1
                        count -= 1
                        break

    while min_pq and entry_map[min_pq[0]] == 0:
        heapq.heappop(min_pq)
    while max_pq and entry_map[-max_pq[0]] == 0:
        heapq.heappop(max_pq)

    if count == 0:
        print('EMPTY')
    else:
        print(-max_pq[0], min_pq[0])
