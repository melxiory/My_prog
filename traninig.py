import numpy, statistics


def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


def part(n):
    partitions_of = list(accel_asc(n))
    prod = sorted(set([numpy.prod(i) for i in partitions_of]))
    return f"Range: {prod[len(prod) - 1] - prod[0]} Average: {sum(prod) / len(prod):.2f} Median: {statistics.median(prod):.2f}"


print(part(10))

