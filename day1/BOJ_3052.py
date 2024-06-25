import sys

num_list = []
for _ in range(10):
    num_list.append(int(sys.stdin.readline().strip()) % 42)

num_set = set(num_list)
print(len(num_set))