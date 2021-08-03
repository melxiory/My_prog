def f(n):
    end_kol_chet = 0
    if n % 2 == 1:
        n -= 1
    a = list(range(n + 1))
    a[1] = 0
    for i in a:
        if i > 1:
            for j in range(i + i, len(a), i):
                a[j] = 0
        i += 1
    lst = [x for x in a if x != 0]
    lst.reverse()
    lst = lst[:int(len(lst)*0.3)]
    for i in lst:
        if len([j for j in str(i) if int(j) % 2 == 0]) > end_kol_chet:
            end_kol_chet = len([j for j in str(i) if int(j) % 2 == 0])
            end_chis = i
    return end_chis


print(f(4683621))
print(f(3563331))
print(f(2714150))
print(f(500))
print(f(487))
