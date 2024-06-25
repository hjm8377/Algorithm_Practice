T = int(input())

'''
for test_case in range(1, T + 1):
    for i in range(test_case):
        n = int(input())
        num_list = list(map(int, input().split()))

        print("#" + str(test_case), sep=" ")
        print(max(num_list) - min(num_list))
        
'''

def find_max(num_list):
    tmp = 0
    for n in num_list:
        if n > tmp:
            tmp = n
    return n

def find_min(num_list):
    tmp = 10000000
    for n in num_list:
        if n < tmp:
            tmp = n

    return n

for test_case in range(1, T + 1):
    for i in range(test_case):
        n = int(input())
        num_list = list(map(int, input().split()))

        print("#" + str(test_case), sep=" ")
        print(find_max(num_list) - find_min(num_list))
