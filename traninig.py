x1, y1, x2, y2 = map(int, input().split())


def nod(a, b):
    if b > 0:
        return nod(b, a % b)
    else:
        return a


a, b = abs(x1 - x2), abs(y1 - y2)
d = nod(a, b)
print(d * (a // d + b // d - 1))
