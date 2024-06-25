import sys


def check_pal(words, k):
    cnt = 0
    for i in range(k-1):
        for j in range(i+1, k):
            word = words[i] + words[j]
            if word == word[::-1]:
                print(word)
                cnt += 1
                return cnt

            word = words[j] + words[i]
            if word == word[::-1]:
                print(word)
                cnt += 1
                return cnt


T = int(sys.stdin.readline().strip())

for t in range(T):
    k = int(sys.stdin.readline().strip())

    words = []
    for _ in range(k):
        words.append(sys.stdin.readline().strip())

    if not check_pal(words, k):
        print(0)
