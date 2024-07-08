import sys

gongyak = ['Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop']

flag = False
N = int(sys.stdin.readline().strip())
for _ in range(N):
    s = sys.stdin.readline().strip()
    if s not in gongyak and not flag:
        print('Yes')
        flag = True
if not flag:
    print('No')
