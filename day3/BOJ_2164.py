from collections import deque

N = int(input())

l = deque(_ for _ in range(1,N+1))

while len(l) > 1:
	l.popleft()
	l.append(l.popleft())


print(l[0])