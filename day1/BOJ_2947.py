import sys


def print_list(l):
    for i in l:
        print(i, end=" ")
    print()

wood_list = list(map(int, sys.stdin.readline().strip().split()))

while True:
    # 1. 첫 번째 조각의 수가 두 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
    if wood_list[0] > wood_list[1]:
        tmp = wood_list[1]
        wood_list[1] = wood_list[0]
        wood_list[0] = tmp
        print_list(wood_list)
    # 2. 2두 번째 조각의 수가 세 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
    if wood_list[1] > wood_list[2]:
        tmp = wood_list[2]
        wood_list[2] = wood_list[1]
        wood_list[1] = tmp
        print_list(wood_list)
    # 3. 세 번째 조각의 수가 네 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
    if wood_list[2] > wood_list[3]:
        tmp = wood_list[3]
        wood_list[3] = wood_list[2]
        wood_list[2] = tmp
        print_list(wood_list)
    # 4. 네 번째 조각의 수가 다섯 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
    if wood_list[3] > wood_list[4]:
        tmp = wood_list[4]
        wood_list[4] = wood_list[3]
        wood_list[3] = tmp
        print_list(wood_list)
    # 5. 만약 순서가 1, 2, 3, 4, 5 순서가 아니라면 1 단계로 다시 간다.
    if wood_list == [1, 2, 3, 4, 5]:
        break

