T = int(input())

for t in range(T):
    S = input()

    sum = 0
    acc = 0
    for s in S:
        if s == 'O':
            acc += 1
        else:
            acc = 0
        sum += acc

    print(sum)