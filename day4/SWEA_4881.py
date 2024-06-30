from collections import deque

def dfs(matrix, N):
    # Stack will hold tuples of (current_row, current_sum, visited_columns)
    stack = deque([(0, 0, set())])  # Start from row 0, sum is 0, no columns visited
    min_sum = float('inf')

    while stack:
        row, current_sum, visited = stack.pop()

        if current_sum > min_sum:
            continue

        if row == N:
            min_sum = min(min_sum, current_sum)
            continue

        for col in range(N):
            if col not in visited:
                new_visited = set(visited)
                new_visited.add(col)
                new_sum = current_sum + matrix[row][col]
                stack.append((row + 1, new_sum, new_visited))

    return min_sum


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = dfs(arr, N)
    print(f"#{t} {result}")
