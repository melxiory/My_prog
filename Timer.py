import time


def total(func, *pargs, _reps=1000, **kargs):
    start = time.perf_counter()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = time.perf_counter() - start
    return elapsed, ret


def bestof(func, *pargs, _reps=5, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        start = time.perf_counter()
        ret = func(*pargs, **kargs)
        elapsed = time.perf_counter() - start
        if elapsed < best:
            best = elapsed
    return best, ret


def bestoftotal(func, _reps1, *pargs, **kargs):
    return min(total(func, *pargs, **kargs) for i in range(_reps1))


print(bestof(str.lower, 'spam'))