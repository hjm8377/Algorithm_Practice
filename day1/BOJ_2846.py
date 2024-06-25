import sys

max_street = 0

N = int(sys.stdin.readline().strip())
streets = list(map(int, sys.stdin.readline().strip().split()))

start = streets[0]
for i, street in enumerate(streets[:-1]):
    if street < streets[i+1]:
        if streets[i+1] - start > max_street:
            max_street = streets[i+1] - start
    else:
        start = streets[i+1]

print(max_street)