import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
list_val1 = [[int(i) if i.isdigit() else i for i in sys.stdin.readline().strip().split()] for _ in range(n)]
hash_table = [[] for _ in range(m)]
dict_key = {}
for i in list_val1:
    if i[0] == 'add':
        acc, l = 0, 0
        for j in i[1]:
            acc += ord(j) * 263 ** l
            l += 1
        else:
            ind = (acc % 1000000007) % m
        if i[1] not in dict_key:
            hash_table[ind - 1].append(i[1])
            dict_key[i[1]] = ind - 1
    if i[0] == 'find':
        if i[1] in dict_key:
            print('yes')
        else:
            print('no')
    if i[0] == 'del':
        if i[1] in dict_key:
            del hash_table[dict_key[i[1]]][hash_table[dict_key[i[1]]].index(i[1])]
            dict_key.pop(i[1])
    if i[0] == 'check':
        if hash_table[i[1]-1]:
            strok = hash_table[i[1]-1][:]
            strok.reverse()
            print(' '.join(strok))
