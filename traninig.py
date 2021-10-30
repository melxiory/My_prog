def add(a, b, c):
    return a + b + c


a = 1
b = 2
c = 3
sum = a + b + c

from inspect import signature
from functools import partial


def curry_partial(main_func, *args):
    if not (callable(main_func)):
        return main_func

    p = len(signature(main_func).parameters)
    func = partial(main_func)

    for a in args:
        if len(func.args) == p: break
        func = partial(func, a)

    if len(func.args) < p:
        return partial(curry_partial, main_func, *func.args)

    return func()

print(curry_partial(add, a)(b)(c))
print(curry_partial(curry_partial(curry_partial(add, a)), b, c))
print(curry_partial(curry_partial(add, a, b), c))

print(curry_partial(add, a)(b, c))
print(curry_partial(add, a, b, c))
print(curry_partial(add, a, b, c, 20))
print(curry_partial(add)(a, b, c))
