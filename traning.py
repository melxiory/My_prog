n = input()


def huffman(n):
    if len(n) == 1 or n.count(n[0]) == len(n):return {n: 0}, '0'*len(n)
    if len(n) == 2:return {n[0]: 0, n[1]: 1}, '01'
    dict_val = sorted([i for i in {i: n.count(i) for i in set(n)}.items()], key=(lambda x: (x[1], x[0])))
    dict_new = []
    while len(dict_val) > 1:
        dict_new += [(dict_val[0][0], '0'), (dict_val[1][0], '1')]
        dict_val.append((dict_val[0][0] + dict_val[1][0], dict_val[0][1] + dict_val[1][1]))
        dict_val = dict_val[2:]
        dict_val.sort(key=lambda x: (x[1], x[0]))
    dict_rez = {}
    for i in set(n):
        numb = []
        for j in dict_new:
            if i in j[0]:
                numb += j[1]
        numb.reverse()
        dict_rez[i] = ''.join(numb)
    return dict_rez, ''.join([dict_rez[i] for i in n])

def main():
    rez = huffman(n)
    print(rez)
    print(len(rez[0]), len(rez[1]))
    for i in sorted(rez[0]):
        print(f'{i}: {rez[0][i]}')
    print(int(rez[1]))

main()