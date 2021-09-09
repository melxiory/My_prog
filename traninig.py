def my_crib(n):
    wide = 4 + 3 + 6 * (n - 1)
    door = 2 + n - 1
    roof = 3 + 2 * (n - 1)
    r = '{0}{1}{0}\n'.format(' ' * (wide // 2 - n), '_' * (3 + 2 * (n - 1)))
    for i in range(1, roof):
        r += '{0}/{1}\\{0}\n'.format(' ' * (wide // 2 - n - i), '_' * (3 + 2 * (n - 1) + 2 * (i -1)))
    for i in range(roof - 1 - door):
        r += '|{}|\n'.format(' ' * (wide - 2))
    r += '|{0}{1}{0}|\n'.format(' ' * ((wide - 1) // 3), '_' * (1 + 2 * (n - 1)))
    for i in range(1, door - 1):
        r += '|{0}|{0}|{0}|\n'.format(' ' * ((wide - 2) // 3))
    return r + '|{0}|{0}|{0}|'.format('_' * ((wide - 2) // 3))



print(my_crib(1))
print(my_crib(2))
print(my_crib(3))
