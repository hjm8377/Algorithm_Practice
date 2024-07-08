import sys

input = sys.stdin.readline

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

korean = 0
if A % C != 0:
    korean = A // C + 1
else:
    korean = A // C

mathmatics = 0
if B % D != 0:
    mathmatics = B // D + 1
else:
    mathmatics = B // D

print(L - max(korean, mathmatics))