import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().strip().split())
city = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 0은 빈칸, 1은 집, 2는 치킨집
chicken_stores = []
for x in range(N):
    for y in range(N):
        if city[x][y] == 2:
            chicken_stores.append((x, y))

alive_chicken = combinations(chicken_stores, M)
mins_city = []
for alive_chicken_stores in alive_chicken:
    min_city = 0
    for x in range(N):
        for y in range(N):
            if city[x][y] == 1:
                min_local = float('inf')
                for cx, cy in alive_chicken_stores:
                    min_local = min(min_local, abs(x - cx) + abs(y - cy))

                min_city += min_local

    mins_city.append(min_city)

print(min(mins_city))
