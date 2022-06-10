import math

a, b, c = map(int, input().split())


def qwer(a, b):
    x = 1
    x1 = 0
    y = 0
    y1 = 1
    while b != 0:
        q = a // b
        r = a % b
        x2 = x - q * x1
        y2 = y - q * y1
        a, b = b, r
        x, x1 = x1, x2
        y, y1 = y1, y2
    return str(a), str(x), str(y)


x, y = 0, 0
gcds = 0
if c % math.gcd(a, b) != 0:
    print('Impossible')
else:
    gcds, x, y = map(int, qwer(a, b))
    x *= c // gcds
    y *= c // gcds
    q = x // (b // gcds)
    x %= b // gcds
    y += a // gcds * q
    print(math.gcd(a, b), x, y)
