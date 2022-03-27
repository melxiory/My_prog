a, b = (int(i) for i in input().split())
lst_f = [input().strip() for _ in range(a)]
lst_end = [[j for j in i] for i in lst_f]
for i in range(a):
    for j in range(b):
        dot_s = [lst_f[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else None, lst_f[i - 1][j]if i - 1 >= 0 else None,
                 lst_f[i - 1][j + 1] if i - 1 >= 0 and j + 1 < b else None, lst_f[i][j - 1] if j - 1 >= 0 else None,
                 lst_f[i][j + 1] if j + 1 < b else None, lst_f[i + 1][j - 1] if i + 1 < a and j - 1 >= 0 else None,
                 lst_f[i + 1][j] if i + 1 < a else None, lst_f[i + 1][j + 1] if i + 1 < a and j + 1 < b else None]
        if lst_f[i][j] == '.':
            if dot_s.count('*') > 0:
                lst_end[i][j] = f'{dot_s.count("*")}'
            else:
                lst_end[i][j] = '0'
for rez in lst_end:
    print(*rez, sep='')