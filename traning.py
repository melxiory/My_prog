import sys

n = int(sys.stdin.readline())
list_val1 = [[int(i) if i.isdigit() else i for i in sys.stdin.readline().strip().split()] for _ in range(n)]
dict_book = {}
for i in list_val1:
    if i[0] == 'add':
        dict_book[i[1]] = i[2]
    if i[0] == 'find':
        if i[1] in dict_book:
            print(dict_book[i[1]])
        else:
            print('not found')
    if i[0] == 'del' and i[1] in dict_book:
        dict_book.pop(i[1])


