num = input()
print(f'x{"-" * (4 * len(num)) + "-" * (len(num) - 1)}x')
for i in range(7):
    st = '|'
    if i in [0, 3, 6]:
        for hyp in num:
            if int(hyp) in [0, 2, 3, 5, 6, 7, 8, 9] and i == 0:
                st += ' -- '
            elif int(hyp) in [2, 3, 4, 5, 6, 8, 9] and i == 3:
                st += ' -- '
            elif int(hyp) in [0, 2, 3, 5, 6, 8, 9] and i == 6:
                st += ' -- '
            else:
                st += '    '
            st += ' '
        else:
            st = st[:-1]
    else:
        for bar in num:
            if int(bar) in [0, 4, 8, 9] and i in [1, 2]:
                st += '|  |'
            elif int(bar) in [0, 6, 8] and i in [4, 5]:
                st += '|  |'
            elif int(bar) in [1, 2, 3, 7] and i in [1, 2]:
                st += '   |'
            elif int(bar) in [1, 3, 4, 5, 7, 9] and i in [4, 5]:
                st += '   |'
            elif int(bar) in [5, 6] and i in [1, 2]:
                st += '|   '
            elif int(bar) == 2 and i in [4, 5]:
                st += '|   '
            st += ' '
        else:
            st = st[:-1]
    print(st+'|')
print(f'x{"-" * (4 * len(num)) + "-" * (len(num) - 1)}x')