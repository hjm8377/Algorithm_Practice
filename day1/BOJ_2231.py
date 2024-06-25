N = input()

flag = 1
for i in range(int(N)):
    s = i
    for n in str(i):
        s += int(n)

    if s == int(N):
        print(i)
        flag = 0
        break

if flag:
    print(0)