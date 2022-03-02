lst = [[i for i in input().split()] for _ in range(int(input()))]
dict_ns = {'global': [['global'], []]}
for i in lst:
    if i[0] == 'create':
        dict_ns[i[2]][1].append(i[1])
        dict_ns[i[1]] = [[i[1]], []]
        dict_ns[i[1]][0].extend(dict_ns[i[2]][0])
    elif i[0] == 'add' and i[1] in dict_ns:
        dict_ns[i[1]][1].append(i[2])
    else:
        for j in dict_ns.get(i[1])[0]:
            if i[2] in dict_ns[j][1]:
                print(j)
                break
        else:
            print(None)



