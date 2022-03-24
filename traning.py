a, b = (int(i) for i in input().split())
lst_f = [input().strip() for _ in range(a)]
lst_end = [[j for j in i] for i in lst_f]
for i in range(a):
    for j in range(b):
        dot_s = [lst_f[i - 1][j - 1], lst_f[i - 1][j], lst_f[i - 1][j + 1 if j + 1 < b else 0],
                 lst_f[i][j - 1], lst_f[i][j + 1 if j + 1 < b else 0],
                 lst_f[i + 1 if i + 1 < a else 0][j - 1], lst_f[i + 1 if i + 1 < a else 0][j],
                 lst_f[i + 1 if i + 1 < a else 0][j + 1 if j + 1 < b else 0]]
        if lst_f[i][j] == '.':
            if dot_s.count('X') == 3:
                lst_end[i][j] = 'X'
        else:
            if dot_s.count('X') not in [2, 3]:
                lst_end[i][j] = '.'
for rez in lst_end:
    print(*rez, sep='')
