import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().strip().split())
alphabets = list(sys.stdin.readline().strip().split())

j = []
m = []
for a in alphabets:
    if a in 'aeiou':
        m.append(a)
    else:
        j.append(a)

# 모음 한 개 이상, 자음 두 개 이상
passwords = []
for i in range(1, (len(m) + 1)):
    if L - i >= 2:
        ms = list(combinations(m, i))
        js = list(combinations(j, L-i))

        for a in js:
            for b in ms:
                passwords.append(sorted(a + b))

for password in sorted(passwords):
    for word in password:
        print(word, end='')
    print()
