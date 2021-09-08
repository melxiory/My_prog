def gap(g, m, n):
    mnog = set(range(3, n+1, 2))
    mnog.add(2)
    for i in range(3, int(n+1), 2):
        if i in mnog:
            mnog -= set(range(2*i, n+1, i))
    lst = sorted(i for i in mnog if i >= m)
    nach = lst[0]
    for i in lst[1:]:
        if i - nach == g:
            return [nach, i]
        nach = i
    else:
        return None


print(gap(2, 100, 110))
print(gap(4, 100, 110))
print(gap(6, 100, 110))
print(gap(8, 300, 400))
print(gap(10, 300, 400))
print(gap(2, 100, 103))

"""
a = list(range(n + 1))
    a[1] = 0
    for i in a:
        if i > 1:
            for j in range(i + i, len(a), i):
                a[j] = 0
    lst = [x for x in a if x != 0 and x > m]
"""
