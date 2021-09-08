def gap(g, m, n):
    previous_prime = n
    for i in range(m, n + 1):
        if is_prime(i):
            if i - previous_prime == g:
                return [previous_prime, i]
            previous_prime = i
    return None


def is_prime(n):
    for i in range(2, int(n ** .5 + 1)):
        if n % i == 0:
            return False
    return True


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
