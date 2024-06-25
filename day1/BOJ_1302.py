# import sys
#
# N = int(sys.stdin.readline().strip())
# books = {}
#
# for _ in range(N):
#     name = sys.stdin.readline().strip()
#     if name in books:
#         books[name] += 1
#     else:
#         books[name] = 1
#
# best = ''
# best_n = 0
# for book, count in books.items():
#     if count > best_n or (count == best_n and (best == '' or book < best)):
#         best = book
#         best_n = count
#
# print(best)

import sys

N = int(sys.stdin.readline().strip())
books = {}

for _ in range(N):
    name = sys.stdin.readline().strip()
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

sorted_books = sorted(books.items(), key=lambda x: (x[1], x[0]))
print(sorted_books[0][0])
