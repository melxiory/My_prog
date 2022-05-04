a, b, n = int(input()), int(input()), int(input())
lst_p, lst_rez, a1, b1 = [], [], 0, 0
if a == n:
    print('>A')
elif b == n:
    print('>B')
else:
    while a1 != n and b1 != n:
        if a < b:
            if b1 in lst_p:
                print('Impossible')
                break
            if a1 == 0:
                a1 += a
                lst_rez.append('>A')
            if b1 == b:
                lst_p.append(b1)
                b1, a1 = a1, 0
                lst_rez.append('B>')
                lst_rez.append('A>B')
            else:
                if b1 + a1 <= b:
                    lst_p.append(b1)
                    b1 += a1
                    a1 = 0
                else:
                    lst_p.append(b1)
                    a1 = a - (b - b1)
                    b1 += b - b1
                lst_rez.append('A>B')
        else:
            if a1 in lst_p:
                print('Impossible')
                break
            if b1 == 0:
                b1 += b
                lst_rez.append('>B')
            if a1 == a:
                lst_p.append(a1)
                a1, b1 = b1, 0
                lst_rez.append('A>')
                lst_rez.append('B>A')
            else:
                if b1 + a1 <= a:
                    lst_p.append(a1)
                    a1 += b1
                    b1 = 0
                else:
                    lst_p.append(a1)
                    b1 = b - (a - a1)
                    a1 += a - a1
                lst_rez.append('B>A')
    else:
        print(*lst_rez, sep='\n')
