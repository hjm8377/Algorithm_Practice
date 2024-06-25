import copy


def find(heights):
    for i in range(8):
        for j in range(i, 8):
            heights_copy = copy.deepcopy(heights)
            heights_copy.pop(i)
            heights_copy.pop(j)

            if sum(heights_copy) == 100:
                heights_copy.sort()
                for i in heights_copy:
                    print(i)
                return

heights = []
for i in range(9):
    heights.append(int(input()))

find(heights)

