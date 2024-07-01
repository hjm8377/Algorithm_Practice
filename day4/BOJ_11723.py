import sys


class S:

    def __init__(self):
        self.s = 0

    def add(self, x):
        self.s |= (1 << x)

    def remove(self, x):
        self.s &= ~(1 << x)

    def check(self, x):
        return int(bool(self.s & (1 << x)))

    def toggle(self, x):
        self.s ^= (1 << x)

    def all(self):
        self.s = 0b11111111111111111111

    def empty(self):
        self.s = 0


M = int(sys.stdin.readline().strip())

s = S()
for _ in range(M):
    tmp = list(sys.stdin.readline().split())

    if len(tmp) == 2:
        f = tmp[0]
        num = int(tmp[1]) - 1

        if f == 'add':
            s.add(num)
        elif f == 'remove':
            s.remove(num)
        elif f == 'toggle':
            s.toggle(num)
        elif f == 'check':
            print(s.check(num))
    else:
        f = tmp[0]

        if f == 'all':
            s.all()
        elif f == 'empty':
            s.empty()
